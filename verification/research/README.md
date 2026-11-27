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

## KeyBreak compressed unconditional route

Run `python3 verification/research/verify_keybreak_compression.py` (standard library). Executed with Python 3.13.5. Output:

```
exact leading constants: 801/100 306/25 direct 28 target 40
finite schedules: 18 depth range: 333 833
exact semismooth content identities: 72000
```

Tested Git blob `85231107645e41ed4b383cc564e543f9b95293f6` matches the committed file; SHA-256 `9f6d2e9f3475ac252961c6f12f0190272d1ffe1261b821c54cddcf882fd03128`. The finite schedules use enormous symbolic bit lengths without instantiating the input integers. They test exact cutoff/shape/height guards, exact rational constant inequalities, and the semismooth content dichotomy and capped valuation cases. They do not establish the analytic transfer, practical running time, or a full factoring theorem. See [the derivation](../../docs/keybreak_unconditional_compression.md).

## KeyBreak fallback and GRH constants

Run `python3 verification/research/verify_keybreak_fallback.py` and `python3 verification/research/verify_keybreak_grh.py` (standard library). Executed with Python 3.13.5. Output:

```
fallback exact leading constants: 17 4959/100 target 100
fallback finite schedules: 18 depth range: 81 206
original geometry: exact target 74/25
revised geometry: exact target 59/20
revised finite schedules: 18 depth range: 111 274
```

Fallback tested blob `ce9361b129c86f87226d2c82e73e2ea46fd1af65`; SHA-256 `b497b0d76597f7bc46e31e98682e5484ab84a0714e927e2f3740fb00abc1cc19`. GRH tested blob `6cb2c6d8e2543662f6d29b2494f454c4920c1de8`; SHA-256 `596a5e465ea8da00c3679e1cf156bfedf4c48385dbca3ac28d9dc1160f1e6d31`. Both match their committed source. These are exact checks of rational parameter inequalities, squared positive margins for radicals, and the specified finite exponent guards at symbolic bit lengths; they do not prove the full source or changed-range analytic estimates. See [U100](../../docs/keybreak_unconditional_fallback.md) and [G2.96/2.95](../../docs/keybreak_grh_constants.md).

## KeyBreak ordinary and semismooth proof checks

Run `python3 verification/research/verify_keybreak_covariance.py` (standard library). Executed with Python 3.13.5. Output:

```
full-content cases: {'capped-parent': 78, 'exact-parent': 24, 'excluded-content': 126, 'unit-parent': 84, 'weighted-content': 156}
conditional projection identities: 36
common-determinant inequalities: 170723
weighted imprimitive induction identities: 90
```

Tested Git blob `cb46a73f00871b5b4be8296df61a9353385be5b8` matches the committed script; SHA-256 `510142605c0f0777dafbae8211579b1a78607d3e545b5ca1a48174afcee46abe`. The finite checks compare exact odd content numerators with the divided-cell counts, including both cap-one and higher-cap parent valuations; verify the ideal CRT full-content law, conditional independence and projection identities; check the squared lcm inequality; and compare weighted imprimitive character induction with direct sums. The earlier U100 and U40 schedule scripts were also rerun successfully (36 schedules and 72,000 semismooth content identities). These exact checks do not certify the asymptotic covariance, analytic imports, bit-complexity proof or practical runtime. See [U100 written proof](../../docs/keybreak_u100_proof.md) and [U40 written proof](../../docs/keybreak_u40_proof.md).


## U14.1 and scale-breaking checks

Run the following standalone scripts (Python 3.13.5; SymPy 1.14.0 for the last two).

- `verify_keybreak_u142.py`: exact 14.2 and 14.1 recursive margins and 18 symbolic schedules (depth range 87–216). Tested blob `25feb8ef6a81e29d013af7d89bed459863800e46`; SHA-256 `a0d5a22950ceaa19c01c74d5bfbd1cfe04bada768ea757245bf6b62ab0128c28`. Tightened 14.1 margins: `9659059/87600656250`, `135796037/700805250000`. See [written proof](../../docs/keybreak_u142_proof.md).
- `verify_exact_descent_certificate.py`: 500 exact Smith kernel matrices and 26,024 sign-pattern tests; cubic-field compact relation `[-3,0,1,1,0]` modulo 77 with all 1,024 sealed private tuples (256 gcd outcomes each for 1,7,11,77); 149 exact lattice content transformations, 7 nonunit-content skips. Tested blob `13e7640339b0c75eefc5f5f03d3b8ae1cecca4c4`; SHA-256 `2189c876ccf5647fc819ac5db3aa5cb88c5b38b7bb95c0aa56eb9a0316cb9c88`. This is not a full implementation of Ge's ideal refinement or certified logarithmic recovery. See [certificate](../../docs/exact_descent_unit_certificate.md).
- `verify_sealed_polynomial.py`: 144 exact CRT coverage patterns including prime powers; 1,775 public lattice candidates in 30 sampled fixtures, 179 reducible, 123 sufficient certificates, 121 certificate splits, six fixtures producing verified proper factors. Candidates within a fixture are correlated, and most larger fixtures failed. Tested blob `671e0d2d69d10db5dbf9a5e966f420f1edbf78c7`; SHA-256 `0a797339071a0ccee20c4c7eae43ef5d9a8703041829d6234bef5031e9bea50f`. See [complete per-fixture results and scope](../../docs/sealed_polynomial_certificate.md).

