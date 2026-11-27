"""Exact power-shift balancing and cross-shift residual cancellation.
Standard library; requires primitive_ratio_lattice.py alongside this file.
Finite checks only, not a uniform smooth-cofactor theorem.
"""
from collections import defaultdict, deque
from fractions import Fraction
from math import gcd, isqrt, prod
from random import Random
from primitive_ratio_lattice import (rect_count, egcd, primitive_pairs,
                                     primes, peel, cancel_large, matrix_rank)


def det(u,v):
    return u[0]*v[1]-u[1]*v[0]


def bound(u):
    return max(map(abs,u))


def first_vector(N,a,H):
    assert 1<=H<N and gcd(a,N)==1 and rect_count(N,a,H,H)>0
    l,r=1,H
    while l<r:
        m=(l+r)//2
        if rect_count(N,a,m,H):r=m
        else:l=m+1
    x=l;y=(a*x+H)%N-H
    assert 0<x<=H and 0<abs(y)<=H and (y-a*x)%N==0
    return x,y


def balance(N,a):
    """Return factor or (j, shifted multiplier, primitive basis)."""
    assert N>=5 and N%2 and gcd(a,N)==1
    h=isqrt((N-1)//3);J=(h*h).bit_length()
    assert 3*h*h<N and 2**J>h*h and 2**J<N
    r=a%N
    last=None
    for j in range(J+1):
        if not rect_count(N,r,h,h):break
        x,y=first_vector(N,r,h)
        g=gcd(x,N)
        if g>1:return g,None
        # Exact rational height escape: consecutive short ratios must double.
        if last is not None:
            assert y*last[0]==2*last[1]*x
        last=(x,y);r=(2*r)%N
    else:raise AssertionError('short-ratio run exceeds rational height limit')
    S=isqrt(N)+1
    l,R=h+1,S
    assert rect_count(N,r,S,S)>0
    while l<R:
        m=(l+R)//2
        if rect_count(N,r,m,m):R=m
        else:l=m+1
    u=first_vector(N,r,l)
    g=gcd(u[0],N)
    if g>1:return g,None
    assert bound(u)==l and gcd(*u)==1 and 4*l*l>N
    d,x,y=egcd(*u);assert d==1
    v=(-N*y,N*x)
    i=max(range(2),key=lambda i:abs(u[i]))
    t=-((Fraction(v[i],u[i])+Fraction(1,2))//1)
    v=tuple(v[k]+t*u[k] for k in range(2))
    assert det(u,v)==N and max(bound(u),bound(v))<=3*S
    assert all((y-r*x)%N==0 for x,y in [u,v])
    return None,(j,r,u,v)


def completion_bound(D):
    """(w+1)*2**w+1, using (w+1)! <= D for distinct prime count."""
    assert D>=1
    w=0;f=1
    while f*(w+2)<=D:
        w+=1;f*=w+1
    return (w+1)*(1<<w)+1


def local_complete(N,a,u,v,D,alpha,beta):
    assert gcd(N,D)==1 and gcd(gcd(alpha,beta),D)==1 and det(u,v)==N
    inv=pow(N,-1,D) if D>1 else 0
    s=((v[1]*alpha-v[0]*beta)*inv-1)%D+1
    t0=((-u[1]*alpha+u[0]*beta)*inv-1)%D+1
    assert gcd(gcd(s,t0),D)==1
    Hc=completion_bound(D)
    for k in range(Hc):
        t=t0+k*D
        if gcd(s,t)==1:break
    else:raise AssertionError('local primitive completion failed')
    assert 1<=s<=D and 1<=t<=D*Hc
    x=s*u[0]+t*v[0];y=s*u[1]+t*v[1]
    assert (x-alpha)%D==0 and (y-beta)%D==0 and (y-a*x)%N==0
    assert gcd(x,y) and N%gcd(x,y)==0
    return x,y,s,t,k+1


def residual_cycle(rows,P):
    """Find a directed cycle of whole residual integers, with exact labels.
    rows are (j,x,y) with x>0, y != 0, and one fixed unshifted multiplier.
    Returns a list of row indices, or None. No residual factorization.
    """
    adj=defaultdict(list)
    endpoints=[]
    for i,(_,x,y) in enumerate(rows):
        left=peel(x,P)[0];right=peel(y,P)[0]
        adj[left].append((right,i));endpoints.append((left,right))
        if left==right:return [i]
    # Iterative DFS. State 1 is on the active path, 2 is finished.
    color={};parent={}
    for s in list(adj):
        if s in color:continue
        color[s]=1;stack=[(s,iter(adj[s]))]
        while stack:
            x,it=stack[-1]
            e=next(it,None)
            if e is None:
                color[x]=2;stack.pop();continue
            y,i=e
            if color.get(y)==1:
                out=[i];z=x
                while z!=y:
                    z,k=parent[z];out.append(k)
                out.reverse()
                assert all(endpoints[k][1]==endpoints[l][0]
                           for k,l in zip(out,out[1:]+out[:1]))
                return out
            if y not in color:
                color[y]=1;parent[y]=(x,i);stack.append((y,iter(adj[y])))
    return None


def test_balance():
    count=fac=local=skew=shifted=maxj=0
    rng=Random(5117)
    for N in (5,7,9,15,21,35,77,143,221,899,1009,47053):
        for a in range(1,N) if N<=1009 else (rng.randrange(1,N) for _ in range(300)):
            if gcd(a,N)!=1:continue
            d,result=balance(N,a)
            if d:
                assert 1<d<N and N%d==0;fac+=1;continue
            j,r,u,v=result;count+=1;shifted+=j>0;maxj=max(maxj,j)
            h=isqrt((N-1)//3)
            assert not any(abs((r*x+h)%N-h)<=h for x in range(1,h+1))
            assert r==a*pow(2,j,N)%N
            for D in (1,2,5,6,15,21,30,77):
                if gcd(D,N)>1:continue
                alpha,beta=rng.randrange(D),rng.randrange(D)
                if gcd(gcd(alpha,beta),D)>1:continue
                x,y,s,t,_=local_complete(N,r,u,v,D,alpha,beta)
                assert gcd(s,t)==1 and x==s*u[0]+t*v[0] and y==s*u[1]+t*v[1]
                local+=1
    big=0
    for _ in range(150):
        N=rng.randrange(1<<200,1<<201)|1;a=rng.randrange(1,N)
        if gcd(a,N)!=1:continue
        d,res=balance(N,a)
        if d:assert 1<d<N and N%d==0;continue
        j,r,u,v=res
        assert not rect_count(N,r,isqrt((N-1)//3),isqrt((N-1)//3))
        D=30030
        if gcd(D,N)==1:
            x,y,s,t,_=local_complete(N,r,u,v,D,0,1)
            assert x%D==0 and y%D==1 and gcd(s,t)==1
        big+=1
    print('balanced lattice checks:',count,'proper factor exits',fac,'nonzero shifts',shifted,'max shift',maxj)
    print('local primitive CRT completion checks:',local,'additional 201-bit balanced lattices',big)


def cross_shift_fixture():
    # Find an example with no successful individual residual graph,
    # but a cycle using more than one shifted multiplier.
    for N in (899,1763,2491,3233,10403,47053,100160063):
        S=isqrt(N)+1
        for H in (S, 2*S, 3*S):
            if H>=N:continue
            P=primes(max(2,2*H*H//N))
            if any(N%p==0 for p in P):continue
            J=(isqrt((N-1)//3)**2).bit_length()
            for q in P:
                T=1
                while q**T<=N*H*H:T+=1
                for T in range(T,T+8):
                    a=pow(q,T,N);rows=[];ok=True
                    for j in range(J+1):
                        d,pairs,_=primitive_pairs(N,a*pow(2,j,N)%N,H,H)
                        if d or (pairs and cancel_large(pairs,P) is not None):
                            ok=False;break
                        rows.extend((j,x,y) for x,y in pairs)
                    if not ok:continue
                    cyc=residual_cycle(rows,P)
                    if cyc is None:continue
                    chosen=[rows[i] for i in cyc]
                    assert len({j for j,x,y in chosen})>1
                    left=prod(x for j,x,y in chosen);right=prod(y for j,x,y in chosen)
                    assert peel(left,P)[0]==peel(right,P)[0]
                    assert (pow(q,T*len(chosen),N)*pow(2,sum(j for j,x,y in chosen),N)*left-right)%N==0
                    print('cross-shift-only fixture:',N,'q',q,'T',T,'H',H,'base bound',P[-1],'shifts',J+1,'rows',len(rows),'cycle',chosen)
                    return
    print('No cross-shift-only fixture in tested range; no claim made')


if __name__=='__main__':
    test_balance();cross_shift_fixture()
