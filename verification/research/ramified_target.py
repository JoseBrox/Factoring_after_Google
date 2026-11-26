"""Exact CRT, Eisenstein, sign-bracket and target-norm fixture."""
from math import gcd
import sympy as S


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def product_roots(rs):
    a=[1]
    for r in rs: a=mul(a,[-r,1])
    return a


def ev(a,x):
    r=0
    for v in a[::-1]: r=r*x+v
    return r


def sign_rational(a,num,den):
    z,scale=a[-1],1
    for v in a[-2::-1]:
        scale*=den
        z=z*num+v*scale
    return (z>0)-(z<0)


def main():
    # Small fixture uses manually chosen sizes, not the eventual asymptotic
    # inequality d-k-J>0. It checks the CRT, Eisenstein and norm identities.
    N,ell,d,k,r=77,5,8,3,3
    m=1<<((N.bit_length()+k-1)//k)
    R=[3*ell*77*101*(2*j+1) for j in range(1,d+1)]
    assert all(gcd(m-x,N)==1 for x in R)
    P,Q=product_roots(R),product_roots(R[:r])
    assert m**k>N and gcd(4*ell*ev(Q,m),N)==1
    for c in (ell,1):
        h0=0
        if c==1:
            h0=next(t for t in (0,2*ell) if (P[0]+c+Q[0]*t)%4==2)
        v=(-(ev(P,m)+c+ev(Q,m)*h0)*pow(4*ell*ev(Q,m),-1,N))%N
        h=[]
        for j in range(k):
            v,a=divmod(v,m);h.append(4*ell*a)
        assert v==0
        h[0]+=h0
        f=P[:];f[0]+=c
        for j,a in enumerate(mul(Q,h)):f[j]+=a
        assert f[-1]==1 and ev(f,m)%N==0
        if c==ell:
            assert all(a%ell==0 for a in f[:-1]) and f[0]%(ell*ell)==ell
        else:
            assert all(a%2==0 for a in f[:-1]) and f[0]%4==2
        assert all(ev(f,x)==c for x in R[:r])
        assert all(sign_rational(f,4*x-1,4)*sign_rational(f,4*x+1,4)==-1 for x in R)
        X=S.symbols('X'); F=sum(a*X**j for j,a in enumerate(f))
        assert S.Poly(F,X).is_irreducible
        assert all(abs(S.resultant(F,X-x,X))==c for x in R[:r])
    V=S.ones(1,r)
    assert V*S.Matrix([-d]+[0]*(r-1))==-d*S.ones(1,1)
    assert len(V.nullspace())==r-1
    print('ramified target: N=%d ell=%d d=%d shared marks=%d, %d exact sign brackets' %(N,ell,d,r,2*d))
    print('target valuation: b=%d, particular coefficient=%d, E=1; kernel rank=%d' %(d,-d,r-1))
    print('No order certificate asserted: target log cancellation remains necessary.')


if __name__=='__main__':
    main()
