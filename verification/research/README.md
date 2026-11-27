## Polynomial-mark research experiment

Run `python verification/research/polynomial_marks.py` with SymPy and mpmath installed. This is deliberately separate from the standard-library verification runner. It uses exact integers for polynomial congruences, sign brackets, norms, rational rank, valuation relation and modular checks. Numerical logs and rank decisions are candidate generation only, not certified estimates.

Observed output:

```
monic construction: N=1000036000099 d=54 ell=227 all 108 sign brackets verified
polynomial marks: retained=123 rows=65 exact rational rank=65
exponent certificate: base=5 M=2105280 modular power=1
split: gcd(34-1,77)=11
```

See [the new algorithm and open covariance hypothesis](../../docs/monic_polynomial_mark_factorer.md).

## Targeted and ramified-target checks

Run `python verification/research/targeted_marks.py` and `python verification/research/ramified_target.py` with SymPy installed. The manufactured rank-zero example checks exact polynomial identities and an exponent certificate; it uses a known exponent when constructing the fixture. The separate large-prime example checks 561 integer resultants and 56 large-prime incidences. The ramified-target check verifies the exact CRT construction, both Eisenstein conditions, 16 real-root sign brackets and six resultant norms, and the particular target valuation equation. It explicitly does not verify an order certificate for that fixture. See the two corresponding research notes for proofs and scope.

## Factor refinement without prime factorization

Run `python verification/research/factor_refinement.py` with SymPy installed. The exact prototype checks all ideal product and comaximality equalities on two fixtures, including one overorder enlargement, and verifies the manufactured target certificate and gcd for N=15. The observed output and tested source hash are in [the factor-refinement note](../../docs/full_degree_factor_refinement.md). This verifies the finite computations, not uniform target coverage or a Lean theorem.

## Scalar-free target and common-order checks

Run `python verification/research/normalized_target.py` with SymPy and the earlier `factor_refinement.py` in the same directory. The exact checked source and output are recorded in [the scalar-free coverage note](../../docs/scalar_free_target_coverage.md). The script verifies diagonal scalar elimination, an exact positive certificate, all quotient-ideal congruences through the first positive gluing exponent 2310 in the N=77 example, and a private-prime negative example with normalized rank 6. These are finite checks, not a uniform coverage result.

## Forced coupled norms and rank-one extraction

Run `python verification/research/coupled_norm_marks.py` with SymPy and `python verification/research/one_field_certificate.py` with the standard library alone. The first checks exact forced norms, coupled valuation rank, the negative target interpolation example, and explicit full-rank units in two fields of degrees six and eight. The second performs a complete one-field finite relation search on N=77, verifies actual ideal valuations at simple roots, and uses 96-bit directed rational intervals and the unit-lattice separation bound to certify the recovered rational coordinate. It then checks the modular exponent and proper gcd. See [the one-field research note](../../docs/one_field_rank_one_coverage.md) for the proved construction, exact extraction criterion, and unresolved asymptotic existence theorem.

## Exact 2-adic and adverse-field experiments

Run `python verification/research/padic_certificate.py` (standard library only) and `python verification/research/adversarial_field.py` (SymPy). The first reconstructs the exact unit coordinate of the N=77 relation by integer 2-adic lifting, using 122-bit modulus precision; it also checks 70 signed compact exponents and 40100 norm-gap cases. The second constructs an intentionally adverse C of 3455 bits for 21 mark polynomials, refines to 18 pairwise coprime factors, and verifies every one of the 17 nonexceptional private-support certificates without prime factoring. The exact tested script hashes and output are recorded in [2-adic extraction](../../docs/padic_rank_one_extraction.md) and [adversarial parameters](../../docs/adversarial_rank_one_parameter.md). These are finite checks, not proof of general successful coverage.

## Positive smooth-relation rank driver

Run `python verification/research/positive_smooth_relations.py` with the standard library. It independently compares the exact arithmetic-progression scanner on 285 present and 50 absent residues, builds full-rank positive modular relation systems for N=47053 and N=23707, verifies their determinants with Bareiss, and obtains factors by exact modular gcd scans. The finite rank fixtures use small exhaustive product tables in place of the asymptotic AP search. See [the new proof](../../docs/positive_smooth_relation_coverage.md) for uniform randomized coverage and the remaining deterministic selection problem.

## Common-translation rank driver

Run `python verification/research/common_translation.py` (standard library). It independently checks the AP scanner on 24 unit residues, all 1296 small translation matrices at T=L+1, a singular example at T=L, and exact determinants, modular relations and gcd splits on N=899, 47053 and 23707. The three rank fixtures use exhaustive small product tables, not a uniform half-scale hitting-set implementation. Exact test output and source hashes are in [the common-anchor note](../../docs/common_anchor_derandomization.md).

## Narrow-band streaming atoms

Run `python verification/research/narrow_band_streaming.py` with the standard library. The test verifies 61,440 exact streaming atom decisions, 5,120 full lift decisions against finite tables, 24 exact conditional-count DP cases, and an independent-anchor rank certificate giving a factor of 21. The exact checked source hash and proof boundary are in [the narrow-band note](../../docs/narrow_band_streaming_atoms.md). No asymptotic product-table search is asserted.

## Shared AP and lattice counting

Run `python verification/research/ap_lattice_count.py` with the standard library. The exact checks cover 130,680 brute-force floor sums, 1,000 large-integer identities, 1,852 CRT anchor counts plus a 44-atom fixture, 656 partial witness counts, and 974 forced signed congruences. The tested source hashes and exact proof scope are recorded in [the AP/lattice note](../../docs/ap_lattice_conditional_counting.md). These checks do not establish smooth-cofactor coverage.

## Primitive-ratio lattice and large-prime cancellation

