#!/usr/bin/env python3
"""Exact fallback U inequalities and finite symbolic bit-length guards."""
from fractions import Fraction as Q
from verify_keybreak_compression import ceildiv, degree


def constants():
    q, k, b = Q(161, 10), 24, 1
    density, search = Q(3259, 100), Q(17)
    raw, target = search+density, Q(100)
    assert q > 16 and Q(2)/(q-1) < b
    # log(q/16)>1/161, log(q)<3; gap 1/3-4alpha > 1/1449.
    assert Q(1, 1449) > Q(2, 3000)
    assert Q(100000, 3000) > 3
    assert Q(31)/(2*k*q) < 1 and Q(11)+Q(6, k) < 12
    assert 2*q + Q(1+Q(3,k), 3*b) < density
    assert 11*b - Q(12+6*b, 3*b) - Q(3,8) == Q(37,8)
    assert Q(3,k) < Q(63,500)
    assert search == b+Q(2*k,3) and raw == Q(4959,100)
    assert max(Q(3), raw+max(Q(1), Q(2,3)), raw+2, Q(28), Q(12)) < 53
    assert (1-search/target)**3 > Q(1,2)
    assert (1-raw/target)**3 > Q(63,500)
    print('fallback exact leading constants:', str(search), str(raw), 'target', str(target))


def schedule(n):
    mb = n.bit_length()
    d = degree(n, mb)
    t, k0 = d*mb, 24*d
    eB, e0 = t, (n-5)//(2*k0)-1
    assert e0 > eB
    e, levels = e0, 0
    while e > eB:
        nex = max(eB, ceildiv(10*(e+2*t), 161))
        assert eB <= nex < e and 60*(e+2*t) <= 966*nex
        e = nex
        levels += 1
    e1 = max(eB, ceildiv(10*(e0+2*t), 161))
    assert 500*(12*d*d*mb+6*d*e0) <= 63*(n-1)
    assert 31*e1+13 <= (n-1)//d-1
    assert 12*e0+2 <= (n-1)//d-1
    mk = k0.bit_length()
    kp = k0 + ceildiv(k0,mk)
    Sb = kp*e0 - ((n-1)//2-2)
    Jb = 2*(Sb+kp)//kp
    Dc = kp*Jb//2
    emin = ceildiv(127*e0,128)
    assert 0 <= Sb <= Dc <= Sb+kp and kp <= 2*k0
    assert 2*mk*(Jb+1) >= e0 and Jb+1 <= e0//128
    assert e0-Jb-1 >= emin > e1
    return levels


if __name__ == '__main__':
    constants()
    js = [schedule(2**a+j) for a in (1000, 1100, 1200, 1500, 2000, 2500) for j in (0,1,19)]
    print('fallback finite schedules:', len(js), 'depth range:', min(js), max(js))
