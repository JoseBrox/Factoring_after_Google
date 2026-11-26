"""Exact finite checks for disjoint narrow bands and streaming lift atoms.

The product table in the small rank fixtures is a finite oracle only.
No asymptotic enumeration of product tuples or anchor values is claimed.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod


def bands(B,L):
    out=[[] for _ in range(L)]
    for q in range(2,B+1):
        if 8*L*q<=B*(8*L-1):
            continue
        if any(q%d==0 for d in range(2,isqrt(q)+1)):
            continue
        j=(8*L*L*q-B*(8*L*L-L)-1)//B
        assert 0<=j<L
        out[j].append(q)
    assert all(out)
    return out


def constants(N,a,n):
    K=1<<(2*n-1).bit_length()
    c=[a*pow(2,i,N)%N for i in range(n)]
    w=[K*z//N for z in c]
    assert 2*n<=K
    return K,c,w


def rep(N,a,R,n):
    K,c,w=constants(N,a,n)
    bits=[(R>>i)&1 for i in range(n)]
    y=sum(c[i]*bits[i] for i in range(n))-N*(sum(w[i]*bits[i] for i in range(n))//K)
    assert 0<=y<2*N and y%N==a*R%N
    return y


def atom(N,a,j,q,R,n):
    K,c,w=constants(N,a,n)
    s=z=0
    for i in range(n-1,-1,-1):
        if (R>>i)&1:
            s+=w[i]
            z=(z+c[i])%q
    return (z+N*(j-s//K))%q==0


def lift_check(N,B,L,P,a,R,n):
    """Exact OR-AND-OR divisibility test using the shifted lift index."""
    M=B**L//N
    y=rep(N,a,R,n)
    for j in range(1,M+1):
        x=y+j*N
        factors=[]
        for I in P:
            hit=[q for q in I if x%q==0]
            if not hit:break
            factors.append(hit[0])
        else:
            assert prod(factors)==x and x<=B**L
            return tuple(factors)
    return None


def exact_count(N,n,atoms,prefix=''):
    """Count completions accepting every atom by exact streaming DP.

    The general state bound is product of the individual q and
    polynomial-in-n counter bounds, for a fixed number of atoms.
    """
    assert len(prefix)<=n and set(prefix)<=set('01')
    aa=sorted({a for a,j,q in atoms})
    aq=sorted({(a,q) for a,j,q in atoms})
    ac={a:constants(N,a,n) for a in aa}
    K=ac[aa[0]][0]
    state={(0,)*(len(aa)+len(aq)):1}
    for place,i in enumerate(range(n-1,-1,-1)):
        bits=[int(prefix[place])] if place<len(prefix) else [0,1]
        nxt=defaultdict(int)
        for t,count in state.items():
            for bit in bits:
                u=tuple(t[z]+bit*ac[a][2][i] for z,a in enumerate(aa))
                v=tuple((t[len(aa)+z]+bit*ac[a][1][i])%q for z,(a,q) in enumerate(aq))
                nxt[u+v]+=count
        state=nxt
    assert sum(state.values())==1<<(n-len(prefix))
    count=0
    for t,cnt in state.items():
        s=dict(zip(aa,t[:len(aa)]));z=dict(zip(aq,t[len(aa):]))
        if all((z[a,q]+N*(j-s[a]//K))%q==0 for a,j,q in atoms):
            count+=cnt
    return count


def bareiss(A):
    A=[row[:] for row in A];m=len(A);d=1;sign=1
    for i in range(m-1):
        j=next(j for j in range(i,m) if A[j][i])
        if j!=i:A[i],A[j]=A[j],A[i];sign=-sign
        p=A[i][i]
        for j in range(i+1,m):
            for k in range(i+1,m):
                x=A[j][k]*p-A[j][i]*A[i][k]
                assert x%d==0
                A[j][k]=x//d
            A[j][i]=0
        d=p
    return sign*A[-1][-1]


def test_atoms():
    # Compare the exact one-pass formula against full integer arithmetic,
    # including raw R>=N and R=0, not just uniformly distributed units.
    N=899;n=N.bit_length();B=400;L=2;P=bands(B,L)
    Q=[q for I in P for q in I];A=[1]+[pow(q,2*L+1,N) for q in Q]
    checks=shifted=0
    for a in A:
        for R in range(1<<n):
            y=rep(N,a,R,n)
            shifted+=y>=N
            for j in [1,2,B**L//N]:
                for q in Q:
                    assert atom(N,a,j,q,R,n)==((y+j*N)%q==0)
                    checks+=1
    # A separate small-N example with plenty of slack in the upper bound.
    N2=899;B2=400;L2=2;P2=bands(B2,L2);n2=N2.bit_length()
    assert B2**L2+2*N2 < 2*Fraction(7,8)*B2**L2
    tab={prod(t)%N2 for t in product(*P2)}
    M=B2**L2//N2
    assert Fraction(7,8)*B2**L2>3*N2
    count=0
    for a in A:
        for R in range(1<<n2):
            z=lift_check(N2,B2,L2,P2,a,R,n2)
            assert (z is not None)==(a*R%N2 in tab)
            if z:assert prod(z)%N2==a*R%N2 and all(q in I for q,I in zip(z,P2))
            count+=1
    print('streaming atom checks',checks,'shifted representatives',shifted,'exact lift decisions',count)


def test_dp():
    N=899;n=N.bit_length();P=bands(400,2)
    q0,q1=P[0];q2=P[1][0];a=pow(q0,5,N)
    tests=[[(1,1,q0)],[(a,3,q1),(a,7,q2)],[(1,1,q0),(a,3,q1),(a,7,q2)],[(a,1,q0),(a,1+q0,q0)]]
    total=0
    for atoms in tests:
        for pref in ['', '0','1','010','10101','0101101110']:
            l=len(pref);base=(int(pref,2) if pref else 0)<<(n-l)
            brute=sum(all(atom(N,a,j,q,R,n) for a,j,q in atoms) for R in range(base,base+(1<<(n-l))))
            assert exact_count(N,n,atoms,pref)==brute
            total+=1
    print('exact conditional DP checks',total)


def test_rank():
    N=21;B=600;L=2;P=bands(B,L);Q=[q for I in P for q in I]
    assert all(gcd(q,N)==1 for q in Q)
    tab={}
    for t in product(*P):tab.setdefault(prod(t)%N,t)
    T=2*L+1;rows=[];used=[]
    for p in Q:
        a=pow(p,T,N)
        r=next(r for r in sorted(tab) if a*r%N in tab)
        u,v=tab[r],tab[a*r%N]
        row=[T*int(p==q)+u.count(q)-v.count(q) for q in Q]
        assert prod(pow(q,c,N) for q,c in zip(Q,row))%N==1
        rows.append(row);used.append(r)
    E=abs(bareiss(rows));assert E and all(pow(p,E,N)==1 for p in Q)
    factor=None
    for p in Q:
        z=E
        while z%2==0:z//=2
        while z<=E:
            h=gcd(pow(p,z,N)-1,N)
            if 1<h<N:factor=h;break
            z*=2
        if factor:break
    assert factor
    print('independent-anchor rank fixture: N',N,'band sizes',list(map(len,P)),'rank',len(Q),'distinct anchors',len(set(used)),'determinant',E,'factor',factor)


if __name__=='__main__':
    test_atoms();test_dp();test_rank()
