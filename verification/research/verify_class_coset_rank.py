#!/usr/bin/env python3
"""Exact reduced-class enumeration, affine norm ranks and small-group readout.
Exhaustive small fixtures only; imports the earlier checked quadratic arithmetic.
"""
from itertools import product,combinations
from math import gcd,isqrt,prod,comb
from random import Random
import sympy as sp
from verify_quadratic_packet_walk import (ONE,canonical,imul,idx,roots,prime_ideal,
    from_ideal,join,identity,FactorFound)


def spf_table(n):
    a=list(range(n+1))
    for p in range(2,isqrt(n)+1):
        if a[p]==p:
            for k in range(p*p,n+1,p):
                if a[k]==k:a[k]=p
    return a


def parity(n,spf,axes):
    v=0
    while n>1:
        p=spf[n];e=0
        while n%p==0:n//=p;e^=1
        if e:v^=1<<axes[p]
    return v


def insert(v,B):
    while v:
        j=v.bit_length()-1
        if j in B:v^=B[j]
        else:B[j]=v;return True
    return False


def in_span(v,B):
    while v:
        j=v.bit_length()-1
        if j not in B:return False
        v^=B[j]
    return True


def form_ideal(f):
    a,b,c=f;assert b%2==0
    return ((a,0),((b//2)%a,1))


def compose(f,g,D):
    return canonical(imul(form_ideal(f),form_ideal(g),D),D)


def enumerate_forms(D):
    X=isqrt((4*D)//3);spf=spf_table(X)
    rt=[() for _ in range(X+1)];rt[1]=(0,)
    fs=[];local=bad=0
    for a in range(1,X+1):
        if a>1:
            p=spf[a];w=a;e=0
            while w%p==0:w//=p;e+=1
            pe=a//w
            if w==1:
                if e==1:rt[a]=tuple(map(int,sp.sqrt_mod(-D,p,all_roots=True)))
                else:
                    prev=a//p
                    rt[a]=tuple(r+j*prev for r in rt[prev] for j in range(p)
                                if ((r+j*prev)**2+D)%a==0)
                if (2*D)%p:assert len(rt[a])<=2;local+=1
                else:assert len(rt[a])<=4*p**(e//2);bad+=1
            elif rt[pe] and rt[w]:
                q=pow(pe,-1,w)
                rt[a]=tuple(r+pe*((z-r)*q%w) for r,z in product(rt[pe],rt[w]))
        assert len(set(rt[a]))==len(rt[a]);count=0
        for r in rt[a]:
            assert (r*r+D)%a==0
            if 2*r>a:r-=a
            b=2*r;c=(r*r+D)//a
            if a>c or gcd(gcd(a,b),c)!=1 or (a==c and b<0):continue
            assert -a<b<=a<=c and b*b-4*a*c==-4*D
            fs.append((a,b,c));count+=1
        assert count<=len(rt[a])
    assert len(set(fs))==len(fs)
    axes={p:i for i,p in enumerate(p for p in range(2,X+1) if spf[p]==p)}
    return fs,spf,axes,local,bad


def direct_forms(D):
    out=set()
    for a in range(1,isqrt((4*D)//3)+1):
        for r in range(-((a-1)//2),a//2+1):
            if (r*r+D)%a:continue
            b=2*r;c=(r*r+D)//a
            if a>c or (a==c and b<0) or gcd(gcd(a,b),c)!=1:continue
            out.add((a,b,c))
    return out


def full_cosets(D):
    fs,spf,axes,local,bad=enumerate_forms(D);F=set(fs);one=(1,0,D)
    squares=[compose(f,f,D) for f in fs];H=set(squares)
    assert H<=F and one in H
    torsion=squares.count(one)
    assert torsion==sum(b==0 or abs(b)==a or a==c for a,b,c in fs)
    assert len(H)*torsion==len(F) and torsion<=9*2**len(sp.factorint(D))
    rem=set(F);cosets=[]
    while rem:
        f=min(rem);C={compose(f,h,D) for h in H}
        assert C<=rem and len(C)==len(H);rem-=C;cosets.append(sorted(C))
    assert len(cosets)==torsion
    vs={a:parity(a,spf,axes) for a,b,c in fs}
    # Match the actual walk design: squares of up to four small split-prime ideals.
    ps=[int(p) for p in sp.primerange(3,100) if roots(p,D)][:4]
    ideals=[prime_ideal(p,roots(p,D)[0],D) for p in ps]
    gs=[canonical(A,D) for A in ideals];steps=[compose(g,g,D) for g in gs]
    W={one};queue=[one]
    for key in queue:
        for step in steps:
            y=compose(key,step,D)
            if y not in W:W.add(y);queue.append(y)
    assert W<=H and len(H)%len(W)==0
    short=0
    for j in range(1,len(ps)+1):
        if max(ps)**(2*j)>=D:continue
        seen=set()
        for ids in combinations(range(len(ps)),j):
            I=ONE
            for i in ids:I=imul(I,ideals[i],D)
            key=canonical(I,D);assert key[0]==idx(I);seen.add(key)
        assert len(seen)==comb(len(ps),j) and len(W)*torsion>=len(seen)
        short+=len(seen)
    return fs,cosets,vs,local,bad,(len(W),len(H),len(ps),short)


def test_counts():
    rng=Random(1701);total=local=bad=affine=0
    for D in (77,899,315,10403,1022117,100160063,9*10403,3*1022117,16*899):
        fs,cosets,vs,lc,bc,stepinfo=full_cosets(D);local+=lc;bad+=bc;total+=len(fs)
        if D<=15000:assert set(fs)==direct_forms(D)
        out=[]
        for C in cosets:
            v0=vs[C[0][0]];full={};diff={}
            for a,b,c in C:insert(vs[a],full);insert(vs[a]^v0,diff)
            B={}
            for _ in range(48):insert(vs[rng.choice(C)[0]],B)
            covered=sum(in_span(vs[a],B) for a,b,c in C)
            for offset in (0,v0,rng.choice(list(vs.values()))):
                hit=[f for f in fs if in_span(vs[f[0]]^offset,B)]
                basis={};support=0
                for f in hit:
                    v=vs[f[0]]
                    if insert(v,basis):support|=v
                assert len(basis)<=len(B)+1
                assert support.bit_count()<=(len(B)+1)*max(1,isqrt((4*D)//3).bit_length()-1)
                assert all(vs[f[0]]&~support==0 for f in hit)
                upper=sum(1 for f in fs if vs[f[0]]&~support==0)
                assert len(hit)<=upper;affine+=1
            out.append((len(C),len(full),len(diff),len(B),covered))
        print('D',D,'h',len(fs),'cosets',len(cosets),'step subgroup/full squares/generators/short products',stepinfo,
              '(size,rank,affine-rank,bank-rank,covered):',out,flush=True)
    print('forms enumerated:',total,'good prime-power root bounds:',local,
          'bad prime-power root bounds:',bad,'affine support checks:',affine,flush=True)


def small_group_certificate(N,D,states,hs,cap):
    steps=[]
    for S in states:
        T=join(S,S,D,N);steps.append((T[0],1,S[1]*T[2]%N))
    one=canonical(ONE,D);H={one:identity()};queue=[one]
    for key in queue:
        for T in steps:
            S=join(H[key],T,D,N);f=canonical(S[0],D)
            if f not in H:
                if len(H)>=cap:return None
                H[f]=S;queue.append(f)
    tab={f:(S,0) for f,S in H.items()}
    for i,T in enumerate(states):
        f=canonical(T[0],D)
        if f in tab:
            S,v=tab[f];assert not (v>>i)&1
            assert idx(S[0])==idx(T[0])==f[0]
            u=T[1]*pow(S[1],-1,N)%N;w=S[2]*pow(T[2],-1,N)%N
            assert w*w%N==u
            assert S[1]==prod(states[j][1] for j in range(i) if v>>j&1)%N
            # Only now expose the hidden sign fibres.
            h=hs[i]*pow(prod(hs[j] for j in range(i) if v>>j&1),-1,N)%N
            assert h*h%N==u
            g=gcd(h*pow(w,-1,N)-1,N);assert N%g==0
            return len(H),len(tab),v|(1<<i),g
        old=list(tab.items())
        if 2*len(old)>cap:return None
        for key,(S,v) in old:
            W=join(S,T,D,N);f1=canonical(W[0],D)
            assert f1 not in tab
            tab[f1]=(W,v|(1<<i))
    return None


def test_small_group():
    rng=Random(314159);certs=guards=0
    for N in (899,10403,1022117):
        D=N;states=[];hs=[]
        for _ in range(2000):
            h=rng.randrange(1,N)
            if gcd(h,N)!=1:continue
            s=h*h%N
            if s==1:continue
            ps=[int(p) for p,e in sp.factorint(s).items() if e%2]
            if not ps or any(not roots(p,D) for p in ps):continue
            A=ONE
            for p in ps:A=imul(A,prime_ideal(p,roots(p,D)[0],D),D)
            q=idx(A);t=isqrt(s//q);assert t*t*q==s
            try:B,u,c=from_ideal(A,D,N)
            except FactorFound as f:guards+=1;continue
            S=(B,s,c*pow(t,-1,N)%N);assert idx(B)%N==s*S[2]**2%N
            states.append(S);hs.append(h)
            if len(states)==5:break
        assert len(states)==5
        try:
            result=small_group_certificate(N,D,states,hs,100000)
            assert result is not None;certs+=1
            print('small-group fixture',N,'(squares subgroup,dict size,odd target mask,gcd)',result,flush=True)
        except FactorFound as f:
            guards+=1;assert N%f.args[0]==0 and 1<f.args[0]<N
            print('small-group fixture',N,'public guard factor',f.args[0],flush=True)
    print('small-group certificates:',certs,'guard exits:',guards,flush=True)


if __name__=='__main__':
    test_counts();test_small_group()
