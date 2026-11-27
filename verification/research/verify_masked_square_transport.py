#!/usr/bin/env python3
"""Finite exact tests of masked anchor coverage and square-resultant transport.
Requires SymPy 1.14. These are not asymptotic relation-supply tests.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, prod
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp

X = sp.Symbol('X')


def append_hnf(H, v):
    return hermite_normal_form(H.row_join(v))


def key(H):
    return tuple(tuple(int(a) for a in H[:, j]) for j in range(H.cols))


def matrix(k, m):
    return sp.Matrix.hstack(*(sp.Matrix(v) for v in k)) if k else sp.zeros(m, 0)


def check_novelty():
    rng = Random(271828)
    cases = repairs = 0
    for _ in range(120):
        n, r = rng.randrange(2, 8), rng.randrange(1, 5)
        r = min(n, r)
        A = sp.Matrix(n, r, [rng.randrange(-5, 6) for _ in range(n*r)])
        vs = [A*sp.Matrix([rng.randrange(-8, 9) for _ in range(r)]) for _ in range(22)]
        H2 = max(1, max(int(v.dot(v)) for v in vs))
        # H <= 2^h; use an integer upper bound for the novelty budget.
        h = (H2.bit_length()+1)//2
        H = sp.zeros(n, 0); novel = 0
        for v in vs:
            G = append_hnf(H, v)
            if G != H:
                novel += 1
                oldvol2 = int((H.T*H).det()) if H.cols else 1
                newvol2 = int((G.T*G).det()) if G.cols else 1
                if G.cols == H.cols:
                    assert oldvol2 >= 4*newvol2 and oldvol2 % newvol2 == 0
                    repairs += 1
                else:
                    assert G.cols == H.cols+1 and newvol2 <= oldvol2*H2
                H = G
        assert novel <= A.rank()*(1+h)
        cases += 1
    print('integer novelty sequences:', cases, 'dependent index repairs:', repairs)


def check_coverage():
    # Deliberately nonuniform core and unrelated exceptional outputs.
    raw = [(None, 2, False), ((4, 0, 0), 2, True), ((2, 0, 0), 1, True),
           ((0, 2, 0), 3, True), ((1, 1, 0), 1, True), ((0, 0, 37), 1, False)]
    vs = [(sp.Matrix(v) if v is not None else None, Fraction(w, 10), c)
          for v,w,c in raw]
    states = {(): Fraction(1)}
    prev = Fraction(1); checked = 0; accumulated = Fraction(0)
    # Core integer rank <=2, all vectors have norm <=4. M=6.
    for m in range(13):
        miss = Fraction(0); new = defaultdict(Fraction)
        for k, mass in states.items():
            H = matrix(k, 3)
            for v, p, core in vs:
                G = H if v is None else append_hnf(H, v)
                if core and G != H:
                    miss += mass*p
                new[key(G)] += mass*p
                checked += 1
        assert sum(states.values()) == 1 and sum(new.values()) == 1
        assert miss <= prev and miss <= Fraction(6, m+1)
        accumulated += miss
        assert accumulated <= 6
        prev = miss; states = new
    print('exact coverage transitions:', checked, 'final missing core mass:', prev)


def solve_span(A, v):
    D,S,T = smith_normal_decomp(A,domain=sp.ZZ)
    assert S*A*T == D
    w = S*v; y = sp.zeros(A.cols, 1)
    for i in range(A.rows):
        di = int(D[i,i]) if i < min(D.shape) else 0
        if di:
            if int(w[i]) % di:
                return None
            y[i] = int(w[i])//di
        elif w[i]:
            return None
    u = T*y
    assert A*u == v
    return [int(a) for a in u]


def check_masks():
    rng = Random(314159); comparisons = strict = fibres = factors = 0
    for N in (77, 899, 1189, 315):
        units = [u for u in range(1,N) if gcd(u,N)==1]
        squares = sorted({u*u % N for u in units})
        ff = {s:sp.factorint(s) for s in squares}  # tiny, deliberately exhaustive fixture
        ps = sorted(set().union(*(set(f) for f in ff.values())))
        V = {s:sp.Matrix([ff[s].get(p,0) for p in ps]) for s in squares}
        roots = [rng.choice(units) for _ in range(12)]
        A = sp.Matrix.hstack(*(V[z*z % N] for z in roots)); E = hermite_normal_form(A)
        covered = {s for s in squares if append_hnf(E,V[s])==E}
        assert covered
        witnesses = {s:solve_span(A,V[s]) for s in covered}
        assert all(w is not None for w in witnesses.values())
        for s in squares:
            masks = [a for a in units if s*a*a%N in covered]
            assert len(masks)*len(squares)==len(units)*len(covered)
            comparisons += len(units)
            # Prefer a nontrivial covered representative.
            a = next((a for a in masks if s*a*a%N != 1), masks[0])
            ss = s*a*a % N
            root = prod(pow(z,e,N) for z,e in zip(roots,witnesses[ss]))*pow(a,-1,N)%N
            assert root*root % N == s
            # Exact old one-target quotient test, including integer index obstructions.
            old = append_hnf(E, 2*V[s])
            if append_hnf(old,V[s]) != old:
                b = V[ss]-V[s]
                assert append_hnf(old,b)!=old
                en = append_hnf(E,b)
                assert append_hnf(en,V[s])==en
                strict += 1
            hs = [h for h in units if h*h%N == s]
            good = sum(1<gcd(h*pow(root,-1,N)-1,N)<N for h in hs)
            assert good == len(hs)-2
            fibres += len(hs); factors += good
        print('mask fixture:', N, 'squares:',len(squares),'covered:',len(covered))
    print('uniform mask comparisons:', comparisons, 'strict old-parity gains:', strict,
          'private fibre checks:', fibres, 'proper gcds:', factors)


def poly(cs):
    return sp.Poly.from_list(list(reversed(cs)), X, domain=sp.ZZ)


def crt(a,n,b,p):
    return (a+n*((b-a)*pow(n,-1,p)%p))%(n*p)


def modpoly(P,N):
    return poly([int(P.nth(j))%N for j in range(P.degree()+1)]) if not P.is_zero else poly([0])


def interpolate_exact(rs, vals):
    return sp.Poly(sp.interpolate(list(zip(rs,vals)),X),X,domain=sp.ZZ)


def interpolate_mod(rs, vals, N):
    k=len(rs); out=poly([0])
    for i,r in enumerate(rs):
        p=sp.Poly(prod(X-v for j,v in enumerate(rs) if j!=i),X,domain=sp.ZZ)
        den=prod(r-v for j,v in enumerate(rs) if j!=i)
        out=modpoly(out+((vals[i]*pow(den,-1,N))%N)*p,N)
    assert all(int(out.eval(r))%N==v%N for r,v in zip(rs,vals))
    return out


def norm_lift(N,t,aa,nn,ww):
    k=len(aa); d=2*k+1
    assert all(gcd(a,N)==gcd(n,N)==gcd(w,N)==1 and (n-a*w*w)%N==0
               for a,n,w in zip(aa,nn,ww))
    ell=int(sp.nextprime(2*k+1))
    while gcd(ell,N*prod(nn))>1: ell=int(sp.nextprime(ell))
    used=set();rs=[]
    for a,n in zip(aa,nn):
        v=next(v for v in range(1,ell) if v not in used and pow(v,(ell-1)//2,ell)==pow(-n,(ell-1)//2,ell))
        used.add(v);rs.append(crt(t-a,N,v,ell))
    C=prod(abs(u-v) for i,u in enumerate(rs) for v in rs[:i])
    assert gcd(C,N*ell)==1
    bs=[]
    for r,n in zip(rs,nn):
        z=pow(r,d,ell)*pow(-n*C*C,-1,ell)%ell
        v=next(v for v in range(1,ell) if v*v%ell==z)
        bs.append(C*crt(1,N,v,ell))
    I=interpolate_exact(rs,[-n*b*b for n,b in zip(nn,bs)])
    P=sp.Poly(prod(X-r for r in rs),X,domain=sp.ZZ)
    g=P+interpolate_mod(rs,[b*w for b,w in zip(bs,ww)],N)
    FN=sp.Poly(X-t,X,domain=sp.ZZ)*g*g
    R1,J1=(FN-I).div(P); R2,J2=(poly([0]*d+[1])-I).div(P)
    assert modpoly(J1,N).is_zero and modpoly(J2,ell).is_zero
    j=d-k; c2=[int(R2.nth(i))%ell for i in range(j)]+[1]
    v=int((I+P*poly(c2)).eval(0))
    assert v%ell==0
    c2[0]+=ell*((1-v//ell)*pow(int(P.eval(0)),-1,ell)%ell)
    Q=poly([crt(int(R1.nth(i)),N,c2[i],ell*ell) for i in range(j)]+[1])
    f=I+P*Q
    assert f.is_monic and f.degree()==d and f.eval(t)%N==0
    assert all(int(f.nth(i))%ell==0 for i in range(d)) and int(f.nth(0))%(ell*ell)==ell
    assert modpoly(f-FN,N).is_zero
    assert int(f.discriminant())%N**k==0
    for r,a,n,b,w in zip(rs,aa,nn,bs,ww):
        m=poly([-r,1]); q=int(sp.resultant(f,m)); z=int(sp.resultant(g,m))%N
        assert q==n*b*b and (t-r)%N==a%N
        assert gcd(z,N)==1 and (q-a*z*z)%N==0
        assert (z*z-b*b*w*w)%N==0
    return f,g


def check_lifts():
    rng=Random(1701); cases=marks=tests=skips=0
    for N,k in product((77,899,1189),range(1,5)):
        for _ in range(2):
            aa=[]
            while len(aa)<k:
                a=rng.randrange(1,N)
                if gcd(a,N)==1 and all(gcd(a-b,N)==1 for b in aa): aa.append(a)
            ww=[rng.choice([u for u in range(1,N) if gcd(u,N)==1]) for a in aa]
            nn=[a*w*w%N for a,w in zip(aa,ww)]
            nn=[n-N if rng.randrange(2) else n for n in nn]
            t=rng.randrange(N); f,g=norm_lift(N,t,aa,nn,ww)
            if k<=2: assert f.is_irreducible
            for _ in range(5):
                P=poly([rng.randrange(-8,9) for _ in range(3)])
                n=int(sp.resultant(f,P)); b=int(sp.resultant(g,P))%N
                v=int(P.eval(t))%N
                assert n%N==v*b*b%N
                if gcd(n,N)==1:
                    assert v==n*pow(b,-2,N)%N
                    tests+=1
                else: skips+=1
            cases+=1;marks+=k
    print('square-cofactor fields:',cases,'exact norm lifts:',marks,
          'additional mark identities:',tests,'nonunit guards:',skips)


def check_shared_divisors():
    rng=Random(1729);count=0
    for N,m in product((27,77,315,1189),range(1,5)):
        for _ in range(8):
            def monic(k):return poly([rng.randrange(-10,11) for _ in range(k)]+[1])
            g=monic(m);a=monic(3);b=monic(2)
            f=g*a+N*poly([rng.randrange(-5,6) for _ in range(m+3)])
            F=g*b+N*poly([rng.randrange(-5,6) for _ in range(m+2)])
            n=int(sp.resultant(f,F))
            if n:
                assert n%N**m==0
                count+=1
    print('shared modular cofactor resultant divisibilities:',count)


if __name__=='__main__':
    check_novelty();check_coverage();check_masks();check_lifts();check_shared_divisors()
