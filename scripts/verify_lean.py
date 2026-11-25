"""Compile the pinned Lean project and audit its actual proof dependencies.

Run from any directory: python3 scripts/verify_lean.py
Use --imports to list the mathlib cache roots required by our source files.
Logs and a source-hash receipt are written under build/lean/.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "lean"
SOURCES = sorted(PROJECT.glob("*.lean")) + sorted((PROJECT / "Factoring").rglob("*.lean"))
MATHLIB = "c44e0c8ee63ca166450922a373c7409c5d26b00b"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    if sys.argv[1:] == ["--imports"]:
        imports = {m for p in SOURCES for m in
                   re.findall(r"^import (Mathlib\.\S+)$", p.read_text(), re.M)}
        print("\n".join(sorted(imports)))
        return
    if sys.argv[1:]:
        raise SystemExit("Usage: verify_lean.py [--imports]")

    out = ROOT / "build/lean"
    out.mkdir(parents=True, exist_ok=True)

    def run(args, filename):
        result = subprocess.run(args, cwd=PROJECT, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        (out / filename).write_text(result.stdout)
        if result.returncode:
            print(result.stdout)
            raise SystemExit(result.returncode)
        return result.stdout.strip()

    modules = {".".join(p.relative_to(PROJECT).with_suffix("").parts)
               for p in (PROJECT / "Factoring").rglob("*.lean")}
    imported = set(re.findall(r"^import (Factoring\.\S+)$",
                             (PROJECT / "Factoring.lean").read_text(), re.M))
    require(modules == imported, "Factoring.lean must import every project proof module")
    require((PROJECT / "lean-toolchain").read_text().strip() == "leanprover/lean4:v4.19.0",
            "Unexpected Lean toolchain")
    manifest = json.loads((PROJECT / "lake-manifest.json").read_text())
    require(next(p for p in manifest["packages"] if p["name"] == "mathlib")["rev"] == MATHLIB,
            "Unexpected mathlib revision")
    for package in manifest["packages"]:
        path = PROJECT / ".lake/packages" / package["name"]
        revision = subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"],
                                           text=True).strip()
        require(revision == package["rev"], f"Wrong dependency revision: {path}")
        dirty = subprocess.check_output(["git", "-C", str(path), "status", "--porcelain",
                                         "--untracked-files=all"],
                                        text=True).strip()
        require(not dirty, f"Modified dependency source: {path}\n{dirty}")

    lean_version = run(["lean", "--version"], "lean-version.txt")
    require("version 4.19.0," in lean_version, f"Unexpected compiler: {lean_version}")
    lake_version = run(["lake", "--version"], "lake-version.txt")
    run(["lake", "build"], "build.txt")
    audit = run(["lake", "env", "lean", "-DwarningAsError=true", "Audit.lean"], "axioms.txt")
    summary = re.search(r"PASS: (\d+) declarations, including (\d+) theorems;", audit)
    require(summary, "Missing compiled-declaration audit summary")
    hashed = SOURCES + [PROJECT / name for name in
                        ("lean-toolchain", "lakefile.toml", "lake-manifest.json")]
    hashed += [ROOT / "scripts/verify_lean.py", ROOT / ".github/workflows/lean.yml"]
    receipt = {
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean": lean_version,
        "lake": lake_version,
        "mathlib_revision": MATHLIB,
        "modules": sorted(modules),
        "declarations_audited": int(summary.group(1)),
        "theorems_audited_including_generated": int(summary.group(2)),
        "audit_roots": "Every persistent logical declaration in the project modules; unsafe compiler runtime objects excluded only as roots.",
        "allowed_axioms": ["propext", "Classical.choice", "Quot.sound"],
        "warnings_are_errors": True,
        "sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(hashed)},
        "scope": "Component theorems only; the full analytic factoring bounds are not formalized.",
    }
    (out / "report.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(lean_version)
    print(summary.group(0))
    print("PASS: pinned dependencies, warning-free compilation, and compiled axiom audit.")
    print("Build logs, axiom inventory, and source hashes: build/lean/")


if __name__ == "__main__":
    main()