Run `python verification/research/primitive_ratio_lattice.py` with the standard library. It independently checks 1,581 exact rectangle enumerations (including 741 collinear cases), 363 additional verified factor exits, 1,583 graph-versus-rational-kernel comparisons, all unit targets in a small disjoint-product fixture (34 count comparisons and 806 factor exits), and 100 prescribed-prefix smooth-completion counts. A further fixture modulo 77 cancels two nonsmooth ratios without factoring the residuals. The exact checked source and proof scope are in [the primitive-ratio note](../../docs/primitive_ratio_lattice_aggregation.md).

## Dyadic balancing and pooled relation rank

Run `python verification/research/target_power_balance.py` and `python verification/research/pooled_shift_relations.py` with the standard library and the earlier `primitive_ratio_lattice.py` in the same directory. The former checks 2,496 balanced lattices, 16,425 primitive local CRT completions, additional 201-bit examples, and a cycle that succeeds only across shifts. The latter verifies full pooled rank seven at N=100160063 although all separate-target ranks vanish, and independently checks the integer coordinate certificates and factor 10007. Tested source hashes, complete output and the scope of the exact checks are recorded in [the power-shift note](../../docs/power_shift_pooled_relations.md). These tests do not prove uniform cofactor coverage.

## Adaptive exponent separation and residual recycling

Run `python verification/research/adaptive_pooled_rank.py` with the earlier primitive-ratio, balancing and pooled-shift scripts in the same directory. The local run checks 100 exact dependencies, a verified factor of 47053, and several intentionally retained unsuccessful searches showing residual rank growth without base rank growth even with shared CRT prescriptions. See [the proof and test scope](../../docs/adaptive_rank_or_residual.md).

## Support-aware selection and 2-primary saturation

Run `python verification/research/two_primary_pool.py` and `python verification/research/support_budget.py` with the existing primitive-ratio, balancing, pooled-shift and adaptive rank scripts in the same directory. The tests verify 998 perfect-power cases, 4,832 independent 2-group comparisons, 150 saturation-index comparisons, a zero-pure-rank square root of unity giving factor 101, and 1,199 factor-free residual-span membership comparisons. The support-aware all-shifts search records both factors and unsuccessful pools, including full pure rank seven on the smaller prior stalled fixture. See [the proof and exact test hashes](../../docs/support_budget_and_two_saturation.md). Uniform support bounds are not established by these experiments.

## Prime-primary and common-order extraction; batch-affine tests

Run `python verification/research/primary_pool.py`, `python verification/research/common_order_factor.py` (SymPy required for this script), and `python verification/research/batch_affine_rank.py` with the earlier research scripts in the same directory. Exact checks cover 7,052 primary subgroups, 300 saturation indices, an odd-primary-only factor of 1333, three supplied-common-modulus LLL fixtures and a manufactured faithful-subgroup interface fixture, 250 affine-rank comparisons, and unsuccessful larger-pool checks. The [proof note](../../docs/primary_pool_extraction.md) gives the exact source hashes, tested outputs, local SymPy floor workaround, and proof boundary. These tests do not establish uniform relation coverage.

## Squareclass pooling at known square multipliers

Run `python verification/research/squareclass_pool.py` with the standard library and the prior primitive-ratio and two-primary scripts. It checks 2,066 squareclass memberships, 1,165 no-factor online prefixes and 92 factor exits, 480 incremental/batch comparisons, a two-ratio collision, and longer parity certificates at N=100160063 and N=1000036000099. The [proof and test receipt](../../docs/squareclass_ratio_pool.md) includes exact tested source hashes and a rigorous sparsity bound for the two-row criterion. Uniform coverage is not asserted.

## Character-lift ratio coverage

Run `python verification/research/character_lift_pool.py` with the earlier `primitive_ratio_lattice.py` alongside it. The script checks 2,000 modular linear systems against brute force, 100 large-modulus solvable systems, 380 Jacobi-labelled root exits, and four seeded finite short-ratio searches at lifting depths one through four. The finite harness ignores already found coordinate gcd factors only to exercise the new character-lift extraction. See [proof, exact receipts and scope](../../docs/character_lift_ratio_coverage.md). No deterministic uniform coverage claim is made.

## Depth-free labels and general rank increase

Run `python verification/research/depth_free_labels.py` with the standard library and the previous lattice and pooled-rank scripts. The verified tests include 177 fibre/translate comparisons, 602 additional proper-factor exits, 300 primitive annihilator checks and five full-rank finite factoring runs. The harness uses seeded random queries; it is not a deterministic coverage proof. Exact tested hashes, output and the analytic proof scope are in [the depth-free note](../../docs/depth_free_character_rigidity.md).

## Descent accounting, height and linear advice checks

Run `python verification/research/descent_and_advice_checks.py` (standard library only). Executed locally with Python 3.13.5. The committed blob matches the tested source.

```
exact small-bias eigenvalues: 80 walk survival bounds: 480
exact incidence, cost cancellation and capped-restart identities: 4
exact finite height/support checks: 60
```

Tested Git blob: `0779cbb260806dbd029e1b998d05c523800314e9`; SHA-256: `fa337fb45b64ddc2dc8010bdb4753be06c48da60ae75b689065cb2dceb331f62`. The small-field checks compare exact Walsh eigenvalues with independent polynomial-root counts, then count walks by integer transitions. Incidence and caps use exact rational probabilities. The height tests enumerate finite smooth pairs, check support preservation under reduction, and use a rational upper bound on the finite Euler product. These checks do not establish the asymptotic estimates, uniform advice construction or the adaptive CRT extension. See [linear advice](../../docs/linear_advice_half_scale.md), [height barrier](../../docs/short_ratio_scale_barrier.md), and [descent accounting](../../docs/multilevel_descent_accounting.md).
