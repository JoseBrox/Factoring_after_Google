# Contributing

The central goal is auditable mathematics. Reports of incorrect statements, missing hypotheses, hidden dependence in constants, or incomplete algorithms are especially valuable.

## Reporting a mathematical issue

Give the repository commit, manuscript title, theorem or equation label, and the exact step at issue. State the proposed counterexample or the hypothesis that seems missing. If computation is involved, include the complete input, exact output, software version, and a small script that reproduces it. A numerical observation should be identified as numerical evidence.

## Proposing a change

Explain the mathematical problem, the corrected statement, its proof, and which downstream results change. Distinguish proved results, conditional implications, conjectures, and experimental observations. Preserve the historical record of a corrected claim in `docs/errata.md`; do not silently rewrite a failed candidate as if it had always been correct.

Keep manuscript source in `manuscripts/`, executable routines in `src/`, and independently useful checks in `verification/`. Update the proof-status register and comparison table whenever a theorem's hypotheses or bound changes. Avoid adding a performance claim without a specified computational model and input promise.

Run `make check` and, for manuscript changes, `make papers`. Review the generated PDF, including tables and long equations. References must identify primary sources and precise versions. New dependencies should have a clear purpose; the current verification suite deliberately needs only Python and Node.js.

By contributing original material, you agree that it is distributed under this repository's CC BY 4.0 license. Preserve attribution and license notices for material from other sources. Do not upload material you lack permission to redistribute.
