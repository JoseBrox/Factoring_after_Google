#!/usr/bin/env python3
"""Exact gluing-order identities and shared prime-packet norm reductions.
Tiny input factorizations are deliberate. No asymptotic supply claim.
"""
from itertools import product
from math import gcd, prod, isqrt
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf
X=sp.Symbol('X')

def poly(cs):return sp.Poly.from_list(list(reversed(cs)),X,domain=sp.ZZ)

def setup(N,Q):
    m=max(3,isqrt(isqrt(8*N*Q))+1)|1
    while m**4<=8*N*Q or gcd(m,N*Q)!=1:m+=2
    H=sp.Poly(X*(X-m)*(X+m)**2-N*Q,X,domain=sp.ZZ)
    assert H.is_monic and H.degree()==4 and H.is_irreducible
    ts=[-2*m,-m,sp.Rational(-m,2),0,2*m]
    assert all(H.eval(x)*H.eval(y)<0 for x,y in zip(ts,ts[1:]))
    assert H.discriminant()>0
    d=4;D=poly([m,1]);I=sp.eye(d)
    powers=[tuple(int(poly([0]*i+[1]).rem(H).nth(k)) for k in range(d)) for i in range(2*d-1)]
    basis=[I[:,i] for i in range(d)]
    def mul(a,b):
        aa=list(map(int,a));bb=list(map(int,b));c=[0]*d
        for i,j in product(range(d),repeat=2):
            if aa[i] and bb[j]:
                v=aa[i]*bb[j]
                for k in range(d):c[k]+=v*powers[i+j][k]
        return sp.Matrix(c)
    def mat(a):
        aa=list(map(int,a))
        return sp.Matrix(d,d,lambda k,j:sum(aa[i]*powers[i+j][k] for i in range(d)))
    G=sp.Matrix(d,d,lambda i,j:sp.trace(mat(mul(basis[i],basis[j]))))
    assert G.det()==H.discriminant() and all(G[:i,:i].det()>0 for i in range(1,d+1))
    return H,D,m,mul,mat,G

def ev(c,t):return sum(int(c[j])*t**j for j in range(len(c)))

def ideal_product(A,B,mul):
    return hnf(sp.Matrix.hstack(*(mul(A[:,i],B[:,j]) for i,j in product(range(A.cols),range(B.cols)))))

def Lratio(N,m,u):
    # C(m)-u C(0) = (1-u)c0 + m c1 + m² c2 + m³ c3.
    a=pow(m,-1,N)
    B=sp.Matrix([[1,0,0,0],[(u-1)*a%N,N,-m%N,-m*m%N],[0,0,1,0],[0,0,0,1]])
    B=hnf(B);assert abs(B.det())==N
    assert all((ev(B[:,i],m)-u*ev(B[:,i],0))%N==0 for i in range(4))
    return B

def root_ideal(q,t):
    return hnf(sp.Matrix([[q,-t,-t*t,-t**3],[0,1,0,0],[0,0,1,0],[0,0,0,1]]))

def anchor_ideal(A,N,m):
    # Exact kernel of the one linear congruence on ideal basis coordinates.
    row=[(ev(A[:,i],m)-ev(A[:,i],0))%N for i in range(4)]
    # gcd row entries with N =1, since ideal index is coprime to N.
    # Extended-gcd column operations make row[0] a gcd of the integer entries.
    T=sp.eye(4);w=sp.Matrix(1,4,row)
    for i in range(1,4):
        x,y=int(w[0]),int(w[i]);
        if y==0:continue
        a,b,g=map(int,sp.gcdex(x,y))
        U=sp.eye(4);U[0,0]=a;U[i,0]=b;U[0,i]=-y//g;U[i,i]=x//g
        assert abs(U.det())==1
        w=w*U;T=T*U
    assert gcd(int(w[0]),N)==1 and all(w[i]==0 for i in range(1,4))
    B=hnf(A*T*sp.diag(N,1,1,1));assert abs(B.det())==N*abs(A.det())
    assert all((ev(B[:,i],m)-ev(B[:,i],0))%N==0 for i in range(4))
    assert all(x.q==1 for x in A.inv()*B)
    return B

