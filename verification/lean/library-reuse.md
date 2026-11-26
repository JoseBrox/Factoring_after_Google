# Library reuse build receipt — 26 November 2026

## Mathlib adapters

- Exact proof-source commit: [b290d5f](https://github.com/JoseBrox/Factoring_after_Google/commit/b290d5f8b2a993e04e899d24eef88593aa7d4901).
- Clean build: [45824077002](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45824077002), conclusion **success**.
- Exact verification: [45824076984](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45824076984), conclusion **success**.
- 22 proof modules, 185 named theorems. Compiled audit: 450 declarations including 364 theorems.
- Log: `PASS: 450 declarations, including 364 theorems;` and `PASS: pinned dependencies, warning-free compilation, and compiled axiom audit.`
- Lean 4.19.0, mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b; standard three logical axioms only.

The four added modules and aggregate import are copied byte-for-byte from the validated commit. See the run's build evidence artifact for the source hashes and complete compiled-declaration inventory. This receipt certifies precisely the stated component results, not their remaining analytic or algorithmic premises.

## Strong PNT and dyadic prime count (separate target)

- Validated source: [5754142](https://github.com/JoseBrox/Factoring_after_Google/commit/5754142e409689cf6a68545fc39520edae8f716a).
- Clean build: [45825262779](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45825262779), conclusion **success**.
- Exact verification: [45825262614](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45825262614), conclusion **success**.
- Lean 4.36.0, PNT+ e9906138410f8f76ca66b9bc252d0993f3ee348c, mathlib fc4f59e577feb1a4956671bc04ac18aaaf8cd842.
- The upstream source target `PrimeNumberTheoremAnd.StrongPNT` was built, the adapter compiled with warnings as errors, and these six declarations were audited: `StrongPNT`, `Factoring.Analytic.sqrt_error_scale`, `theta_strongPNT`, `theta_relative_error`, `dyadic_density_of_theta`, `dyadic_density` (last four in namespace `Factoring.Analytic`). Every reported axiom set was exactly [propext, Classical.choice, Quot.sound].
- Log: `PASS: exact PNT+ revision and all analytic adapter theorem dependencies checked.`

Five new local theorems, in a separately compiled project. These are not counted among the 185 theorems of the 4.19 core. The mathematical PNT constants and eventual threshold are existential, not a certified numerical cutoff. No full factoring complexity statement is proved by this adapter.
