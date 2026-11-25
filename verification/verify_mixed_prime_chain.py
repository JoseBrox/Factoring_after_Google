"""Independent exact tests of the general mixed-prime N1101 chain.

The factor routine receives only n, b, M, a. Known prime divisors are used
solely to construct promised test inputs and check the proved success set.
"""
from math import gcd
from verify_ramification_and_relation import relation_chain_factor
import json

counts = {'promised_instances': 0, 'tested_parameters': 0,
          'forced_success_witnesses': 0, 'proper_factors': 0}
for p in (3, 5, 7, 11):
    for q in (3, 5, 7, 11):
        if p == q:
            continue
        for n in (p*p*q, p*q*q, p*q*13):
            b = next(x for x in range(1, n)
                     if gcd(x, n) == 1
                     and pow(x, (p-1)//2, p) == 1
                     and pow(x, (q-1)//2, q) == q-1)
            for M in (p-1, 2*(p-1), 3*(p-1)):
                counts['promised_instances'] += 1
                success = 0
                for a in range(n):
                    factor = relation_chain_factor(n, b, M, a)
                    counts['tested_parameters'] += 1
                    if factor is not None:
                        assert 1 < factor < n and n % factor == 0
                        success += 1
                        counts['proper_factors'] += 1
                    value = (a*a-b) % p
                    if value == 0 or pow(value, (p-1)//2, p) == p-1:
                        assert factor is not None, (p, q, n, b, M, a)
                        counts['forced_success_witnesses'] += 1
                assert 2*p*success >= (p+3)*n

# Exact N1124 transfer screen: all traces and the characteristic polynomial
# can coincide while kernel dimensions differ, even for symmetric F_2 matrices.
A = ((1, 1), (1, 1))
A2 = tuple(tuple(sum(A[i][k]*A[k][j] for k in range(2)) % 2
                 for j in range(2)) for i in range(2))
assert A2 == ((0, 0), (0, 0))
assert (A[0][0]+A[1][1]) % 2 == 0
assert (A[0][0]*A[1][1]-A[0][1]*A[1][0]) % 2 == 0
assert A != A2

print(json.dumps({
    'checks': counts,
    'symmetric_trace_counterexample': {'A': A, 'A_squared': A2,
                                      'characteristic_polynomial': 'T^2',
                                      'ranks': [1, 0]},
    'scope': 'Exact finite checks of the mixed-prime theorem and trace screen; no asymptotic runtime claim is tested.'
}, indent=2))
