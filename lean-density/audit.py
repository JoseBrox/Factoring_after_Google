import re
import sys
from pathlib import Path
s = Path(sys.argv[1]).read_text()
expected = {"OAI.Ostmann.actualCharacterZeros_respectsMultiplicity",
            "OAI.Ostmann.publishedComplexZeroDensity",
            "Factoring.Density.near_one_exponent",
            "Factoring.Density.uniform_near_one_count",
            "Factoring.Density.bad_character_count"}
seen = set()
for name, axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", s):
    if name in expected:
        seen.add(name)
        extras = {a.strip() for a in axioms.split(",") if a.strip()} - {
            "propext", "Classical.choice", "Quot.sound"}
        if extras:
            raise SystemExit(f"Unexpected axioms in {name}: {extras}")
if seen != expected:
    raise SystemExit(f"Missing reports: {expected-seen}")
print("PASS: all imported density and adapter dependencies audited.")
