"""Check every candidate's compiler exit status, then all explicit audit roots."""
import re
import sys
from pathlib import Path

src = Path(__file__).resolve().parent
logs = Path(sys.argv[1])
allowed = {"propext", "Classical.choice", "Quot.sound"}
failed = False
for source in sorted(src.glob("*.lean")):
    try:
        status = (logs / (source.stem + ".exit")).read_text().strip()
        if status != "0":
            raise ValueError(f"Lean exit status {status}")
        expected = set(re.findall(r"^#print axioms (\S+)$", source.read_text(), re.M))
        if not expected:
            raise ValueError("No audit roots")
        log = (logs / (source.stem + ".log")).read_text()
        seen = set()
        for name, axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log):
            if name in expected:
                seen.add(name)
                extra = {a.strip() for a in axioms.split(",") if a.strip()} - allowed
                if extra:
                    raise ValueError(f"Unexpected axioms in {name}: {extra}")
        for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
            if name in expected:
                seen.add(name)
        if seen != expected:
            raise ValueError(f"Missing reports: {expected - seen}")
        print(f"PASS {source.name}: strict compiler success and {len(seen)} named proof roots.")
    except (ValueError, OSError) as exc:
        failed = True
        print(f"FAIL {source.name}: {exc}")
sys.exit(int(failed))
