#!/usr/bin/env python3
"""Exact rational and finite symbolic guards for U14.2; not an analytic proof."""
from fractions import Fraction as Q
from math import isqrt

c, b, v, s0 = Q(233, 1000), Q(151, 100), Q(301, 100), Q(401, 200)
kappa, a, hstar = 9, 44, 265
pA, pden, target, theta = Q(171, 50), Q(453, 100), Q(71, 5), Q(21, 125)


def ceilq(x):
    return -(-x.numerator // x.denominator)


def check_constants():
    R0, R1 = Q(1, 2*kappa), v/(2*kappa*a)
    H = (3 + v/kappa + 2*v/(kappa*a))/c**3
    r = (1 + v/(2*kappa))/(3*b*c)
    p = a*c/3
    assert H < hstar < (a-v)*b/c
    assert 2 < s0 < 3 and 1+s0 < v < kappa
    assert (2*v-4)*b > r and 4*R0 < 1
    assert 0 < R1 < Q(127,128)*R0
    assert (5*v+1)*R1 < 1
    assert p < pA and p+r < pden
    assert (2*v-1)*b-pden > 3
    assert v/(2*kappa) < theta
    s = b+2*kappa*c/3
    va, vr = s+pA, s+pden
    assert (s, va, vr) == (Q(727,250), Q(791,125), Q(3719,500))
    direct = max(3*b, vr+max(b, 2*c/3), vr+2*b, 28*c, b+2*c)
    assert direct == Q(5229,500) and direct < 11 < target
    assert 0 < s < target and 0 < va < target
    assert (1-s/target)**3 > Q(1,2)
    assert (1-va/target)**3 > theta
    print('exact coefficients:', 'shape', s, 'algebraic', va, 'raw', vr,
          'direct', direct, 'target', target)
    print('strict cube margins:', (1-s/target)**3-Q(1,2), (1-va/target)**3-theta)


def check_tighter_target():
    s, va, C, shrink = Q(727,250), Q(791,125), Q(141,10), Q(3011,18000)
    assert Q(301,1800) < shrink
    assert (1-s/C)**3 > Q(1,2) and (1-va/C)**3 > shrink
    print('U14.1 strict cube margins:', (1-s/C)**3-Q(1,2), (1-va/C)**3-shrink)


def degree(n, mb):
    threshold = c**3*n
    lo, hi = 1, 1
    while hi**3*mb < threshold:
        hi *= 2
    while lo < hi:
        mid = (lo+hi)//2
        if mid**3*mb >= threshold:
            hi = mid
        else:
            lo = mid+1
    d = max(3, lo | 1)
    assert d % 2 and d**3*mb >= threshold
    assert d == 3 or (d-2)**3*mb < threshold
    return d


def schedule(n):
    mb = n.bit_length()
    d = degree(n, mb)
    t, k0 = d*mb, kappa*d
    eb, e0 = ceilq(b*t/c), (n-5)//(2*k0)-1
    assert e0 > eb
    def ve(e): return ceilq(v*e)
    def nxt(e): return max(eb, ceilq(Q(hstar*t+ve(e),a)))
    e1 = nxt(e0)
    # Conservative integer upper bounds on log_2 M, H and the reference height.
    mhi = ceilq(Q(n,d))
    mlo = (n-1)//d - 1
    re = t*(isqrt(d-1)+1)
    he = d+20+10*d.bit_length()+2*mhi+2*ve(e0)+4*e1+2*re
    assert he+mhi+2+(32*(d+2)).bit_length() <= hstar*d*t
    assert he+mhi+4 < n-1
    assert 125*(hstar*d*t+d*ve(e0)) <= 21*(n-1)
    assert 18000*(hstar*d*t+d*ve(e0)) <= 3011*(n-1)
    assert 2*ve(e0)+2 <= mlo
    assert 5*ve(e1)+e1+20 <= mlo
    e, levels = e0, 0
    while e > eb:
        f = nxt(e)
        assert eb <= f < e and hstar*t+ve(e) <= a*f
        assert ve(e)-e >= 6
        assert Q(ve(e)-e) > s0*eb
        e = f
        levels += 1
    mk = k0.bit_length()
    k = k0 + ceilq(Q(k0,mk))
    Lx = (n-1)//2-2
    Sb = k*e0-Lx
    Jb = 2*(Sb+k)//k
    Dc = k*Jb//2
    emin = ceilq(Q(127*e0,128))
    assert Sb >= 0 and k <= 2*k0 and Sb <= Dc <= Sb+k
    assert 2*mk*(Jb+1) >= e0 and Jb+1 <= e0//128
    assert emin > e1 and e0-Jb-1 >= emin
    return levels


if __name__ == '__main__':
    check_constants()
    check_tighter_target()
    lengths = [2**a+j for a in (1000,1100,1200,1500,2000,2500) for j in (0,1,19)]
    levels = [schedule(n) for n in lengths]
    print('finite schedules:', len(levels), 'depth range:', min(levels), max(levels))
