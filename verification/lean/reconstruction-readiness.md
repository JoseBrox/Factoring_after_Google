# Reconstruction, arithmetic and readiness continuation — 26 November 2026

## Verified components

- [Run 45834603731](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45834603731), commit 37b49b9: strict individual compilation and axiom reports for DeterminantHeight and ModularPower succeeded. Both were promoted at e95b3a3. The actual digit-list modular exponentiation is correct, with a cell-count budget of at most the initial remainder cost plus twice the exponent bit length times the modular multiplication budget.
- [Run 45835090424](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45835090424), commit e95b3a3: complete aggregate audit succeeded, 608 logical declarations including 475 kernel theorem objects.
- [Run 45835727903](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45835727903), commit 64286c1: BinaryGCD passed strict compilation and all nine named proof roots (the aggregate candidate job failed on a different module). Promoted at b1ce73b. The actual digit-list Euclidean gcd is correct, and its cell cost is bounded by 8n^3 + 20n^2 + 2n for equal-width inputs (see theorem for the precise width convention).
- [Run 45836362453](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836362453), commit b1ce73b: complete aggregate audit succeeded, 654 logical declarations including 505 kernel theorem objects.
- [Run 45836411619](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836411619): SaddleCalculus passed strict compilation and all five named roots (another candidate failed). Promoted at 439f2b9.
- [Run 45836806888](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836806888), commit 439f2b9: **successful warning-free aggregate compilation, pinned dependencies and full compiled axiom audit**, 661 logical declarations including 510 kernel theorem objects. This is 243 explicitly named source theorems in 32 modules. No nonstandard axioms were accepted.

The bit-cell results are not a full multitape-machine execution proof. SaddleCalculus establishes exact finite derivative, positivity, uniqueness and second-difference statements, not a full uniform saddle asymptotic. [Run 45837470102](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45837470102) confirmed strict compilation and all three named roots of ReadinessTransfer (other candidate errors persisted). The exact checked readiness module was promoted, bringing the core to 246 named theorems in 33 modules; its new aggregate run is pending. RationalRecovery and SaddleDecay remain staged pending strict success.

## QRH integration

The [source build](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45832742669) failed on three RellichKondrachov modules. Commit efb10ff verifies and applies the pinned upstream patch rellich-kondrachov-lean4341.patch (blob 43600843a74f7736b17db51af4783dc7ba69f6a2), verifies the target dependency revision, and preserves logs with pipeline failure propagation. The [patched rebuild](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836288815) was still running when inspected; no completed project QRH source build or exact axiom audit is claimed in this receipt.

## Written mathematics, not full Lean proofs

- [Uniform deterministic saddle/Edgeworth expansion](../../docs/deterministic_saddle_proof.md), including the derivative bound and covariance second difference.
- [Effective number-field reconstruction](../../docs/effective_number_field_recovery.md), with explicit precision and certificate-size bounds under the stated valuation, norm and unit-lattice inputs.
- [Enlarged lattice-fibre coupling and backward readiness implication](../../docs/randomized_fibre_coupling.md).
- [Enlarged local conditional moment transfer](../../docs/randomized_local_moments.md), conditional on QRH and the stated reduced-basis and homogeneous linear-form inputs. The rough bad-child argument is corrected to require only the square-root cap, and the mean exponent uses the actual-node bound 17/18 rather than the abstract admissibility ceiling .96.

The rational-root smoothing, actual sampler and all-history hypotheses, ideal/valuation construction, square certification and full bit-machine endpoint remain open; see the unchanged fixed 36-package [completion metric](../../docs/lean_completion.md). None of these larger packages is counted checked merely because a constituent theorem or a written proof is present.
