"""Finite exact checks of the targeted certificate and resultant cutoff.

Requires SymPy. The first fixture is manufactured from a known order:
it tests the exact rank-deficient criterion, not general factoring coverage.
"""
from itertools import product, combinations
from math import gcd
import sympy as S

x = S.symbols('x')


def targeted_fixture():
    N, ell, m = 15, 2, 0
    g1, g2 = x-1, x-46
    P = g1*g2
    f1, f2 = S.Poly(P-16, x), S.Poly(P-1,x)
    assert all(f.is_irreducible and S.discriminant(f)>0 and f.eval(m)%N==0
               for f in (f1,f2))
    assert S.Poly(f1,x,modulus=2).sqf_part().degree()==2
    assert S.Poly(f2,x,modulus=2).is_irreducible
    assert S.Poly(f1,x,modulus=2).eval(0)==0
    assert S.Poly(f1,x,modulus=2).eval(1)==0
    for g in (g1,g2):
        assert abs(S.resultant(f1.as_expr(),g,x))==16
        assert abs(S.resultant(f2.as_expr(),g,x))==1
        assert gcd(int(g.subs(x,m)),N)==1
    # At each good prime over 2, the two linear marks hit distinct roots,
    # so the entire exponent 4 of the norm is at one target prime ideal.
    assert (1%2)!=(46%2)
    assert S.rem(P-16,f1.as_expr(),x)==0
    assert S.rem(P-1,f2.as_expr(),x)==0
    V=S.diag(4,4)
    assert not V.nullspace() and V*S.Matrix([-1,-1])==-4*S.ones(2,1)
    assert pow(ell,4,N)==1 and gcd(pow(ell,2,N)-1,N)==3
    print('targeted fixture: kernel rank 0, required full log rank 2; exact certificate 2^4 = 1 mod 15; factor 3')


def large_prime_fixture():
    s,H=2,2
    R=((s+1)*H)**(2*s)
    gs=[]
    for c in product(range(-H,H+1),repeat=s+1):
        p=S.Poly(sum(c[k]*x**k for k in range(s+1)),x)
        if p.degree()<1 or p.LC()<1 or p.content()!=1 or not p.is_irreducible:
            continue
        gs.append(p)
    resultants={}
    for i,j in combinations(range(len(gs)),2):
        r=abs(int(S.resultant(gs[i],gs[j])))
        assert 0<r<=R
        resultants[i,j]=r
    f=S.Poly((x-770)**3-19*(x-770)-25,x)
    assert f.is_irreducible and S.discriminant(f)>0
    D=abs(int(S.discriminant(f)))
    incidences={}
    retained=0
    for i,g in enumerate(gs):
        norm=abs(int(S.resultant(f,g)))
        assert norm
        factors=S.factorint(norm)
        assert S.prod(p**e for p,e in factors.items())==norm
        # All factors in this finite fixture are small enough for SymPy's
        # deterministic primality test (below 2^64).
        assert all(p<2**64 and S.isprime(p) for p in factors)
        if all(p<=R for p in factors):
            retained+=1
        for p in factors:
            if p<=R or D%p==0:
                continue
            fp=S.Poly(f,x,modulus=int(p))
            gp=S.Poly(g,x,modulus=int(p))
            r=S.gcd(fp,gp)
            assert r.degree()>0
            for j,other in incidences.get(p,[]):
                assert resultants[min(i,j),max(i,j)]%p!=0
                assert S.gcd(r,other).degree()==0
            incidences.setdefault(p,[]).append((i,r))
    print('large-prime fixture: marks=%d pairs=%d R=%d max resultant=%d; cutoff-retained=%d; large prime incidences=%d distinct rational primes=%d' % (len(gs),len(resultants),R,max(resultants.values()),retained,sum(map(len,incidences.values())),len(incidences)))


if __name__=='__main__':
    targeted_fixture()
    large_prime_fixture()
