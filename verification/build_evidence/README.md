# Evidence for the published PDFs

The five manuscript PDFs were compiled from source commit
`c8b2feae86f98003f3279562928cd95666bf8622` in the successful
[manuscript workflow run](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45688355921).

This directory preserves the final pdfLaTeX and BibTeX logs, TeX tool versions,
and source-file hash receipt from that run. Log filenames end in `.txt` so they
remain visible despite the repository's ignore rules for disposable TeX output.
Absolute runner paths in the logs describe the build environment; they are not
required local paths.

[The build report](../build_report.json) records the exact PDF hashes, page counts,
metadata, and final layout inspection. [The release manifest](../release_manifest.json)
records the bytes of the published sources, PDFs, and verification material.
Run `python3 scripts/verify_release.py` from an unmodified release checkout to
verify them. The manifest deliberately excludes itself.

The archived logs and receipts are build evidence, not a formal proof certificate.
Rebuilding from the same source with different TeX packages can produce different
PDF bytes. The [reproducibility guide](../../docs/reproducibility.md) explains the
supported reconstruction procedure and its limits.
