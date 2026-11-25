# Lean formalizations

These files prove selected mathematical components of the factoring manuscripts. They include universal parameter inequalities, finite matrix arguments, recursion bounds, and an executable quadratic coefficient routine with a soundness proof. **They do not constitute an end-to-end formal proof of any claimed factoring complexity bound.**

The sources favor short proofs with explicit hypotheses. Theorems stated for every parameter or path depth are proved universally; the small executable examples are identified separately.

## What to read first

Names below belong to the namespace `Factoring.<module>`. For example, the first theorem is `Factoring.Deterministic.schedule_valid`.

| Priority and source | Main theorems | What Lean proves |
|---|---|---|
| 1. [Deterministic](Factoring/Deterministic.lean) | `schedule_valid`, `exists_rational_epsilon_schedule`, `power_budget_minimax`, `height_budget_margin` | All 19 schedule inequalities throughout the stated interval; an admissible rational parameter for every real ε > 0 with height exponent below 2/3 + ε; the limitation of the specified affine height constraints. |
| 2. [Gram](Factoring/Gram.lean) | `odd_block_identity`, `odd_block_posSemidef`, `even_block_posSemidef`, `schur`, `entryProduct_above_ones`, `sparse_average` | Local outer-product identities and positivity, the real Schur product theorem, preservation of the all-ones matrix lower bound, and the finite sparse averaging inequality. Repeated local classes are allowed. |
| 3. [Recursion](Factoring/Recursion.lean) | `m1_upper`, `m2_upper`, `repaired_root_margin`, `exponential_recurrence_bound`, `repaired_time_bound`, `workspace_bound` | Path bounds at every natural depth, exact repaired margins, and conditional time/workspace recurrences with coefficients 91.4 and 19. |
| 4. [Quadratic](Factoring/Quadratic.lean) | `power_eq_spec`, `eval_power`, `norm_power`, `reduce_power`, `split_sound` | Quadratic ring arithmetic, correctness of binary powering, compatibility with reduction, and that every returned candidate is a proper divisor. |
| 5. [SquareRoot](Factoring/SquareRoot.lean) | `proper_factor_of_product`, `proper_factor_of_square_congruence` | A supplied square congruence with both trivial signs excluded yields a proper gcd factor. Even moduli, repeated prime factors, and noninvertible roots are permitted. |

## Understanding the contracts

**Deterministic parameters.** `exists_rational_epsilon_schedule` proves an existence statement over exact real and rational numbers. It does not connect the height parameter to a program's running time. The minimax statements concern their displayed constraints, rather than a lower bound for all factoring algorithms.

**Gram argument.** Positive semidefiniteness means that every real quadratic form associated with the matrix is nonnegative. Entrywise products preserve it. The stronger all-ones lower bound means that `A - J` is positive semidefinite, where every entry of `J` equals one. `sparse_average` combines these hypotheses over a finite collection, subtracts an explicitly bounded diagonal, and produces a large off-diagonal entry. Identifying these abstract matrix entries with quadratic ideal-character coefficients is still outside the formalization, as are the required analytic estimates.

**Recursion.** The path maxima use exact difference identities and induction. The time theorem bounds a sum of three exponential costs, reserving 0.01 of the coefficient to absorb their addition. Both time and workspace theorems allow an arbitrary threshold: the recursive inequalities hold above it, and the desired initial bounds are explicit hypotheses below it. Proving that the actual algorithm satisfies these hypotheses, including its enlarged analytic and probabilistic contract, remains necessary. No automatic asymptotic transfer or absorption of arbitrary initial costs is asserted.

**Quadratic arithmetic and extraction.** Evaluation lemmas assume a supplied root satisfying its quadratic equation. The executable splitter works directly with coefficient pairs and supplied exponent parameters. Its soundness theorem guarantees correctness of a returned factor, not that a factor will be returned. Likewise, square-root extraction assumes the congruence and excludes both trivial signs; producing suitable roots and proving success probabilities are separate tasks. Smoothness, equidistribution, number-field constructions, and overall operation counts are not certified by these files.

## Reproduce the checks

The project pins **Lean 4.19.0** in [lean-toolchain](lean-toolchain) and mathlib commit **`c44e0c8ee63ca166450922a373c7409c5d26b00b`** in [lakefile.toml](lakefile.toml). The committed [lake-manifest.json](lake-manifest.json) also fixes the transitive dependency revisions.

With Git, Python 3, and the pinned Lean/Lake toolchain available, start at the repository root:

```sh
cd lean
lake exe cache get $(python3 ../scripts/verify_lean.py --imports)
cd ..
python3 scripts/verify_lean.py
```

The cache command fetches the required mathlib modules. The verifier checks dependency revisions and tracked/untracked source cleanliness, builds every project module with warnings treated as errors, and runs [Audit.lean](Audit.lean). It writes compilation logs, the axiom inventory, tool versions, and a source-hash receipt to `build/lean/` at the repository root. The initial passing run's receipt and full axiom inventory are preserved in [the build evidence](../verification/lean/README.md).

The audit examines every persistent logical declaration, including private and generated proofs. Unsafe compiler runtime objects are counted separately and excluded only as audit roots; traversal of logical proof dependencies is unfiltered. The only allowed axioms are `propext`, `Classical.choice`, and `Quot.sound`; the audit rejects logical project axioms and additional proof dependencies such as `sorryAx` or native-decision axioms. Project proofs use neither `sorry` nor `native_decide`. All executable examples are named theorems and included in the inventory. A successful audit certifies the component theorems under their actual hypotheses; the remaining manuscript bridges retain their stated proof status.
