"""Compile all manuscripts from repository root, with a fixed PDF date epoch."""

import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("deterministic_factoring", "order_splitting", "quadratic_nonresidues",
         "randomized_factoring", "quadratic_relations")


def main():
    if not shutil.which("latexmk") or not shutil.which("pdflatex"):
        raise SystemExit("Install latexmk and the TeX Live packages listed in docs/reproducibility.md")
    env = dict(os.environ, SOURCE_DATE_EPOCH="1795564800", FORCE_SOURCE_DATE="1", TZ="UTC")
    versions = {}
    (ROOT / "papers").mkdir(exist_ok=True)
    for tool in ("latexmk", "pdflatex", "bibtex"):
        proc = subprocess.run([tool, "--version" if tool != "latexmk" else "-v"],
                              text=True, capture_output=True, check=True)
        versions[tool] = proc.stdout.splitlines()[:3]
    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build" / "tool_versions.json").write_text(json.dumps(versions, indent=2) + "\n")
    failures = []
    for name in NAMES:
        out = ROOT / "build" / name
        out.mkdir(parents=True, exist_ok=True)
        command = ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                   "-file-line-error", f"-outdir={out}", f"-jobname={name}",
                   f"manuscripts/{name}/main.tex"]
        result = subprocess.run(command, cwd=ROOT, env=env)
        if result.returncode:
            failures.append(name)
            continue
        shutil.copyfile(out / f"{name}.pdf", ROOT / "papers" / f"{name}.pdf")
    if failures:
        raise SystemExit("Manuscript build failed: " + ", ".join(failures))
    print("Compiled all five manuscripts into papers/.")


if __name__ == "__main__":
    main()
