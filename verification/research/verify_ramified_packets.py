#!/usr/bin/env python3
"""Exact CRT/Eisenstein packet and cross-map norm-gluing tests.
Requires SymPy 1.14. These are finite identities, not a random supply theorem.
"""
from itertools import product
from math import gcd, prod
from random import Random
import sympy as sp

x=sp.Symbol('x')


def poly(cs):
    return sp.Poly.from_list(list(reversed(cs)),x,domain=sp.ZZ)


def vp(a,p):
    assert a!=0
    v=0
    while a%p==0:a//=p;v+=1
    return v


def norm(f,h): return int(sp.resultant(f,h))


def root_packet(N,qs,ts,real):
    Q=prod(qs);d=len(ts)
    assert d>=3 and d%2 and gcd(Q,N)==1 and prod(ts)%N==Q%N
    F=sp.Poly(prod(x-t for t in ts),x,domain=sp.ZZ)
    S=0
    if real:
        S=Q*(8*d*N*(4*(d+1))**(d-1)+1)
        P=sp.Poly(prod(x-i*S for i in range(d)),x,domain=sp.ZZ)
    else:
        P=sp.Poly(x**d,x,domain=sp.ZZ)
    cs=[-Q]+[int(P.nth(j))+Q*((int(F.nth(j)-P.nth(j))*pow(Q,-1,N))%N)
              for j in range(1,d)]+[1]
    f=poly(cs)
    assert all(int((f-F).nth(j))%N==0 for j in range(d+1))
    assert f.is_monic and f.degree()==d and f.is_irreducible
    disc=int(f.discriminant());assert disc
    for p in qs:
        assert sp.isprime(p) and all(c%p==0 for c in cs[:-1]) and vp(cs[0],p)==1
        assert vp(disc,p)>=d-1
    if real:
        for i in range(d):
            v=[sum(c*(4*i*S+sg*S)**j*4**(d-j) for j,c in enumerate(cs))
               for sg in (-1,1)]
            assert v[0]*v[1]<0
    assert norm(f,poly([0,1]))==Q
    u=sp.Poly(1-sum((cs[j]//Q)*x**j for j in range(1,d)),x,domain=sp.ZZ)
    assert (Q*u-poly([0]*d+[1])).rem(f).is_zero and norm(f,u)==1
    assert prod(int(u.eval(t))%N for t in ts)%N==1
    return f


def check_packets():
    rng=Random(1701);fields=local=norms=glues=0
    for N,qs,d,real in product((77,1189),((3,5),(13,17)),(3,5,7),(False,True)):
        Q=prod(qs);ts=[]
        while len(ts)<d-1:
            t=rng.randrange(1,N)
            if gcd(t,N)==1:ts.append(t)
        ts.append(Q*pow(prod(ts),-1,N)%N)
        f=root_packet(N,qs,ts,real);fields+=1;local+=len(qs)
        for _ in range(12):
            h=poly([rng.randrange(-5,6) for i in range(d)])
            assert norm(f,h)%N==prod(int(h.eval(t)) for t in ts)%N
            norms+=1
        for _ in range(6):
            hs=[]
            while len(hs)<d:
                h=poly([rng.randrange(-5,6) for i in range(d)])
                if gcd(norm(f,h),N)==1:hs.append(h)
            lhs=prod(int(h.eval(t)) for h,t in zip(hs,ts))%N
            rhs=norm(f,hs[-1])*prod(int(h.eval(t))*pow(int(hs[-1].eval(t)),-1,N)
                                       for h,t in zip(hs[:-1],ts[:-1]))%N
            assert lhs==rhs
            glues+=1
    # Include repeated roots: the norm formula is a resultant identity, not semisimplicity.
    f=root_packet(77,(13,),[1,1,13],False)
    assert norm(f,poly([2,3]))%77==5*5*(2+3*13)%77
    norms+=1;fields+=1;local+=1
    print('constructed ramified fields:',fields,'local discriminant guards:',local,
          'norm evaluations:',norms,'cross-map transitions:',glues)


def check_cross_map_rank():
    rng=Random(1729);count=0
    for _ in range(200):
        d=rng.choice((3,5,7));m=rng.randrange(1,5);fs=sp.Matrix([rng.randrange(1,5) for i in range(m)])
        n=1+d*m;P=sp.zeros(1+(d-1)*m,n);P[0,0]=1;P[0,n-m:n]=fs.T
        for i in range(d-1):
            P[1+i*m:1+(i+1)*m,1+i*m:1+(i+1)*m]=sp.eye(m)
            P[1+i*m:1+(i+1)*m,n-m:n]=-sp.eye(m)
        G=sp.Matrix.vstack(-fs.T,*([sp.eye(m)]*d))
        assert P*G==sp.zeros(P.rows,m) and P.rank()==n-m
        W=sp.Matrix(n,6,[rng.randrange(-5,6) for i in range(n*6)])
        assert (P*W).rank()==W.row_join(G).rank()-m
        count+=1
    print('cross-map exact rank cases:',count)


def fixture():
    N=1189;Q=143;qs=(11,13);ts=[2,3,Q*pow(6,-1,N)%N]
    f=root_packet(N,qs,ts,True)
    ss=[t*t%N for t in ts]+[Q*Q%N]
    assert len(set(ss))==4 and all(gcd(s,N)==1 for s in ss)
    # Old separate norm-valuation rows have rank 4; the exact common factor
    # in the three modular copies is sent to its norm, canceling the last row.
    theta2=poly([0,0,1]);assert norm(f,theta2)==Q*Q
    assert prod(ss[:3])%N==ss[3]
    c=(1,1,1,-1)
    roots=[[h for h in range(N) if gcd(h,N)==1 and h*h%N==s] for s in ss]
    assert all(len(rr)==4 for rr in roots)
    counts={}
    for hs in product(*roots):
        z=prod(pow(h,e,N) for h,e in zip(hs,c))%N
        assert z*z%N==1
        g=gcd(z-1,N);counts[g]=counts.get(g,0)+1
    assert sum(v for g,v in counts.items() if 1<g<N)==128
    print('manufactured cross-map fixture: N',N,'squares',ss,'relation',c,'gcd counts',sorted(counts.items()))


if __name__=='__main__':
    check_packets();check_cross_map_rank();fixture()
