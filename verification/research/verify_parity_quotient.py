#!/usr/bin/env python3
"""Exact binary quotient test for integer-canceled anchor batches.
Requires SymPy 1.14. Finite tests, not a batch-supply theorem.
"""
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp


def kernel(A):
    D,S,T=smith_normal_decomp(A,domain=sp.ZZ)
    assert S*A*T==D and abs(S.det())==abs(T.det())==1
    r=sum(D[i,i]!=0 for i in range(min(D.shape)))
    K=T[:,r:];assert A*K==sp.zeros(A.rows,K.cols)
    return K


def mod2_image(K,k):
    out={0}
    for j in range(K.cols):
        x=sum((int(K[i,j])&1)<<i for i in range(k))
        out|={y^x for y in out}
    return out


def in_lattice(H,v):
    if H.cols==0:return v==sp.zeros(H.rows,1)
    try:
        sol,params=H.gauss_jordan_solve(v)
    except ValueError:
        return False
    assert params.rows==0
    return all(a.q==1 for a in sol)


def quotient_parities(V,C):
    H=hermite_normal_form((2*V).row_join(C));k=V.cols
    return {i for i in range(1<<k)
            if in_lattice(H,V*sp.Matrix([(i>>j)&1 for j in range(k)]))}


def main():
    rng=Random(1701);checks=parities=gains=plateaux=0
    for _ in range(200):
        m,k,l,n,h=(rng.randrange(1,6),rng.randrange(2,7),rng.randrange(1,5),
                   rng.randrange(1,5),rng.randrange(1,5))
        def mat(r,s):return sp.Matrix(r,s,[rng.randrange(-5,6) for i in range(r*s)])
        V,C,Co,Cn=mat(m,k),mat(m,l),mat(m,h),mat(n,h)
        for j in range(l):
            if rng.randrange(2):C[:,j]*=2
        if h>1 and rng.randrange(2):Cn[:,1]=Cn[:,0]
        old=mod2_image(kernel(V.row_join(C)),k)
        assert old==quotient_parities(V,C)
        H=Co*kernel(Cn)
        new=mod2_image(kernel(V.row_join(C).row_join(H)),k)
        VV=V.col_join(sp.zeros(n,k));CC=C.col_join(sp.zeros(n,l));AA=Co.col_join(Cn)
        full=mod2_image(kernel(VV.row_join(CC).row_join(AA)),k)
        assert new==full==quotient_parities(V,C.row_join(H)) and old<=new
        # Integer intersection: projection of the integer kernel of [V C -H].
        J=kernel(V.row_join(C).row_join(-H));B=V.row_join(C)*J[:k+l,:]
        denom=hermite_normal_form((2*V).row_join(C))
        witness=any(not in_lattice(denom,B[:,j]) for j in range(B.cols))
        assert witness==(len(new)>len(old))
        gains+=witness
        r0=V.row_join(C).rank()-C.rank();C2=C.row_join(H)
        r1=V.row_join(C2).rank()-C2.rank()
        plateaux+=int(witness and r0==r1)
        parities+=2*(1<<k);checks+=1
    # A parity gain at exactly constant rational quotient rank.
    V=sp.Matrix([[1]]);C=sp.Matrix([[2]]);H=sp.Matrix([[1]])
    assert quotient_parities(V,C)=={0} and quotient_parities(V,C.row_join(H))=={0,1}
    assert V.row_join(C).rank()-C.rank()==0
    print('integer anchor batches:',checks,'binary membership comparisons:',parities,
          'strict parity gains:',gains,'rational-rank plateau gains:',plateaux,
          'explicit even-factor repair: passed')


if __name__=='__main__':main()
