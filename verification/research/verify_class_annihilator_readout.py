#!/usr/bin/env python3
"""Exact black-box 2-primary coordinates from a supplied annihilator.
Finite abstract-group and quadratic class fixtures; class numbers are supplied by
exhaustive enumeration only in the latter. No uniform annihilator-supply claim.
"""
from collections import deque
from math import gcd,isqrt,lcm,prod
from random import Random
import sympy as sp
from verify_class_coset_rank import enumerate_forms,compose
from verify_quadratic_packet_walk import (ONE,canonical,imul,idx,roots,prime_ideal,
    from_ideal,join,power,identity,FactorFound)


def pw(x,e,mul,one):
    z=one;assert e>=0
    while e:
        if e&1:z=mul(z,x)
        e//=2
        if e:x=mul(x,x)
    return z


def word_value(gs,es,mul,one):
    z=one
    for g,e in zip(gs,es):z=mul(z,pw(g,e,mul,one))
    return z


def projection(M):
    odd=M;t=0
    while odd%2==0:odd//=2;t+=1
    p2=odd*pow(odd,-1,1<<t) if t else 0
    return t,odd,p2,(1-p2)%M


def ord2(x,t,mul,one):
    for a in range(t+1):
        if x==one:return a
        x=mul(x,x)
    raise AssertionError('not killed by supplied two-power')


def basis2(gs,M,mul,one):
    t,odd,e2,eo=projection(M);m=len(gs)
    assert all(pw(g,M,mul,one)==one for g in gs)
    todo=[]
    for i,g in enumerate(gs):
        v=pw(g,e2,mul,one);w=[0]*m;w[i]=e2
        todo.append((ord2(v,t,mul,one),v,w))
    B=[];top={one:0};repairs=0
    while todo:
        j=max(range(len(todo)),key=lambda i:todo[i][0]);a,g,w=todo.pop(j)
        if not a:continue
        z=pw(g,1<<(a-1),mul,one)
        if z not in top:
            j=len(B);B.append((a,g,w))
            add={mul(v,z):mask|(1<<j) for v,mask in top.items()}
            assert not set(top)&set(add);top.update(add)
        else:
            mask=top[z];u=g
            for i,(b,h,v) in enumerate(B):
                if mask>>i&1:
                    assert b>=a;e=(1<<(b-a))
                    u=mul(u,pw(h,(-e)%M,mul,one))
                    w=[(x-e*y)%M for x,y in zip(w,v)]
            aa=ord2(u,t,mul,one);assert aa<a
            todo.append((aa,u,w));repairs+=1
    assert all(word_value(gs,w,mul,one)==g for a,g,w in B)
    return B,top,repairs


def coords2(x,B,top,M,mul,one):
    aa=[a for a,g,w in B];vs=[g for a,g,w in B]
    shift=[0]*len(B);out=[0]*len(B);start=x
    for a in range(max(aa,default=0),0,-1):
        z=pw(x,1<<(a-1),mul,one);mask=top[z]
        for i in range(len(B)):
            if aa[i]==a:
                if mask>>i&1:
                    x=mul(x,pw(vs[i],M-1,mul,one));out[i]+=1<<shift[i]
                vs[i]=mul(vs[i],vs[i]);aa[i]-=1;shift[i]+=1
            else:assert not mask>>i&1
        assert pw(x,1<<(a-1),mul,one)==one
    assert x==one and word_value([g for a,g,w in B],out,mul,one)==start
    return out