def lll_gram(A,G):
    B=A.copy();n=A.cols
    def gs():
        U=[];mu=sp.zeros(n,n);norm=[]
        for i in range(n):
            v=B[:,i]
            for j in range(i):
                mu[i,j]=(B[:,i].T*G*U[j])[0]/norm[j]
                v-=mu[i,j]*U[j]
            U.append(v);norm.append((v.T*G*v)[0]);assert norm[-1]>0
        return mu,norm
    k=1;steps=0
    while k<n:
        steps+=1;assert steps<10000
        mu,b=gs()
        for j in range(k-1,-1,-1):
            c=sp.floor(mu[k,j]+sp.Rational(1,2))
            B[:,k]-=c*B[:,j];mu,b=gs()
        if b[k]>=(sp.Rational(3,4)-mu[k,k-1]**2)*b[k-1]:k+=1
        else:B.col_swap(k,k-1);k=max(k-1,1)
    mu,b=gs()
    assert hnf(B)==hnf(A)
    assert all(abs(mu[i,j])<=sp.Rational(1,2) for i in range(n) for j in range(i))
    assert all(b[i]>=(sp.Rational(3,4)-mu[i,i-1]**2)*b[i-1] for i in range(1,n))
    return B

def verify_gluing():
    rng=Random(1701);checks=0
    for N in (77,315,899,10403):
        Q=prod(q for q in (3,5,7,11,13) if gcd(q,N)==1)
        H,D,m,mul,mat,G=setup(N,Q)
        B=Lratio(N,m,1)
        assert (B.T*G*B).det()==N*N*G.det()
        for _ in range(12):
            us=[]
            while len(us)<2:
                u=rng.randrange(1,N)
                if gcd(u,N)==1:us.append(u)
            u,v=us;A=Lratio(N,m,u);C=Lratio(N,m,v)
            assert ideal_product(A,C,mul)==Lratio(N,m,u*v%N)
            assert ideal_product(A,Lratio(N,m,pow(u,-1,N)),mul)==B
            assert ideal_product(A,sp.eye(4),mul)==sp.eye(4)
            checks+=1
        for q in sp.factorint(Q):
            for t in (0,m):
                I=root_ideal(q,t);assert H.eval(t)%q==0 and gcd(int(H.diff().eval(t)),q)==1
                assert ideal_product(I,sp.eye(4),mul)==I
                J=anchor_ideal(I,N,m)
                assert ideal_product(J,sp.eye(4),mul)==I
    print('gluing multiplication/inverse/extension checks:',checks,flush=True)

def squareclass_rows(vals):
    axes=[]
    for value in sorted(set(abs(n) for n in vals)):
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
    axes.sort();assert all(gcd(a,b)==1 for i,a in enumerate(axes) for b in axes[:i])
    ix={j:i+1 for i,j in enumerate(j for j,a in enumerate(axes) if isqrt(a)**2!=a)}
    rows=[];exps=[]
    for n in vals:
        z=abs(n);v=int(n<0);e={}
        for j,a in enumerate(axes):
            while z%a==0:z//=a;e[j]=e.get(j,0)+1
            if e.get(j,0)%2 and j in ix:v^=1<<ix[j]
            if z==1:break
        assert z==1
        rows.append(v);exps.append(e)
    return axes,rows,exps

