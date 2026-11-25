"""Check pinned inputs, archived notes, manuscript dependencies, and local links.

This is a publication-integrity check, not a mathematical proof checker.
Generated PDFs may be absent in a source-only checkout before the build.
"""

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from fetch_sources import git_blob


def expanded_tex(path, seen=None):
    seen = set() if seen is None else set(seen)
    if path in seen:
        raise AssertionError(f"Cyclic TeX input: {path}")
    seen.add(path)
    text = path.read_text()
    def expand(match):
        target = ROOT / match.group(1)
        if not target.suffix:
            target = target.with_suffix(".tex")
        assert target.exists(), f"Missing TeX input: {target}"
        return expanded_tex(target, seen)
    return re.sub(r"\\input\{([^}]+)\}", expand, text)


def main():
    lock = json.loads((ROOT / "references/sources.lock.json").read_text())
    upstream = 0
    for item in lock["files"]:
        path = ROOT / item["local_path"]
        if path.exists():
            assert git_blob(path.read_bytes()) == item["git_blob_sha1"], path
            upstream += 1
        else:
            assert path.suffix == ".pdf", f"Missing source text: {path}"
    notes = json.loads((ROOT / "provenance/manifest.json").read_text())
    for item in notes:
        assert hashlib.sha256((ROOT / item["file"]).read_bytes()).hexdigest() == item["sha256"], item["file"]
    bib = (ROOT / "manuscripts/shared/references.bib").read_text()
    keys = set(re.findall(r"@\w+\s*\{\s*([^,]+),", bib))
    manuscripts = sorted((ROOT / "manuscripts").glob("*/main.tex"))
    assert len(manuscripts) == 5
    for main_path in manuscripts:
        text = expanded_tex(main_path)
        citations = [k.strip() for group in re.findall(r"\\cite\w*\s*(?:\[[^]]*\])*\{([^}]+)\}", text)
                     for k in group.split(",")]
        assert set(citations) <= keys, (main_path, set(citations) - keys)
        labels = re.findall(r"\\label\{([^}]+)\}", text)
        assert len(labels) == len(set(labels)), f"Duplicate labels in {main_path}"
        refs = re.findall(r"\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}", text)
        missing = {r.strip() for group in refs for r in group.split(",")} - set(labels)
        assert not missing, (main_path, missing)
        assert "\\author{Jose Brox}" in text
        assert "\\begin{abstract}" in text and "\\tableofcontents" in text
        assert len(text.split()) > 1500, f"Manuscript unexpectedly short: {main_path}"
    links = 0
    pages = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    pages += list((ROOT / "docs").glob("*.md"))
    pages += [ROOT / d / "README.md" for d in ("manuscripts", "papers", "src", "references", "provenance", "verification", "lean")]
    for page in pages:
        for target in re.findall(r"\]\(([^)\s]+)\)", page.read_text()):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            path = (page.parent / unquote(target.split("#", 1)[0])).resolve()
            assert path.is_relative_to(ROOT.resolve()), (page, target)
            if not path.exists():
                assert path.parent == ROOT / "papers" and path.suffix == ".pdf", (page, target)
            links += 1
    for name, count in (("deterministic", 59), ("randomized", 54)):
        text = (ROOT / f"references/upstream/{name}-paper.txt").read_text()
        pages_found = re.findall(r"^=== PAGE (\d+) ===$", text, re.M)
        assert pages_found == list(map(str, range(1, count + 1)))
        assert "Cleaning up orphan processes" not in text
    assert "Attribution 4.0 International" in (ROOT / "LICENSE").read_text()
    assert "Conditional" in (ROOT / "README.md").read_text() or "conditional" in (ROOT / "README.md").read_text()
    assert (ROOT / "verification/expected_results.json").exists()
    print(f"PASS: {len(manuscripts)} manuscripts; citations, labels, and {links} local links checked.")
    print(f"PASS: {upstream} available upstream files and {len(notes)} historical notes match their pinned hashes.")
    print("PASS: source page ranges, attribution, and expected verification transcript present.")


if __name__ == "__main__":
    main()
