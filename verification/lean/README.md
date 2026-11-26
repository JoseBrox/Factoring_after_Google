# Lean build evidence

**26 November update:** [continuation receipt](continuation.md) records the clean build of sixteen modules. The following records are retained for the original five-module checkpoint.

These records accompany the first Lean component formalization. The five proof
modules contain 94 explicitly named theorems, including five executable examples.
The compiled audit checks 231 persistent logical declarations, of which 169 are
theorems when Lean-generated equations and other auxiliary proofs are included.
Those larger counts are not counts of distinct mathematical results.

- [report.json](report.json): actual compiler/Lake versions, pinned mathlib
  revision, audit policy, and SHA-256 hashes of every formal source, configuration
  file, and verification/CI entry point.
- [axioms.txt](axioms.txt): the full theorem axiom inventory and audit totals.

The recorded local run used Lean 4.19.0 and passed with warnings treated as errors.
Only `propext`, `Classical.choice`, and `Quot.sound` were used as logical axioms.
The 127 unsafe compiler runtime objects are excluded only as audit roots; the
dependency traversal of each logical declaration is unfiltered. This uses the
same logical/unsafe distinction as Lean's kernel replay routine. The executable
examples are named theorems and are included in the audit.

The [Lean workflow](../../.github/workflows/lean.yml) repeats the build on a clean
runner and preserves fresh compilation logs and a receipt in its artifact.
[Workflow runs](https://github.com/JoseBrox/Factoring_after_Google/actions/workflows/lean.yml)
identify the exact source commit checked. Reproduce the run with
`python3 scripts/verify_lean.py` after fetching the pinned dependencies, as
explained in the [Lean guide](../../lean/README.md).

This receipt describes the source hashes it records. Later proof edits require
a new build and receipt; neither old logs nor source hashes certify new proofs.
The full factoring complexity theorems, analytic contracts, and success
probabilities remain outside this first formalization.
