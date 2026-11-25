"""Run all finite checks and compare with the committed expected JSON.

Use --record only when intentionally updating the public check transcript.
The normal command never rewrites expected results.
"""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    "verify_deterministic_parameters.py",
    "verify_enumeration_burgess_audit.py",
    "verify_recursion_budget.py",
    "verify_ramification_and_relation.py",
    "verify_mixed_prime_chain.py",
    "verify_sparse.js",
    "verify_public_implementation.py",
    "verify_selected_sections.py",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true")
    args = parser.parse_args()
    results = {}
    if not shutil.which("node"):
        raise SystemExit("Node.js is required for verify_sparse.js")
    for name in CASES:
        program = "node" if name.endswith(".js") else sys.executable
        proc = subprocess.run([program, str(ROOT / "verification" / name)],
                              cwd=ROOT, text=True, capture_output=True, check=True)
        results[name] = json.loads(proc.stdout)
        print("PASS", name)
    expected = ROOT / "verification" / "expected_results.json"
    if args.record:
        expected.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
        print("Recorded", expected.relative_to(ROOT))
    elif results != json.loads(expected.read_text()):
        raise SystemExit("CHECK OUTPUT MISMATCH: inspect exact results before changing the expected transcript")
    else:
        print("All eight programs match the committed expected results.")
    return results


if __name__ == "__main__":
    main()
