# Lean continuation build receipt — 26 November 2026

This record describes the verified core checkpoint, not an end-to-end proof of the asymptotic factoring algorithms.

- Exact proof-source commit: [4438d17](https://github.com/JoseBrox/Factoring_after_Google/commit/4438d17e7d79a75010ab7b072b90ceeeb4d990bd).
- Clean Lean workflow: [45803199207](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45803199207), job [139851485343](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45803199207/job/139851485343), conclusion **success**.
- Exact verification workflow: [45803199417](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45803199417), conclusion **success**.
- Lean 4.19.0 and pinned mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b.
- Sixteen proof modules, 159 explicitly named theorem/lemma declarations (source count, including previous examples); compiled audit counts 403 persistent logical declarations, including 326 theorems with generated equations and auxiliary declarations.
- Workflow log: `PASS: 403 declarations, including 326 theorems;` and `PASS: pinned dependencies, warning-free compilation, and compiled axiom audit.`
- Only the standard logical axioms propext, Classical.choice and Quot.sound are permitted by the audit. No `sorry` or `native_decide` in the project proofs.
- Build evidence artifact [15108686715](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45803199207/artifacts/15108686715), SHA-256 digest reported by GitHub: `04263be4228a2fb9050d5c59abdf41979a7cd447fa350e806801924405aaa9e2`. GitHub reports expiration 24 February 2027. The workflow preserves the compiled audit inventory, logs, source-hash receipt and versions; this Markdown record is a summary of the observed run, not a replacement for the full receipt.

The documentation update following the source commit does not change Lean source or dependency pins. The five-module receipt and axiom inventory remain unchanged as historical records.

See [the Lean guide](../../lean/README.md) for exact statements and [the proof-status register](../../docs/proof_status.md) for outstanding obligations. Reproduce with `python3 scripts/verify_lean.py` after installing the pinned toolchain and fetching its required mathlib cache.