All three committed blobs match the locally executed scripts. The earlier U100/U40 and covariance scripts were rerun successfully (36 schedules, 72,000 semismooth content identities, 170,723 determinant inequalities, 36 projection and 90 induction checks). These checks verify exact finite identities and numerical inequalities, not the general analytic proof or asymptotic witness supply. No full repository, PDF or Lean rebuild was performed.

## Quarter-scale terminal interpolation and discriminant checks

Run `python3 verification/research/verify_terminal_interpolation.py` (Python 3.13.5, SymPy 1.14.0). Executed locally, with the tested Git blob `f1fc1142ce24b34632a84a66d69ac600c54ded6a` matching the committed file; SHA-256 `8eb4bb71e2a2be43393472507560aae91917b2201bf1427eb877b3145b8a414b`.

```
primitive binary transformations: 1061 local inequalities: 1927 sharp even-degree local fixtures: 27
arbitrary-image odd-degree fields: 24 exact norm/image/bracket checks: 144
rigidity finite fixtures: {'compact exponent checks': 3500, 'explicit multiplicity relations': 3, 'nonproduct correction fixtures': 5, 'product correction fixtures': 3}
``

The first part checks the exact discriminant scaling, local content valuations, squared rational diameter inequality and equality examples, including degree-drop/infinity handling. The second verifies modular root, irreducibility, integer norm and half-integer real-root sign brackets. The last uses exact polynomial remainders for bounded exponent combinations and verifies the explicit multiplicity relations in product-correction fixtures. It does not certify general numerical log rank or the asymptotic relation supply; those statements have separate proofs. See [discriminant bound](../../docs/projective_discriminant_barrier.md), [interpolation rigidity](../../docs/norm_one_terminal_interpolation.md), and [ideal reduction and support](../../docs/terminal_ideal_reduction_and_support.md). No full repository, PDF or Lean rebuild was performed.


## Correlated ideal-image transport and parity progress

Run the three standalone scripts below with Python 3.13.5 and SymPy 1.14.0. All executed locally; their committed Git blobs match the tested files.

- `verify_joint_ideal_transport.py`: 250 joint Smith/parity blocks; 184 odd pivots; 94 sufficient-parity cases; 85 strict novelty-batch gains; 250 relative projections and 216 strict packet savings; 15 exact trace-Gram base ideal reductions and 30 extension ideal identities. The manufactured four-row shared-base fixture modulo 1189 has old separate valuation rank four and verified relation (-1,1,1,-1); all 256 private-root tuples give 128 proper gcds. Blob `581804e86f20a64e842d335f029781ff0eefadd4`, SHA-256 `094c64c4af84b2b015725f7580079d3a8e32109f9db05c5fa7f5febf85c9c414`. See [proof and implementation scope](../../docs/shared_base_norm_transport.md#7-exact-finite-check-receipt-and-packet-construction).
- `verify_ramified_packets.py`: 25 constructed fields, 49 local discriminant guards, 289 norm evaluations, 144 cross-map identities, 200 rank cases. Includes repeated modular roots and verified sign brackets in the real subfamily. A manufactured cross-map fixture modulo 1189 with relation (1,1,1,-1) gives 128 proper gcds over 256 private-root tuples. Blob `8226685aba49fa128a2f2d37dd3d2bf57aa0d340`, SHA-256 `0555cb84d8b4c10b92ab14e3e0afee0ec48ca9f3b4d7ffc2b985e7516d4ad423`. See [ramified construction and capacity bound](../../docs/ramified_packet_generation.md).
- `verify_parity_quotient.py`: 200 integer anchor batches, 8,976 exhaustive binary membership comparisons, 68 strict parity gains (18 with unchanged rational rank), explicit even-factor repair. Blob `b0471f221ee85915843742bc31a2597f2f531765`, SHA-256 `ac3715e5c4de54c91971c1fe394096e2d8f6f8eb65ca1ed7bd96261f84e8edad`. See [exact parity progress](../../docs/joint_ideal_image_transport.md#7-exact-binary-quotient-and-a-parity-progress-target).

The constructed factoring fixtures intentionally have known public correlated expressions; they exercise the certificate under all possible sealed-root fibres and do not estimate random relation supply. The actual ideal reductions in the first script use a real cubic base with explicit order arithmetic; the two degree-nine extension reductions are chosen explicit multiples, not a general higher-degree LLL implementation. The first local script's initial HNF domain mismatch was repaired by converting a checked integral rational matrix to an integer matrix. No full implementation of Ge's general ideal refinement or the general certified unit-log recovery was exercised by these scripts. No full repository suite, Lean or PDF rebuild was performed.
