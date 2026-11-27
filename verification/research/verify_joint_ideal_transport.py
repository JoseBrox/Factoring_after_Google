#!/usr/bin/env python3
"""Exact checks of correlated port kernels, odd parity and common-base ideal transport.
Requires SymPy 1.14. Finite fixtures are not a relation-supply theorem.
"""
from itertools import product
from math import gcd, prod, lcm
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp


def rank2(A):
    piv = {}
    for j in range(A.cols):
        x = sum((int(A[i,j]) & 1) << i for i in range(A.rows))
        while x:
            h = x.bit_length()-1
            if h in piv:
                x ^= piv[h]
            else:
                piv[h] = x
                break
    return len(piv)


def ikernel(A):
    D,S,T = smith_normal_decomp(A,domain=sp.ZZ)
    assert S*A*T == D and abs(S.det()) == abs(T.det()) == 1
    r = sum(D[i,i] != 0 for i in range(min(D.shape)))
    K = T[:,r:]
    assert A*K == sp.zeros(A.rows,K.cols)
    assert rank2(K) == K.cols
    return K


def randmat(rng,m,n):
    return sp.Matrix(m,n,[rng.randrange(-5,6) for _ in range(m*n)])


def check_blocks():
    rng = Random(271828)
    par = odd = novel = sufficient = 0
    for _ in range(250):
        m,k,h = rng.randrange(1,7),rng.randrange(2,8),rng.randrange(1,6)
        V,C = randmat(rng,m,k),randmat(rng,m,h)
        for j in range(h):
            if rng.randrange(2): C[:,j] *= 2
        A = V.row_join(C)
        q = A.rank()-C.rank(); e = C.rank()-rank2(C)
        K = ikernel(A)
        b = rank2(K[:k,:])
        assert b >= k-q-e
        t = rng.randrange(1,4)
        L = ikernel(A.col_join(randmat(rng,t,k+h)))
        assert rank2(L[:k,:]) >= b-t
        # One arbitrary binary sign equation on the final saturated basis.
        sign = [rng.randrange(2) for _ in range(k+h)]
        witnesses = []
        for j in range(L.cols):
            z = L[:,j]
            if sum(int(a)*s for a,s in zip(z,sign))%2 == 0:
                witnesses.append(z)
        bad = [j for j in range(L.cols)
               if sum(int(a)*s for a,s in zip(L[:,j],sign))%2]
        if bad:
            witnesses += [L[:,bad[0]]+L[:,j] for j in bad[1:]]
        if k-q-e > t+1:
            assert any(any(int(v)%2 for v in z[:k]) for z in witnesses)
            sufficient += 1
        par += 1
        # Odd minor chosen greedily using binary ranks of columns, then rows.
        J=[]
        for j in range(h):
            if rank2(C[:,J+[j]])>len(J): J.append(j)
        R=[]; CC=C[:,J]
        for i in range(m):
            if rank2(CC[R+[i],:])>len(R): R.append(i)
        if J:
            pivot=CC[R,:]; D=abs(int(pivot.det()))
            assert D%2
            lam=D*pivot.inv()*V[R,:]
            assert all(a.q==1 for a in lam)
            W=D*V-CC*lam
            assert W[R,:]==sp.zeros(len(R),k)
            B=randmat(rng,5,m)
            assert W.col_join(-B*W).rank()==V.row_join(CC).rank()-CC.rank()
            odd += 1
        # Batch with unknown new-label directions. No need for individual smoothness.
        z,l=rng.randrange(1,5),rng.randrange(1,6)
        Co,Cn=randmat(rng,m,l),randmat(rng,z,l)
        # Introduce correlations in the novel labels in half the samples.
        if l>1 and rng.randrange(2): Cn[:,1]=Cn[:,0]
        ker=Cn.nullspace()
        H=Co*sp.Matrix.hstack(*ker) if ker else sp.zeros(m,0)
        E=C; old=E.row_join(V)
        gain=old.rank()+E.row_join(H).rank()-old.row_join(H).rank()-E.rank()
        EE=E.col_join(sp.zeros(z,h)); VV=V.col_join(sp.zeros(z,k)); AA=Co.col_join(Cn)
        after=EE.row_join(AA).row_join(VV).rank()-EE.row_join(AA).rank()
        assert after==q-gain and gain>=0
        novel += int(gain>0)
    print('joint Smith/parity blocks:',par,'odd pivots:',odd,
          'sufficient-parity cases:',sufficient,'strict novelty-batch gains:',novel)


