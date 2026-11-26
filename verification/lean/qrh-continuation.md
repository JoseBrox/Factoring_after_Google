# QRH and arithmetic continuation — 26 November 2026

## Build evidence

- [Run 45832975266](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45832975266), commit 7089eec: all three candidates compiled with warnings as errors, and the 13 explicitly printed axiom reports passed (BitArithmetic 8, EulerDecay 2, LatticeClearing 3). They were promoted into the core in 910d7b4.
- [Run 45833320193](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45833320193), commit 910d7b4: **successful aggregate build and complete declaration audit**, reporting 536 logical declarations including 427 kernel theorem objects. The core at that commit contains 211 explicitly named source theorems in 26 modules, up from 195 in 23 modules.
- [Run 45833684962](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45833684962), commit b3bd9c9: ModularBits compiled without errors/warnings and every one of its 11 printed axiom reports lists only the three standard axioms (or no axioms). The whole workflow failed on a separate CharacterMoments error, subsequently fixed. The exact ModularBits source was promoted in d3d7497.
- [Run 45834125543](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45834125543), commit 0abf4a4: CharacterMoments compiled without errors/warnings and all three printed axiom reports were accepted. The overall run failed on a separate DeterminantHeight missing-import error. The exact checked CharacterMoments source was promoted in 335b76e.
- Thus the current promoted core has 225 explicitly named source theorems in 28 modules; the newer aggregate build has not yet been confirmed in this receipt. Do not confuse the source theorem count with Lean's generated kernel declarations.
- DeterminantHeight initially failed for missing real ring imports. The corrected source at bb7599a has both theorem roots accepted by Lean with only standard axioms, but the strict linter rejected one unused hypothesis. This was removed in 37b49b9; a fresh passing strict run is required before promotion.
- The previous audit script could report passing axiom roots even after a file failed elaboration, although the overall workflow correctly failed. The revised script and workflow at 83b91e3 and 1c2ce22 require the actual per-file strict compiler exit code and report every file independently. This is a reporting correction, not a weakening of the kernel checks.

## QRH source build

[Run 45829584073](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45829584073) stopped before compilation: the pinned closure contained 2930 local modules and 258 mathlib roots, and the additional imports Architect and RellichKondrachov.Analysis.FunctionalSpaces.Sobolev.Euclidean.Rellich required pinning. Both packages have been pinned to the exact upstream manifest revisions. The corrected [run 45832742669](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45832742669) has passed closure discovery and toolchain installation and was still building when inspected. No new fresh QRH verification is claimed.

The isolated proof target remains separate from Lean 4.19.0 and PNT+ 4.36.0. The independent comparator receipt and mathematical scope audit remain as in [quasi_rh_audit](../../docs/quasi_rh_audit.md).

## Mathematical developments not yet Lean-certified

The new written [weighted AP proof](../../docs/qrh_weighted_progressions.md) derives the enlarged main two-sided asymptotic from QRH and strong PNT via actual ordered-tuple character moments. The [rough and bad-child proof](../../docs/weighted_rough_bad_child.md) also treats the local-limit density, nearby tuned-scale comparability and the actual source's exceptional sets. The finite character moment inequality itself is now checked in CharacterMoments; the complex-analytic estimates, uniform probability estimates and full randomized contract are not.

The determinant height and modular exponentiation modules are pending final strict checking; no full Turing-machine bit-cost theorem is claimed. See the [completion register](../../docs/lean_completion.md) for the fixed metric.
