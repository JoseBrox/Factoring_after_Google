"""Exact AP conjunction / partial-lattice counts and finite cross-checks.
No asymptotic enumeration of all prime tuples is claimed.
Python standard library only.
"""
from itertools import product
from math import gcd, isqrt, prod
from random import Random


def ceildiv(x, y):
    return -((-x)//y)


def floor_sum(n, m, a, b):
    """sum_{0 <= i < n} floor((a*i+b)/m); signed a,b allowed."""
    assert n >= 0 and m > 0
    out = 0
    while n:
        qa, a = divmod(a, m)
        qb, b = divmod(b, m)
        out += qa*n*(n-1)//2 + qb*n
        Y, b1 = divmod(a*n+b, m)
        if Y == 0:
            return out
        assert a > 0
        n, m, a, b = Y, a, m, b1
    return out


def count_rect(N, c, d, s0, s1, t0, t1):
    """Count (s,t) in integer rectangle with t = c*s+d mod N."""
    if s0>s1 or t0>t1:
        return 0
    n = s1-s0+1
    offset = c*s0+d
    return (floor_sum(n,N,-c,t1-offset)
            -floor_sum(n,N,-c,t0-1-offset))


def congruences(N, atoms):
    """Reduce q | r+jN to r=u mod U. Atoms (j,q), q distinct or repeated primes."""
    u,U = 0,1
    seen = {}
    for j,q in atoms:
        assert q>1 and gcd(q,N)==1
        r = (-j*N)%q
        if q in seen:
            if seen[q]!=r:
                return None
            continue
        assert gcd(U,q)==1
        seen[q]=r
        u += U*(((r-u)*pow(U,-1,q))%q)
        U *= q
        assert 0<=u<U
    return u,U


def count_atoms(N,a,I,J,left,right):
    """Number of canonical anchors r in I with a*r mod N in J, satisfying lists."""
    assert N>1 and gcd(a,N)==1
    assert 0<=I[0]<=I[1]<N and 0<=J[0]<=J[1]<N
    l,r=congruences(N,left),congruences(N,right)
    if l is None or r is None:
        return 0
    u,U=l; v,V=r
    c=a*U*pow(V,-1,N)%N
    d=(a*u-v)*pow(V,-1,N)%N
    return count_rect(N,c,d,ceildiv(I[0]-u,U),(I[1]-u)//U,
                       ceildiv(J[0]-v,V),(J[1]-v)//V)


def count_raw(N,a,n,prefix,left,right):
    """Count completions of n-bit raw prefix, canonicalized modulo N."""
    assert N.bit_length()==n and len(prefix)<=n
    lo=(int(prefix,2) if prefix else 0)<<(n-len(prefix))
    hi=lo+(1<<(n-len(prefix)))-1
    result=0
    for k in range(lo//N,hi//N+1):
        I=(max(lo,k*N)-k*N,min(hi,(k+1)*N-1)-k*N)
        result+=count_atoms(N,a,I,(0,N-1),left,right)
    return result


def count_partial(N,a,U,V,X,Y,I=None):
    """Count x in X,y in Y, U|x,V|y,y=a*x mod N; optional x mod N in I."""
    assert U>0 and V>0 and gcd(a*U*V,N)==1
    if X[0]>X[1] or Y[0]>Y[1]:
        return 0
    c=a*U*pow(V,-1,N)%N
    t0,t1=ceildiv(Y[0],V),Y[1]//V
    def sub(lo,hi):
        return count_rect(N,c,0,ceildiv(lo,U),hi//U,t0,t1)
    if I is None:
        return sub(*X)
    assert 0<=I[0]<=I[1]<N
    return sum(sub(max(X[0],k*N+I[0]),min(X[1],k*N+I[1]))
               for k in range(X[0]//N,X[1]//N+1))


def forced_pair(N,a,U,V):
    """Construct a nonzero signed partial relation using a box of side sqrt(N)."""
    assert N>=5 and gcd(a*U*V,N)==1
    S=isqrt(N)+1
    assert S*S>N and S<N
    c=a*U*pow(V,-1,N)%N
    assert count_rect(N,c,0,1,S,-S,S)>0
    lo,hi=1,S
    while lo<hi:
        mid=(lo+hi)//2
        if count_rect(N,c,0,lo,mid,-S,S):
            hi=mid
        else:
            lo=mid+1
    s=lo; t=(c*s+S)%N-S
    assert 0<s<=S and 0<abs(t)<=S
    assert (a*U*s-V*t)%N==0
    return s,t


def test_floor_sum():
    tests=0
    for n,m,a,b in product(range(10),range(1,13),range(-16,17),range(-16,17)):
        assert floor_sum(n,m,a,b)==sum((a*i+b)//m for i in range(n))
        tests+=1
    # independent identities on very large integers, including signed offsets
    rng=Random(516)
    for _ in range(1000):
        n=rng.randrange(1,1<<256);m=rng.randrange(1,1<<256)
        a=rng.randrange(-(1<<256),1<<256);b=rng.randrange(-(1<<256),1<<256)
        k=rng.randrange(n+1)
        z=floor_sum(n,m,a,b)
        assert z==floor_sum(k,m,a,b)+floor_sum(n-k,m,a,b+a*k)
        assert z+floor_sum(n,m,-a,-b-1)==-n
    print('floor sums:',tests,'brute-force checks, 1000 large-integer identity checks')


def test_counts():
    rng=Random(915)
    N=899;n=N.bit_length();ps=[3,5,7,11,13,17,19,23,37]
    ps=[q for q in ps if gcd(q,N)==1]
    checks=0
    for _ in range(1000):
        a=rng.randrange(1,N)
        if gcd(a,N)!=1:continue
        l=[(rng.randrange(1,20),rng.choice(ps)) for _ in range(rng.randrange(12))]
        r=[(rng.randrange(1,20),rng.choice(ps)) for _ in range(rng.randrange(12))]
        lo=rng.randrange(N);hi=rng.randrange(lo,N)
        l2=rng.randrange(N);h2=rng.randrange(l2,N)
        brute=sum(l2<=a*x%N<=h2 and all((x+j*N)%q==0 for j,q in l)
                  and all((a*x%N+j*N)%q==0 for j,q in r) for x in range(lo,hi+1))
        assert count_atoms(N,a,(lo,hi),(l2,h2),l,r)==brute
        p=''.join(str(rng.randrange(2)) for _ in range(rng.randrange(n+1)))
        base=(int(p,2) if p else 0)<<(n-len(p))
        brute2=sum(all((x%N+j*N)%q==0 for j,q in l)
                   and all((a*x%N+j*N)%q==0 for j,q in r)
                   for x in range(base,base+(1<<(n-len(p)))))
        assert count_raw(N,a,n,p,l,r)==brute2
        checks+=2
    # Deliberate high-degree conjunction with nonzero solutions and large CRT moduli.
    N=1000003*1000033;a=pow(5,99,N)
    ps=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
    x=123456789012;y=a*x%N
    l=[(-x*pow(N,-1,q)%q,q) for q in ps]
    r=[(-y*pow(N,-1,q)%q,q) for q in ps]
    assert prod(ps)>N
    assert count_atoms(N,a,(0,N-1),(0,N-1),l,r)==1
    assert count_atoms(N,a,(0,x-1),(0,N-1),l,r)==0
    assert count_atoms(N,a,(0,N-1),(0,N-1),l+[(l[0][0]+1,l[0][1])],r)==0
    print('CRT anchor counts:',checks,'brute-force cases and 44-atom unique-anchor fixture')


def test_partial():
    rng=Random(141)
    checks=0
    for _ in range(500):
        N=rng.randrange(5,130)|1;a=rng.randrange(1,N)
        U,V=rng.randrange(1,20),rng.randrange(1,20)
        if gcd(a*U*V,N)!=1:continue
        x0=rng.randrange(-2*N,N);x1=x0+rng.randrange(0,4*N)
        y0=rng.randrange(-2*N,N);y1=y0+rng.randrange(0,4*N)
        lo=rng.randrange(N);hi=rng.randrange(lo,N)
        # Independent direct pair enumeration over signed multiples.
        pairs=[(x,y) for x in range(x0,x1+1) if x%U==0
               for y in range(y0,y1+1) if y%V==0 and (a*x-y)%N==0]
        assert count_partial(N,a,U,V,(x0,x1),(y0,y1))==len(pairs)
        assert count_partial(N,a,U,V,(x0,x1),(y0,y1),(lo,hi))==sum(lo<=x%N<=hi for x,y in pairs)
        checks+=2
    print('partial witness counts:',checks,'brute-force cases (signed ranges and prefix intervals)')
    # Exhaustive multipliers for small composite moduli, plus large deterministic fixtures.
    checked=0
    for N in (15,21,35,77,899):
        for a in range(1,N):
            if gcd(a*2*5,N)!=1:continue
            s,t=forced_pair(N,a,2,5)
            assert (2*a*s-5*t)%N==0
            checked+=1
    for _ in range(100):
        N=(rng.randrange(1<<200,1<<201)|1);a=rng.randrange(1,N)
        U,V=rng.randrange(1,1<<100),rng.randrange(1,1<<100)
        if gcd(a*U*V,N)!=1:continue
        s,t=forced_pair(N,a,U,V)
        assert (a*U*s-V*t)%N==0
        checked+=1
    print('forced signed pairs:',checked,'checks, including 201-bit moduli')


if __name__=='__main__':
    test_floor_sum();test_counts();test_partial()
