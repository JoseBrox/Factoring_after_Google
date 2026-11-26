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
