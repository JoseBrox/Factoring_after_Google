#!/usr/bin/env python3
"""Exact checks of projective discriminant and norm-one mark identities.
Requires SymPy. Finite tests, not proofs of asymptotic relation supply.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd, prod
from random import Random
import sympy as sp

X = sp.Symbol('X')


def poly(cs):
    return sp.Poly.from_list(list(reversed(cs)), X, domain=sp.ZZ)


def binary_disc(cs, d):
    f = poly(cs)
    if f.degree() == d:
        return abs(int(f.discriminant()))
    if f.degree() == d - 1:
        return abs(int(f.LC()) ** 2 * int(f.discriminant()))
    return 0


def transform(cs, A):
    a, b, c, e = A
    d = len(cs) - 1
    out = [0] * (d + 1)
    for i, fi in enumerate(cs):
        for j in range(i + 1):
            for k in range(d - i + 1):
                out[j+k] += (fi * comb(i,j) * a**j * b**(i-j)
                             * comb(d-i,k) * c**k * e**(d-i-k))
    return out


def vp(n, p):
    assert n != 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def disc_check(cs, A):
    d = len(cs) - 1
    assert gcd(*cs) == 1
    a, b, c, e = A
    D = abs(a*e-b*c)
    df = binary_disc(cs,d)
    assert D and df
    tr = transform(cs,A)
    cont = gcd(*tr)
    assert cont > 0
    dg = binary_disc([u//cont for u in tr],d)
    assert dg * cont**(2*d-2) == df * D**(d*(d-1))
    s1 = gcd(*A)
    assert D % (s1*s1) == 0
    index = D // (s1*s1)
    assert (df*dg)**2 >= index**(d*(d-2))
    locals_checked = 0
    for p in sp.factorint(index):
        ap = vp(index,p)
        cp = vp(cont,p) - d*vp(s1,p)
        v1, v2 = vp(df,p), vp(dg,p)
        assert 0 <= cp <= d*ap
        assert ap*v1 >= cp*cp-ap*cp
        assert ap*v2 >= (d*ap-cp)**2-ap*(d*ap-cp)
        assert 2*ap*(v1+v2) >= (2*cp-d*ap)**2+d*(d-2)*ap**2
        locals_checked += 1
    return df, dg, index, locals_checked


def check_discriminants():
    rng = Random(271828)
    ncases = nlocal = 0
    for d in range(3,9):
        for _ in range(180):
            cs = [rng.randrange(-20,21) for _ in range(d+1)]
            h = gcd(*cs)
            if not h:
                continue
            cs = [a//h for a in cs]
            if not binary_disc(cs,d):
                continue
            A = tuple(rng.randrange(-12,13) for _ in range(4))
            if A[0]*A[3] == A[1]*A[2]:
                continue
            _, _, _, count = disc_check(cs,A)
            ncases += 1
            nlocal += count
    sharp = 0
    for d, p, a in product((4,6,8), (11,13,17), (1,2,3)):
        k = d//2
        roots = [p**a*i for i in range(k)] + list(range(1,k+1))
        f = sp.Poly(prod(X-r for r in roots),X,domain=sp.ZZ)
        cs = [int(f.nth(j)) for j in range(d+1)]
        df,dg,index,_ = disc_check(cs,(p**a,0,0,1))
        # Equality in the *local* diameter inequality at p.
        assert 2*(vp(df,p)+vp(dg,p)) == d*(d-2)*a
        assert index == p**a
        sharp += 1
    print('primitive binary transformations:',ncases,'local inequalities:',nlocal,
          'sharp even-degree local fixtures:',sharp)


def signed_eval_at_half(f,r,sign):
    d = f.degree()
    return sum(int(f.nth(i)) * (2*r+sign)**i * 2**(d-i) for i in range(d+1))


def unit_lift(N, residues):
    k = len(residues)
    d = max(3,k+1)
    if d % 2 == 0:
        d += 1
    ss = [s%N for s in residues] + [1]*(d-1-k)
    ss.append(pow(prod(ss)%N,-1,N))
    marks = [4*i*N-s for i,s in enumerate(ss,1)]
    us = [sp.Poly(X-r,X,domain=sp.ZZ) for r in marks]
    f = prod(us)-sp.Poly(1,X,domain=sp.ZZ)
    assert f.is_monic and f.degree()==d and f.is_irreducible
    assert int(f.eval(0))%N==0
    assert prod(us).rem(f)==sp.Poly(1,X,domain=sp.ZZ)
    for r,s,u in zip(marks,ss,us):
        assert (-r)%N == s
        assert f.eval(r)==-1
        assert signed_eval_at_half(f,r,-1)*signed_eval_at_half(f,r,1)<0
        assert int(sp.resultant(f,u))==1
    return d


def check_lifts():
    rng = Random(314159)
    fields=marks=0
    for N,k in product((77,899,100160063),range(1,9)):
        ss=[]
        while len(ss)<k:
            h=rng.randrange(1,N)
            if gcd(h,N)==1:
                ss.append(h*h%N)
        marks+=unit_lift(N,ss)
        fields+=1
    print('arbitrary-image odd-degree fields:',fields,'exact norm/image/bracket checks:',marks)


def check_rigidity_fixtures():
    # Check all arithmetic guards using a rational upper bound on the log ratio.
    # This is not a certified numerical log-rank test: use exact products in Q[X]/f.
    counts=Counter()
    for k,m in ((3,2),(4,1),(4,3)):
        marks=[1000000*(i+1) for i in range(k)]
        S=1000000; H=marks[-1]; d=k+m
        C=max(Fraction(8),Fraction(2*H+2,S-4))
        ratio=Fraction((2*H+2).bit_length(), (S-2).bit_length()-1)
        assert S-4>=64 and (S-2)**(k-1)>(4*(m+1))**m
        assert 4*d*ratio <= Fraction(S-2,2)
        assert (S-4)**(k-m)>C**(2*m)
        us=[sp.Poly(X-r,X,domain=sp.ZZ) for r in marks]
        P=prod(us)
        cases=[(us[0]**m, (m+1,)+(1,)*(k-1)),
               (prod(sp.Poly(X+(i+1)*S,X,domain=sp.ZZ) for i in range(m)),None)]
        if m>=2:
            cases.append((sp.Poly(((X-marks[0])**2+1)*(X+S)**(m-2),X,domain=sp.ZZ),None))
        for Q,relation in cases:
            f=P*Q-1
            if not f.is_irreducible:
                counts['reducible rejected']+=1
                continue
            one=sp.Poly(1,X,domain=sp.ZZ)
            invs=[((P.exquo(u))*Q).rem(f) for u in us]
            assert all((u*v).rem(f)==one for u,v in zip(us,invs))
            bound=2
            if relation is not None:
                val=prod(u**e for u,e in zip(us,relation)).rem(f)
                assert val==one
                counts['explicit multiplicity relations']+=1
            powers=[]
            for u,iv in zip(us,invs):
                powers.append([(iv**(-j) if j<0 else u**j).rem(f)
                               for j in range(-bound,bound+1)])
            for es in product(range(-bound,bound+1),repeat=k):
                val=one
                for i,e in enumerate(es):
                    val=(val*powers[i][e+bound]).rem(f)
                equal=val==one
                predicted=not any(es) if relation is None else (
                    all(es[i]*relation[0]==es[0]*relation[i] for i in range(k))
                    and es[0]%relation[0]==0)
                assert equal==predicted,(marks,Q,es,relation)
                counts['compact exponent checks']+=1
            counts['product correction fixtures' if relation else 'nonproduct correction fixtures']+=1
    print('rigidity finite fixtures:',dict(sorted(counts.items())))


if __name__=='__main__':
    check_discriminants()
    check_lifts()
    check_rigidity_fixtures()
