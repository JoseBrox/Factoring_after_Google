"""Exact affine-power checks for the deterministic 2/3+epsilon schedule.

This certifies rational inequalities only. The analytic proof is in the notes.
Run with Python 3; no external packages are required.
"""
from fractions import Fraction as F
import json

# Each pair represents constant + slope * delta, 0 < delta <= 1/100.
def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def sub(x, y):
    return (x[0]-y[0], x[1]-y[1])

def mul(n, x):
    return (n*x[0], n*x[1])

one = (F(1), F(0))
a = (F(1,3), F(0))
t = (F(1,3), F(1))
k = (F(1,3), F(2))
v = (F(1,3), F(5,2))
b = (F(1,3), F(3))
j = (F(1,3), F(4))
r = (F(1,3), F(5))
c = (F(1,3), F(6))
h = (F(2,3), F(8))
s = (F(0), F(1))
m0 = sub(one, a)
assert sub(h, b) == r

gaps = {}
for (nx, x), (ny, y) in zip(
    [('a', a), ('t', t), ('k', k), ('v', v), ('b', b), ('j', j), ('r', r)],
    [('t', t), ('k', k), ('v', v), ('b', b), ('j', j), ('r', r), ('c', c)]):
    gaps[ny+'>'+nx] = sub(y, x)
gaps.update({
    'h>1-a': sub(h, m0),
    'h>a+c': sub(h, add(a,c)),
    'r>2/3-b': sub(r, sub(m0,b)),
    'b>2/3-v': sub(b, sub(m0,v)),
    'b>2/3-b': sub(b, sub(m0,b)),
    'h+b>2c': sub(add(h,b), mul(2,c)),
    '3>2h+r': sub(mul(3,one), add(mul(2,h),r)),
    'h>1-b+delta': sub(h, add(sub(one,b),s)),
    'c>j+delta': sub(c, add(j,s)),
    '1>h': sub(one,h),
    '1>r': sub(one,r),
    '1-b>b': sub(sub(one,b),b),
})

for name, (constant, slope) in gaps.items():
    # An affine function is positive throughout this half-open interval iff
    # its zero-end limit is nonnegative, it is not identically zero there,
    # and its closed right endpoint is positive.
    assert constant >= 0, (name, constant, slope)
    assert constant > 0 or slope > 0, (name, constant, slope)
    assert constant + slope/F(100) > 0, (name, constant, slope)

# Independent finite counterexample to the literal printed Proposition 6.2.
p = 5
values = [(x**3+2*x) % p for x in range(p)]
legendre = lambda z: 0 if z == 0 else (1 if pow(z,2,p) == 1 else -1)
assert values.count(0) == 1
assert sum(legendre(z) for z in values) == -4

print(json.dumps({
    'interval': '0 < delta <= 1/100',
    'verified_affine_inequalities': len(gaps),
    'spectral_guard_power': '5/3 + 21 delta < 3',
    'source_character_sum_counterexample': -4,
    'scope': 'Exact power comparisons and a finite counterexample only; no analytic theorem is computationally certified.'
}, indent=2))
