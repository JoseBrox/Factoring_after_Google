"""Exact adaptive exponent separation and residual recycling.
Standard library; imports the previous exact lattice routines.
No assumption of uniform half-scale coverage is made.
"""
from fractions import Fraction as Q
from math import factorial, gcd, isqrt, lcm
from random import Random
from primitive_ratio_lattice import (primitive_pairs, primes, peel,
                                     factorfree_columns, matrix_rank)
from target_power_balance import balance, local_complete, completion_bound
from pooled_shift_relations import exact_eliminate, coordinate_relation, sub


def base_image(N,P,A):
    z=1
    for p,a in zip(P,A):z=z*pow(p,a,N)%N
    return z


def norm1(A):return sum(map(abs,A))


def annihilator(rows,m):
    piv=exact_eliminate([{i:Q(a) for i,a in enumerate(row) if a} for row in rows])
    if len(piv)==m:return None
    w=[Q(0)]*m;w[next(j for j in range(m) if j not in piv)]=Q(1)
    for j in sorted(piv,reverse=True):
        v,_=piv[j];w[j]=-sum(a*w[i] for i,a in v.items() if i!=j)
    assert all(sum(a*b for a,b in zip(row,w))==0 for row in rows)
    q=max(range(m),key=lambda j:abs(w[j]))
    if w[q]<0:w=[-a for a in w]
    W=w[q];return q,[a/W for a in w]


def row_vectors(residuals):
    m=len(residuals)
    basis=factorfree_columns([x for x,y in residuals]+[y for x,y in residuals])
    rows=[{} for _ in residuals]
    for j,v in enumerate(basis.values()):
        for i in range(m):
            if v[i]!=v[i+m]:rows[i][j]=Q(v[i]-v[i+m])
    return rows,basis


def dependency(old,new):
    rows,basis=row_vectors(old+[new]);piv=exact_eliminate(rows[:-1])
    assert len(piv)==len(old)
    v=rows[-1].copy();c={}
    while v:
        j=min(v);a=v[j]
        if j not in piv:return None,len(basis)
        r,d=piv[j];sub(v,r,a);sub(c,d,-a)
    for j in range(len(basis)):
        assert rows[-1].get(j,0)==sum(a*rows[i].get(j,0) for i,a in c.items())
    return c,len(basis)


def dot(A,w):return sum(a*z for a,z in zip(A,w))


def dual_solution(old,w):
    rows,basis=row_vectors([(x,y) for A,x,y,s in old]) if old else ([],{})
    piv=exact_eliminate(rows);assert len(piv)==len(old)
    lam=[Q(0)]*len(basis)
    for j in sorted(piv,reverse=True):
        v,c=piv[j];rhs=sum(a*dot(old[i][0],w) for i,a in c.items())
        lam[j]=rhs-sum(a*lam[k] for k,a in v.items() if k!=j)
    for i,row in enumerate(rows):
        assert sum(a*lam[j] for j,a in row.items())==dot(old[i][0],w)
    return max(map(abs,lam),default=Q(0))


