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
