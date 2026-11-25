# Reconstructing and verifying the results

Reproduction includes finite calculations, Lean component proofs, manuscript builds, and audits of the remaining mathematical arguments. This repository supplies the inputs for each and states their scope explicitly.

## 1. Obtain an exact version

Clone `https://github.com/JoseBrox/Factoring_after_Google`, check out the commit you wish to audit, and record `git rev-parse HEAD`. Citation metadata is in `CITATION.cff`; the theorem statements are in `manuscripts/`. Use immutable commit links when reporting an issue.

The files in `provenance/notes/` are frozen historical material. Their original repository, commit, paths, and SHA-256 hashes are in `provenance/manifest.json`. Current manuscripts may correct or strengthen those notes; the current proof-status register identifies what is claimed now.

## 2. Reproduce exact finite checks

Requirements: Python 3.10+ and Node.js 18+. No Python packages, numerical libraries, network access, or secret data are required.

```sh
python3 verification/run_all.py
python3 scripts/verify_repository.py
python3 examples/quadratic_relation_example.py
```

The first command runs eight programs and compares their full JSON results with `verification/expected_results.json`. Rational inequalities use `fractions.Fraction`. Local character and quadratic-ring computations use exact modular arithmetic. The small-field sparse checks use a fixed seed and exact arithmetic in $\mathbb F_{256}$. The section checker compares complete polynomial coefficient arrays from independent constructions. Input families, loop ranges, and the seed are in the code.

The second command checks available source bytes, archived-note hashes, LaTeX inputs, bibliography keys, theorem-reference labels, local documentation links, source page counts, and authorship. It permits the generated PDFs to be absent before the manuscript build. It is an integrity check, not a theorem prover.

The example reports the saturated-exponent case $N=35$, $b=2$, $M=48$: 10 successful parameters for the one-shot relation, and all 35 for the chain. Known factors are used to prove and test the promise, not as inputs to the splitting routine.

The release's Python and Node.js versions and file hashes are recorded in [release_manifest.json](../verification/release_manifest.json). The exact manuscript source commit, successful workflow run, TeX versions, PDF hashes, page counts, and layout checks are recorded in [build_report.json](../verification/build_report.json). These records document the performed runs. The minimum version requirements above describe the language features needed, not a claim that every future interpreter release has been tested.

To check every file recorded for the initial publication, check out [commit `af09583`](https://github.com/JoseBrox/Factoring_after_Google/tree/af09583053f45e910e865bb6594b2ba0f8706bc2) and run `python3 scripts/verify_release.py`. That manifest describes the initial snapshot. Later editorial changes and the Lean formalization have their own source history and build evidence.

## 3. Retrieve and verify the primary source manuscripts

```sh
python3 scripts/fetch_sources.py
```

This command reads `references/sources.lock.json` and fetches only its immutable Google Research URLs when files are missing. It verifies Git's SHA-1 blob digest, including the `blob <byte length>\0` header, before saving or reusing a file. A mismatch fails the command. It also writes a SHA-256 receipt to `build/source_receipt.json`.

The pinned deterministic PDF has Git blob `973002e0eb92acf3964fc020ca52ba6f1ac384ac`; the randomized PDF has Git blob `19f36b2f189ed41ec8e112b92aa9b88a96c6bd1e`. Both belong to commit `4a7bc8ab0bc770e71a259b7966c500496b99010a`. The source README hashes are pinned too.

Searchable plain-text extractions are committed alongside the source READMEs. They originated in a hash-verified extraction run, contain all 59 and 54 page markers respectively, and have had workflow boilerplate removed. Re-extracting text with another PDF library may change spacing or mathematical symbol encoding; the authoritative object is the pinned PDF, not a text-extraction byte sequence.

## 4. Build the five PDFs

On Ubuntu, the build dependencies are available from the normal package repositories:

```sh
sudo apt-get install latexmk texlive-latex-extra texlive-fonts-recommended lmodern poppler-utils
python3 scripts/build_manuscripts.py
```

Run from the repository root. The script uses `latexmk` to run pdfLaTeX and BibTeX as needed, writes searchable PDFs to `papers/`, and preserves auxiliary files and logs under `build/`. Each PDF has a title, author, version date, linked contents, theorem labels, and bibliography. The common technical appendix is included directly in both relevant PDFs.

The build fixes `SOURCE_DATE_EPOCH` to 25 November 2026 UTC and suppresses volatile PDF dates and trailer identifiers. The TeX tool versions are recorded in `build/tool_versions.json`. This reduces accidental differences; byte-for-byte identity across distinct TeX distributions is not promised. The source, mathematical content, and successful build are the reproducibility target.

The GitHub Actions workflow uses Ubuntu 24.04, pinned action commits, explicit package names, and read-only repository permissions. It preserves compiled PDFs, upstream PDFs, build logs, and source receipts in the `manuscripts-and-sources` artifact. The published PDFs, source PDFs, and final logs and receipts are also committed in the repository, so verification does not depend on the temporary Actions artifact remaining available. See [build evidence](../verification/build_evidence/README.md). The runner's package repositories can evolve, so use the recorded tool versions when investigating a layout difference.

## 5. Audit the proofs

Begin with the main theorem and its input promises. Follow the dependency register in the manuscript and `docs/proof_status.md`. For the deterministic factorer, examine the corrected progression estimate, the actual congruence covolumes, the blockwise covariance bound, exceptional conductors, adaptive deletion, and exact extraction. Verify that every parameter inequality is used at the range proved.

For the splitter and nonresidue constructor, check the ramified local PSD identities, the finite enumeration procedure, primitive character/conductor conditions, the short-sum range, and the guarded multiscale stopping rule. For the relation chain, check the distinction between the one-shot endpoint and scalarization at an intermediate squaring stage, including repeated prime factors of $N$.

For the randomized manuscript, first read the conditional contract. The widened analytic assertions are not consequences of a finite parameter check. The sparse-kernel theorem and recurrence have separate proofs that can be audited without assuming the complete factoring theorem. Replacing the contract by a proved theorem is a substantive open task.

## 6. Compile and audit the Lean component proofs

Use the toolchain named in `lean/lean-toolchain` and the dependency revisions in `lean/lake-manifest.json`. From the repository root:

```sh
cd lean
lake exe cache get $(python3 ../scripts/verify_lean.py --imports)
cd ..
python3 scripts/verify_lean.py
```

The verifier checks that the actual dependency checkouts match the manifest and have no tracked or untracked source changes. It checks that every proof module is imported by `Factoring.lean`, compiles the project with warnings treated as errors, and audits compiled logical declarations for unexpected axioms. The allowlist is `propext`, `Classical.choice`, and `Quot.sound`. Source hashes, the complete axiom inventory, compiler versions, and build output are written to `build/lean/`. The [Lean CI workflow](../.github/workflows/lean.yml) repeats these checks in a fresh Ubuntu runner and checksum-verifies the pinned Lean distribution.

See the [Lean guide](../lean/README.md) for theorem names, hypotheses, and remaining bridges, and the [initial build evidence](../verification/lean/README.md) for the preserved receipt and axiom inventory. The universal schedule and recursion proofs strengthen earlier finite checks. The full analytic complexity theorems have not been formalized.

## What is not supplied

There is no hidden empirical dataset or unpublished timing benchmark. There is no complete implementation of the asymptotic general factorers or end-to-end Lean proof of their complexity. The repository supplies mathematical specifications, written proofs and conditional implications, compiled Lean component proofs, pinned dependencies, and reproducible finite checks. Their distinct scopes are recorded in the proof-status register.
