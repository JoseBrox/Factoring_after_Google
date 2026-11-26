"""Extract just the reachable source files from a pinned openai/math checkout."""
import json
import re
import shutil
import sys
from pathlib import Path

source, target, adapter, pnt = map(Path, sys.argv[1:])
roots, external, visited = set(), set(), set()
def imports(path):
    # A conservative scan of import directives. All actual imports are also
    # checked by Lake when it elaborates each module.
    for line in path.read_text().splitlines():
        match = re.match(r"^\s*(?:public |private )?import (?:all )?([A-Za-z0-9_.]+)", line)
        if match:
            yield match.group(1)
def visit(name):
    if name in visited:
        return
    visited.add(name)
    if name == "Mathlib" or name.startswith("Mathlib."):
        roots.add(name)
    elif name.startswith("OAI.") or name.startswith("PrimeNumberTheoremAnd."):
        rel = Path(name.replace(".", "/") + ".lean")
        src = (source if name.startswith("OAI.") else pnt) / rel
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        for dep in imports(src):
            visit(dep)
    elif name.split(".")[0] not in {"Lean", "Init", "Std", "Batteries", "Aesop", "Qq"}:
        external.add(name)
for dep in imports(adapter):
    visit(dep)
report = {"entrypoint": str(adapter.name), "local_modules": sorted(n for n in visited if n.startswith(("OAI.", "PrimeNumberTheoremAnd."))),
          "mathlib_roots": sorted(roots), "other_imports": sorted(external)}
(target / "closure.json").write_text(json.dumps(report, indent=2)+"\n")
(target / "cache-roots.txt").write_text("\n".join(sorted(roots))+"\n")
print("Local proof modules:", len(report["local_modules"]))
print("Mathlib roots:", len(roots))
print("Additional external imports:", sorted(external))
if external:
    raise SystemExit("Additional packages require pinning and possibly the upstream compatibility patches.")
