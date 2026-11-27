#!/usr/bin/env python3
"""Exact sealed-polynomial fibre checks and finite public LLL searches.
Requires SymPy 1.14; no asymptotic success claim.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd, comb
from random import Random
import sympy as sp

x = sp.Symbol('x')


def poly(cs):
    return sp.Poly.from_list(list(reversed(cs)), x, domain=sp.ZZ)


def crt(a, p, b, q):
    return (a + p*((b-a)*pow(p,-1,q) % q)) % (p*q)


def public_poly(hs, N):
    f = [1]
    for h in hs:
        g = [0]*(len(f)+1)
        for i, a in enumerate(f):
            g[i] = (g[i]-h*a) % N
            g[i+1] = (g[i+1]+a) % N
        f = g
    return poly([(a+N//2) % N-N//2 for a in f[:-1]]+[1])


def in_ideal(g, f, N):
    return all(int(a) % N == 0 for a in g.rem(f).all_coeffs())


def splits(g, hs, N):
    return {d for h in hs for d in [gcd(int(g.eval(h)), N)] if 1 < d < N}


def check_fibres():
    checks = 0
    for p,q in ((5,7),(9,25),(11,13)):
        N = p*q
        k = 3
        pp, qq = (3 if p==9 else p), (5 if q==25 else q)
        a, b = tuple(range(k)), tuple(range(1,k+1))
        hs = [crt(u,p,v,q) for u,v in zip(a,b)]
        f = public_poly(hs,N)
        # Independent exact CRT labels.  Fix the first component order;
        # relabeling both components simultaneously cannot affect any split.
        fibres = [[crt(u,p,v,q) for u,v in zip(a,perm)]
                  for perm in permutations(b)]
        for H in fibres:
            assert public_poly(H,N)==f
            assert all(gcd(u-v,N)==1 for u,v in combinations(H,2))
        # Manufacture local rank patterns, using known factors ONLY to test theorem.
        for I,J in product(range(1,1<<k),repeat=2):
            aa=[0 if I>>i&1 else 1 for i in range(k)]
            bb=[0 if J>>i&1 else 1 for i in range(k)]
            gp=sp.Poly(sp.interpolate(list(zip(a,aa)),x),x,domain=sp.QQ)
            gq=sp.Poly(sp.interpolate(list(zip(b,bb)),x),x,domain=sp.QQ)
            def coeff(g,i,m):
                c=Fraction(g.nth(i)); return c.numerator*pow(c.denominator,-1,m)%m
            g=poly([crt(coeff(gp,i,p),p,coeff(gq,i,q),q) for i in range(k)])
            assert int(sp.resultant(f,g)) % N == 0
            assert [int(g.eval(u))%p for u in a]==aa
            assert [int(g.eval(v))%q for v in b]==bb
            allmask=(1<<k)-1
            if I==J==allmask:
                assert in_ideal(g,f,N)
                continue
            assert not in_ideal(g,f,N)
            r,s=I.bit_count(),J.bit_count()
            fail=Fraction(sum(not splits(g,H,N) for H in fibres),len(fibres))
            predicted=Fraction(1,comb(k,r)) if r==s else Fraction(0)
            assert fail==predicted and fail<=Fraction(1,k)
            checks+=1
        # All roots vanish mod pp but one has valuation strictly below that of p^a.
        if p!=pp:
            g=poly([crt(pp,p,0,q)])
            assert int(sp.resultant(f,g)) % N==0
            assert not in_ideal(g,f,N)
            assert all(splits(g,H,N) for H in fibres)
    print('exact CRT coverage cases:',checks,'(including prime powers)')


def search(N, k, D, seed):
    # The search receives only N and f.  hs are used by sampler and final extractor.
    rng=Random(seed)
    hs=[]
    while len(hs)<k:
        h=rng.randrange(N)
        # Discard other factor exits to isolate the polynomial experiment.
        if all(gcd(h-z,N)==1 for z in hs):
            hs.append(h)
    f=public_poly(hs,N)
    F=[int(f.nth(j)) for j in range(k+1)]
    B=[[N*int(i==j) for j in range(D+1)] for i in range(k)]
    B += [[0]*i+F+[0]*(D-k-i) for i in range(D-k+1)]
    assert abs(int(sp.Matrix(B).det()))==N**k
    rows=[[int(a) for a in row] for row in sp.Matrix(B).lll().tolist()]
    candidates=rows+[[a+sg*b for a,b in zip(u,w)]
                      for u,w in combinations(rows,2) for sg in (-1,1)]
    counts=Counter()
    factors=set()
    for cs in candidates:
        P=poly(cs)
        assert in_ideal(P,f,N)
        counts['vectors']+=1
        content,fs=sp.factor_list(P)
        assert sp.Poly(content,x,domain=sp.ZZ)*sp.prod(g**e for g,e in fs)==P
        d=gcd(int(content),N)
        if 1<d<N:
            counts['content exits']+=1
            factors.add(d)
        if d!=1 or sum(e for g,e in fs)<2:
            continue
        counts['reducible']+=1
        if any(in_ideal(g,f,N) for g,e in fs):
            counts['trivial multiples']+=1
        else:
            counts['public certificates']+=1
            valid=set().union(*(splits(g,hs,N) for g,e in fs))
            assert all(N%d==0 and 1<d<N for d in valid)
            if valid:
                counts['certificates split']+=1
                factors |= valid
    return counts,factors


def experiments():
    rng=Random(271828)
    total=Counter()
    for N in (3127,10403,1022117,100160063,1000036000099):
        for k in (2,3):
            c=Counter(); factors=set(); fixtures=0
            for D in (k+2,k+4,k+6):
                counts,ff=search(N,k,D,rng.randrange(2**32))
                c+=counts; factors |= ff; fixtures+=bool(ff)
            total+=c
            print('N',N,'k',k,'fixtures split',fixtures,'of 3',
                  dict(sorted(c.items())),'verified factors',sorted(factors))
    print('total (not independent trials):',dict(sorted(total.items())))


if __name__=='__main__':
    check_fibres()
    experiments()
