"""Fetch only the immutable upstream files recorded in sources.lock.json.

No credentials are used. The Git blob digest includes Git's byte-length header.
Existing files are checked before they are reused. A digest mismatch is fatal.
"""

import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def main():
    lock = json.loads((ROOT / "references" / "sources.lock.json").read_text())
    receipts = []
    for item in lock["files"]:
        path = ROOT / item["local_path"]
        if path.exists():
            data = path.read_bytes()
        else:
            request = urllib.request.Request(item["raw_url"], headers={"User-Agent": "Factoring-after-Google-source-check/0.1"})
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
        actual = git_blob(data)
        if actual != item["git_blob_sha1"]:
            raise SystemExit(f"Source digest mismatch for {item['local_path']}: {actual}")
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_bytes(data)
        receipts.append({"path": item["local_path"], "bytes": len(data),
                         "git_blob_sha1": actual, "sha256": hashlib.sha256(data).hexdigest()})
        print("Verified", item["local_path"])
    build = ROOT / "build"
    build.mkdir(exist_ok=True)
    (build / "source_receipt.json").write_text(json.dumps(receipts, indent=2) + "\n")


if __name__ == "__main__":
    main()
