"""Finite exact checks of the norm normalization and common-order gluing.
These fixtures do not establish uniform coverage. Requires SymPy and
factor_refinement.py in the same directory.
"""
from math import gcd, lcm
import sympy as S
from sympy.ntheory.modular import crt
from factor_refinement import Order

X=S.symbols('X')

def field_order(f):
    return Order(list(reversed(S.Poly(f,X).all_coeffs())))

def power(K,g,e):
    a=K.one
    while e:
        if e&1: a=K.mul(a,g)
        g=K.mul(g,g);e//=2
    return a

def gluing_characteristic(K1,K2):
    # D = A1/(f2(theta1)); C is the least positive integer in this ideal.
    a=K1.reduce(K2.f)
    inv=K1.matrix(a).inv()*K1.one
    C=lcm(*(int(x.q) for x in inv))
    assert all(x.q==1 for x in C*inv)
    assert K1.mul(a,C*inv)==C*K1.one
    return C,a

def normalized_matrix(orders,polys,ell):
    d=orders[0].d
    # First-field signed norm: rational denominator in both fields.
    norms=[int(orders[0].matrix(orders[0].reduce(g)).det()) for g in polys]
    assert all(norms)
    blocks=[]
    for i,K in enumerate(orders):
        vals=[K.reduce(g) for g in polys]
        scalars=[K.reduce([a]) for a in norms]
        C,F,_,_=K.refine(vals+scalars+[K.reduce([ell])])
        r=len(vals)
        M=d*F[:,:r]-F[:,r:2*r]
        target=S.zeros(F.rows,1) if i==0 else -d*F[:,-1]
        blocks.append(M.row_join(target))
    return S.Matrix.vstack(*blocks)

def success_fixture():
    N,ell=15,2
    f1=(X-1)*(X-46)-16
    f2=(X-1)*(X-46)-1
    K1,K2=map(field_order,(f1,f2))
    gs=[[-1,1],[-46,1],[3],[7]]
    M=normalized_matrix((K1,K2),gs,ell)
    assert M[:,2:4]==S.zeros(M.rows,2) # diagonal rational columns vanish
    assert M*S.Matrix([-1,-1,0,0,4])==S.zeros(M.rows,1)
    # Norm-normalized relation also holds as actual field equality.
    d=K1.d
    for i,K in enumerate((K1,K2)):
        g,h=map(K.reduce,gs[:2])
        nu=int(K1.matrix(K1.reduce(gs[0])).det()*K1.matrix(K1.reduce(gs[1])).det())
        a=power(K,K.mul(g,h),d)/nu
        tau=K.one if i==0 else K.one/ell**d
        assert a==power(K,tau,4)
    print('positive fixture: normalization kills rational columns; target relation verified exactly')

def private_fixture(r=5):
    N,ell,m=77,5,0
    f1=S.Poly((X-5)*(X-230)+5,X)
    f2=S.Poly((X-5)*(X-277)+1,X)
    assert all(f.is_irreducible and S.discriminant(f)>0 and f.eval(m)%N==0 for f in (f1,f2))
    K1,K2=map(field_order,(f1,f2));d=K1.d
    C,a=gluing_characteristic(K1,K2)
    res=abs(int(S.resultant(f1,f2)))
    assert res%C==0 and C%N==0 and gcd(ell,C)==1
    assert pow(ell,S.n_order(ell,C),C)==1
    E=int(S.n_order(ell,C))
    assert E==S.n_order(ell,N) or E%S.n_order(ell,N)==0
    g1=K1.reduce([-5,1]);g2=K2.reduce([-5,1])
    assert K1.matrix(g1).det()==ell and K2.matrix(g2).det()==1
    xi1=power(K1,g1,d)/ell;xi2=power(K2,g2,d)
    assert all(x.q==1 for x in xi1) and K1.matrix(xi1).det()==1 and K2.matrix(xi2).det()==1
    # Exact gluing test via polynomial representatives, without evaluating a huge power:
    # xi1 = g^d/ell, xi2 = g^d; ratio in D is ell^{-1}.
    h=K1.reduce([-5,1]);barxi2=power(K1,h,d)
    assert K1.mul(xi1,K1.reduce([ell]))==barxi2
    assert gcd(int(K1.matrix(barxi2).det()),C)==1
    # Check the first congruence of the actual pair in the fiber product.
    inverse=K1.matrix(a).inv()
    v=w=K1.one
    for j in range(1,E+1):
        v=K1.mul(v,xi1).applyfunc(lambda q: int(q)%C)
        w=K1.mul(w,barxi2).applyfunc(lambda q: int(q)%C)
        assert all(q.q==1 for q in inverse*(v-w))==(j==E)
    print('gluing fixture: N=%d resultant=%d characteristic=%d target order=%d' %(N,res,C,E))
    bad=N*ell*res*abs(int(S.discriminant(f1)*S.discriminant(f2)))
    ps=[];roots=[];avoids=[]
    for p0 in S.primerange(2*d+1,10000):
        p=int(p0)
        if bad%p==0:continue
        hits=[u for u in range(p) if f1.eval(u)%p==0 and f2.eval(u)%p!=0]
        if not hits:continue
        avoids.append(next(u for u in range(p) if f1.eval(u)%p and f2.eval(u)%p))
        roots.append(hits[0]);ps.append(p)
        if len(ps)==r:break
    assert len(ps)==r
    bs=[]
    for j in range(r):
        b=int(crt([N]+ps,[5]+[roots[k] if k==j else avoids[k] for k in range(r)])[0])
        assert gcd(b,N)==1 and f1.eval(b)%ps[j]==0 and f2.eval(b)%ps[j]!=0
        bs.append(b)
    for j,p in enumerate(ps):
        for k,b in enumerate(bs):
            if k!=j:assert f1.eval(b)%p and f2.eval(b)%p
    gs=[[-5,1]]+[[-b,1] for b in bs]+[[2],[3],[13]]
    # Diagonal constants may contain the private primes: normalization removes them.
    M=normalized_matrix((K1,K2),gs,ell)
    assert M[:,1+r:1+r+3]==S.zeros(M.rows,3)
    A=M[:,:r+1];t=M[:,-1]
    assert A.rank()==r+1 and A.row_join(t).rank()==r+1
    sol=A.gauss_jordan_solve(-t)[0]
    assert sol[0]!=0 and all(x==0 for x in sol[1:])
    # The sole valuation solution uses g_1; its second-field projected log
    # is nonzero, because g_1 is a norm-one unit but is neither +1 nor -1.
    assert K2.matrix(g2).det()==1 and g2!=K2.one and g2!=-K2.one
    print('negative fixture: %d private-prime marks, normalized valuation rank %d, target valuation solvable, log cancellation impossible' %(r,A.rank()))

if __name__=='__main__':
    success_fixture();private_fixture()
