#!/usr/bin/env python3
"""Exact same-square-coset tag collision checks for finite rational fixtures.
Factoring of tiny integer representatives is deliberate; no asymptotic claim.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, prod
from random import Random
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp


def solve_span(A, v):
    if A.cols == 0:
        return [] if not any(v) else None
    D,S,T=smith_normal_decomp(A,domain=sp.ZZ)
    assert S*A*T==D
    w=S*v;y=sp.zeros(A.cols,1)
    for i in range(A.rows):
        d=int(D[i,i]) if i<min(D.shape) else 0
        if d:
            if int(w[i])%d:return None
            y[i]=int(w[i])//d
        elif w[i]:return None
    z=T*y;assert A*z==v
    return [int(a) for a in z]


def main():
    rng=Random(1701); comparisons=corematches=maskchecks=rootschecks=0
    for N in (77,899,1189,315):
        U=[u for u in range(1,N) if gcd(u,N)==1]
        S=sorted({u*u%N for u in U});sset=set(S)
        remain=set(U);cosets=[]
        while remain:
            u=min(remain);C={u*s%N for s in S}
            assert C<=remain;remain-=C;cosets.append(C)
        ff={u:sp.factorint(u) for u in U}
        full=sorted(set().union(*(set(f) for f in ff.values())))
        assert all(p in U for p in full)  # all prime label axes really occur
        for B in (3,7):
            base=[p for p in full if p<=B]
            tag={u:tuple((p,e) for p,e in sorted(ff[u].items()) if p>B) for u in U}
            v={u:tuple(ff[u].get(p,0) for p in base) for u in U}
            joint=Counter((i,tag[u]) for i,C in enumerate(cosets) for u in C)
            tags=Counter(tag.values())
            G=Fraction(sum(n*n for n in joint.values()),len(U)*len(S))
            independent=Fraction(sum(n*n for n in tags.values()),len(U)**2)
            assert G>=independent>=Fraction(1,len(tags))
            pairs=defaultdict(list);ds=set();count=0
            for s in S:
                for u in U:
                    w=u*s%N;comparisons+=1
                    if tag[u]!=tag[w]:continue
                    z=tuple(b-a for a,b in zip(v[u],v[w]))
                    # No unmatched prime factor, and exact rational evaluation.
                    assert all(ff[u].get(p,0)==ff[w].get(p,0) for p in full if p>B)
                    assert prod(pow(p,e,N) for p,e in zip(base,z))%N==s
                    pairs[s].append((u,z));ds.add(z);count+=1
            assert G==Fraction(count,len(U)*len(S));corematches+=count
            diff=sp.Matrix.hstack(*(sp.Matrix(z) for z in ds))
            dr=diff.rank();assert dr<=len(base)<len(full)
            # Unsealed bank, using the ratio sampler on known-root squares only.
            hs=[];vs=[]
            for _ in range(60):
                h=rng.choice(U);u=rng.choice(U);s=h*h%N;w=u*s%N
                if tag[u]==tag[w]:
                    hs.append(h);vs.append(tuple(b-a for a,b in zip(v[u],v[w])))
            A=sp.Matrix.hstack(*(sp.Matrix(z) for z in vs)) if vs else sp.zeros(len(base),0)
            H=hermite_normal_form(A)
            covered={z:hermite_normal_form(H.row_join(sp.Matrix(z)))==H for z in ds}
            counts={s:sum(covered[z] for u,z in pairs[s]) for s in S}
            total=sum(counts.values());assert total>=len(U)  # s=1 is always covered
            # Exact uniformity of masked query mass, even for targets never covered directly.
            for s in S:
                assert sum(counts[s*a*a%N] for a in U)*len(S)==total*len(U)
                maskchecks+=len(U)
                a=next(a for a in U if counts[s*a*a%N]>0)
                ss=s*a*a%N;u,z=next((u,z) for u,z in pairs[ss] if covered[z])
                c=solve_span(A,sp.Matrix(z));assert c is not None
                root=prod(pow(h,e,N) for h,e in zip(hs,c))*pow(a,-1,N)%N
                assert root*root%N==s;rootschecks+=1
            print('affine fixture:',N,'B',B,'raw rank',len(full),'difference rank',dr,
                  'collision',G,'covered mass',Fraction(total,len(U)*len(S)))
    print('same-coset pair comparisons:',comparisons,'exact tag matches:',corematches,
          'uniform masked mass comparisons:',maskchecks,'verified roots:',rootschecks)


if __name__=='__main__':main()
