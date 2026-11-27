#!/usr/bin/env python3
"""Exact normalized resultant transport and LLL candidate tests."""
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf
from functools import lru_cache
from math import gcd,isqrt
from random import Random
X=sp.Symbol('X')

def poly(cs): return sp.Poly.from_list(list(reversed(cs)),X,domain=sp.ZZ)
def coefs(f,d): return [int(f.nth(j)) for j in range(d)]
def res(f,g): return int(sp.resultant(f,g))
def mp(f,q): return poly([int(c)%q for c in coefs(f,f.degree()+1)]) if not f.is_zero else poly([0])

@lru_cache(None)
def lifted(H,t0,t1,N,K):
    q=N**K
    def root(t):
        a=t%N;b=N
        assert int(H.eval(a))%N==0 and gcd(int(H.diff().eval(a)),N)==1
        while b<q:
            b*=N;a=(a-int(H.eval(a))*pow(int(H.diff().eval(a)),-1,b))%b
            assert int(H.eval(a))%b==0
        return a
    a,b=root(t0),root(t1)
    G,R=H.div(poly([a*b,-a-b,1]));assert mp(R,q).is_zero
    G=mp(G,q);assert G.is_monic and gcd(int(G.eval(a)*G.eval(b)*(a-b)),N)==1
    return a,b,G

def lattice(H,N,t0,t1,u,js):
    j0,j1,jg=js;d=H.degree();K=1+max(js);q=N**K
    a,b,G=lifted(H,t0,t1,N,K)
    def crt(v0,v1,Q):
        h0=(v0-int(Q.eval(a)))*pow(int(G.eval(a)),-1,q)%q
        h1=(v1-int(Q.eval(b)))*pow(int(G.eval(b)),-1,q)%q
        s=(h1-h0)*pow(b-a,-1,q)%q
        return mp(Q+G*poly([(h0-a*s)%q,s]),q)
    cs=[crt(N**j0,N**j1*u,poly([0])),crt(0,N**(j1+1),poly([0]))]
    cs +=[crt(0,0,poly([0]*i+[N**jg])) for i in range(d-2)]
    B=hnf(sp.Matrix.hstack(*(sp.Matrix(coefs(c,d)) for c in cs),q*sp.eye(d)))
    E=j0+j1+(d-2)*jg
    assert abs(int(B.det()))==N**(E+1)
    return B