def witnessed_square(gs,M,mul,one):
    """Return a nonempty binary target relation and a word for its class root."""
    t,odd,e2,eo=projection(M);B,top,repairs=basis2(gs,M,mul,one)
    cs=[coords2(pw(g,e2,mul,one),B,top,M,mul,one) for g in gs]
    piv={};relation=0
    for i,c in enumerate(cs):
        v=sum((a%2)<<j for j,a in enumerate(c));w=1<<i
        while v:
            j=v.bit_length()-1
            if j in piv:a,b=piv[j];v^=a;w^=b
            else:piv[j]=(v,w);break
        if not v:relation=w;break
    if not relation:return None,(B,top,repairs,cs)
    ex=[(relation>>i)&1 for i in range(len(gs))];target=word_value(gs,ex,mul,one)
    n=coords2(pw(target,e2,mul,one),B,top,M,mul,one)
    assert all(v%2==0 for v in n)
    ans=[x*eo*((odd+1)//2)%M for x in ex]
    for v,(a,g,w) in zip(n,B):ans=[(x+(v//2)*y)%M for x,y in zip(ans,w)]
    root=word_value(gs,ans,mul,one);assert mul(root,root)==target
    return (ex,ans),(B,top,repairs,cs)


def abstract_tests():
    rng=Random(1701);checks=repairs=certs=0
    for _ in range(250):
        mods=[(1<<rng.randrange(6))*rng.choice((1,3,5,9)) for j in range(rng.randrange(1,5))]
        one=tuple(0 for m in mods);M=lcm(*mods)
        def mul(x,y):return tuple((a+b)%m for a,b,m in zip(x,y,mods))
        gs=[tuple(rng.randrange(m) for m in mods) for i in range(len(mods)+2)]
        out,(B,top,rep,cs)=witnessed_square(gs,M,mul,one);assert out is not None
        t,odd,e2,eo=projection(M);pg=[pw(g,e2,mul,one) for g in gs]
        H={one};q=deque([one])
        while q:
            x=q.popleft()
            for g in pg:
                y=mul(x,g)
                if y not in H:H.add(y);q.append(y)
        assert len(H)==prod(1<<a for a,g,w in B)
        assert set(top)=={x for x in H if mul(x,x)==one}
        # Independent check on all group elements for smaller 2-primary groups.
        if len(H)<=128:
            for x in H:coords2(x,B,top,M,mul,one);checks+=1
        ex,es=out;assert any(ex) and pw(word_value(gs,es,mul,one),2,mul,one)==word_value(gs,ex,mul,one)
        repairs+=rep;certs+=1
    print('abstract-group certificates:',certs,'order-lowering repairs:',repairs,
          'exhaustive coordinate checks:',checks,flush=True)


def class_tests():
    rng=Random(314159);certs=guards=0
    for N in (899,10403,1022117):
        D=N;M=len(enumerate_forms(D)[0]);states=[];hs=[]
        for _ in range(2000):
            h=rng.randrange(1,N)
            if gcd(h,N)!=1:continue
            s=h*h%N
            if s==1:continue
            ps=[int(p) for p,e in sp.factorint(s).items() if e%2]
            if not ps or any(not roots(p,D) for p in ps):continue
            A=ONE
            for p in ps:A=imul(A,prime_ideal(p,roots(p,D)[0],D),D)
            q=idx(A);v=isqrt(s//q);assert v*v*q==s
            try:B,u,c=from_ideal(A,D,N)
            except FactorFound:guards+=1;continue
            states.append((B,s,c*pow(v,-1,N)%N));hs.append(h)
            if len(states)==5:break
        assert len(states)==5
        one=canonical(ONE,D);gs=[canonical(S[0],D) for S in states]
        def mul(x,y):return compose(x,y,D)
        out,(B,top,rep,cs)=witnessed_square(gs,M,mul,one);assert out is not None
        ex,es=out
        try:
            T=identity();R=identity()
            for S,x,e in zip(states,ex,es):
                if x:T=join(T,S,D,N)
                if e:R=join(R,power(S,e,D,N),D,N)
            W=join(R,R,D,N);assert canonical(W[0],D)==canonical(T[0],D)
            assert idx(W[0])==idx(T[0])
            root=R[1]*W[2]*pow(T[2],-1,N)%N
            assert root*root%N==T[1]
            # Public certificate fixed before private-root comparison.
            hp=prod(h for h,x in zip(hs,ex) if x)%N;assert hp*hp%N==T[1]
            g=gcd(hp*pow(root,-1,N)-1,N);assert N%g==0;certs+=1
            print('class fixture:',N,'supplied h:',M,'2-rank:',len(B),'odd mask:',sum(x<<i for i,x in enumerate(ex)),'gcd:',g,flush=True)
        except FactorFound as f:
            guards+=1;assert 1<f.args[0]<N and N%f.args[0]==0
            print('class fixture:',N,'public guard factor:',f.args[0],flush=True)
    print('class certificates:',certs,'guard exits:',guards,flush=True)

if __name__=='__main__':
    abstract_tests();class_tests()