def step(N,P,H,old,pure,attempt,local=False,dual=False):
    """Return factor or (normalized row, dependency, pure rank gain, statistics).
    old entries (A, x_res, y_res, sign); residuals form an independent family.
    pure entries integral signed small-base relations.
    """
    m=len(P);r=len(old);found=annihilator(pure,m)
    assert found is not None
    q,w=found;assert P[0]==2 and w[q]==1
    J=(isqrt((N-1)//3)**2).bit_length();nH=H.bit_length()
    # Recycle one previous residual (round-robin), using no large coordinate.
    A0=[0]*m;shift_factor=1;sign0=1
    if old:
        A0,x0,y0,sign0=old[attempt%r];A0=A0[:]
        shift_factor=y0*pow(x0,-1,N)%N
        assert shift_factor==sign0*base_image(N,P,A0)%N
    D=(r+1 if r else 1) # exact crude Cramer bound, not a heuristic
    D=factorial(D)*(2*nH+1)**D
    sep=D*sum(norm1(row[0]) for row in old)
    if dual:sep=2*nH*dual_solution(old,w)
    T=1+(norm1(A0)+J+2*nH+sep)//1
    a=pow(P[q],T,N)*shift_factor%N
    d,result=balance(N,a)
    if d:return d,None
    j,c,u,v=result
    assert j<=J and c==pow(2,j,N)*a%N
    oldres=[(x,y) for A,x,y,s in old]
    if local:
        S=isqrt(N)+1
        # Prefer an actual old residual factor, if the proven CRT budget fits.
        _,bs=row_vectors(oldres) if oldres else ([],{})
        choices=[(z,True) for z in bs if 3*S*z*(1+completion_bound(z))<=H]
        if not choices:choices=[(p,False) for p in P if 3*S*p*(1+completion_bound(p))<=H]
        if choices:
            mod,shared=choices[attempt%len(choices)]
            x,y,_,_,_=local_complete(N,c,u,v,mod,0,1)
            assert x%mod==0 and y%mod==1
        else:
            x,y=u;mod=1;shared=False
        if x<0:x,y=-x,-y
        g=gcd(x,N)
        if g>1:
            assert g<N and N%g==0;return g,None
        assert gcd(x,y)==1 and gcd(y,N)==1 and 0<x<=H and 0<abs(y)<=H
        candidates=[(x,y)]
    else:
        d,candidates,_=primitive_pairs(N,c,H,H)
        if d:return d,None
        assert candidates
        mod=1;shared=False
    best=None;best_overlap=-1
    # In the enumeration variant inspect the entire balanced rectangle until
    # a genuine residual dependence is found. If none, choose maximal overlap
    # with the already exposed residual support, not maximal base rank.
    Rprod=1
    for x,y in oldres:Rprod*=x*y
    for x,y in candidates:
        assert (c*x-y)%N==0
        rx,px=peel(x,P);ry,py=peel(y,P)
        dep,nb=dependency(oldres,(rx,ry))
        score=gcd(rx*ry,Rprod).bit_length()
        if dep is not None or score>best_overlap:
            best=(x,y,rx,ry,px,py,dep,nb);best_overlap=score
        if dep is not None:break
    x,y,rx,ry,px,py,dep,nb=best
    A=[A0[i]+T*(i==q)+j*(p==2)+px.get(p,0)-py.get(p,0) for i,p in enumerate(P)]
    sig=sign0*(1 if y>0 else -1)
    assert base_image(N,P,A)*rx*pow(ry,-1,N)%N==sig%N
    assert dot(A,w)>sep
    row=(A,rx,ry,sig)
    if dep is None:
        # Genuine independent residual direction; no claim of rank increase.
        return None,(row,None,None,(mod,shared,T.bit_length(),nb))
    assert all(abs(z)<=D for z in dep.values())
    den=lcm(*(a.denominator for a in dep.values()))
    gain=[den*A[k]-sum(int(den*z)*old[i][0][k] for i,z in dep.items()) for k in range(m)]
    assert dot(gain,w)>0
    # Independent exact residual-product cancellation check without factoring.
    rr,basis=row_vectors(oldres+[(rx,ry)])
    for j0 in range(len(basis)):
        assert den*rr[-1].get(j0,0)==sum(int(den*z)*rr[i].get(j0,0) for i,z in dep.items())
    assert base_image(N,P,[2*a for a in gain])==1
    return None,(row,dep,gain,(mod,shared,T.bit_length(),nb))


def recover(N,P,pure):
    piv=exact_eliminate([{i:Q(z) for i,z in enumerate(row) if z} for row in pure]);covered={}
    for j,p in enumerate(P):
        got=coordinate_relation(piv,j)
        if got is None:continue
        E,c=got;assert pow(p,2*E,N)==1
        covered[p]=2*E
        z=2*E
        while z%2==0:z//=2
        while z<=2*E:
            d=gcd(pow(p,z,N)-1,N)
            if 1<d<N:return d,len(piv),covered
            z*=2
    return None,len(piv),covered


def run(N,P,H,limit,local=False,stop_split=True,dual=False):
    assert H<N and H>=isqrt(N)+1 and all(gcd(p,N)==1 for p in P)
    old=[];pure=[];overlaps=0;prescriptions=0;maxbits=0;d=None
    for attempt in range(limit):
        d,result=step(N,P,H,old,pure,attempt,local,dual)
        if d:break
        row,dep,gain,(mod,shared,bits,nb)=result
        maxbits=max(maxbits,bits);prescriptions+=mod>1;overlaps+=shared
        if gain is None:old.append(row)
        else:pure.append(gain)
        assert len(old)+len(pure)==attempt+1
        assert matrix_rank([[z.get(j,0) for j in range(nb)] for z in row_vectors([(x,y) for A,x,y,s in old])[0]],nb)==len(old) if old and gain is None else True
        assert matrix_rank(pure,len(P))==len(pure)
        factor,rank,coords=recover(N,P,pure)
        if factor and stop_split:d=factor;break
        if rank==len(P):d=factor;break
    if d:assert 1<d<N and N%d==0
    print('adaptive dual' if dual else 'adaptive Cramer',N,'base',P[-1],'H',H,'rows',len(old)+len(pure),'residual rank',len(old),'base rank',len(pure),'CRT',prescriptions,'shared CRT',overlaps,'max exponent bits',maxbits,'factor',d,flush=True)
    return d,len(old),len(pure),prescriptions,overlaps


def test_cramer():
    # Exact arithmetic test of the key implication on abstract sparse residual
    # matrices. The residue values are actual integer products, not random floats.
    rng=Random(941);ps=[11,13,17,19,23,29,31,37,41,43];checked=0
    for _ in range(100):
        r=rng.randrange(1,8);old=[]
        while len(old)<r:
            v=[rng.randrange(-3,4) for p in ps]
            x=y=1
            for p,e in zip(ps,v):
                if e>0:x*=p**e
                if e<0:y*=p**(-e)
            if dependency(old,(x,y))[0] is None:old.append((x,y))
        c=[rng.randrange(-5,6) for i in range(r)]
        x=y=1
        for (u,v),z in zip(old,c):
            if z>=0:x*=u**z;y*=v**z
            else:x*=v**(-z);y*=u**(-z)
        g=gcd(x,y);x//=g;y//=g
        dep,_=dependency(old,(x,y));assert dep is not None
        assert all(dep.get(i,0)==z for i,z in enumerate(c))
        H=max([x,y]+[z for pair in old for z in pair]);D=factorial(r+1)*(2*H.bit_length()+1)**(r+1)
        assert all(abs(z)<=D for z in dep.values())
        checked+=1
    print('Cramer dependency checks:',checked,flush=True)


if __name__=='__main__':
    test_cramer()
    for dual in (False,True):
        for N in (47053,100160063,1000036000099):
            P=primes(17);S=isqrt(N)+1
            run(N,P,3*S,40,dual=dual)
        # Test true local CRT choices on larger boxes without enumerating the boxes.
        for N in (100160063,1000036000099):
            run(N,primes(7),min(N-1,5000*(isqrt(N)+1)),25,local=True,dual=dual)
