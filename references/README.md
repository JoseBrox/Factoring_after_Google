# Pinned reference material

The recent sources are pinned to immutable commits and Git blob hashes in [sources.lock.json](sources.lock.json). All source theorem and page numbers in the manuscripts refer to those versions.

- [Deterministic source README](upstream/deterministic-README.md) and [searchable extracted text](upstream/deterministic-paper.txt), 59 pages.
- [Randomized source README](upstream/randomized-README.md) and [searchable extracted text](upstream/randomized-paper.txt), 54 pages.
- The authoritative PDFs are `upstream/deterministic-paper.pdf` and `upstream/randomized-paper.pdf`; fetch or verify them with `python3 scripts/fetch_sources.py`.

The source PDFs are unchanged. The text extractions preserve page markers and remove workflow logging; line breaks and mathematical symbols can be imperfect. Consult the PDF whenever typography matters. The extraction originated in the [hash-verifying audit run](https://github.com/JoseBrox/factoring-algorithms/actions/runs/45666731595).

Copyright 2026 Google LLC. The paper-specific READMEs state CC BY 4.0 licensing and attribute the papers to Cogentic using Gemini 4. See [NOTICE](../NOTICE) for attribution and a description of changes. Classical articles and books are cited through the [BibTeX database](../manuscripts/shared/references.bib); they are not redistributed under this repository's license.

Hashes establish which bytes were read. They do not establish mathematical validity. The [comparison register](../docs/comparison_sources.md) and [proof-status register](../docs/proof_status.md) describe how the sources are used.
