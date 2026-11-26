"""Finite checks of the signed common-translation relation construction.
The rank fixtures use exhaustive product tables ONLY at small sizes.
The independent AP scanner does not use a table.
Standard library only. No factorization of N is used to find relations.
"""
from itertools import combinations_with_replacement, product
from math import gcd, isqrt, prod
from random import Random


def band(B):
    return [p for p in range(B//2+1,B+1) if p>=2 and
            all(p%d for d in range(2,isqrt(p)+1))]


def scan(r,N,B,L,P):
    assert 1<=r<N and gcd(r,N)==1
    for x in range(r,B**L+1,N):
        v=x; counts=[]
        for p in P:
            e=0
            while v%p==0:
                v//=p;e+=1
            counts.append(e)
        if v==1 and sum(counts)==L:
            assert prod(p**e for p,e in zip(P,counts))==x
            return counts
    return None


def table(N,P,L):
    tab={}
    for w in combinations_with_replacement(range(len(P)),L):
        row=[0]*len(P)
        for j in w:row[j]+=1
        tab.setdefault(prod(P[j] for j in w)%N,row)
    return tab


def det(A):
    A=[r[:] for r in A]; prev=1; sign=1
    for i in range(len(A)-1):
        j=next((j for j in range(i,len(A)) if A[j][i]),None)
        if j is None:return 0
        if j!=i:A[i],A[j]=A[j],A[i];sign=-sign
        p=A[i][i]
        for j in range(i+1,len(A)):
            for k in range(i+1,len(A)):
                a=A[j][k]*p-A[j][i]*A[i][k]
                assert a%prev==0
                A[j][k]=a//prev
            A[j][i]=0
        prev=p
    return sign*A[-1][-1]


def rank_demo(N,B,L):
    P=band(B); assert all(gcd(p,N)==1 for p in P)
    T=L+1
    tab=table(N,P,L)
    good=[r for r in tab if all(pow(p,T,N)*r%N in tab for p in P)]
    assert good
    r=min(good)
    base=tab[r]
    A=[]
    for i,p in enumerate(P):
        other=tab[pow(p,T,N)*r%N]
        row=[T*int(i==j)+x-y for j,(x,y) in enumerate(zip(base,other))]
        assert sum(row)==T and prod(pow(q,z,N) for q,z in zip(P,row))%N==1
        A.append(row)
    E=abs(det(A)); assert E>0
    assert E<=(T+2*L)**len(P)
    assert all(pow(p,E,N)==1 for p in P)
    for p in P:
        e=E
        while e%2==0:e//=2
        while e<=E:
            z=gcd(pow(p,e,N)-1,N)
            if 1<z<N:
                print('N',N,'B',B,'L',L,'band',len(P),'support',len(tab),'good anchors',len(good),'T',T,'anchor',r,'determinant bits',E.bit_length(),'factor',z)
                return
            e*=2
    raise AssertionError('no separating prime in this finite fixture')


def check_scanner():
    N,B,L=35,19,4
    P=band(B);tab=table(N,P,L)
    count=0
    for r in range(1,N):
        if gcd(r,N)>1:continue
        row=scan(r,N,B,L,P)
        assert (row is not None)==(r in tab)
        if row is not None:
            assert prod(pow(p,e,N) for p,e in zip(P,row))%N==r
        count+=1
    print('AP scanner:',count,'unit residues,',len(tab),'represented')


def exhaustive_matrix_check():
    # Check every possible common vector and all collections of target
    # vectors of nonnegative coordinate sum L for small m=3,L=2.
    # T=L+1 is sufficient, whereas T=L can be singular.
    m,L=3,2;T=L+1
    rows=[a for a in product(range(L+1),repeat=m) if sum(a)==L]
    count=0;counterexample=None
    for u in rows:
        for vv in product(rows,repeat=m):
            A=[[T*int(i==j)+u[j]-vv[i][j] for j in range(m)] for i in range(m)]
            assert det(A)!=0
            if counterexample is None:
                C=[[L*int(i==j)+u[j]-vv[i][j] for j in range(m)] for i in range(m)]
                if det(C)==0:counterexample=C
            count+=1
    assert counterexample is not None
    print('matrix check:',count,'nonsingular matrices at T=L+1; singular at T=L:',counterexample)


if __name__=='__main__':
    check_scanner()
    exhaustive_matrix_check()
    rank_demo(899,23,12)
    rank_demo(47053,200,6)
    rank_demo(23707,150,8)
