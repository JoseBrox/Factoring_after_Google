"""Exact global factor-free elimination across target powers and dyadic shifts.
Finite experiment; no uniform success theorem. Standard library only.
"""
from fractions import Fraction as Q
from math import gcd, isqrt, lcm, prod
from primitive_ratio_lattice import primitive_pairs, primes, peel, factorfree_columns, rect_count


def sub(v,w,t):
    for k,a in w.items():
        v[k]=v.get(k,0)-t*a
        if not v[k]:del v[k]


def pool_matrix(rows,P):
    # rows are (target prime, positive exponent, dyadic shift, x, y).
    n=len(rows);rx=[];ry=[];small=[]
    for q,T,j,x,y in rows:
        a,u=peel(x,P);b,v=peel(y,P)
        rx.append(a);ry.append(b)
        w={p:u.get(p,0)-v.get(p,0)+T*(p==q)+j*(p==2) for p in P}
        small.append(w)
    basis=list(factorfree_columns(rx+ry).values())
    R=len(basis);mat=[]
    for i,w in enumerate(small):
        v={k:e[i]-e[i+n] for k,e in enumerate(basis) if e[i]!=e[i+n]}
        v.update({R+j:w[p] for j,p in enumerate(P) if w[p]})
        mat.append(v)
    return R,mat


def exact_eliminate(mat):
    piv={}
    for i,row in enumerate(mat):
        v={j:Q(a) for j,a in row.items() if a};c={i:Q(1)}
        while v:
            j=min(v);a=v[j]
            if j not in piv:
                piv[j]=({k:z/a for k,z in v.items()}, {k:z/a for k,z in c.items()})
                break
            r,d=piv[j];sub(v,r,a);sub(c,d,a)
    return piv


def coordinate_relation(piv,j):
    v={j:Q(1)};c={}
    while v:
        k=min(v)
        if k not in piv:return None
        a=v[k];r,d=piv[k];sub(v,r,a);sub(c,d,-a)
    E=lcm(*(z.denominator for z in c.values()))
    return E,{i:int(z*E) for i,z in c.items()}


def pool(N,rows,P):
    assert all((pow(q,T,N)*pow(2,j,N)*x-y)%N==0 and gcd(x*y,N)==1 for q,T,j,x,y in rows)
    R,mat=pool_matrix(rows,P);piv=exact_eliminate(mat)
    residual_rank=sum(i<R for i in piv);rank=sum(i>=R for i in piv)
    assert rank<=len(P)
    coords={}
    for k,p in enumerate(P):
        got=coordinate_relation(piv,R+k)
        if got is None:continue
        E,c=got
        w={}
        for i,z in c.items():sub(w,mat[i],-z)
        assert w=={R+k:E}
        assert pow(p,2*E,N)==1
        coords[p]=2*E
    return rank,residual_rank,coords


def collect(N,H,P,extras=1):
    J=(isqrt((N-1)//3)**2).bit_length();data={}
    for q in P:
        T=1
        while q**T<=N*H*H:T+=1
        rows=[]
        for E in range(T,T+extras):
            a=pow(q,E,N)
            for j in range(J+1):
                d,vs,_=primitive_pairs(N,a*pow(2,j,N)%N,H,H)
                if d:return d,{}
                rows.extend((q,E,j,x,y) for x,y in vs)
        data[q]=rows
    return None,data


def split(N,coords):
    for p,E in coords.items():
        z=E
        while z%2==0:z//=2
        while z<=E:
            h=gcd(pow(p,z,N)-1,N)
            if 1<h<N:return h
            z*=2
    return None


def tests():
    # In each fixture compare the dimension of the sum of per-target
    # small-prime relation spaces with the pooled small-prime space.
    tested=0;early=0;improvements=0;full_fixture=None
    for N in (899,1763,2491,3233,10403,47053,100160063,1000036000099):
        S=isqrt(N)+1
        for mul in (1,2,3):
            H=mul*S
            if H>=N:continue
            P=primes(max(2,2*H*H//N))
            if any(N%p==0 for p in P):continue
            d,data=collect(N,H,P)
            if d:
                assert 1<d<N and N%d==0;early+=1;continue
            allrows=sum(data.values(),[])
            rank,R,coords=pool(N,allrows,P)
            # Compute exact combined per-target row-space dimension using
            # separate eliminations; each yields a true subspace of pooled.
            separate=[];individual_ranks=[]
            for q,rows in data.items():
                r,mat=pool_matrix(rows,P);piv=exact_eliminate(mat)
                rr=[{k-r:a for k,a in v.items()} for j,(v,c) in piv.items() if j>=r]
                individual_ranks.append(len(rr));separate+=rr
            srank=len(exact_eliminate(separate))
            assert srank<=rank
            tested+=1;improvements+=srank<rank
            if srank<rank:
                fac=split(N,coords)
                print('pool gain:',N,'H',H,'base',P,'rows',len(allrows),'separate rank',srank,'pooled rank',rank,'residual rank',R,'factor',fac)
                if rank==len(P) and fac and full_fixture is None:
                    full_fixture=(N,H,P,len(allrows),srank,rank,individual_ranks,fac)
            if full_fixture and tested>=8:break
        if full_fixture and tested>=8:break
    print('pooled versus separate exact rank:',tested,'comparisons,',improvements,'strict gains,',early,'proper-factor exits')
    assert full_fixture is not None
    print('full-rank fixture:',full_fixture)
    N,H,P,_,_,_,_,fac=full_fixture
    d,data=collect(N,H,P);assert d is None
    rows=sum(data.values(),[]);h=isqrt((N-1)//3)
    for name,keep in [('unshifted',lambda r:r[2]==0),
                      ('balanced_only',lambda r:not rect_count(N,pow(r[0],r[1],N)*pow(2,r[2],N)%N,h,h))]:
        selected=[r for r in rows if keep(r)]
        rank,rr,coords=pool(N,selected,P)
        factor=split(N,coords)
        if name=='unshifted':assert rank==0 and factor is None
        else:assert rank==len(P) and factor is not None and 1<factor<N and N%factor==0
        print(name,len(selected),'pooled rank',rank,'residual rank',rr,'certificate exponent bits',max((e.bit_length() for e in coords.values()),default=0),'factor',factor)


if __name__=='__main__':tests()
