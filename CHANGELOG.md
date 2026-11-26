# Changelog

## Mathlib reuse — 26 November 2026

Four additional checked modules (185 named theorems in 22 modules overall). Reuse Dirichlet's unit theorem, localization, Dirichlet-character orthogonality, smooth numbers and finite-field quadratic-character counting. The affine-to-projective numerical transfer retains the actual point-count hypothesis. No end-to-end factoring bound is claimed.

## Lean finite theorem continuation — 26 November 2026

Extended the checked project to eighteen modules and 169 explicitly named theorems. The main finite mixed-prime quadratic-chain theorem now has an executable supplied-M routine, certified soundness, exact success probability, and abstract arithmetic budgets. The deterministic exponent-saturation lemma is certified under its finite density and modular-certificate guards, and its cost transfer is formalized under explicit cost hypotheses. Added ramification-sensitive local Gram matrices and uniform group/linear projection fibres, the adaptive peeling invariant, and verified Krylov correction from a supplied recurrence. All proof modules pass a clean warning-free build and compiled axiom audit. The complete asymptotic factorers and their analytic obligations are not yet formalized.

## Lean component formalization — 25 November 2026

Added five Lean proof modules in priority order: deterministic parameter schedules, sparse Gram linear algebra, repaired randomized recurrences, executable quadratic coefficient arithmetic, and square-root factor extraction. Universal proofs strengthen the earlier finite checks of the schedule and path maxima. Added a pinned Lean/mathlib project, warning-failing builds, a compiled-declaration axiom audit, reproducible source hashes, and CI. This is a component formalization; analytic complexity, arithmetic construction, and probability bridges remain explicit open formalization tasks.

## 0.1.0 — 25 November 2026

First public research collection: five manuscripts, explicit theorem and dependency status, comparison bounds with pinned references, exact finite checks, a quadratic relation-chain implementation, build workflows, and CC BY 4.0 licensing.

This collection supersedes the working-note presentation at research snapshot `94d84cf90cc958aebde8853a1ecfcda304f60500` of `JoseBrox/factoring-algorithms`. Historical notes remain available as provenance. Publication of the collection does not change conditional results into unconditional ones.
