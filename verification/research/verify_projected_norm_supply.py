#!/usr/bin/env python3
"""Exact local-square cofactor lifts, norm parity energy, finite supply tests."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, gcd, isqrt, prod
from random import Random
import sympy as sp

X = sp.Symbol('X')


def poly(cs):
    return sp.Poly.from_list(list(reversed(cs)), X, domain=sp.ZZ)


def digits(a, m, k):
    c=[]
    for _ in range(k):
        a,r=divmod(a,m); c.append(r)
    assert a==0
    return poly(c)


def res(f,g): return int(sp.resultant(f,g))


def lift(N,u,m,k):
    assert 2<=m and k>=2 and m**k>N and gcd(u*m,N)==1
    inv2=pow(2,-1,N)
    # Select a public difference-of-squares parametrization, no hidden root.
    for a in range(1,2*N.bit_length()+2):
        if gcd(a,N)!=1: continue
        v=u*pow(a,-1,N)%N
        w=(v-a)*inv2%N;z=(v+a)*inv2%N
        if gcd(w,N)==1:break
    else:return None
    assert (z*z-w*w-u)%N==0
    F=poly([0]*k+[1])-digits(m**k-N,m,k)
    assert F.eval(m)==N
    D=(F-poly([N])).exquo(poly([-m,1]))
    R0=poly([0]*k+[1])+digits((w-m**k)%N,m,k)
    R=None
    for j in range(k*N.bit_length()+2):
        T=R0+j*poly([-m,1])
        if gcd(res(T,D),N)==1:
            R=T;break
    if R is None:return None
    f=F*F+poly([-m,1])*R*R
    g=(f-poly([N*N])).exquo(poly([-m,1]))
    A=R*R+F*D
    assert f.is_monic and f.degree()==2*k+1 and g.degree()==2*k
    assert (g-A)==N*D and f.eval(m)==N*N
    assert (F*A-N*R*R).rem(f).is_zero
    assert gcd(res(g,R),N)==1
    Q0=poly([0]*k+[1])+digits((z-m**k)%N,m,k)
    W=None
    for j in range(2*k*N.bit_length()+2):
        T=Q0+j*poly([-m,1])
        if gcd(res(g,T),N)==1:
            W=T;break
    if W is None:return None
    B=res(g,R*W)
    U=A+R*W; V=A-R*W
    n1=res(f,U);n2=res(f,V)
    assert gcd(n1*n2*w*B,N)==1
    assert (n1*n2+u*(w*B)**2)%N==0
    assert res(f,F)==N*res(F,R)**2
    assert res(f,A)==N**(2*k)*res(F,R)**2
    assert res(f,R)==(-1)**k*res(F,R)**2
    # Resultant identities in the quotient, checked independently by multiplication.
    assert N*n1==(-1)**k*res(f,N*R+F*W)
    assert N*n2==(-1)**k*res(f,N*R-F*W)
    return -n1*n2,n1,n2,k,A,f


def check_parity_series():
    # Independent exhaustive enumeration with arbitrary ideal residue degrees.
    rng=Random(314159);cases=coeff=0
    for _ in range(160):
        fs=[rng.randrange(1,5) for _ in range(rng.randrange(1,5))]
        D=sum(fs);cap=10
        actual=Counter()
        for es in product(*(range(cap//f+1) for f in fs)):
            n=sum(e*f for e,f in zip(es,fs))
            if n<=cap:actual[n]+=1
        dp=[1]+[0]*cap
        for f in fs:
            for i in range(f,cap+1):dp[i]+=dp[i-f]
        for i in range(cap+1):
            assert actual[i]==dp[i]
            assert dp[i]<=comb(len(fs)+i-1,i)
            if i%2==0:assert dp[i]<=comb(D+i-1,i)
            coeff+=1
        cases+=1
    # Even-energy formula for rational x and repeated ideal axes.
    for d,den in product(range(1,13),(2,3,5,11,101)):
        x=Q(1,den);E=((1-x)**(-d)+(1+x)**(-d))/2
        assert E>=1+comb(d+1,2)*x*x
        if d*x<=Q(1,2):
            # Exact elementary bound from the second derivative on [-x,x].
            assert E-1<=Q(d*(d+1),2)*x*x*(1-x)**(-d-2)
    print('weighted Euler coefficient cases:',cases,'coefficients:',coeff,'even-energy checks:',60)


def binary_rank(vs):
    basis={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j in basis:v^=basis[j]
            else:basis[j]=v;break
    return len(basis)


def gcd_free_parities(ns):
    # Exact squareclasses in the span of the given integers, without factoring.
    pool=set(abs(n) for n in ns if abs(n)>1)
    while True:
        hit=None
        seq=sorted(pool)
        for i,a in enumerate(seq):
            for b in seq[:i]:
                g=gcd(a,b)
                if g>1:
                    hit=(a,b,g);break
            if hit:break
        if hit is None:break
        a,b,g=hit;pool.remove(a);pool.remove(b)
        pool.update(v for v in (g,a//g,b//g) if v>1)
    axes=sorted(pool)
    assert all(gcd(a,b)==1 for i,a in enumerate(axes) for b in axes[:i])
    nonsq=[a for a in axes if isqrt(a)**2!=a]
    idx={a:i+1 for i,a in enumerate(nonsq)}
    rows=[]
    for n in ns:
        z=abs(n);v=int(n<0);recon=1
        for a in axes:
            e=0
            while z%a==0:z//=a;e+=1
            recon*=a**e
            if e%2 and a in idx:v^=1<<idx[a]
        assert z==1 and recon==abs(n)
        rows.append(v)
    return rows,len(nonsq)+1


def check_supply():
    rng=Random(271828);total=skips=verified=0
    for N in (77,899,1189,10403,1022117):
        U=[u for u in range(1,N) if gcd(u,N)==1] if N<20000 else None
        if U is None:
            U=[]
            while len(U)<80:
                u=rng.randrange(1,N)
                if gcd(u,N)==1:U.append(u)
        elif len(U)>80:U=rng.sample(U,80)
        m=isqrt(N)+1
        while gcd(m,N)!=1:m+=1
        k=2
        norms=[];height=[];smooth=Counter()
        for u in U:
            total+=1;out=lift(N,u,m,k)
            if out is None:skips+=1;continue
            n,n1,n2,_,A,f=out;verified+=1
            height.append(abs(n).bit_length());norms.append(n)
            # Exact smooth-squareclass test without factoring the cofactor.
            for B in (13,31,101):
                z=abs(n)
                for p in list(sp.primerange(2,B+1)):
                    while z%p==0:z//=p
                if isqrt(z)**2==z:smooth[B]+=1
        rows,labels=gcd_free_parities(norms)
        rank=binary_rank(rows)
        print('N',N,'m',m,'verified',len(height),'norm-product bits', (min(height),max(height)) if height else None,
              'rank',rank,'gcd-free labels incl sign',labels,'distinct signatures',len(set(rows)),
              'smooth parity 13/31/101',tuple(smooth[B] for B in (13,31,101)))
    print('uniform public-unit lifts:',verified,'out of',total,'failed guards:',skips)


def fixed_environment(N,a):
    m=a*a;assert gcd(a,N)==1
    k=1
    while m**k<=N:k+=1
    G=poly([0]*(k+1)+[1])-digits(m**(k+1)-N,m,k+1)
    F0=poly([0,1])*G
    T=digits((1-int(F0.diff().eval(m)))*pow(m,-1,N)%N,m,k)
    F=F0+poly([0,-m,1])*T
    D=(F-poly([m*N])).exquo(poly([-m,1]))
    H=4*m*N*F+poly([0,-m,1])*D*D
    K=(-1)**D.degree()*res(D,poly([(m*N)**2-m,1]))
    assert F.is_monic and F.eval(0)==0 and F.eval(m)==m*N
    assert D.eval(0)==N and D.eval(m)%N==1 and K%N==1
    assert H.is_monic and (H-poly([0,-m,1])*D*D)==4*m*N*F
    return F,D,H,K,k,m


def fixed_offset_lift(N,u,a,env):
    F,D,H,K,k,m=env;w=(u*pow(a,-1,N)-a)*pow(2,-1,N)%N
    if gcd(w,N)!=1:return None
    S=poly([0,1])*(poly([0]*k+[1])+digits((w-1-m**(k+1))*pow(m,-1,N)%N,m,k))
    R=poly([1])+D*S;Q=R+a*D
    f=F*F+poly([-m,1])*R*R
    g=(f-poly([(m*N)**2])).exquo(poly([-m,1]))
    A=R*R+F*D;P=A+R*Q;M=A-R*Q;C=2*F-poly([0,1])*D-2*a*R
    assert R.eval(0)==1 and R.eval(m)%N==w
    assert M==D*(F-a*R)
    assert (P*(F-a*R)-R*R*C).rem(f).is_zero
    assert C.eval(0)==-2*a and (C.eval(m)+u)%N==0
    b=res(g,R*Q);n1=res(f,P);n2=res(f,M)
    assert gcd(w*b*n1*n2,N)==1 and (n1*n2+u*(w*b)**2)%N==0
    assert res(f,D)==K
    assert n2==-a*K*res(F-a*R,R)**2
    nc=res(H,C)
    assert n1*(2*a)**(2*F.degree())==2*nc*res(R,F)**2
    assert (nc-2*a*u*res(D,C)**2)%N==0
    assert gcd(nc,N)==1
    return 2*a*nc,n1,n2,nc


def check_fixed_offsets():
    rng=Random(112358);count=guards=0
    for N in (77,899,1189,10403,1022117):
        a=isqrt(isqrt(N))+1
        while gcd(a,N)!=1:a+=1
        env=fixed_environment(N,a);F,D,H,K,k,m=env
        vals=[];norm_bits=[];smooth=Counter()
        for _ in range(24):
            u=rng.randrange(1,N)
            while gcd(u,N)!=1:u=rng.randrange(1,N)
            out=fixed_offset_lift(N,u,a,env)
            if out is None:guards+=1;continue
            v,n1,n2,nc=out;count+=1
            vals.append(v);norm_bits.append(abs(v).bit_length())
            for B in (13,31,101):
                z=abs(v)
                for p in list(sp.primerange(2,B+1)):
                    while z%p==0:z//=p
                if isqrt(z)**2==z:smooth[B]+=1
        rows,labels=gcd_free_parities(vals)
        print('fixed offset N',N,'a',a,'fixed H degree',H.degree(),'accepted',len(vals),
              'projected rank',binary_rank(rows),'labels',labels,'projected norm bits',
              (min(norm_bits),max(norm_bits)) if vals else None,
              'smooth parity 13/31/101',tuple(smooth[B] for B in (13,31,101)))
    print('fixed-offset exact lifts:',count,'nonunit w guards:',guards)


if __name__=='__main__':
    check_parity_series();check_supply();check_fixed_offsets()
