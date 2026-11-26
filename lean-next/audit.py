"""Require every explicit #print axioms report in the candidate sources."""
import re
import sys
from pathlib import Path
src = Path(__file__).resolve().parent
logs = Path(sys.argv[1])
allowed = {"propext", "Classical.choice", "Quot.sound"}
for source in sorted(src.glob("*.lean")):
    expected = set(re.findall(r"^#print axioms (\S+)$", source.read_text(), re.M))
    if not expected:
        raise SystemExit(f"No audit roots in {source}")
    log = (logs / (source.stem + ".log")).read_text()
    seen = set()
    for name, axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log):
        if name in expected:
            seen.add(name)
            extra = {a.strip() for a in axioms.split(",") if a.strip()} - allowed
            if extra:
                raise SystemExit(f"Unexpected axioms in {name}: {extra}")
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        if name in expected:
            seen.add(name)
    if seen != expected:
        raise SystemExit(f"Missing reports for {source}: {expected - seen}")
    print(f"PASS {source.name}: {len(seen)} named proof roots.")
