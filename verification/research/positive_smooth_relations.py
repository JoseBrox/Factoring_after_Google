"""Exact finite checks for positive smooth relation rank-building.

The support-table mode below is ONLY for small fixtures. The asymptotic
randomized algorithm uses scan_inverse(), not enumeration of all words.
No factorization of the input N is used by either routine.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import gcd, isqrt, prod
from random import Random


def band(B):
    return [p for p in range(B//2+1,B+1) if p>=2 and
            all(p%d for d in range(2,isqrt(p)+1))]


def scan_inverse(r,N,B,L,S):
    """Exact AP search: x=r+jN<=B^L, x a product of L primes in S."""
    assert 1<=r<N and gcd(r,N)==1
    for x in range(r,B**L+1,N):
        v=x; row={}
        for p in S:
            while v%p==0:
                v//=p; row[p]=row.get(p,0)+1
            if v==1:break
        if v==1 and sum(row.values())==L:
            assert prod(p**e for p,e in row.items())==x
            return row
    return None


def add(v,w,c):
    for p,a in w.items():
        v[p]=v.get(p,0)+c*a
        if not v[p]:del v[p]


def insert(v,piv):
    v={p:Q(a) for p,a in v.items() if a}
    while v:
        p=max(v); a=v[p]
        if p in piv:add(v,piv[p],-a)
        else:
            piv[p]={q:c/a for q,c in v.items()}
            return a
    raise AssertionError('dependent row')


def sign_subset(P,piv):
    w={p:Q(0) for p in P}
    w[next(p for p in P if p not in piv)]=Q(1)
    for p in sorted(piv):
        w[p]=-sum(a*w[q] for q,a in piv[p].items() if p!=q)
    assert all(sum(a*w[q] for q,a in v.items())==0 for v in piv.values())
    S=next(S for S in ([p for p in P if w[p]>=0],
                       [p for p in P if w[p]<=0])
           if 2*len(S)>=len(P) and any(w[p] for p in S))
    p=next(p for p in S if w[p])
    return S,p,w


def finite_table(S,L,N):
    tab={}
    for word in combinations_with_replacement(S,L):
        tab.setdefault(prod(word)%N,word)
    return tab


def bareiss_det(A):
    A=[r[:] for r in A]; n=len(A); prev=1; sign=1
    for i in range(n-1):
        j=next(j for j in range(i,n) if A[j][i])
        if j!=i:A[i],A[j]=A[j],A[i];sign=-sign
        p=A[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                a=A[j][k]*p-A[j][i]*A[i][k]
                assert a%prev==0
                A[j][k]=a//prev
            A[j][i]=0
        prev=p
    return sign*A[-1][-1]


def finite_rank_demo(N,B,L,seed=237):
    P=band(B); assert all(gcd(p,N)==1 for p in P)
    rng=Random(seed); piv={}; rows=[]; attempts=0; determinant=Q(1)
    while len(piv)<len(P):
        S,p,w=sign_subset(P,piv)
        # Exhaustive finite truth table replaces the AP scan ONLY here.
        # It is too expensive for the asymptotic algorithm.
        tab=finite_table(S,L,N)
        for _ in range(10000):
            word=[rng.choice(S) for _ in range(L)]
            r=pow(p*p*prod(word),-1,N); attempts+=1
            if r in tab:break
        else:raise AssertionError('finite sampling cap reached')
        other=tab[r]; x=prod(other)
        assert x%N==r and 1<=x<=B**L
        row={p:2}
        for q in word+list(other):row[q]=row.get(q,0)+1
        assert set(row)<=set(S) and sum(row.values())==2*L+2
        assert prod(pow(q,a,N) for q,a in row.items())%N==1
        assert sum(w[q]*a for q,a in row.items())!=0
        determinant*=insert(row,piv);rows.append(row)
    E=abs(determinant);assert E.denominator==1;E=int(E)
    assert E==abs(bareiss_det([[r.get(p,0) for p in P] for r in rows]))
    assert all(pow(p,E,N)==1 for p in P)
    for p in P:
        e=E
        while e%2==0:e//=2
        while e<=E:
            d=gcd(pow(p,e,N)-1,N)
            if 1<d<N:
                print('N',N,'B',B,'L',L,'rank',len(P),'trials',attempts,
                      'determinant bits',E.bit_length(),'factor',d)
                return
            e*=2
    raise AssertionError('no separating prime in the finite band')


def check_scanner():
    N,B,L=47053,200,3
    S=band(B)[:11];tab=finite_table(S,L,N)
    # Exact comparison on every represented residue, and a set of
    # absent residues. The small fixture has only floor(B^L/N) candidates
    # per AP. No precomputed table is used inside scan_inverse().
    absent=[r for r in range(1,N) if gcd(r,N)==1 and r not in tab][:50]
    for r in list(tab)+absent:
        row=scan_inverse(r,N,B,L,S)
        assert (row is not None)==(r in tab)
        if row is not None:
            assert prod(p**e for p,e in row.items())%N==r
    print('AP scanner:',len(tab),'represented residues and',len(absent),'absent residues checked')


if __name__=='__main__':
    check_scanner()
    finite_rank_demo(47053,200,6)
    finite_rank_demo(23707,150,8)
