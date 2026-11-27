#!/usr/bin/env python3
"""Fixed cubic norm-packet transport, exact arithmetic and parity pool tests.
Imports finite arithmetic helpers from verify_glued_norm_reduction.py.
The tiny public square representatives are factored for experimental inputs.
"""
from verify_glued_norm_reduction import poly, X, ev, ideal_product, lll_gram, pool_rank
from itertools import product
from math import gcd, prod, isqrt
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form as hnf

def setup(N,near=False):
    m=int(sp.integer_nthroot((27*N)//4 if near else 7*N,3)[0])+1
    m|=1
    while 4*m**3<=27*N or gcd(m,N)!=1:m+=2
    H=sp.Poly(X*(X-m)**2-N,X,domain=sp.ZZ)
    ts=[0,sp.Rational(m,3),m,2*m]
    assert H.is_monic and H.degree()==3 and H.is_irreducible
    assert all(H.eval(a)*H.eval(b)<0 for a,b in zip(ts,ts[1:]))
    assert H.discriminant()==N*(4*m**3-27*N)>0
    d=3;I=sp.eye(d);base=[I[:,i] for i in range(d)]
    powers=[tuple(int(poly([0]*i+[1]).rem(H).nth(k)) for k in range(d)) for i in range(2*d-1)]
    def mul(a,b):
        aa=list(map(int,a));bb=list(map(int,b));c=[0]*d
        for i,j in product(range(d),repeat=2):
            v=aa[i]*bb[j]
            for k in range(d):c[k]+=v*powers[i+j][k]
        return sp.Matrix(c)
    def mat(a):
        aa=list(map(int,a));return sp.Matrix(d,d,lambda k,j:sum(aa[i]*powers[i+j][k] for i in range(d)))
    G=sp.Matrix(d,d,lambda i,j:sp.trace(mat(mul(base[i],base[j]))))
    assert G.det()==H.discriminant()
    return H,m,mul,mat,G

def choices(H,q):
    # Tiny q only; general input would use polynomial factoring over F_q.
    roots=[r for r in range(q) if H.eval(r)%q==0 and H.diff().eval(r)%q!=0]
    # A simple degree-one factor gives an invertible ideal even if another
    # factor is repeated. Include scalar qA as a universally valid odd option.
    ans=[(hnf(sp.Matrix([[q,-r,-r*r],[0,1,0],[0,0,1]])),1) for r in roots]
    ans.append((q*sp.eye(3),3));return ans

def run(joint=False):
    rng=Random(271828);reductions=checks=guards=0
    for N in ((899,10403,1022117) if joint else (899,10403,1022117,100160063)):
        H,m,mul,mat,G=setup(N,near=joint);hs=[];ss=[];fs=[]
        while len(ss)<8:
            h=rng.randrange(1,N);s=h*h%N
            if gcd(h,N)==1 and s not in ss:hs.append(h);ss.append(s);fs.append(sp.factorint(s))
        cache={};data=[];seen=set();bits=[];best=[];proper=set();oldbest=[];jointchecks=0;olddata=[]
        for i,(s,f) in enumerate(zip(ss,fs)):
            ps=[p for p,e in f.items() if e%2];q=prod(ps);t=isqrt(s//q);assert t*t*q==s
            for p in ps:
                if p not in cache:cache[p]=choices(H,p)
            combos=list(product(*(cache[p] for p in ps)))
            if len(combos)>16:combos=rng.sample(combos,16)
            vals=[];oldvals=[]
            for combo in combos:
                I=sp.eye(3);Q=1
                for p,(P,fdeg) in zip(ps,combo):
                    I=ideal_product(I,P,mul);Q*=p**fdeg
                assert abs(I.det())==Q and Q%q==0
                b=isqrt(Q//q);assert Q==q*b*b
                R=lll_gram(I,G);reductions+=1
                cs=[R[:,j] for j in range(3)]+[R[:,a]+sg*R[:,j] for a in range(3) for j in range(a) for sg in (-1,1)]
                for a in cs:
                    C=poly(list(a));n=int(mat(a).det());assert n==int(sp.resultant(H,C)) and n%Q==0
                    v=(ev(a,0)+N//2)%N-N//2
                    k=ev(a,m)%N
                    assert (n-v*k*k)%N==0
                    checks+=1;g=gcd(v*k,N)
                    if g!=1:
                        if 1<g<N:proper.add(g)
                        guards+=1;continue
                    z=(n//Q)*v;assert gcd(z,N)==1
                    c=v*k*pow(q*b*t,-1,N)%N
                    assert (z-s*c*c)%N==0
                    vals.append(abs(z).bit_length());oldvals.append(abs(z).bit_length());bits.append(abs(z).bit_length())
                    olddata.append((i,z,c))
                    if (i,z) not in seen:seen.add((i,z));data.append((i,z,c))
                if joint:
                    J=I.row_join(sp.zeros(3,1)).col_join(sp.Matrix([[int(I[0,j]) for j in range(3)]+[N]]))
                    assert abs(J.det())==N*Q
                    for weight in (sp.Rational(1,m),1,m):
                        M=sp.diag(G,weight**2)
                        B=lll_gram(J,M)
                        js=[B[:,j] for j in range(4)]+[B[:,a]+sg*B[:,j] for a in range(4) for j in range(a) for sg in (-1,1)]
                        for v0 in js:
                            a=v0[:3,:];v=int(v0[3]);C=poly(list(a));n=int(mat(a).det());k=ev(a,m)%N
                            assert (v-ev(a,0))%N==0 and n%Q==0 and (n-v*k*k)%N==0
                            assert n==int(sp.resultant(H,C))
                            jointchecks+=1;g=gcd(v*k,N)
                            if g!=1:
                                if 1<g<N:proper.add(g)
                                continue
                            z=(n//Q)*v;assert gcd(z,N)==1
                            c=v*k*pow(q*b*t,-1,N)%N;assert (z-s*c*c)%N==0
                            vals.append(abs(z).bit_length());bits.append(abs(z).bit_length())
                            if (i,z) not in seen:seen.add((i,z));data.append((i,z,c))
            best.append(min(vals) if vals else -1);oldbest.append(min(oldvals) if oldvals else -1)
        rank,dim,g=pool_rank(N,ss,hs,data)
        print('fixed cubic',N,'m',m,'disc bits',int(H.discriminant()).bit_length(),'unique',len(data),'rank',rank,'useful parity',dim,'gcd',g,
              'bits min/median/max',(min(bits),sorted(bits)[len(bits)//2],max(bits)),
              'best per target',best,'guard factors',sorted(proper),flush=True)
        if joint:
            print('near-cusp independent only:',N,'best',oldbest,'rank/dim/gcd',pool_rank(N,ss,hs,olddata),'joint checks',jointchecks,flush=True)
    print('fixed cubic reductions:',reductions,'exact norm identities:',checks,'nonunit guards:',guards,flush=True)

if __name__=='__main__':
    import sys
    run(joint='joint' in sys.argv[1:])
