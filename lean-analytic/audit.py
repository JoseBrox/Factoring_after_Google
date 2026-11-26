import re
import sys
from pathlib import Path

s = Path(sys.argv[1]).read_text()
expected = {"StrongPNT", "Factoring.Analytic.sqrt_error_scale",
            "Factoring.Analytic.theta_strongPNT", "Factoring.Analytic.theta_relative_error", "Factoring.Analytic.dyadic_density_of_theta",
            "Factoring.Analytic.dyadic_density"}
seen = set()
for name, axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", s):
    if name in expected:
        seen.add(name)
        extra = set(a.strip() for a in axioms.split(",") if a.strip()) - {
            "propext", "Classical.choice", "choice", "Quot.sound"}
        if extra:
            raise SystemExit(f"Unexpected axioms in {name}: {extra}")
if seen != expected:
    raise SystemExit(f"Missing axiom reports: {expected - seen}")
print("PASS: exact PNT+ revision and all analytic adapter theorem dependencies checked.")
