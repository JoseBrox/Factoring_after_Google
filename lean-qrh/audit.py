"""Reject missing reports or nonstandard axioms in the exact imported endpoints."""
import re
import sys
from pathlib import Path

expected = {
    "OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re",
    "OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re",
    *("Factoring.QRH." + n for n in (
        "dirichlet_nonzero", "zeta_nonzero", "zero_re_le",
        "real_zero_gap", "no_bad_character")),
}
text = Path(sys.argv[1]).read_text()
seen = set()
for name, axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text):
    if name in expected:
        seen.add(name)
        extra = {a.strip() for a in axioms.split(",") if a.strip()} - {
            "propext", "Classical.choice", "Quot.sound"}
        if extra:
            raise SystemExit(f"Unexpected axioms in {name}: {extra}")
for name in re.findall(r"'([^']+)' does not depend on any axioms", text):
    if name in expected:
        seen.add(name)
if seen != expected:
    raise SystemExit(f"Missing reports: {expected - seen}")
print("PASS: all seven exact QRH dependencies audited.")
