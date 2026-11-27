"""Exact 2-power character-lift obstruction and labelled short-ratio tests.
Standard library. No uniform deterministic target-selection claim.
"""
from itertools import product
from math import gcd, isqrt, prod
from random import Random
from primitive_ratio_lattice import primitive_pairs, primes, peel


def jacobi(a,n):
    assert n>0 and n%2
    a%=n;v=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5):v=-v
        a,n=n,a
        if a%4==n%4==3:v=-v
        a%=n
    return v if n==1 else 0


def solve_power_two(A,b,m,M):
    """A z = b (mod M), M a positive power of two.
    Return (solution,None) or (None,dual witness c: cA=0, cb!=0 mod M).
    No enumeration of M; row operations and backward substitution only.
    """
    assert M>=2 and M&(M-1)==0 and len(A)==len(b)
    r=len(A);C=[[x%M for x in row] for row in A];d=[x%M for x in b]
    U=[[int(i==j) for j in range(r)] for i in range(r)]
    left=set(range(m));piv=[]
    def witness(i,p):
        c=[M//p*x%M for x in U[i]]
        assert all(sum(c[j]*A[j][k] for j in range(r))%M==0 for k in range(m))
        assert sum(x*y for x,y in zip(c,b))%M
        return None,c
    for i in range(min(m,r)):
        ij=min(((C[u][v]&-C[u][v],u,v) for u in range(i,r) for v in left if C[u][v]),default=None)
        if ij is None:break
        p,u,v=ij
        C[i],C[u]=C[u],C[i];d[i],d[u]=d[u],d[i];U[i],U[u]=U[u],U[i]
        k=pow(C[i][v]//p,-1,M)
        C[i]=[x*k%M for x in C[i]];d[i]=d[i]*k%M;U[i]=[x*k%M for x in U[i]]
        assert C[i][v]==p and all(x%p==0 for x in C[i])
        if d[i]%p:return witness(i,p)
        for j in range(i+1,r):
            assert C[j][v]%p==0
            q=C[j][v]//p
            if q:
                C[j]=[(x-q*y)%M for x,y in zip(C[j],C[i])]
                d[j]=(d[j]-q*d[i])%M
                U[j]=[(x-q*y)%M for x,y in zip(U[j],U[i])]
            assert C[j][v]==0
        left.remove(v);piv.append((i,v,p))
    for i in range(len(piv),r):
        assert not any(C[i])
        if d[i]:return witness(i,M)
    z=[0]*m
    for i,v,p in reversed(piv):
        t=(d[i]-sum(x*y for x,y in zip(C[i],z)))%M
        assert t%p==0
        z[v]=t//p
    assert all((sum(x*y for x,y in zip(row,z))-w)%M==0 for row,w in zip(A,b))
    return z,None


def lift_system(N,P,rows,e):
    M=1<<e;eta=[int(jacobi(p,N)==-1) for p in P]
    h=[]
    for row in rows:
        assert prod(pow(p,x,N) for p,x in zip(P,row))%N==1
        s=sum(x*y for x,y in zip(row,eta));assert s%2==0
        h.append((-s//2)%M)
    z,c=solve_power_two(rows,h,len(P),M)
    if z is not None:
        labels=[a+2*b for a,b in zip(eta,z)]
        assert all(sum(x*y for x,y in zip(row,labels))%(2*M)==0 for row in rows)
        return labels,None
    total=[sum(c[i]*rows[i][j] for i in range(len(rows))) for j in range(len(P))]
    assert all(x%M==0 for x in total)
    u=prod(pow(p,x//M,N) for p,x in zip(P,total))%N
    assert pow(u,M,N)==1 and jacobi(u,N)==-1
    return None,u


def jacobi_root_split(N,u,e):
    assert N%(1<<(e+1))==1 and jacobi(u,N)==-1 and pow(u,1<<e,N)==1
    for _ in range(e+1):
        d=gcd(u-1,N)
        if 1<d<N:return d
        u=u*u%N
    raise AssertionError('Jacobi-labelled root must split at k<v2(N-1)')


def label_collision(N,a,H,P,labels,e):
    M=1<<e
    d,pairs,_=primitive_pairs(N,a,H,H)
    if d:return d,None,0
    first=None;hits=0
    for x,y in pairs:
        if y<=0:continue
        rx,u=peel(x,P);ry,v=peel(y,P)
        if rx!=1 or ry!=1:continue
        w=[v.get(p,0)-u.get(p,0) for p in P]
        assert prod(pow(p,j,N) for p,j in zip(P,w))%N==a
        label=sum(x*y for x,y in zip(w,labels))%(2*M);hits+=1
        if first is None:first=(label,w)
        elif label!=first[0]:
            row=[x-y for x,y in zip(w,first[1])]
            assert prod(pow(p,j,N) for p,j in zip(P,row))%N==1
            assert sum(x*y for x,y in zip(row,labels))%(2*M)
            return None,row,hits
    return None,None,hits


def test_solver():
    rng=Random(707);count=bad=0
    for M in (2,4,8,16):
        for _ in range(500):
            m=rng.randrange(1,4);r=rng.randrange(0,6)
            A=[[rng.randrange(-2*M,2*M+1) for j in range(m)] for i in range(r)]
            b=[rng.randrange(-2*M,2*M+1) for i in range(r)]
            z,c=solve_power_two(A,b,m,M)
            brute=next((x for x in product(range(M),repeat=m) if all((sum(a*u for a,u in zip(row,x))-d)%M==0 for row,d in zip(A,b))),None)
            assert (z is None)==(brute is None)
            count+=1;bad+=c is not None
    # Large modulus: exponent bits, not 2^e, determine solver cost.
    for _ in range(100):
        M=1<<rng.randrange(50,250);m=8;r=10
        A=[[rng.randrange(M) for j in range(m)] for i in range(r)]
        t=[rng.randrange(M) for j in range(m)];b=[sum(x*y for x,y in zip(row,t))%M for row in A]
        assert solve_power_two(A,b,m,M)[0] is not None
    print('2-power system:',count,'brute-force comparisons,',bad,'dual certificates; 100 large-modulus solvable checks',flush=True)


def test_jacobi_roots():
    checks=0
    for N in range(9,500,4):
        s=((N-1)&-(N-1)).bit_length()-1
        for u in range(1,N):
            if jacobi(u,N)!=-1:continue
            for e in range(1,s):
                if pow(u,1<<e,N)!=1:continue
                d=jacobi_root_split(N,u,e);assert 1<d<N and N%d==0
                checks+=1
    print('Jacobi-labelled root split:',checks,'exhaustive cases',flush=True)


def finite_demo(N,e,base_bound,H,seed,limit=6000):
    # The exact query is the primitive lattice enumeration, not a precomputed
    # table of all unit residues. We allow all base-smooth positive ratios
    # in these small tests, not the asymptotic disjoint narrow bands.
    # Ignore coordinate-gcd exits ONLY to exercise the new extractor.
    P=primes(base_bound);assert all(N%p for p in P) and N%(1<<(e+1))==1
    rng=Random(seed);rows=[];early=0;attempts=0;hits=0
    for _ in range(limit):
        labels,u=lift_system(N,P,rows,e)
        if u is not None:
            d=jacobi_root_split(N,u,e);assert 1<d<N and N%d==0
            print('label-lift split:',N,'depth',e,'base',len(P),'H',H,'relations',len(rows),'queries',attempts,'ignored gcd exits',early,'root',u,'factor',d,flush=True)
            return True
        a=rng.randrange(1,N)
        if gcd(a,N)!=1:continue
        d,row,n=label_collision(N,a,H,P,labels,e);attempts+=1;hits+=n
        if d:early+=1;continue
        if row is not None:rows.append(row)
    print('label-lift cap:',N,e,'relations',len(rows),'queries',attempts,'ignored gcd exits',early,'smooth hits',hits,flush=True)
    return False


if __name__=='__main__':
    test_solver();test_jacobi_roots()
    for N,e,B,H in [(47053,1,47,650),(11009,2,43,312),(31921,3,67,540),(27233,4,67,495)]:
        finite_demo(N,e,B,H,791+e)
