#!/usr/bin/env python3
"""Exact rational ledger for KeyBreak GRH cap/schedule variants."""
from fractions import Fraction as Q


def radical_lt(base, multiplier, radicand, target):
    margin = target - base
    assert margin > 0 and margin**2 > multiplier**2 * radicand


def original():
    c, b = Q(3, 4), Q(19, 20)
    sA, sR = Q(43, 40), Q(5926, 12255)
    pA, pd = Q(10751, 10000), Q(15587, 10000)
    S, C, m = Q(7, 5), Q(74, 25), Q(20001, 10000)
    z0, z1 = Q(40, 81), Q(40, 81) * Q(51, 430)
    assert pA > sA and pd > sA + sR
    assert (Q(5, 3) * b - pd) / c > Q(1, 50)
    assert max(b, S+pd, Q(2), Q(49, 20), 3*b) < C
    radical_lt(S, m, z0, C)
    radical_lt(S+pA, m, z1, C)
    print('original geometry: exact target', C)


def revised():
    c, k, b = Q(151, 200), Q(91, 100), Q(19, 20)
    v, w, a, h = Q(501, 1000), Q(407, 500), Q(21, 5), Q(723, 200)
    z = v+w
    H = (1+v/k)/c**3
    r0, r1 = 1/(2*k), v/(2*k*a)
    assert Q(18, 5) < H < h < (a-z)*b/c
    assert 1/c**3 < Q(7, 3)
    assert Q(1, 2) < v < k and r0 < 1 and z > 1
    assert Q(127, 128) > max(v, v/a)
    assert (a-1)*z*b/c > h and 2*v-3*v/a > 0
    assert Q(15, 32)*(1+v*r1) > Q(33, 32)*r1
    assert Q(15, 32)*(1+(v-1)*r0) > Q(33, 32)*r1
    assert (2*z-1)*b > 1/(3*c*b)
    sA, sR = a*c/3, (1/c+v*r1/c)/(3*b)
    pA, pd = Q(10571, 10000), Q(15371, 10000)
    assert pA > sA and pd > sA+sR
    assert ((2*z-1)*b-pd)/c > Q(1, 100)
    assert Q(15, 32)*(Q(18, 5)+z*b/c)-Q(33, 32)*Q(7, 3) == Q(1099, 19328)
    S, C = b+2*k*c/3, Q(59, 20)
    assert S == Q(42241, 30000)
    assert max(b, S+pd, 8*c/3, b+2*c, 3*b) < C
    radical_lt(S, Q(201, 100), Q(2, 3)*r0/c, C)
    radical_lt(S+pA, Q(201, 100), Q(2, 3)*r1/c, C)
    print('revised geometry: exact target', C)


def ceilq(x):
    return -(-x.numerator // x.denominator)


def schedule(n):
    c, k, b = Q(151, 200), Q(91, 100), Q(19, 20)
    v, w, a, h = Q(501, 1000), Q(407, 500), Q(21, 5), Q(723, 200)
    mb = n.bit_length()
    lo, hi = 1, 1
    target = c**3*n
    while hi**3*mb < target:
        hi *= 2
    while lo < hi:
        mid = (lo+hi)//2
        if mid**3*mb >= target:
            hi = mid
        else:
            lo = mid+1
    d = max(3, lo | 1)
    assert d**3*mb >= target and (d-2)**3*mb < target
    t, k0 = d*mb, ceilq(k*d)
    eB, e0 = ceilq(b*t/c), (n-5)//(2*k0)-1
    assert e0 > eB
    e, levels = e0, 0
    Vexp = lambda e: ceilq(v*e+w*eB)
    while e > eB:
        nex = max(eB, ceilq((v*e+w*eB+h*t)/a))
        assert eB <= nex < e
        assert a*nex >= v*e+w*eB+h*t
        assert Vexp(e) >= eB+2 and 2*Vexp(e) >= e
        assert Vexp(e) >= nex+6
        e = nex
        levels += 1
    emin, e1 = ceilq(Q(127, 128)*e0), max(eB, ceilq((v*e0+w*eB+h*t)/a))
    Mlo = (n-1)//d-1
    assert Vexp(e0)+2 <= Mlo and e0+2 <= Mlo
    assert emin > e1 and emin >= Vexp(e0)
    assert 2*Vexp(e0) >= 20*(levels+10)**6*t+3*e1
    assert 2*(int(h*d*t)+d*Vexp(e0)) <= n-1
    mk = k0.bit_length()
    kp = k0 + (k0+mk-1)//mk
    Sb = kp*e0 - ((n-1)//2-2)
    Jb = 2*(Sb+kp)//kp
    Dc = kp*Jb//2
    assert 0 <= Sb <= Dc <= Sb+kp and kp <= 2*k0
    assert 2*mk*(Jb+1) >= e0 and Jb+1 <= e0//128
    assert e0-Jb-1 >= emin
    return levels


if __name__ == '__main__':
    original()
    revised()
    js = [schedule(2**a+j) for a in (1000, 1100, 1200, 1500, 2000, 2500) for j in (0, 1, 19)]
    print('revised finite schedules:', len(js), 'depth range:', min(js), max(js))