def check_relative_projection():
    rng=Random(314159); count=packets=0
    for _ in range(250):
        J=rng.randrange(1,5)
        ds=[rng.choice([1,3,5,7,9]) for _ in range(J)]
        es=[];fs=[]
        for d in ds:
            parts=[];left=d
            while left:
                n=rng.randrange(1,left+1);left-=n
                e=rng.choice(sp.divisors(n));parts.append((e,n//e))
            es.append(sp.Matrix([e for e,f in parts]));fs.append(sp.Matrix([f for e,f in parts]))
        n=1+sum(e.rows for e in es); P=sp.zeros(n,n);P[0,0]=1
        pos=1;D=lcm(*ds); G=sp.zeros(n,J); E=sp.zeros(n,J+1);E[0,0]=1
        for j,(d,e,f) in enumerate(zip(ds,es,fs)):
            m=e.rows;P[0,pos:pos+m]=f.T/d
            P[pos:pos+m,pos:pos+m]=sp.eye(m)-e*f.T/d
            G[0,j]=-1;G[pos:pos+m,j]=e
            E[pos:pos+m,j+1]=e
            pos+=m
        assert P*G==sp.zeros(n,J) and P.rank()==n-J
        assert all(v.q==1 for v in D*P) and D%2
        assert rank2(D*P)==n-J
        W=randmat(rng,n,rng.randrange(1,9))
        assert (P*W).rank()==W.row_join(G).rank()-J
        X=randmat(rng,J+1,rng.randrange(1,9))
        assert (P*E*X).rank()==(sp.ones(1,J+1)*X).rank()
        packets+=int((E*X).rank()>(P*E*X).rank())
        count+=1
    print('relative projection cases:',count,'strict packet rank savings:',packets)

# Explicit totally real cubic base, known modular root, and two odd relative extensions.
x=sp.Symbol('x'); f=sp.Poly(x**3-x*x-2*x+1,x,domain=sp.ZZ)
N=1189; m=11; d=3
one=sp.Matrix([1,0,0]); theta=sp.Matrix([0,1,0]); basis=[sp.eye(3)[:,i] for i in range(3)]


def base_mul(a,b):
    z=[0]*5
    for i,j in product(range(3),repeat=2): z[i+j]+=a[i]*b[j]
    for i in (4,3):
        w=z[i];z[i]=0;z[i-1]+=w;z[i-2]+=2*w;z[i-3]-=w
    return sp.Matrix(z[:3])


def base_mat(a): return sp.Matrix.hstack(*(base_mul(a,b) for b in basis))
def base_norm(a): return int(base_mat(a).det())
def base_eval(a): return sum(int(a[i])*pow(m,i,N) for i in range(3))%N


def ideal_mul(A,B,mul):
    return hermite_normal_form(sp.Matrix.hstack(*(mul(a,b) for a in A.columnspace() for b in B.columnspace())))


def root_ideal(q,r):
    return hermite_normal_form(sp.Matrix([[q,-r,-r*r],[0,1,0],[0,0,1]]))


def lll_gram(A,G):
    B=A.copy(); n=A.cols
    def gs():
        ortho=[];mu=sp.zeros(n,n);norm=[]
        for i in range(n):
            u=B[:,i]
            for j in range(i):
                mu[i,j]=(B[:,i].T*G*ortho[j])[0]/norm[j]
                u-=mu[i,j]*ortho[j]
            ortho.append(u);norm.append((u.T*G*u)[0]);assert norm[-1]>0
        return mu,norm
    k=1;steps=0
    while k<n:
        steps+=1;assert steps<1000
        mu,b=gs()
        for j in range(k-1,-1,-1):
            c=sp.floor(mu[k,j]+sp.Rational(1,2))
            B[:,k]-=c*B[:,j];mu,b=gs()
        if b[k]>=(sp.Rational(3,4)-mu[k,k-1]**2)*b[k-1]: k+=1
        else: B.col_swap(k,k-1);k=max(k-1,1)
    mu,b=gs()
    assert abs(B.det())==abs(A.det()) and hermite_normal_form(B)==hermite_normal_form(A)
    assert all(abs(mu[i,j])<=sp.Rational(1,2) for i in range(n) for j in range(i))
    assert all(b[i]>=(sp.Rational(3,4)-mu[i,i-1]**2)*b[i-1] for i in range(1,n))
    return B[:,0]


def ext_mul(u,v,a):
    z=[sp.zeros(3,1) for _ in range(3)]
    for i,j in product(range(3),repeat=2):
        z[(i+j)%3]+=base_mul(u[3*i:3*i+3,:],v[3*j:3*j+3,:])*a**((i+j)//3)
    return sp.Matrix.vstack(*z)


def embed(u): return sp.Matrix.vstack(u,sp.zeros(6,1))
def ext_mat(u,a): return sp.Matrix.hstack(*(ext_mul(u,sp.eye(9)[:,i],a) for i in range(9)))
def ext_eval(u,t): return sum(base_eval(u[3*i:3*i+3,:])*pow(t,i,N) for i in range(3))%N


def relative_norm(u,a):
    # Compute determinant independently in Q[X]/f, using the explicit relative matrix.
    v=[sum(u[3*i+j]*x**j for j in range(3)) for i in range(3)]
    M=sp.Matrix([[v[0],a*v[2],a*v[1]],[v[1],v[0],a*v[2]],[v[2],v[1],v[0]]])
    z=sp.Poly(M.det(),x,domain=sp.QQ).rem(f)
    out=sp.Matrix([z.nth(i) for i in range(3)])
    aa,bb,cc=[u[3*i:3*i+3,:] for i in range(3)]
    def cube(q):return base_mul(q,base_mul(q,q))
    assert out==cube(aa)+a*cube(bb)+a*a*cube(cc)-3*a*base_mul(aa,base_mul(bb,cc))
    return out


def ext_inv(u,a): return ext_mat(u,a).inv()*embed(one)
def ext_pow(u,k,a):
    z=embed(one)
    if k<0:u=ext_inv(u,a);k=-k
    while k:
        if k&1:z=ext_mul(z,u,a)
        u=ext_mul(u,u,a);k//=2
    return z


def eval_fraction(u,t):
    # Exact evaluation even for field products with rational coefficient denominators.
    z=0
    for i,j in product(range(3),repeat=2):
        v=u[3*i+j];z+=int(v.p)*pow(int(v.q),-1,N)*pow(t,i,N)*pow(m,j,N)
    return z%N


def check_actual_ideals():
    assert f.is_irreducible and f.eval(m)==N and f.discriminant()==49
    G=sp.Matrix(3,3,lambda i,j:sp.trace(base_mat(base_mul(basis[i],basis[j]))))
    assert G.det()==49 and all(G[:i,:i].det()>0 for i in range(1,4))
    ts={a:next(t for t in range(N) if pow(t,3,N)==a) for a in (2,3)}
    # Both pure cubic extensions are irreducible over the totally real Galois base:
    # a real root in the base would generate a non-totally-real cubic field.
    checked=extensions=0;fixture=None
    for q in list(sp.primerange(11,110)):
        if gcd(q,N*49)>1:continue
        roots=[r for r in range(q) if f.eval(r)%q==0]
        if len(roots)!=3:continue
        Is=[root_ideal(q,r) for r in roots]
        assert ideal_mul(ideal_mul(Is[0],Is[1],base_mul),Is[2],base_mul)==q*sp.eye(3)
        for idx,I in enumerate(Is):
            alpha=lll_gram(I,G); norm=abs(base_norm(alpha))
            assert norm%q==0 and norm**2*27<=8*49*q*q
            if gcd(base_eval(alpha),N)>1:continue
            others=[j for j in range(3) if j!=idx]
            rest=ideal_mul(Is[others[0]],Is[others[1]],base_mul)
            b=base_mat(alpha)*rest/q
            assert all(v.q==1 for v in b)
            b=hermite_normal_form(sp.Matrix(3,3,[int(v) for v in b]))
            assert ideal_mul(I,b,base_mul)==hermite_normal_form(base_mat(alpha))
            assert abs(b.det())==norm//q
            checked+=1
            # Use scaled base reductions in one test per prime to exercise nonunit residuals.
            if idx==0:
                alpha=2*alpha;b=2*b
                assert ideal_mul(I,b,base_mul)==hermite_normal_form(base_mat(alpha))
            Iext=sp.diag(I,I,I);bext=sp.diag(b,b,b)
            aa=[];dd=[]
            for a,t in ts.items():
                delta=embed(one);delta[3]=1
                al=ext_mul(embed(alpha),delta,a)
                be=hermite_normal_form(ext_mat(delta,a)*bext)
                assert ideal_mul(Iext,be,lambda u,v:ext_mul(u,v,a))==hermite_normal_form(ext_mat(al,a))
                assert abs(ext_mat(al,a).det())==q**3*abs(be.det())
                nu=relative_norm(al,a)
                assert nu==base_mul(base_mul(alpha,base_mul(alpha,alpha)),(1+a)*one)
                eta=ext_mul(ext_pow(al,3,a),ext_inv(embed(nu),a),a)
                assert relative_norm(eta,a)==one
                assert gcd(base_eval(nu),N)==1
                assert ext_eval(al,t)==base_eval(alpha)*ext_eval(delta,t)%N
                assert pow(ext_eval(al,t),3,N)==pow(base_eval(alpha),3,N)*(1+a)*eval_fraction(eta,t)%N
                aa.append(al);dd.append(delta);extensions+=1
            if q==43 and idx==0: fixture=(alpha,aa,dd,ts)
    assert fixture is not None
    alpha,aa,dd,ts=fixture
    # Four public expressions with genuine field-specific factors, but a shared base ratio.
    # Manufactured correlations, not a random supply claim. Old separate valuation rank is 4.
    vals=[];normrows=[]
    for j,(a,t) in enumerate(ts.items()):
        al=aa[j]
        u=ext_pow(al,2,a);v=ext_pow(ext_mul(al,embed(alpha),a),2,a)
        vals.extend([ext_eval(u,t),ext_eval(v,t)])
        ns=[abs(int(ext_mat(z,a).det())) for z in (u,v)]
        ps=sorted(set().union(*(sp.factorint(n) for n in ns)))
        V=sp.Matrix([[sp.factorint(n).get(p,0) for n in ns] for p in ps]);assert V.rank()==2
        assert ext_mul(v,ext_inv(u,a),a)==embed(base_mul(alpha,alpha))
        normrows.append(V)
    assert sp.diag(*normrows).rank()==4
    c=(-1,1,1,-1)
    assert prod(pow(s,e,N) for s,e in zip(vals,c))%N==1
    assert len(set(vals))==4
    roots=[[h for h in range(N) if gcd(h,N)==1 and h*h%N==s] for s in vals]
    assert all(len(rr)==4 for rr in roots)
    freq={}
    for hs in product(*roots):
        z=prod(pow(h,e,N) for h,e in zip(hs,c))%N
        assert z*z%N==1
        g=gcd(z-1,N);freq[g]=freq.get(g,0)+1
    assert sum(n for g,n in freq.items() if 1<g<N)==128
    print('exact trace-Gram ideal reductions:',checked,'extension ideal identities:',extensions)
    print('shared-base fixture: N',N,'public squares',vals,'old separate rank',4,
          'glued relation',c,'CRT gcd counts',sorted(freq.items()))


if __name__=='__main__':
    check_blocks();check_relative_projection();check_actual_ideals()
