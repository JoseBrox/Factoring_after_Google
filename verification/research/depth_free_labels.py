"""Exact short-ratio fibre/translate rank driver; finite verification only.
No uniform deterministic hitter is claimed. Standard library.
"""
from fractions import Fraction as Q
from functools import reduce
from math import gcd, isqrt, lcm, prod
from random import Random
from primitive_ratio_lattice import primitive_pairs, primes, peel
from pooled_shift_relations import exact_eliminate


def primitive_annihilator(rows, m):
    piv = exact_eliminate([{j:Q(x) for j,x in enumerate(r) if x} for r in rows])
    if len(piv) == m:
        return None
    w = [Q(0)]*m
    w[next(j for j in range(m) if j not in piv)] = Q(1)
    for j in sorted(piv,reverse=True):
        r,_ = piv[j]
        w[j] = -sum(a*w[k] for k,a in r.items() if k!=j)
    d = lcm(*(x.denominator for x in w))
    z = [int(d*x) for x in w]
    g = reduce(gcd,z)
    z = [x//g for x in z]
    assert reduce(gcd,z)==1 and any(x%2 for x in z)
    assert all(sum(a*b for a,b in zip(r,z))==0 for r in rows)
    return z


def image(N,P,v):
    return prod(pow(p,e,N) for p,e in zip(P,v))%N


def label(v,z,M):
    return sum(a*b for a,b in zip(v,z))%M


def fibre(N,a,H,P):
    d,pairs,_ = primitive_pairs(N,a,H,H)
    if d:return d,[]
    out=[]
    for x,y in pairs:
        if y<=0:continue
        rx,u=peel(x,P);ry,v=peel(y,P)
        if rx!=1 or ry!=1:continue
        row=[v.get(p,0)-u.get(p,0) for p in P]
        assert image(N,P,row)==a
        out.append(row)
    return None,out


def query(N,a,H,P,z,M,j):
    """Find unequal labels in fibre(a) U q0*fibre(a/q0)."""
    assert M==1<<(N.bit_length()+1) and z[j]%2
    first=None
    for shift in (0,1):
        target = a*pow(P[j],-shift,N)%N
        d,vs = fibre(N,target,H,P)
        if d:return d,None,None
        for v in vs:
            v=v[:];v[j]+=shift
            assert image(N,P,v)==a
            t=label(v,z,M)
            if first is None:first=(t,v,shift)
            elif t!=first[0]:
                row=[x-y for x,y in zip(v,first[1])]
                assert image(N,P,row)==1 and label(row,z,M)
                return None,row,(first[2],shift)
    return None,None,None


def determinant(A):
    # Independent exact Bareiss elimination for a full rank square matrix.
    A=[r[:] for r in A];n=len(A);prev=1;sign=1
    for i in range(n-1):
        j=next(j for j in range(i,n) if A[j][i])
        if i!=j:A[i],A[j]=A[j],A[i];sign=-sign
        p=A[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                z=A[j][k]*p-A[j][i]*A[i][k]
                assert z%prev==0
                A[j][k]=z//prev
            A[j][i]=0
        prev=p
    return sign*A[-1][-1]


def split(N,P,E):
    assert E>0 and all(pow(p,E,N)==1 for p in P)
    t=E
    while t%2==0:t//=2
    for p in P:
        s=t
        while s<=E:
            d=gcd(pow(p,s,N)-1,N)
            if 1<d<N:return d
            s*=2
    return None


def brute_fibre(N,a,H,P):
    out=[]
    for x in range(1,H+1):
        if gcd(x,N)!=1:continue
        rx,u=peel(x,P)
        if rx!=1:continue
        y=a*x%N
        while y<=H:
            if y>0 and gcd(x,y)==1:
                ry,v=peel(y,P)
                if ry==1:out.append([v.get(p,0)-u.get(p,0) for p in P])
            y+=N
    return out


def test_queries():
    rng=Random(8829);count=early=internal=translated=0
    for N in (35,77,143,899,1333,1763):
        H=min(N-1,3*(isqrt(N)+1));P=[p for p in primes(19) if gcd(p,N)==1]
        M=1<<(N.bit_length()+1)
        for _ in range(150):
            a=rng.randrange(1,N)
            if gcd(a,N)!=1:continue
            z=[rng.randrange(M) for p in P];j=rng.randrange(len(P));z[j]|=1
            if rng.randrange(3)==0:z=[1]*len(P)
            vals=[]
            for s in (0,1):
                for v in brute_fibre(N,a*pow(P[j],-s,N)%N,H,P):
                    v[j]+=s;vals.append(label(v,z,M))
            d,row,typ=query(N,a,H,P,z,M,j)
            if d:
                assert 1<d<N and N%d==0;early+=1;continue
            assert (row is not None)==(len(set(vals))>1)
            if row is not None:
                assert image(N,P,row)==1 and label(row,z,M)
                if typ[0]==typ[1]:internal+=1
                else:translated+=1
            count+=1
    print('fibre/translate query comparisons:',count,'factor exits',early,'internal disagreements',internal,'translated disagreements',translated,flush=True)


def test_annihilators():
    rng=Random(734);count=0
    for _ in range(300):
        m=rng.randrange(1,13);r=rng.randrange(0,m)
        A=[[rng.randrange(-10,11) for _ in range(m)] for _ in range(r)]
        z=primitive_annihilator(A,m)
        assert z is not None and reduce(gcd,z)==1 and any(x%2 for x in z)
        count+=1
    print('primitive annihilator checks:',count,flush=True)


def run(N,B,H,seed,limit=5000):
    # Ignore coordinate gcd exits only in this finite rank-driver experiment.
    # A production algorithm would return the factor immediately.
    rng=Random(seed);P=primes(B);assert all(gcd(p,N)==1 for p in P)
    M=1<<(N.bit_length()+1);rows=[];queries=early=internal=translated=0
    for _ in range(limit):
        z=primitive_annihilator(rows,len(P))
        if z is None:
            E=abs(determinant(rows));d=split(N,P,E)
            assert d and 1<d<N and N%d==0
            print('rank driver:',N,'v2(N-1)',((N-1)&-(N-1)).bit_length()-1,'base',len(P),'H',H,'rank',len(rows),'queries',queries,'ignored gcd exits',early,'internal',internal,'translated',translated,'exponent bits',E.bit_length(),'factor',d,flush=True)
            return
        j=next(j for j,x in enumerate(z) if x%2)
        a=rng.randrange(1,N)
        if gcd(a,N)!=1:continue
        d,row,typ=query(N,a,H,P,z,M,j);queries+=1
        if d:early+=1;continue
        if row is None:continue
        assert sum(x*y for x,y in zip(row,z))!=0
        rows.append(row)
        if typ[0]==typ[1]:internal+=1
        else:translated+=1
        assert len(exact_eliminate([{k:Q(a) for k,a in enumerate(v) if a} for v in rows]))==len(rows)
    print('rank cap:',N,'rank',len(rows),'base',len(P),'queries',queries,flush=True)
    raise AssertionError('finite driver did not reach full rank')


if __name__=='__main__':
    test_queries();test_annihilators()
    for N,B,H in ((47053,47,650),(11009,43,312),(100160063,67,60048),(3233,31,300),(1333,29,148)):
        run(N,B,H,907+N)