def pool_rank(N,ss,hs,data):
    seen=set();data=[r for r in data if not ((r[0],r[1]) in seen or seen.add((r[0],r[1])))]
    axes,rows,exps=squareclass_rows([v for i,v,c in data]);piv={};targ={}
    for j,((i,n,c),v) in enumerate(zip(data,rows)):
        t=1<<i;b=1<<j
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=(v,t,b);break
            vv,tt,bb=piv[k];v^=vv;t^=tt;b^=bb
        if not v:
            while t:
                k=t.bit_length()-1
                if k not in targ:targ[k]=(t,b);break
                tt,bb=targ[k];t^=tt;b^=bb
    aug={}
    for (i,n,c),v in zip(data,rows):
        z=(v<<len(ss))|(1<<i)
        while z:
            k=z.bit_length()-1
            if k not in aug:aug[k]=z;break
            z^=aug[k]
    assert len(aug)-len(piv)==len(targ)
    certificates=[]
    for parity,witness in targ.values():
        w=1;expect=1;sign=0;counts={};xp={}
        for j,(i,n,c) in enumerate(data):
            if not (witness>>j)&1:continue
            sign^=int(n<0);counts[i]=counts.get(i,0)+1;w=w*pow(c,-1,N)%N;expect=expect*ss[i]%N
            for k,e in exps[j].items():xp[k]=xp.get(k,0)+e
        assert sign==0 and sum((e%2)<<i for i,e in counts.items())==parity and parity
        for k,e in xp.items():
            a=axes[k];r=isqrt(a)
            if r*r==a:w=w*pow(r,e,N)%N
            else:assert e%2==0;w=w*pow(a,e//2,N)%N
        assert w*w%N==expect
        certificates.append((w,expect,counts))
    # Fix and verify the entire witness basis before accessing private roots.
    gs=[]
    for w,expect,counts in certificates:
        pr=prod(pow(hs[i],e,N) for i,e in counts.items())%N
        assert pr*pr%N==expect
        g=gcd(pr*pow(w,-1,N)-1,N);assert N%g==0;gs.append(g)
    return len(piv),len(targ),sorted(set(gs))

def experiments():
    rng=Random(271828);checks=guards=reductions=0
    for N in (899,10403,1022117,100160063):
        hs=[];ss=[];fs=[]
        while len(ss)<8:
            h=rng.randrange(1,N);s=h*h%N
            if gcd(h,N)==1 and s not in ss:
                hs.append(h);ss.append(s);fs.append(sp.factorint(s))
        # Factoring the tiny public representatives is an explicit test input step.
        Q=prod(sorted({p for f in fs for p,e in f.items() if p!=2 and e%2})) or 1
        H,D,m,mul,mat,G=setup(N,Q)
        print('environment',N,'Qbits',Q.bit_length(),'m',m,'disc bits',int(H.discriminant()).bit_length(),flush=True)
        data=[];seen=set();bits=[];best=[]
        for i,(s,f) in enumerate(zip(ss,fs)):
            ps=[p for p,e in f.items() if p!=2 and e%2];q=prod(ps);tw=2**(f.get(2,0)%2)
            t=isqrt(s//(q*tw));assert s==t*t*q*tw
            orientations=list(product((0,m),repeat=len(ps)))
            if len(orientations)>16:orientations=rng.sample(orientations,16)
            vals=[]
            for ori in orientations:
                I=sp.eye(4)
                for p,r in zip(ps,ori):I=ideal_product(I,root_ideal(p,r),mul)
                assert abs(I.det())==q
                J=anchor_ideal(I,N,m);R=lll_gram(J,G);reductions+=1
                candidates=[R[:,j] for j in range(4)]+[R[:,a]+sg*R[:,b] for a in range(4) for b in range(a) for sg in (-1,1)]
                for a in candidates:
                    C=poly(list(a));n=int(mat(a).det());assert n==int(sp.resultant(H,C)) and n%q==0
                    b=n//q;c=ev(a,0)*int(sp.resultant(D,C))%N
                    assert (n-c*c)%N==0 and (ev(a,m)-ev(a,0))%N==0
                    checks+=1
                    if gcd(c,N)!=1:guards+=1;continue
                    assert gcd(b,N)==1
                    v=tw*b;root= b*pow(t*c,-1,N)%N
                    # v = s*root² modulo N.
                    assert (v-s*root*root)%N==0
                    vals.append(abs(v).bit_length());bits.append(abs(v).bit_length())
                    if (i,v) not in seen:seen.add((i,v));data.append((i,v,root))
            best.append(min(vals) if vals else -1)
        rank,dim,g=pool_rank(N,ss,hs,data)
        print('packet pool:',N,'unique',len(data),'rank',rank,'useful parity',dim,'gcd',g,
              'bits min/median/max', (min(bits),sorted(bits)[len(bits)//2],max(bits)),
              'best per target',best,flush=True)
    print('ideal reductions:',reductions,'candidate norm identities:',checks,'nonunit guards:',guards,flush=True)

if __name__=='__main__':
    verify_gluing();experiments()
