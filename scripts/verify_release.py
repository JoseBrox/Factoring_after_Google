"""Verify the recorded bytes of an unmodified published release.

This checks file integrity, not mathematical correctness. Rebuilding PDFs with
different TeX packages or intentionally editing sources may change their hashes.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "verification/release_manifest.json").read_text())
    failures = []
    for relative, expected in manifest["files"].items():
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            failures.append(f"Missing or invalid path: {relative}")
            continue
        data = path.read_bytes()
        if len(data) != expected["bytes"] or hashlib.sha256(data).hexdigest() != expected["sha256"]:
            failures.append(f"Changed bytes: {relative}")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"PASS: {len(manifest['files'])} files match the release manifest.")


if __name__ == "__main__":
    main()
