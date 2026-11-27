"""Exact batch affine residual dependence; finite checks only.
Uses the previous factor-free and lattice routines, standard library.
"""
from fractions import Fraction as Q
from random import Random
from math import gcd,isqrt,lcm
from two_primary_pool import normalized_basis
from pooled_shift_relations import exact_eliminate
from primitive_ratio_lattice import matrix_rank,primitive_pairs,peel


def affine_dependency(old,new):
    """Return coeffs with sum_new=1 and zero residual, or None."""
    data=old+new;r=len(old);m=len(data)
    D=normalized_basis([x for x,y in data]+[y for x,y in data]);keys=list(D)
    rows=[[D[z][i]-D[z][i+m] for z in keys]+[int(i>=r)] for i in range(m)]
    t=len(keys);piv=exact_eliminate([{j:Q(z) for j,z in enumerate(v) if z} for v in rows])
    if t not in piv:return None,rows
    v,c=piv[t];assert v=={t:Q(1)}
    z=[c.get(i,Q(0)) for i in range(m)]
    assert sum(z[r:])==1
    assert all(sum(z[i]*rows[i][j] for i in range(m))==int(j==t) for j in range(t+1))
    return z,rows


def test_abstract():
    rng=Random(4891);checked=0;found=0
    for _ in range(250):
        r=rng.randrange(0,7);s=rng.randrange(1,9);data=[]
        for j in range(r+s):
            x,y=rng.randrange(1,1000),rng.randrange(1,1000);g=gcd(x,y);data.append((x//g,y//g))
        z,rows=affine_dependency(data[:r],data[r:]);m=len(rows[0])-1
        assert (z is not None)==(matrix_rank(rows,m+1)>matrix_rank([row[:-1] for row in rows],m))
        if z is not None:found+=1
        checked+=1
    # Deterministic signed affine dependence with no nonnegative cancellation.
    z,_=affine_dependency([],[(1,3),(1,9)])
    assert z==[Q(2),Q(-1)]
    print('batch affine rank comparisons:',checked,'positive cases',found)


def test_signed_fixture():
    N=77;T=14;raw=[(7,4,-3),(2,1,9)]
    residual=[];A=[]
    for j,x,y in raw:
        assert (pow(2,T+j,N)*x-y)%N==0
        u,v=peel(x,[2]);s,t=peel(y,[2]);residual.append((u,s));A.append(T+j+v.get(2,0)-t.get(2,0))
    z,_=affine_dependency([],residual)
    assert z==[Q(2),Q(-1)] and all(y>x for x,y in residual)
    E=sum(a*v for a,v in zip(z,A));assert E==30
    assert pow(2,int(E),N)==1
    f=gcd(pow(2,int(E)//2,N)-1,N);assert 1<f<N and N%f==0
    print('signed-only batch:',N,'raw',raw,'residual',residual,'coefficients',list(map(str,z)),'E',E,'factor',f)


def adaptive_batch(N,H):
    # One full batch from an empty pool; q=2,w=1. All candidate rows
    # share the same T, with a proved upper bound M on the batch size.
    J=(isqrt((N-1)//3)**2).bit_length();M=(J+1)*(1+18*H*H//N)
    h=H.bit_length();D=2*h+1;bound=M*D**M
    T=1+bound*(J+2*h)
    a=pow(2,T,N);raw=[];res=[];A=[]
    for j in range(J+1):
        f,pairs,_=primitive_pairs(N,a*pow(2,j,N)%N,H,H)
        if f:return f,0,0,T.bit_length(),None
        for x,y in pairs:
            u,v=peel(x,[2]);s,t=peel(y,[2]);res.append((u,s));A.append(T+j+v.get(2,0)-t.get(2,0));raw.append((j,x,y))
    assert len(raw)<=M
    # Deliberately discard individually smooth rows in this finite test,
    # to test whether a signed batch dependence can achieve the gain.
    keep=[i for i,(x,y) in enumerate(res) if (x,y)!=(1,1)]
    res=[res[i] for i in keep];A=[A[i] for i in keep];raw=[raw[i] for i in keep]
    if not res:return None,len(raw),0,T.bit_length(),None
    z,rows=affine_dependency([],res)
    if z is None:return None,len(raw),matrix_rank([r[:-1] for r in rows],len(rows[0])-1),T.bit_length(),None
    k=lcm(*(v.denominator for v in z));c=[int(v*k) for v in z]
    E=sum(i*j for i,j in zip(c,A));assert E>0
    assert all(sum(c[i]*rows[i][j] for i in range(len(rows)))==0 for j in range(len(rows[0])-1))
    assert pow(2,2*E,N)==1
    f=None;s=2*E
    while s%2==0:s//=2
    while s<=2*E:
        g=gcd(pow(2,s,N)-1,N)
        if 1<g<N:f=g;break
        s*=2
    return f,len(raw),matrix_rank([r[:-1] for r in rows],len(rows[0])-1),T.bit_length(),(sum(v!=0 for v in c),E.bit_length())


if __name__=='__main__':
    test_abstract();test_signed_fixture()
    for N in (47053,100160063,1000036000099):
        out=adaptive_batch(N,3*(isqrt(N)+1))
        if out[0]:assert 1<out[0]<N and N%out[0]==0
        print('separated full batch:',N,'factor/rows/residual rank/T bits/gain support and bits',out)
