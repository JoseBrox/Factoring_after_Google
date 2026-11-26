#!/usr/bin/env python3
"""Select only the mathlib cache roots reached from the external Lean entry points."""
import re
import sys
from pathlib import Path

seen = set()
roots = set()
def walk(path):
    if path in seen:
        return
    seen.add(path)
    for line in path.read_text().splitlines():
        match = re.match(r"^(?:public |private )?import (?:all )?([A-Za-z0-9_.]+)", line)
        if match is None:
            continue
        name = match[1]
        if name.startswith("Mathlib."):
            roots.add(name)
        elif name.startswith("PrimeNumberTheoremAnd."):
            walk(Path(name.replace(".", "/") + ".lean"))

for name in sys.argv[1:]:
    walk(Path(name))
print("\n".join(sorted(roots)))
