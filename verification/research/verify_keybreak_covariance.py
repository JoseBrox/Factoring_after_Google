#!/usr/bin/env python3
"""Finite exact checks for U100/U40; not a test of asymptotic estimates."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm


def smooth(n, primes=(2, 3, 5)):
    if n < 1:
        return False
    for p in primes:
        while n % p == 0:
            n //= p
    return n == 1


def semismooth(n, parents):
    n = abs(n)
    return sum((w for p, w in parents.items()
                if n % p == 0 and smooth(n // p)), F(0))


def phi(n):
    return sum(gcd(a, n) == 1 for a in range(n))


def check_contents():
    checks = Counter()
    parents = {11: F(2, 3), 13: F(1)}  # full prime band (7,14]
    for K, lo, hi in product((6, 22, 242, 26, 338, 286, 572, 3146),
                             (1, 103, 987), (3001, 6002)):
        Ko = K
        while Ko % 2 == 0:
            Ko //= 2
        cells = defaultdict(list)
        for n in range(lo | 1, hi, 2):
            cells[gcd(n, Ko)].append(n)
        for delta, ns in cells.items():
            weighted = F(0)
            for p, w in parents.items():
                actual = sum(n % p == 0 and smooth(n // p) for n in ns)
                if Ko % p:
                    vs = [v for v in range((lo+p-1)//p, (hi+p-1)//p)
                          if v % 2 and gcd(v, Ko) == delta]
                    predicted = sum(map(smooth, vs))
                    checks['unit-parent'] += 1
                elif delta % p or delta % (p*p) == 0:
                    predicted = 0
                    checks['excluded-content'] += 1
                else:
                    e, rest = 0, Ko
                    while rest % p == 0:
                        rest //= p
                        e += 1
                    vs = [v for v in range((lo+p-1)//p, (hi+p-1)//p)
                          if v % 2 and gcd(v, rest) == delta//p
                          and (e == 1 or v % p)]
                    assert sorted(p*v for v in vs) == ns
                    predicted = sum(map(smooth, vs))
                    checks['capped-parent' if e == 1 else 'exact-parent'] += 1
                assert actual == predicted, (K, lo, hi, delta, p)
                weighted += w * predicted
            assert weighted == sum(semismooth(n, parents) for n in ns)
            checks['weighted-content'] += 1
    assert all(checks[k] > 0 for k in ('unit-parent', 'excluded-content',
                                       'capped-parent', 'exact-parent'))
    return checks


def means(rows, weights, values, key):
    numer = defaultdict(F)
    denom = defaultdict(F)
    for row, w, v in zip(rows, weights, values):
        numer[key(row)] += w*v
        denom[key(row)] += w
    return [numer[key(row)]/denom[key(row)] for row in rows]


def check_projections():
    count = 0
    parents = {11: F(2, 3), 13: F(1)}
    for Q, K in product((9, 45, 75), (6, 18, 54, 110, 726, 234)):
        Ko = K//2
        period = lcm(Q, K)
        ns = list(range(1, period+1, 2))
        rows = [(gcd(n, Q), gcd(n, Ko), gcd(n, gcd(Q, Ko))) for n in ns]
        total = len(ns)
        st = Counter((s, t) for s, t, _ in rows)
        s_count = Counter(s for s, _, _ in rows)
        t_count = Counter(t for _, t, _ in rows)
        v_count = Counter(v for _, _, v in rows)
        for (s, t), c in st.items():
            v = gcd(s, t)
            assert c*v_count[v] == s_count[s]*t_count[t]
        for t, c in t_count.items():
            assert F(c, total) == F(2*phi(K//t), K)
        weights = [F(1,total)]*total
        for values in ([semismooth(n, parents) for n in ns],
                       [F((n*n+17*n+3)%19,18) for n in ns]):
            DS = means(rows, weights, values, lambda r:r[0])
            DT = means(rows, weights, values, lambda r:r[1])
            DV = means(rows, weights, values, lambda r:r[2])
            assert means(rows, weights, DS, lambda r:r[1]) == DV
            assert means(rows, weights, [f-g for f,g in zip(values,DS)],
                         lambda r:r[1]) == [a-b for a,b in zip(DT,DV)]
            count += 1
    return count


def check_determinants():
    count = 0
    for q, H1, H2, r, s in product((3,5,7), range(1,13), range(1,14,2),
                                  range(2,31), range(2,31)):
        if H1 % q == 0:
            continue
        L = lcm(H1*r//gcd(r,q), H2*s//gcd(s,2))
        assert r*s*H1*H2 <= 4*L*L*gcd(r,q)
        count += 1
    return count


def chi3(n):
    return (0,1,-1)[n%3]


def squarefree_divisors(primes):
    terms = [(1,1)]
    for p in primes:
        terms += [(d*p,-m) for d,m in terms]
    return terms


def check_induction():
    parents = {11:F(2,3), 13:F(1)}
    count = 0
    for primes in ((5,), (11,), (5,11,13), (7,13), (5,7,11,13)):
        k = 6
        for p in primes:
            k *= p*p
        terms = squarefree_divisors(primes)
        for h, L in product((1, 3, 5, 11, 13, 33, 121, 143, 17), (119, 989)):
            direct = sum(semismooth(h*n,parents)*chi3(n)
                         for n in range(1,L+1,2) if gcd(n,k)==1)
            expanded = sum(m*chi3(e)*sum(semismooth(h*e*v,parents)*chi3(v)
                           for v in range(1,L//e+1,2)) for e,m in terms)
            assert direct == expanded
            count += 1
    return count


if __name__ == '__main__':
    print('full-content cases:', dict(sorted(check_contents().items())))
    print('conditional projection identities:', check_projections())
    print('common-determinant inequalities:', check_determinants())
    print('weighted imprimitive induction identities:', check_induction())