def transport(H,D,N,t0,t1,u,js,C):
    j0,j1,jg=js;E=j0+j1+(H.degree()-2)*jg
    a,b,G=lifted(H,t0,t1,N,1+max(js))
    w0=int(C.eval(a));w1=int(C.eval(b));Q=C.rem(G)
    assert w0%N**j0==w1%N**j1==0 and all(int(c)%N**jg==0 for c in Q.all_coeffs())
    w0=w0//N**j0%N;w1=w1//N**j1%N
    Q=poly([int(Q.nth(j))//N**jg%N for j in range(H.degree()-2)])
    assert (w1-u*w0)%N==0
    c=w0*res(D,Q)%N;n=res(H,C)
    assert n%N**E==0
    v=n//N**E;assert (v-u*c*c)%N==0,(v,u,c,js,C)
    return v,c

def environment(N,d,t0,t1):
    r=(d-2)//2
    for a in range(1,2*N.bit_length()+2):
        D=poly([a]+[0]*(r-1)+[1])
        if gcd(int(D.eval(t0)*D.eval(t1)),N)==1:break
    else:raise ValueError('no D guard')
    P=poly([t0*t1,-t0-t1,1])*D**2
    H=poly([((int(P.nth(j))+N//2)%N)-N//2 for j in range(d)]+[1])
    for i in range(d+1):
        F=H+poly([i*N])
        if F.discriminant()!=0:H=F;break
    else:raise ValueError('discriminant')
    assert mp(H-P,N).is_zero
    return H,D

@lru_cache(None)
def metric(H,scale):
    d=H.degree();powers=[poly([0]*i+[1]).rem(H) for i in range(2*d-1)]
    # Frobenius metric for multiplication in X^j/scale^j, cleared denominators.
    return sp.Matrix([[int(powers[i+j].nth(k))*scale**(d-1+k-j)
        for j in range(d) for k in range(d)] for i in range(d)])

def reduced(B,H,method,scale):
    if method=='coeff':return B.T.lll().T
    L=B.T*metric(H,scale);R,T=L.lll_transform()
    assert T*L==R and abs(int(T.det()))==1
    return B*T.T

def squareclass_rank(ns):
    pool=set(abs(n) for n in ns if abs(n)>1)
    while True:
        hit=None;seq=sorted(pool)
        for i,a in enumerate(seq):
            for b in seq[:i]:
                g=gcd(a,b)
                if g>1:hit=(a,b,g);break
            if hit:break
        if not hit:break
        a,b,g=hit;pool.remove(a);pool.remove(b);pool.update(x for x in (g,a//g,b//g) if x>1)
    axes=sorted(pool);ix={a:i+1 for i,a in enumerate(axes) if isqrt(a)**2!=a};piv={}
    for n in ns:
        z=abs(n);v=int(n<0)
        for a in axes:
            e=0
            while z%a==0:z//=a;e+=1
            if e%2 and a in ix:v^=1<<ix[a]
        assert z==1
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)

PRIMES=list(sp.primerange(2,102))
def smooth(n):
    n=abs(n)
    for p in PRIMES:
        while n%p==0:n//=p
    return isqrt(n)**2==n

def candidates(B,seed):
    d=B.rows
    for j in range(d):yield poly(list(B[:,j]))
    for i in range(d):
        for j in range(i):
            for s in (-1,1):yield poly(list(B[:,i]+s*B[:,j]))
    rng=Random(seed)
    for _ in range(8):yield poly(list(B*sp.Matrix([rng.randrange(-2,3) for _ in range(d)])))

def experiment():
    rng=Random(1701)
    for N in (899,10403,1022117,100160063):
        d=6;t0=0;t1=isqrt(isqrt(N))+1
        while gcd(t1,N)!=1:t1+=1
        H,D=environment(N,d,t0,t1);us=[]
        while len(us)<16:
            u=rng.randrange(1,N)
            if gcd(u,N)==1:us.append(u)
        print('environment',N,d,t1,'H height',max(abs(c) for c in H.all_coeffs()),'D',D.as_expr(),flush=True)
        for js in [(0,0,0),(0,0,1),(0,0,2),(1,1,1)]:
            for method in ('coeff','mult'):
                vals=[];bits=[];bad=good=0
                for idx,u in enumerate(us):
                    B=lattice(H,N,t0,t1,u,js);R=reduced(B,H,method,max(2,t1))
                    assert hnf(R)==B
                    vs=[]
                    for C in candidates(R,idx):
                        v,c=transport(H,D,N,t0,t1,u,js,C)
                        if gcd(c,N)==1:
                            assert v and gcd(v,N)==1;good+=1;vs.append(v)
                        else:bad+=1
                    if vs:
                        v=min(vs,key=lambda v:abs(v));vals.append(v);bits.append(abs(v).bit_length())
                print(js,method,'accepted',len(vals),'unit/other',good,bad,'bits', (min(bits),max(bits),sum(bits)//len(bits)) if bits else None,'rank',squareclass_rank(vals),'smooth101',sum(smooth(v) for v in vals),flush=True)

# Additional tests are exposed as separate entrypoints below.
def mult_matrix(H,W):
    d=H.degree()
    return sp.Matrix.hstack(*(sp.Matrix(coefs((W*poly([0]*i+[1])).rem(H),d)) for i in range(d)))

def principal_equivalence():
    rng=Random(314159);cases=0
    for N in (899,10403,1022117,100160063,315):
        d=6;t0=0;t1=2
        while gcd(t1,N)!=1:t1+=1
        _,D=environment(N,d,t0,t1)
        H=poly([t0*t1,-t0-t1,1])*D**2+poly([N])
        assert H.discriminant()!=0
        delta=t1-t0;D0=int(D.eval(t0));D1=int(D.eval(t1))
        us=[]
        while len(us)<8:
            u=rng.randrange(1,N)
            if gcd(u,N)==1:us.append(u)
        for js in [(0,0,1),(0,0,2),(1,0,0),(0,2,1),(2,1,2),(1,1,1)]:
            j0,j1,jg=js;E=j0+j1+(d-2)*jg
            W=(poly([-t0,1])**j0*poly([-t1,1])**j1*D**(2*jg)).rem(H)
            M=mult_matrix(H,W)
            assert int(M.det())==N**E==res(H,W)
            rho=pow(delta,j1-j0,N)*pow(D0,jg-j0,N)*pow(D1,j1-jg,N)%N
            for u in us:
                v=u*rho*rho%N
                B=lattice(H,N,t0,t1,v,(0,0,0))
                assert hnf(M*B)==lattice(H,N,t0,t1,u,js)
                C=poly(list(B[:,0]+B[:,1]));WC=(W*C).rem(H)
                n,c=transport(H,D,N,t0,t1,v,(0,0,0),C)
                nn,cc=transport(H,D,N,t0,t1,u,js,WC)
                assert n==nn and (cc*cc-rho*rho*c*c)%N==0
                cases+=1
    print('principal jet lattice equalities:',cases,flush=True)

def gcd_free_axes(ns):
    # Incremental refinement; all stored axes remain pairwise coprime.
    axes=[]
    for value in sorted(set(abs(n) for n in ns)):
        todo=[value]
        while todo:
            z=todo.pop()
            if z<=1:continue
            for i,a in enumerate(axes):
                g=gcd(z,a)
                if g==1:continue
                if g==a:
                    while z%a==0:z//=a
                    todo.append(z)
                else:
                    axes.pop(i);todo.extend((g,a//g,z//g))
                break
            else:axes.append(z)
    axes.sort()
    assert all(gcd(a,b)==1 for i,a in enumerate(axes) for b in axes[:i])
    return axes

def row_data(ns,axes):
    nonsq={j:i+1 for i,j in enumerate(j for j,a in enumerate(axes) if isqrt(a)**2!=a)}
    rows=[];exps=[]
    for n in ns:
        z=abs(n);v=int(n<0);e={}
        for j,a in enumerate(axes):
            if z==1:break
            while z%a==0:z//=a;e[j]=e.get(j,0)+1
            if e.get(j,0)%2 and j in nonsq:v^=1<<nonsq[j]
        assert z==1
        rows.append(v);exps.append(e)
    return rows,exps

def parity_pool(N,ss,hs,data):
    axes=gcd_free_axes([n for i,n,c in data]); rows,exps=row_data([n for i,n,c in data],axes)
    piv={};pp={};witness=None
    for j,(i,n,c) in enumerate(data):
        v=rows[j];t=1<<i;b=1<<j
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=(v,t,b);break
            vv,tt,bb=piv[k];v^=vv;t^=tt;b^=bb
        if v==0 and t:
            if witness is None:witness=b
            while t:
                k=t.bit_length()-1
                if k not in pp:pp[k]=t;break
                t^=pp[k]
    # Independent augmented-rank comparison.
    aug={}
    for (i,n,c),v in zip(data,rows):
        z=(v<<len(ss))|(1<<i)
        while z:
            j=z.bit_length()-1
            if j in aug:z^=aug[j]
            else:aug[j]=z;break
    assert len(aug)-len(piv)==len(pp)
    if witness is None:return len(piv),len(pp),None
    w=1;expected=1;sign=0;counts={};xp={}
    for j,(i,n,c) in enumerate(data):
        if not (witness>>j)&1:continue
        sign^=int(n<0);counts[i]=counts.get(i,0)+1
        w=w*pow(c,-1,N)%N;expected=expected*ss[i]%N
        for k,e in exps[j].items():xp[k]=xp.get(k,0)+e
    assert sign==0 and any(e%2 for e in counts.values())
    for k,e in xp.items():
        a=axes[k];r=isqrt(a)
        if r*r==a:w=w*pow(r,e,N)%N
        else:
            assert e%2==0;w=w*pow(a,e//2,N)%N
    assert w*w%N==expected
    # Only now use the private roots, after public verification.
    pr=1
    for i,e in counts.items():pr=pr*pow(hs[i],e,N)%N
    assert pr*pr%N==expected
    g=gcd((pr*pow(w,-1,N)-1)%N,N)
    assert N%g==0
    return len(piv),len(pp),g

def pooled_experiment(only=None):
    rng=Random(271828)
    for N in (899,10403,1022117,100160063):
        d=6;t0=0;t1=isqrt(isqrt(N))+1
        while gcd(t1,N)!=1:t1+=1
        _,D=environment(N,d,t0,t1);P=poly([0,-t1,1])*D**2
        hs=[];ss=[]
        while len(ss)<12:
            h=rng.randrange(1,N);s=h*h%N
            if gcd(h,N)==1 and s not in ss:hs.append(h);ss.append(s)
        if only is not None and N not in only:continue
        for name,H in [('constant',P+poly([N])),('linear',P+poly([N,N]))]:
            assert H.discriminant()!=0
            data=[];seen={};checks=good=0;correction_gcds=set();proper_guard=set()
            for i,s in enumerate(ss):
                for js in [(0,0,0),(0,0,1),(0,0,2)]:
                    B=lattice(H,N,t0,t1,s,js)
                    for method in ('coeff','mult'):
                        R=reduced(B,H,method,max(2,t1));assert hnf(R)==B
                        for C in candidates(R,i):
                            n,c=transport(H,D,N,t0,t1,s,js,C);checks+=1
                            g=gcd(c,N)
                            if g!=1:
                                if 1<g<N:proper_guard.add(g)
                                continue
                            good+=1;assert n and gcd(n,N)==1
                            key=(i,n)
                            if key in seen:
                                assert (seen[key]**2-c*c)%N==0
                                g=gcd(seen[key]-c,N)
                                if 1<g<N:correction_gcds.add(g)
                            else:
                                seen[key]=c;data.append((i,n,c))
            # This is intentionally a relation-supply experiment: early proper gcds
            # are recorded, not used to select the rows or stop the sampler.
            rank,dim,g=parity_pool(N,ss,hs,data)
            print('pooled',N,name,'checks',checks,'unit',good,'unique',len(data),'norm rank',rank,
                'useful target dimension',dim,'gcd witness',g,'guard factors',sorted(proper_guard),
                'public correction factors',sorted(correction_gcds),flush=True)

def localized_equivalence():
    rng=Random(161803);cases=0
    for N in (899,10403,1022117,315):
        d=6;t0=0;t1=2
        _,D=environment(N,d,t0,t1)
        for Epoly in (poly([1,1]),poly([2,0,1]),poly([-1,1])):
            E0=int(Epoly.eval(t0));E1=int(Epoly.eval(t1));RDE=res(D,Epoly)
            if gcd(E0*E1*RDE,N)!=1:continue
            H=poly([t0*t1,-t0-t1,1])*D**2+N*Epoly
            if H.discriminant()==0:continue
            for js in [(0,0,2),(1,0,0),(0,2,1),(2,1,1)]:
                j0,j1,jg=js;depth=j0+j1+(d-2)*jg
                S=E0**j0*E1**j1*RDE**(2*jg);assert S
                W=(poly([-t0,1])**j0*poly([-t1,1])**j1*D**(2*jg)).rem(H)
                M=mult_matrix(H,W);assert M.det()==S*N**depth
                rho=pow(t1-t0,j1-j0,N)*pow(int(D.eval(t0)),jg-j0,N)*pow(int(D.eval(t1)),j1-jg,N)%N
                for _ in range(4):
                    u=rng.randrange(1,N)
                    while gcd(u,N)!=1:u=rng.randrange(1,N)
                    v=u*rho*rho*pow(E0,j0,N)*pow(E1,-j1,N)%N
                    B=lattice(H,N,t0,t1,u,js);A=lattice(H,N,t0,t1,v,(0,0,0))
                    T=B.inv()*M*A;assert all(a.q==1 for a in T) and abs(T.det())==abs(S)
                    V=M.inv()*(abs(S)*B);assert all(a.q==1 for a in V)
                    assert all(a.q==1 for a in A.inv()*V)
                    C=poly(list(B[:,0]+B[:,1]));C0=poly(list(V[:,0]+V[:,1]))
                    n,c=transport(H,D,N,t0,t1,u,js,C)
                    n0,c0=transport(H,D,N,t0,t1,v,(0,0,0),C0)
                    assert n0==S**(d-1)*n
                    cases+=1
    print('localized jet index and norm identities:',cases,flush=True)

if __name__=='__main__':
    import sys
    mode=sys.argv[1] if len(sys.argv)>1 else 'all'
    if mode in ('all','single'):experiment()
    if mode in ('all','principal'):principal_equivalence();localized_equivalence()
    if mode in ('all','pool'):pooled_experiment(set(map(int,sys.argv[2:])) if len(sys.argv)>2 else None)
