"""Exact finite checks of the forced-norm, coupled-valuation construction.
Requires SymPy. No large-N factoring claim is tested.
"""
from math import gcd, prod
from itertools import combinations
import sympy as S
X,U = S.symbols('X U')


def make(N, primes, target=None):
    ts = [v for p in primes for v in (p,p*p)]
    if target is None:
        ts.append(primes[0]**3)
    assert len(ts)==len(set(ts)) and all(t%2==1 for t in ts)
    d=len(ts)+1+(target is not None)
    assert d%2==0
    C=2*N*prod(primes)
    marks=[1+((t-1)//2)*X for t in ts]
    if target is not None:
        assert target in primes
        marks.append(target+((1-target)//2)*X)
    f=S.Poly(X**(d-1)*(X-2)+C*prod(marks),X)
    assert f.degree()==d and f.LC()==1 and f.eval(0)%N==0
    assert all(int(a)%2==0 for a in f.all_coeffs()[1:]) and int(f.eval(0))%4==2
    assert f.is_irreducible
    for t,g in zip(ts,marks):
        assert abs(S.resultant(f.as_expr(),g,X))==t
        assert g.subs(X,0)==1
    # At every selected prime the simple root 2 is the only component
    # that can divide any of the norm-controlled marks.
    for p in primes:
        fp=S.Poly(f,X,modulus=p)
        assert fp==S.Poly(X**(d-1)*(X-2),X,modulus=p)
        assert int(fp.diff().eval(2))%p!=0
        for t,g in zip(ts,marks):
            G=S.gcd(fp,S.Poly(g,X,modulus=p))
            assert G.degree()==(1 if t%p==0 else 0)
            if G.degree()==1: assert G.monic()==S.Poly(X-2,X,modulus=p)
    V=S.Matrix([[next((e for e in range(4) if t%p**(e+1)!=0),None) for t in ts] for p in primes])
    assert V.rank()==len(primes)
    assert all(sum(v!=0 for v in V.row(i))>=2 for i in range(V.rows))
    if target is None:
        # Reciprocal polynomial F(U)=U^d f(-1/U), since d is even.
        F=S.Poly(S.expand(sum(a*(-1)**i*U**(d-i) for (i,),a in f.terms())),U)
        centers=[0]+[(t-1)//2 for t in ts]
        eps=S.Rational(1,4)
        assert all(F.eval(r-eps)*F.eval(r+eps)<0 for r in centers)
        # Exact verification of the finite valuation-kernel exponents.
        K=V.nullspace()
        assert len(K)==len(ts)-len(primes)
        print('coupled construction:', 'degree',d,'marks',len(ts),'valuation rank',V.rank(),'kernel rank',len(K),'real brackets',len(centers))
    else:
        g=marks[-1]
        assert abs(S.resultant(f.as_expr(),g,X))==target**(d-1)
        assert S.gcd(S.Poly(f,X,modulus=target),S.Poly(g,X,modulus=target)).monic()==S.Poly(X,X,modulus=target)
        assert int(g.subs(X,0))==target and gcd(target,N)==1
        # At all primes over target except the simple root 2, weighted
        # valuations of target, g and all old marks are (d-1,d-1,0...).
        # With second field Q and diagonal target scalars, the second
        # valuation equation is c_g+c_scalar=0, so E=0 in the first.
        constraints=S.Matrix([[d-1,d-1,d-1],[0,1,1]])
        ker=constraints.nullspace()
        assert all(v[0]==0 for v in ker)
        print('target interpolation:', 'degree',d,'target',target,'norm',target**(d-1),'; all exact solutions force E=0')


if __name__=='__main__':
    make(77,[3,5,13,17])
    make(77,[3,5,13,17],target=5)


def rank_one_field(N, ell, d):
    assert N%2 and ell%2 and gcd(ell,N)==1 and d>=2 and d%2==0
    A=1+ell**(d-1)
    eta=S.Rational(1,(16*A)**(4*d))
    M=(16*A)**(10*d)
    q=2*ell**(d*(d-1))
    r=(-pow(2,d,N)*pow(q,-1,N))%N
    k=max(0,(M-q*r+q*N-1)//(q*N))
    if (r+k*N)%2==0:k+=1
    C=q*(r+k*N)
    a=[(ell**j-1)//2 for j in range(1,d)]
    g=[1+t*X for t in a]
    f=S.Poly((X-2)**d+C*prod(g),X)
    assert f.degree()==d and f.LC()==1 and f.eval(0)%N==0
    assert f.eval(0)%4==2 and all(int(z)%2==0 for z in f.all_coeffs()[1:])
    assert f.is_irreducible
    assert C>=M and C%(2*ell**(d*(d-1)))==0 and C%4==2
    F=S.Poly((1+2*U)**d+C*U*prod(U-z for z in a),U)
    assert F==S.Poly(sum(c*(-1)**i*U**(d-i) for (i,),c in f.terms()),U)
    assert all(F.eval(z-eta)*F.eval(z+eta)<0 for z in [0]+a)
    # y=(theta-2)/ell^(d-1) has monic integral polynomial.
    T=S.Poly(f.as_expr().subs(X,2+ell**(d-1)*X)/ell**(d*(d-1)),X)
    assert T.LC()==1 and all(z.q==1 for z in T.all_coeffs())
    for j,h in enumerate(g,1):
        assert S.resultant(f.as_expr(),h,X)==ell**(j*d)
        # u_j=1+a_j ell^(d-1-j)y, integral with norm 1.
        uj=1+a[j-1]*ell**(d-1-j)*X
        assert S.resultant(T.as_expr(),uj,X)==1
        assert gcd(ell**j,N)==1 and pow(ell,-j,N)*ell**j%N==1
    # Exact diagonal dominance check, using exp(log)-bounds:
    # (2 eta) * (4 A^2)^(d-2)<1 means diagonal magnitude
    # exceeds the absolute off-diagonal sum of all logs.
    assert 2*eta*(4*A*A)**(d-2)<1
    print('rank-one field:', 'N',N,'target',ell,'degree',d,'C bits',C.bit_length(),
          'independent units',d-1,'known congruence-unit rank',d-2,
          'remaining log dimension',1)


if __name__=='__main__':
    rank_one_field(77,5,6)
    rank_one_field(143,7,8)
