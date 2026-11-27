#!/usr/bin/env python3
"""Exact quadratic packet reductions, compact powers and public parity pools.
Tiny fixture factorizations are supplied explicitly; no asymptotic supply claim.
"""
from collections import Counter
from itertools import product
from math import gcd,isqrt,prod
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
ONE=((1,0),(0,1))

def xgcd(a,b):
    g,h=abs(a),abs(b);x,y,z,w=1,0,0,1
    while h:
        q=g//h;g,h=h,g-q*h;x,z=z,x-q*z;y,w=w,y-q*w
    return g,x*(1 if a>=0 else -1),y*(1 if b>=0 else -1)

def hnf(vs):
    vs=list(vs);c=r=0
    for x,y in vs:
        c,s,t=xgcd(c,y);r=s*r+t*x
    assert c>0
    a=0
    for x,y in vs:
        assert y%c==0;a=gcd(a,x-y//c*r)
    assert a>0
    return ((a,0),(r%a,c))

def mul(v,w,D):
    x,y=v;a,b=w;return x*a-D*y*b,x*b+y*a

def idx(A):return A[0][0]*A[1][1]
def conj(A):return hnf((x,-y) for x,y in A)
def imul(A,B,D):
    C=hnf(mul(a,b,D) for a,b in product(A,B));assert idx(C)==idx(A)*idx(B)
    return C

def dot(v,w,D):return v[0]*w[0]+D*v[1]*w[1]

def gauss(A,D):
    v,w=A
    while True:
        a,b=dot(v,v,D),dot(w,w,D)
        if a>b:v,w=w,v;a,b=b,a
        z=(2*dot(v,w,D)+a)//(2*a)
        w=tuple(x-z*y for x,y in zip(w,v))
        if dot(w,w,D)>=a:break
    b,c=dot(w,w,D),dot(v,w,D)
    assert a<=b and 2*abs(c)<=a and a*b-c*c==idx(A)**2*D
    assert 3*a*a<=4*idx(A)**2*D and hnf((v,w))==A
    return v,w

class FactorFound(Exception):pass

def red(A,D,N):
    Q=idx(A);assert gcd(Q,N)==1 and imul(A,conj(A),D)==((Q,0),(0,Q))
    (x,y),_=gauss(A,D);nn=x*x+D*y*y;assert nn%Q==0
    b=nn//Q;raw=[mul((x,-y),v,D) for v in A];assert all(t%Q==0 for v in raw for t in v)
    B=hnf(tuple(t//Q for t in v) for v in raw)
    assert idx(B)==b and 3*b*b<=4*D and imul(B,conj(B),D)==((b,0),(0,b))
    g=gcd(x,N)
    if g!=1:
        assert 1<g<N and N%g==0;raise FactorFound(g)
    c=x*pow(Q,-1,N)%N;assert gcd(b,N)==1 and (b-Q*c*c)%N==0
    return B,c

def roots(p,D):
    if p==2:return [1] if D%4==1 else []
    if D%p==0:return []
    return list(map(int,sp.sqrt_mod(-D,p,all_roots=True)))

def prime_ideal(p,r,D):
    assert r in roots(p,D);A=((p,0),(r%p,1));assert imul(A,conj(A),D)==((p,0),(0,p))
    return A

def join(S,T,D,N):
    A,u,c=S;B,v,e=T;C,z=red(imul(A,B,D),D,N);W=(C,u*v%N,c*e*z%N)
    assert (idx(C)-W[1]*W[2]**2)%N==0
    return W

def identity():return ONE,1,1

def from_ideal(A,D,N):
    B,c=red(A,D,N);return B,idx(A)%N,c

def power(S,e,D,N):
    R=identity()
    while e:
        if e&1:R=join(R,S,D,N)
        e//=2
        if e:S=join(S,S,D,N)
    return R

def square_step(A,D,N):
    B,u,c=power(from_ideal(A,D,N),2,D,N);e=idx(A)*c%N
    assert (idx(B)-e*e)%N==0
    return B,1,e

def canonical(A,D):
    Q=idx(A);u,v=A;a=dot(u,u,D)//Q;b=2*dot(u,v,D)//Q;c=dot(v,v,D)//Q
    assert b*b-4*a*c==-4*D and gcd(a,gcd(b,c))==1
    while True:
        z=(a-b)//(2*a);b,c=b+2*a*z,c+b*z+a*z*z
        if c<a:a,b,c=c,-b,a
        else:break
    if abs(b)==a or a==c:b=abs(b)
    assert abs(b)<=a<=c and b*b-4*a*c==-4*D
    return a,b,c

def test_exact():
    rng=Random(1701);hnfs=checks=large=0;factors=set()
    for _ in range(300):
        vs=[(rng.randrange(-100,101),rng.randrange(-100,101)) for _ in range(4)]
        M=sp.Matrix(vs).T
        if M.rank()!=2:continue
        H=hermite_normal_form(M);assert hnf(vs)==tuple(tuple(map(int,H[:,j])) for j in range(2));hnfs+=1
    for N in (77,899,10403,1022117,100160063,101**2*103):
        for k in (1,2,3,5,7,11):
            if gcd(N,k)>1 or 4*k>=3*N:continue
            D=k*N;ps=[int(p) for p in sp.primerange(3,150) if roots(p,D)]
            if not ps:continue
            for _ in range(8):
                ss=rng.sample(ps,min(len(ps),rng.randrange(1,5)));A=ONE
                for p in ss:A=imul(A,prime_ideal(p,rng.choice(roots(p,D)),D),D)
                assert idx(A)==prod(ss)
                try:
                    S=from_ideal(A,D,N);checks+=1;e=(1<<128)+rng.randrange(1,1<<32)
                    T=power(S,e,D,N);assert T[1]==pow(idx(A),e,N)
                    W=power(S,2,D,N);J=join(T,(W[0],1,idx(A)*W[2]%N),D,N)
                    assert J[1]==T[1] and (idx(J[0])-J[1]*J[2]**2)%N==0;large+=1
                except FactorFound as f:factors.add((N,f.args[0]))
    print('independent HNF checks:',hnfs,'packet reductions:',checks,'128-bit exponent cases:',large,'guard factors:',len(factors),flush=True)
    N=899;D=N;ps=[int(p) for p in sp.primerange(3,40) if roots(p,D)]
    steps=[square_step(prime_ideal(p,roots(p,D)[0],D),D,N) for p in ps[:3]]
    keys={canonical(ONE,D):identity()};todo=list(keys)
    while todo:
        k=todo.pop()
        for T in steps:
            W=join(keys[k],T,D,N);f=canonical(W[0],D)
            if f not in keys:keys[f]=W;todo.append(f)
    orders=[]
    for T in steps:
        W=T;o=1
        while canonical(W[0],D)!=canonical(ONE,D):W=join(W,T,D,N);o+=1
        orders.append(o)
    powers=[[power(T,e,D,N) for e in range(o)] for T,o in zip(steps,orders)];counts=Counter()
    for ts in product(*powers):
        W=identity()
        for T in ts:W=join(W,T,D,N)
        counts[canonical(W[0],D)]+=1
    assert set(counts)==set(keys) and len(set(counts.values()))==1
    print('exact square-coset fixture: generator orders',orders,'subgroup classes',len(keys),'equal multiplicity',next(iter(counts.values())),flush=True)

def rank_pool(N,ss,hs,data):
    # Tiny residual values factored only in this finite test, not in the theorem.
    fs=[sp.factorint(b) for i,b,c in data];ps=sorted(set().union(*(set(f) for f in fs)))
    vs=[sum(1<<j for j,p in enumerate(ps) if f.get(p,0)%2) for f in fs]
    piv={};targ={}
    for j,((i,b,c),v) in enumerate(zip(data,vs)):
        assert (b-ss[i]*c*c)%N==0;t=1<<i;w=1<<j
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=(v,t,w);break
            a,b1,c1=piv[k];v^=a;t^=b1;w^=c1
        if not v:
            while t:
                k=t.bit_length()-1
                if k not in targ:targ[k]=(t,w);break
                a,b1=targ[k];t^=a;w^=b1
    def rank(vs):
        P={}
        for v in vs:
            while v:
                k=v.bit_length()-1
                if k not in P:P[k]=v;break
                v^=P[k]
        return len(P)
    assert rank([(v<<len(ss))|(1<<i) for v,(i,b,c) in zip(vs,data)])-len(piv)==len(targ)
    certs=[]
    for parity,w in targ.values():
        root=1;target=1;counts=[0]*len(ss);ee=Counter()
        for j,(i,b,c) in enumerate(data):
            if not (w>>j)&1:continue
            root=root*pow(c,-1,N)%N;target=target*ss[i]%N;counts[i]+=1;ee.update(fs[j])
        assert sum((e%2)<<i for i,e in enumerate(counts))==parity and parity
        for p,e in ee.items():assert e%2==0;root=root*pow(p,e//2,N)%N
        assert root*root%N==target;certs.append((root,counts))
    # Private roots used only after fixing all public certificates.
    gs=[]
    for root,counts in certs:
        t=prod(pow(h,e,N) for h,e in zip(hs,counts))%N
        g=gcd(t*pow(root,-1,N)-1,N);assert N%g==0;gs.append(g)
    return len(piv),len(targ),sorted(set(gs))

def pool():
    rng=Random(271828)
    for N in (899,10403,1022117,100160063,1000036000099):
        hs=[];ss=[];qs=[];facts=[]
        while len(ss)<12:
            h=rng.randrange(1,N);s=h*h%N
            if gcd(h,N)==1 and s not in ss:
                hs.append(h);ss.append(s);ff=sp.factorint(s);ps=[int(p) for p,e in ff.items() if e%2];qs.append(prod(ps));facts.append(ps)
        ps=sorted(set(p for pp in facts for p in pp));ks=[1]
        # Finite shared bank by deterministic scan; not the asymptotic density test.
        cover={k:{p for p in ps if roots(p,k*N)} for k in range(1,300) if gcd(k,N)==1 and 4*k<3*N}
        left=set(ps)-cover[1]
        while left:
            k=max(cover,key=lambda k:len(cover[k]&left));assert cover[k]&left
            ks.append(k);left-=cover[k]
        factexits=set();walkchecks=0;stepmap={}
        for k in ks:
            D=k*N;sp0=[int(p) for p in sp.primerange(3,100) if roots(p,D)][:4];steps=[]
            for p in sp0:
                try:steps.append(square_step(prime_ideal(p,roots(p,D)[0],D),D,N))
                except FactorFound as f:factexits.add(f.args[0])
            stepmap[k]=steps
        base=[];walk=[]
        for i,(q,pp) in enumerate(zip(qs,facts)):
            t=isqrt(ss[i]//q);assert t*t*q==ss[i];groups={}
            for p in pp:
                k=next(k for k in ks if p in cover[k]);groups.setdefault(k,[]).append(p)
            cur=[]
            for k,pl in groups.items():
                D=k*N;A=ONE
                for p in pl:A=imul(A,prime_ideal(p,roots(p,D)[0],D),D)
                try:cur.append((k,from_ideal(A,D,N)))
                except FactorFound as f:factexits.add(f.args[0]);cur=[];break
            if pp and not cur:continue
            def row(items):
                b=prod(idx(S[0]) for k,S in items);c=prod(S[2] for k,S in items)*pow(t,-1,N)%N
                assert (b-ss[i]*c*c)%N==0
                return i,b,c
            base.append(row(cur));walk.append(base[-1])
            for j in range(48):
                cc=[]
                try:
                    for k,S in cur:
                        D=k*N;W=S
                        for T in stepmap[k]:W=join(W,power(T,rng.getrandbits(2*N.bit_length()+8),D,N),D,N)
                        cc.append((k,W));walkchecks+=1
                    walk.append(row(cc))
                except FactorFound as f:factexits.add(f.args[0])
        def unique(rows):
            seen=set();return [z for z in rows if not ((z[0],z[1]) in seen or seen.add((z[0],z[1])))]
        b0=unique(base);w0=unique(walk);pr=rank_pool(N,ss,hs,b0);wr=rank_pool(N,ss,hs,w0)
        assert wr[1]>=pr[1]
        print('N',N,'twists',ks,'direct',len(b0),pr,'pooled',len(w0),wr,'walk steps',walkchecks,
              'public guards',sorted(factexits),flush=True)

if __name__=='__main__':
    import sys
    if 'pool' in sys.argv:pool()
    else:test_exact()
