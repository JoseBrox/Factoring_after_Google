#!/usr/bin/env python3
"""Exact checks of the KeyBreak compressed U parameter ledger, not the analytic transfer."""
from fractions import Fraction as Q
from math import gcd


def ceildiv(a, b):
    return -(-a // b)


def degree(n, mb):
    lo, hi = 1, 1
    while hi**3 * mb < n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**3 * mb >= n:
            hi = mid
        else:
            lo = mid + 1
    d = max(3, lo | 1)
    assert d % 2 == 1 and d**3 * mb >= n
    assert d == 3 or (d - 2)**3 * mb < n
    return d


def schedule(n):
    mb = n.bit_length()
    d = degree(n, mb)
    t, k0 = d * mb, 9 * d
    eB = ceildiv(201 * t, 100)
    e0 = (n - 5) // (2 * k0) - 1
    assert eB > 2 * t and e0 > eB
    e = e0
    levels = 0
    while e > eB:
        nxt = max(eB, ceildiv(e + 2 * t, 2))
        assert eB <= nxt < e
        assert 12 * t + 6 * e <= 12 * nxt
        e = nxt
        levels += 1
    e1 = max(eB, ceildiv(e0 + 2 * t, 2))
    # Strict finite exponent tests; no materialization of Y_i or N.
    assert 500 * (12 * d * d * mb + 6 * d * e0) <= 167 * (n - 1)
    # 4 (4 Y_1^12)^2 <= M/(64 Y_1^7) with M >= 2^floor((n-1)/d)-1.
    assert 31 * e1 + 13 <= (n - 1) // d - 1
    assert 12 * e0 + 2 <= (n - 1) // d - 1
    mk = k0.bit_length()
    k = k0 + ceildiv(k0, mk)
    Lx = (n - 1) // 2 - 2
    Sb = k * e0 - Lx
    Jb = 2 * (Sb + k) // k
    Dc = k * Jb // 2
    emin = ceildiv(127 * e0, 128)
    assert Sb >= 0 and k <= 2 * k0
    assert Sb <= Dc <= Sb + k
    assert 2 * mk * (Jb + 1) >= e0
    assert Jb + 1 <= e0 // 128
    assert emin > e1
    assert e0 - Jb - 1 >= emin
    return levels


def check_constants():
    b, kappa = Q(201, 100), 9
    s = b + Q(2 * kappa, 3)
    rho = Q(423, 100)
    v = s + rho
    assert Q(4) + Q(4, 3) / (3 * b) < rho
    assert 11 * b - rho > 17
    assert 11 + Q(6, kappa) < 12
    assert Q(31, 4 * kappa) < 1
    assert Q(3, kappa) < Q(167, 500)
    assert s == Q(801, 100) and v == Q(1224, 100)
    direct = [3*b, 3*b, v + max(b, Q(2, 3)), v + 2*b,
              Q(28), 12*b]
    assert max(direct) == 28 and max(direct) < 29
    target = Q(40)
    assert (1 - s / target)**3 > Q(1, 2)
    assert (1 - v / target)**3 > Q(167, 500)
    # Source G: exact stated h_1 and its cost margin.
    h1_sq = Q(76313, 322500)
    assert (Q(2967, 1000) - Q(62, 25))**2 > h1_sq
    print('exact leading constants:', str(s), str(v), 'direct', max(direct), 'target', target)


def check_semismooth_identity():
    # Exact check of the support dichotomy after division by content h.
    # Smooth cutoff 5, complete sample of eligible parents in (5, 14].
    parents = (7, 11, 13)
    weights = {7: 2, 11: 3, 13: 5}
    def smooth(n):
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
        return n == 1
    def f(n):
        return sum(weights[p] for p in parents if n % p == 0 and smooth(n//p))
    checked = 0
    for h in range(1, 181):
        for n in range(1, 401):
            if smooth(h):
                rhs = sum(weights[p] for p in parents if n % p == 0 and smooth(n//p))
            else:
                eligible = [p for p in parents if h % p == 0 and smooth(h//p)]
                assert len(eligible) <= 1
                rhs = sum(weights[p] for p in eligible if smooth(n))
            assert f(h*n) == rhs
            checked += 1
    # Capped full-gcd branch: a parent above the smooth bound has valuation exactly one.
    for ell in parents:
        for a in range(1, 4):
            mod = ell**a
            accepted = sum(1 for u in range(1, mod+1) if gcd(u, mod) >= ell)
            assert accepted * ell == mod
            for u in range(1, mod+1):
                if f(u) and u % ell == 0:
                    assert u % (ell*ell) != 0
    print('exact semismooth content identities:', checked)


if __name__ == '__main__':
    check_constants()
    lengths = [2**a + j for a in (1000, 1100, 1200, 1500, 2000, 2500) for j in (0, 1, 19)]
    js = [schedule(n) for n in lengths]
    print('finite schedules:', len(js), 'depth range:', min(js), max(js))
    check_semismooth_identity()
