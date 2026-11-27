#!/usr/bin/env python3
"""Exact local root prescriptions, linear square-pairing budget, and fibre amplification."""
from itertools import product
from math import gcd,prod
from random import Random
import sympy as sp
X=sp.Symbol('X')

def prescribe(N,ps):
    n=N.bit_length();Q=prod(ps);a,M=1,2;rs=[]
    for p in ps:
        assert p>2 and gcd(p,N)==1 and sp.isprime(p)
        r=N%p;eps=1 if (2*r-1)%p else -1
        assert (2*r-eps)%p
        v=(r+eps)%p
        a+=M*((v-a)*pow(M,-1,p)%p);M*=p;rs.append(r)
    assert M==2*Q
    t=int(sp.integer_nthroot(27*N//4,3)[0])+1
    m=a+M*((t-a+M-1)//M)
    count=0
    while gcd(m,N)!=1:m+=M;count+=1
    assert count<=n and t<=m<t+2*Q*(n+1)
    f=sp.Poly(X*(X-m)**2-N,X,domain=sp.ZZ)
    assert f.is_irreducible and 4*m**3>27*N and m%2
    disc=N*(4*m**3-27*N);assert disc==f.discriminant()
    U=t+2*Q*(n+1)
    assert disc<N*(4*U**3-27*N)
    for p,r in zip(ps,rs):
        assert f.eval(r)%p==0 and f.diff().eval(r)%p!=0
    return len(ps)

def check_prescriptions():
    rng=Random(1701);count=roots=0
    for N in (899,10403,1022117,100160063,101**2*103):
        assert min(sp.factorint(N))>2*N.bit_length()+3
        ps=[int(p) for p in sp.primerange(3,200) if gcd(p,N)==1]
        for _ in range(40):
            roots+=prescribe(N,rng.sample(ps,rng.randrange(1,5)));count+=1
    print('cubic CRT packet fields:',count,'simple root prescriptions:',roots)

def rank2(rows):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)

def check_fibres():
    rng=Random(1729);cases=0;tuples=0
    for N in (77,315,899):
        T=[t for t in range(N) if t*t%N==1];g=len(T);k=4
        for r in (1,2,3,4):
            for _ in range(3):
                rows=[]
                while len(rows)<r:
                    v=rng.randrange(1,1<<k)
                    if rank2(rows+[v])>len(rows):rows.append(v)
                counts={}
                for hs in product(T,repeat=k):
                    out=tuple(prod(hs[i] for i in range(k) if v>>i&1)%N for v in rows)
                    counts[out]=counts.get(out,0)+1;tuples+=1
                assert len(counts)==g**r and set(counts.values())=={g**(k-r)}
                bad=sum(c for z,c in counts.items() if all(a in (1,N-1) for a in z))
                assert bad==2**r*g**(k-r)
                cases+=1
    print('independent parity fibre cases:',cases,'exact root tuples:',tuples)

def check_pairing_budget():
    rng=Random(271828);cases=0
    for _ in range(1000):
        s=rng.randrange(1,15);ms=[rng.randrange(1,5) for i in range(s)];d=sum(ms)
        gs=[rng.randrange(s) for i in range(s)];groups={}
        for i,j in enumerate(gs):groups[j]=groups.get(j,0)+ms[i]
        g=len(groups);c=s-g;odd=sum(v%2 for v in groups.values())
        assert d>=2*g-odd and 2*(d-s+c)>=d-odd
        cases+=1
    print('local pairing partition budgets:',cases)

if __name__=='__main__':
    check_prescriptions();check_fibres();check_pairing_budget()
