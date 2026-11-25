"""Reproduce the saturated-exponent example from the relation manuscript."""

from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from factoring_after_google import chain_split, one_shot_split

n, b, m = 35, 2, 48
one_shot = [a for a in range(n) if one_shot_split(n, b, m, a)]
chain = [a for a in range(n) if chain_split(n, b, m, a)]
print(json.dumps({"N": n, "b": b, "M": m,
                  "one_shot_successes": len(one_shot),
                  "chain_successes": len(chain),
                  "example_a": 0, "example_factor": chain_split(n, b, m, 0)},
                 indent=2))
