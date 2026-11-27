#!/usr/bin/env python3
"""Finite exact tests of parity-preserving unit extraction and lattice content.
No implementation of general ideal refinement or certified log recovery.
"""
from itertools import product
from math import gcd, prod
from random import Random
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp


def kernel(A):
    D,S,T=smith_normal_decomp(A,domain=sp.ZZ)
    assert S*A*T==D and abs(S.det())==abs(T.det())==1
    r=sum(D[i,i]!=0 for i in range(min(D.shape)))
    K=T[:,r:]
    assert A*K==sp.zeros(A.rows,K.cols)
    return K


def sign_vector(K,signs):
    # With at least two independent parity columns, one is sign-even or
    # the sum of any two is sign-even and nonzero mod 2.
    for i in range(K.cols):
        u=K[:,i]
        if sum(int(a)*b for a,b in zip(u,signs))%2==0:
            break
    else:
        u=K[:,0]+K[:,1]
    assert any(int(x)%2 for x in u)
    assert sum(int(a)*b for a,b in zip(u,signs))%2==0
    return [int(a) for a in u]


def check_kernels():
    rng=Random(317)
    count=0
    for _ in range(500):
        n=rng.randrange(3,8); m=rng.randrange(1,n-1)
        A=sp.Matrix(m,n,[rng.randrange(-9,10) for _ in range(m*n)])
        K=kernel(A)
        assert K.cols>=2
        parities={tuple(int(a)%2 for a in K*sp.Matrix(v))
                  for v in product((0,1),repeat=K.cols)}
        assert len(parities)==2**K.cols
        for signs in product((0,1),repeat=n):
            v=sign_vector(K,signs)
            assert A*sp.Matrix(v)==sp.zeros(m,1)
            count+=1
    print('saturated-kernel and sign tests:',count)


def check_unit_fixture():
    # theta^3-theta-1=0, norm theta=1; theta maps to 61 mod 77.
    N, theta = 77, 61
    x=sp.Symbol('x')
    f=sp.Poly(x**3-x-1,x)
    assert f.eval(theta)%N==0
    assert f.is_irreducible
    a=(2,0,2,4,0); b=(0,2,0,0,2); u=(2,2,4,2,6)
    M=sp.Matrix([a,b,u])
    K=kernel(M)
    v=sign_vector(K,[0]*5)
    assert M*sp.Matrix(v)==sp.zeros(3,1)
    # These are genuine compact exact identities: q_i=2^b_i,
    # gamma_i=2^a_i*theta^u_i; the exact summed exponents are zero.
    R=[pow(2,aa+bb,N)*pow(theta,uu,N)%N for aa,bb,uu in zip(a,b,u)]
    assert prod(pow(r,e,N) for r,e in zip(R,v))%N==1
    fibres=[[h for h in range(N) if gcd(h,N)==1 and h*h%N==r] for r in R]
    assert all(len(F)==4 for F in fibres)
    outputs={}
    for hs in product(*fibres):
        X=prod(pow(h,e,N) for h,e in zip(hs,v))%N
        assert X*X%N==1
        g=gcd(X-1,N)
        outputs[g]=outputs.get(g,0)+1
    assert sum(outputs.get(g,0) for g in (7,11))==4**5//2
    print('exact cubic field fixture:',v,'CRT gcd frequencies:',sorted(outputs.items()))


def check_transforms():
    rng=Random(1729)
    x,y=sp.symbols('x y')
    N=77; r,Q=2,3
    checked=skipped=0
    for _ in range(160):
        d=rng.randrange(2,7)
        cs=[rng.randrange(-20,21) for _ in range(d+1)]
        value=sum(a*r**(d-i)*Q**i for i,a in enumerate(cs))
        cs[-1]+=(-value*pow(Q**d,-1,N))%N
        F=sp.Poly(sum(a*x**(d-i)*y**i for i,a in enumerate(cs)),x,y)
        fv=int(F.eval({x:r,y:Q}))
        if not fv: continue
        assert fv%N==0
        A=sp.Matrix(2,2,[rng.randrange(-10,11) for _ in range(4)])
        D=int(A.det())
        if D==0: continue
        G=sp.Poly(F.as_expr().subs({x:A[0,0]*x+A[0,1]*y,
                                  y:A[1,0]*x+A[1,1]*y},simultaneous=True),x,y)
        c=abs(int(G.content()))
        if gcd(c,N)!=1:
            skipped+=1; continue
        P=sp.Poly(G.as_expr()/c,x,y)
        uv=A.adjugate()*sp.Matrix([r,Q]); u,w=map(int,uv)
        g=gcd(u,w); assert D%g==0
        val=int(P.eval({x:u//g,y:w//g}))
        assert c*val==(D//g)**d*fv and val%N==0
        H=sp.Poly(r*(A[1,0]*x+A[1,1]*y)-Q*(A[0,0]*x+A[0,1]*y),x,y)
        prim=H.primitive()[1]
        assert max(abs(int(a)) for a in prim.coeffs())==max(abs(u//g),abs(w//g))
        assert prim.eval({x:u//g,y:w//g})==0
        checked+=1
    print('exact lattice transformations:',checked,'nonunit-content skips:',skipped)


if __name__=='__main__':
    check_kernels()
    check_unit_fixture()
    check_transforms()
