#!/usr/bin/env python3
"""Exact divisor coordinates and partial-annihilator collision certificates."""
from collections import deque
from math import gcd,isqrt,lcm,prod
from random import Random
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from verify_class_coset_rank import enumerate_forms,compose
from verify_class_annihilator_readout import pw,word_value,projection,ord2
from verify_quadratic_packet_walk import (ONE,canonical,imul,idx,roots,prime_ideal,
    from_ideal,join,power,identity,conj,FactorFound)


def divisor(f,D):
    a,b,c=f
    assert D>4 and D%2 and -a<b<=a<=c and b*b-4*a*c==-4*D
    assert gcd(a,gcd(b,c))==1 and b%2==0
    if b==0 or b==a:d=a
    else:
        assert a==c and b>=0
        d=2*(a-b//2)
    t=d//2 if d%2==0 else d
    assert D%t==0 and gcd(t,D//t)==1 and (d%2 or D%4==1)
    return d


def bits(D,ds):
    axes=[D]+([2] if D%4==1 else [])
    for d in ds:
        for a in axes[:]:
            g=gcd(a,d)
            if 1<g<a:axes.remove(a);axes.extend((g,a//g))
    out=[]
    for d in [D]+list(ds):
        u=1;v=0
        for i,a in enumerate(axes):
            if d%a==0:u*=a;v|=1<<i
        assert u==d;out.append(v)
    return out[0],out[1:]


def solve(gs,v):
    P={}
    for j,u in enumerate(gs):
        w=1<<j
        while u:
            h=u.bit_length()-1
            if h in P:a,b=P[h];u^=a;w^=b
            else:P[h]=(u,w);break
    w=0
    while v:
        h=v.bit_length()-1
        if h not in P:return None
        a,b=P[h];v^=a;w^=b
    return w


def top_solve(D,tops,z,N=None):
    ds=[divisor(f,D) for f in tops+[z]]
    if N is not None:
        for d in ds:
            a=gcd(d,N)
            if 1<a<N:raise FactorFound(a)
    u,vs=bits(D,ds);w=solve(vs[:-1]+[u],vs[-1])
    return None if w is None else w&((1<<len(tops))-1)


def basis2(gs,M,mul,one,top):
    t,odd,e2,eo=projection(M);s=len(gs)
    assert all(pw(g,M,mul,one)==one for g in gs)
    B=[];tops=[];todo=[]
    for i,g in enumerate(gs):
        y=pw(g,e2,mul,one);w=[0]*s;w[i]=e2
        todo.append((ord2(y,t,mul,one),y,w))
    while todo:
        a,g,w=todo.pop(max(range(len(todo)),key=lambda i:todo[i][0]))
        if a==0:continue
        z=pw(g,1<<(a-1),mul,one);mask=top(tops,z)
        if mask is None:B.append((a,g,w));tops.append(z);continue
        assert word_value(tops,[(mask>>i)&1 for i in range(len(tops))],mul,one)==z
        for i,(b,h,v) in enumerate(B):
            if mask>>i&1:
                assert b>=a;e=1<<(b-a)
                g=mul(g,pw(h,(-e)%M,mul,one));w=[(x-e*y)%M for x,y in zip(w,v)]
        aa=ord2(g,t,mul,one);assert aa<a;todo.append((aa,g,w))
    assert all(word_value(gs,w,mul,one)==g for a,g,w in B)
    return B,tops


def coordinates(x,B,tops,M,mul,one,top):
    aa=[a for a,g,w in B];vs=[g for a,g,w in B];out=[0]*len(B);shift=[0]*len(B);start=x
    for a in range(max(aa,default=0),0,-1):
        z=pw(x,1<<(a-1),mul,one);mask=top(tops,z);assert mask is not None
        assert word_value(tops,[(mask>>i)&1 for i in range(len(tops))],mul,one)==z
        for i in range(len(B)):
            if aa[i]==a:
                if mask>>i&1:x=mul(x,pw(vs[i],M-1,mul,one));out[i]+=1<<shift[i]
                vs[i]=mul(vs[i],vs[i]);aa[i]-=1;shift[i]+=1
            else:assert not mask>>i&1
        assert pw(x,1<<(a-1),mul,one)==one
    assert x==one and word_value([g for a,g,w in B],out,mul,one)==start
    return out


def square_word(gs,M,mul,one,top):
    t,odd,e2,eo=projection(M);B,tops=basis2(gs,M,mul,one,top)
    def coord(g):return coordinates(pw(g,e2,mul,one),B,tops,M,mul,one,top)
    cols=[sum((n&1)<<j for j,n in enumerate(coord(g))) for g in gs]
    for i,c in enumerate(cols):
        mask=solve(cols[:i],c)
        if mask is None:continue
        mask|=1<<i;v=[(mask>>j)&1 for j in range(len(gs))];target=word_value(gs,v,mul,one)
        z=coord(target);assert all(n%2==0 for n in z)
        ans=[x*eo*((odd+1)//2)%M for x in v]
        for n,(a,g,w) in zip(z,B):ans=[(x+(n//2)*y)%M for x,y in zip(ans,w)]
        assert pw(word_value(gs,ans,mul,one),2,mul,one)==target
        return (v,ans),len(B)
    return None,len(B)


def test_divisors():
    rng=Random(1701);nt=pair=queries=0
    for D in (5,7,9,15,21,45,63,77,105,225,315,899,10403,9*10403,1022117,3*1022117,255255):
        fs=enumerate_forms(D)[0];one=(1,0,D);M=len(fs);tops=[f for f in fs if compose(f,f,D)==one]
        ds=[divisor(f,D) for f in tops];u,vs=bits(D,ds);m=dict(zip(tops,vs))
        for f,d in zip(tops,ds):
            A=((d,0),(d//2 if d%2==0 else 0,1))
            assert canonical(A,D)==f and imul(A,A,D)==((d,0),(0,d));nt+=1
        for f in tops:
            for g in tops:
                z=compose(f,g,D);assert m[f]^m[g]^m[z] in (0,u);pair+=1
        def mul(x,y):return compose(x,y,D)
        def top(xs,z):return top_solve(D,xs,z)
        for _ in range(10):
            gs=rng.sample(fs,min(len(fs),6));B,T=basis2(gs,M,mul,one,top)
            t,odd,e2,eo=projection(M)
            for g in gs:coordinates(pw(g,e2,mul,one),B,T,M,mul,one,top);queries+=1
        print('D',D,'class number',M,'2-torsion',len(tops),flush=True)
    print('ambiguous divisor classes:',nt,'pair products:',pair,'linear coordinate checks:',queries,flush=True)


def harvest(gs,E,H,need,cap,rng,mul,one,mode):
    """Fixed cap; H is an order upper bound, not a supplied annihilator."""
    s=len(gs);nb=(128*cap*s*(2*H+1)).bit_length();base=[pw(g,E,mul,one) for g in gs]
    powers=[]
    for g in base:
        row=[g]
        for _ in range(1,nb):row.append(mul(row[-1],row[-1]))
        powers.append(row)
    def evaluate(x):
        z=one
        for e,row in zip(x,powers):
            while e:b=e&-e;z=mul(z,row[b.bit_length()-1]);e^=b
        return z
    pending={};out=[];masks=[];matches=0
    for j in range(1,cap+1):
        x=tuple(rng.getrandbits(nb) for _ in gs);z=evaluate(x)
        if z not in pending:pending[z]=x;continue
        y=pending.pop(z);v=[a-b for a,b in zip(x,y)];matches+=1
        if mode=='parity':
            mask=sum((a&1)<<i for i,a in enumerate(v));ok=solve(masks,mask) is None
            if ok:masks.append(mask)
        else:ok=sp.Matrix(out+[v]).rank()>len(out)
        if ok:out.append(v)
        if len(out)==need:return out,j,matches
    return out,cap,matches


def test_abstract():
    rng=Random(271828);full=partial=draws=large=0
    for _ in range(100):
        mods=[(1<<rng.randrange(1,5))*rng.choice((3,9,27))*rng.choice((1,5,7,11)) for j in range(rng.randrange(1,5))]
        M=lcm(*mods);H=prod(mods);one=tuple(0 for _ in mods)
        def mul(x,y):return tuple((a+b)%m for a,b,m in zip(x,y,mods))
        gs=[tuple(rng.randrange(m) for m in mods) for _ in range(len(mods)+3)]
        E=2**H.bit_length()*27;rs=[pw(g,E,mul,one) for g in gs];Q={one};q=deque([one])
        while q:
            x=q.popleft()
            for g in rs:
                y=mul(x,g)
                if y not in Q:Q.add(y);q.append(y)
        R=len(Q);large+=int(R>1);s=len(gs);k=len(mods)+1
        cap=16*(s+8+isqrt((s+8)*R)+1)
        vs,n,m=harvest(gs,E,H,s,cap,rng,mul,one,'full');assert len(vs)==s
        A=smith_normal_form(sp.Matrix(vs),domain=sp.ZZ);e=abs(int(A[s-1,s-1]));ann=E*e
        assert e>0 and all(pw(g,ann,mul,one)==one for g in gs);full+=1;draws+=n
        vs,n,m=harvest(gs,E,H,k,cap,rng,mul,one,'parity');assert len(vs)==k
        bs=[word_value(gs,[e%M for e in v],mul,one) for v in vs];assert all(pw(b,E,mul,one)==one for b in bs)
        def top(xs,z):
            d={one:0}
            for i,x in enumerate(xs):d.update({mul(y,x):v|(1<<i) for y,v in list(d.items())})
            return d.get(z)
        out,r=square_word(bs,E,mul,one,top);assert out is not None
        ex,w=out;v=[sum(ex[j]*vs[j][i] for j in range(k)) for i in range(s)]
        a=[sum(w[j]*vs[j][i] for j in range(k)) for i in range(s)]
        assert any(z%2 for z in v)
        assert pw(word_value(gs,[z%M for z in a],mul,one),2,mul,one)==word_value(gs,[z%M for z in v],mul,one)
        partial+=1;draws+=n
    print('abstract full annihilators:',full,'partial certificates:',partial,'nontrivial residual groups:',large,'word draws:',draws,flush=True)


def state_word(states,ex,D,N):
    S=identity()
    for g,e in zip(states,ex):
        if e<0:A,u,c=g;g=(conj(A),pow(u,-1,N),u*c%N);e=-e
        if e:S=join(S,power(g,e,D,N),D,N)
    return S


def actual_classes():
    rng=Random(314159);certs=guards=fail=0
    for N in (899,10403,1022117,100160063,1000036000099):
        D=N;H=8*D+1;one=(1,0,D);states=[];hs=[];ss=[];initguard=set()
        for _ in range(10000):
            h=rng.randrange(1,N);s=h*h%N
            if gcd(h,N)!=1 or s==1 or s in ss:continue
            ps=[int(p) for p,e in sp.factorint(s).items() if e%2]
            if not ps or any(not roots(p,D) for p in ps):continue
            I=ONE
            for p in ps:I=imul(I,prime_ideal(p,roots(p,D)[0],D),D)
            q=idx(I);t=isqrt(s//q);assert t*t*q==s
            try:B,u,c=from_ideal(I,D,N)
            except FactorFound as f:initguard.add(f.args[0]);continue
            states.append((B,s,c*pow(t,-1,N)%N));ss.append(s);hs.append(h)
            if len(states)==4:break
        assert len(states)==4
        gs=[canonical(S[0],D) for S in states]
        def mul(x,y):return compose(x,y,D)
        E=2**H.bit_length()*3**(H.bit_length()//2)
        killed=sum(pw(g,E,mul,one)==one for g in gs);need=2 if D%4==1 else 1
        vs,draws,matches=harvest(gs,E,H,need,1600,rng,mul,one,'parity')
        if len(vs)<need:
            print('class fixture',N,'cap exhausted; killed',killed,'draws',draws,'matches',matches,flush=True);fail+=1;continue
        try:
            bs=[state_word(states,v,D,N) for v in vs];ks=[canonical(S[0],D) for S in bs]
            assert all(pw(g,E,mul,one)==one for g in ks)
            out,r=square_word(ks,E,mul,one,lambda xs,z:top_solve(D,xs,z,N));assert out is not None
            ex,w=out;v=[sum(ex[j]*vs[j][i] for j in range(need)) for i in range(len(gs))]
            assert any(a&1 for a in v)
            T=state_word(bs,ex,D,N);W=state_word(bs,w,D,N);W2=join(W,W,D,N)
            assert canonical(T[0],D)==canonical(W2[0],D) and idx(T[0])==idx(W2[0])
            root=W[1]*W2[2]*pow(T[2],-1,N)%N;assert root*root%N==T[1]
            assert T[1]==prod(pow(s,e,N) for s,e in zip(ss,v))%N
            hp=prod(pow(h,e,N) for h,e in zip(hs,v))%N;assert hp*hp%N==T[1]
            g=gcd(hp*pow(root,-1,N)-1,N);assert N%g==0;certs+=1
            print('class fixture',N,'E kills',killed,'of',len(gs),'draws',draws,'matches',matches,'2-rank',r,'gcd',g,'init guards',sorted(initguard),flush=True)
        except FactorFound as f:
            g=f.args[0];assert 1<g<N and N%g==0;guards+=1
            print('class fixture',N,'E kills',killed,'of',len(gs),'draws',draws,'matches',matches,'public guard',g,'init guards',sorted(initguard),flush=True)
    print('class certificates:',certs,'public guard exits:',guards,'cap failures:',fail,flush=True)

if __name__=='__main__':
    import sys
    mode=sys.argv[1] if len(sys.argv)>1 else 'all'
    if mode in ('all','divisors'):test_divisors()
    if mode in ('all','abstract'):test_abstract()
    if mode in ('all','class'):actual_classes()
