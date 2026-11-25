# Compiled manuscripts

This directory contains the five searchable PDFs built from `manuscripts/`. The [manuscript index](../manuscripts/README.md) describes them and links their editable sources.

Regenerate them from the repository root with `python3 scripts/build_manuscripts.py`. The build workflow preserves logs, source retrieval receipts, and TeX tool versions as an artifact. Committed PDF hashes are recorded in the release manifest; byte identity across different TeX distributions is not assumed.
