"""Exact primitive-ratio enumeration and large-prime cancellation.
Standard library. All tests use bounded finite inputs; no uniform coverage claim.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt, lcm, prod
from random import Random


def ceildiv(a,b):
    assert b>0
    return -((-a)//b)


def floor_sum(n,m,a,b):
    assert n>=0 and m>0
    ans=0
    while n:
        q,a=divmod(a,m);r,b=divmod(b,m)
        ans+=q*n*(n-1)//2+r*n
        Y,b1=divmod(a*n+b,m)
        if not Y:return ans
        assert a>0
        n,m,a,b=Y,a,m,b1
    return ans


def rect_count(N,a,X,Y):
    # x=1,...,X, y=-Y,...,Y, y=a*x mod N.
    return floor_sum(X,N,-a,Y-a)-floor_sum(X,N,-a,-Y-1-a)


def egcd(a,b):
    r,s=1,0;t,u=0,1
    while b:
        q,a,b=a//b,b,a%b
        r,s=s,r-q*s;t,u=u,t-q*u
    if a<0:return -a,-r,-t
    return a,r,t


def slope_interval(u,w,H):
    # -H <= s*u+w <= H
    assert u
    if u<0:u,w=-u,-w
    return ceildiv(-H-w,u),(H-w)//u


def primitive_pairs(N,a,X,Y):
    """Return (proper factor or None, primitive pairs, stats).
    x positive, |y| positive, unit coordinates, box X,Y<N.
    If a nonunit lattice point reveals a factor, stop instead of counting.
    """
    assert N>=3 and 0<a<N and gcd(a,N)==1 and 1<=X<N and 1<=Y<N
    if not rect_count(N,a,X,Y):return None,[],(0,0,0)
    lo,hi=1,X
    while lo<hi:
        mid=(lo+hi)//2
        if rect_count(N,a,mid,Y):hi=mid
        else:lo=mid+1
    ux=lo;uy=(a*ux+Y)%N-Y
    assert 0<abs(uy)<=Y
    for z in (ux,uy):
        g=gcd(z,N)
        if g>1:
            assert g<N
            return g,[],(0,0,0)
    g=gcd(ux,uy);ux//=g;uy//=g
    assert gcd(ux,uy)==1 and (uy-a*ux)%N==0
    # ux*r+uy*s=1 gives det((ux,uy),(-s,r))=1.
    d,r,s=egcd(ux,uy);assert d==1
    vx,vy=-N*s,N*r
    assert ux*vy-uy*vx==N and (vy-a*vx)%N==0
    K=(ux*Y+abs(uy)*X)//N
    if K==0:return None,[(ux,uy)],(K,1,1)
    out=[];visited=0
    for t in range(-K,K+1):
        l1,h1=slope_interval(ux,t*vx,X)
        l2,h2=slope_interval(uy,t*vy,Y)
        for j in range(max(l1,l2),min(h1,h2)+1):
            x=j*ux+t*vx;y=j*uy+t*vy;visited+=1
            assert abs(x)<=X and abs(y)<=Y and (y-a*x)%N==0
            if x<=0 or y==0:continue
            g=gcd(x,N)
            if g>1:
                assert g<N
                return g,[],(K,visited,0)
            assert gcd(y,N)==1
            if gcd(x,y)==1:out.append((x,y))
    assert visited*N<=18*X*Y
    assert len(out)==len(set(out))
    return None,sorted(out),(K,visited,len(out))


def primes(B):
    return [p for p in range(2,B+1) if all(p%q for q in range(2,isqrt(p)+1))]


def peel(n,P):
    n=abs(n);v={}
    assert n>=1
    for p in P:
        e=0
        while n%p==0:n//=p;e+=1
        if e:v[p]=e
        if n==1:break
    return n,v


def factorfree_columns(nums):
    """Pairwise coprime bases, exact exponents, via gcd splitting only."""
    m=len(nums);rows={}
    def add(d,v):
        if d==1:return
        if d not in rows:rows[d]=[0]*m
        rows[d]=[x+y for x,y in zip(rows[d],v)]
    for i,z in enumerate(nums):
        e=[0]*m;e[i]=1;add(z,e)
    while True:
        keys=sorted(rows)
        hit=None
        for j,p in enumerate(keys):
            for q in keys[j+1:]:
                g=gcd(p,q)
                if g>1:hit=(p,q,g);break
            if hit:break
        if hit is None:break
        p,q,g=hit;u=rows.pop(p);v=rows.pop(q)
        add(p//g,u);add(q//g,v);add(g,[x+y for x,y in zip(u,v)])
    for i,z in enumerate(nums):assert prod(d**v[i] for d,v in rows.items())==z
    return rows


def cancel_large(pairs,P):
    """Return nonnegative coefficients in kernel of outside-P valuations.
    Requires residuals on each side pairwise coprime (as certified by determinant).
    No factorization of residuals. The returned vector is nonzero or None.
    """
    m=len(pairs)
    rx=[peel(x,P)[0] for x,y in pairs];ry=[peel(y,P)[0] for x,y in pairs]
    for zs in (rx,ry):
        assert all(gcd(x,y)==1 for i,x in enumerate(zs) for y in zs[i+1:])
    rows=factorfree_columns(rx+ry)
    adj=[[] for _ in pairs];bad=set()
    for d,v in rows.items():
        left=[(i,e) for i,e in enumerate(v[:m]) if e]
        right=[(i,e) for i,e in enumerate(v[m:]) if e]
        assert len(left)<=1 and len(right)<=1
        if not left:bad.add(right[0][0]);continue
        if not right:bad.add(left[0][0]);continue
        (i,e),(j,f)=left[0],right[0]
        # e*c_i=f*c_j
        adj[i].append((j,Q(e,f)));adj[j].append((i,Q(f,e)))
    done=set()
    for i in range(m):
        if i in done:continue
        vals={i:Q(1)};todo=[i];ok=True
        while todo:
            j=todo.pop();done.add(j)
            if j in bad:ok=False
            for k,t in adj[j]:
                v=vals[j]*t
                if k in vals:
                    if vals[k]!=v:ok=False
                else:vals[k]=v;todo.append(k)
        if ok:
            d=lcm(*(v.denominator for v in vals.values()))
            c=[int(d*vals.get(j,0)) for j in range(m)]
            assert sum(c)>0
            assert all(sum((v[i]-v[i+m])*c[i] for i in range(m))==0 for v in rows.values())
            return c
    return None


def matrix_rank(rows,m):
    piv={}
    for row in rows:
        v=[Q(x) for x in row]
        for j in range(m):
            if not v[j]:continue
            if j not in piv:
                z=v[j];piv[j]=[x/z for x in v];break
            z=v[j];v=[x-z*y for x,y in zip(v,piv[j])]
    return len(piv)


def test_graph(pairs,P):
    m=len(pairs)
    rx=[peel(x,P)[0] for x,y in pairs];ry=[peel(y,P)[0] for x,y in pairs]
    C=factorfree_columns(rx+ry)
    rows=[[v[i]-v[i+m] for i in range(m)] for v in C.values()]
    rank=matrix_rank(rows,m)
    got=cancel_large(pairs,P)
    assert (got is not None)==(rank<m)
    if got is not None:
        assert all(v>=0 for v in got) and sum(got)>0
        assert all(sum(x*y for x,y in zip(r,got))==0 for r in rows)
    return got


def matching_pairs(N,a,bands_x,bands_y,pre_x=1,pre_y=1,I=None):
    """Exact complete products with given prefixes, by residual rectangle.
    All prime bands are assumed pairwise disjoint; both residual upper bounds <N.
    I optionally restricts the original x residue to an inclusive interval.
    """
    X=prod(max(s) for s in bands_x);Y=prod(max(s) for s in bands_y)
    assert gcd(N,pre_x*pre_y)==1
    fac,pairs,stats=primitive_pairs(N,(a*pre_x*pow(pre_y,-1,N))%N,X,Y)
    if fac:return fac,[]
    def valid(z,bands):
        if z<=0:return False
        for S in bands:
            hit=[p for p in S if z%p==0]
            if len(hit)!=1:return False
            z//=hit[0]
        return z==1
    out=[]
    for x,y in pairs:
        if valid(x,bands_x) and valid(y,bands_y):
            u,v=pre_x*x,pre_y*y
            assert (v-a*u)%N==0
            if I is None or I[0]<=u%N<=I[1]:out.append((u,v))
    return None,sorted(out)


def tests():
    rng=Random(87621);count=fac_count=skew=noncol=empty=graph_count=0
    for N in (15,21,35,77,899,1009,47053):
        for _ in range(350):
            a=rng.randrange(1,N)
            if gcd(a,N)>1:continue
            # Include skinny boxes and boxes below the determinant scale.
            X=rng.randrange(1,min(N,1+3*isqrt(N)))
            Y=rng.randrange(1,min(N,1+3*isqrt(N)))
            d,out,st=primitive_pairs(N,a,X,Y)
            if d:
                assert 1<d<N and N%d==0;fac_count+=1;continue
            direct=[]
            for x in range(1,X+1):
                for y in range(-Y,Y+1):
                    if gcd(x,y)==1 and gcd(x,N)==1 and (y-a*x)%N==0:direct.append((x,y))
            assert out==direct
            count+=1
            if st[1]==0:empty+=1
            elif st[0]==0:skew+=1
            else:noncol+=1
            # Certified private-prime property for all primitive candidates.
            B=max(2,2*X*Y//N);P=primes(B)
            for zs in ([peel(x,P)[0] for x,y in out],[peel(y,P)[0] for x,y in out]):
                assert all(gcd(u,v)==1 for i,u in enumerate(zs) for v in zs[i+1:])
            test_graph(out,P);graph_count+=1
    print('rectangle comparisons',count,'early factors',fac_count,'empty',empty,'collinear',skew,'noncollinear',noncol)
    assert test_graph([(3,5),(5,9)],[]) is None
    assert test_graph([(3,5),(5,3)],[])==[1,1]
    print('graph versus exact rational kernel:',graph_count+2,'comparisons')
    N=899;S=[[3,5],[7,11]];T=[[13,17],[19,23]]
    A=[prod(w) for w in product(*S)];B=[prod(w) for w in product(*T)]
    count=fac_count=0
    for a in range(1,N):
        if gcd(a,N)>1:continue
        d,out=matching_pairs(N,a,S,T)
        if d:assert N%d==0 and 1<d<N;fac_count+=1;continue
        assert out==sorted((x,y) for x in A for y in B if (y-a*x)%N==0)
        count+=1
    print('all-target disjoint product counts',count,'early factors',fac_count)
    N=47053;S=[[2,3],[5,7],[11,13]];T=[[17,19],[23,29],[31,37]]
    count=fac_count=0
    for _ in range(100):
        u=rng.choice(S[0]);v=rng.choice(T[0]);x=u*prod(rng.choice(z) for z in S[1:]);y=v*prod(rng.choice(z) for z in T[1:]);a=y*pow(x,-1,N)%N
        I=(rng.randrange(x%N+1),rng.randrange(x%N,N))
        d,out=matching_pairs(N,a,S[1:],T[1:],u,v,I)
        if d:assert N%d==0;fac_count+=1;continue
        A=[u*prod(w) for w in product(*S[1:])];B=[v*prod(w) for w in product(*T[1:])]
        assert out==sorted((s,t) for s in A for t in B if I[0]<=s%N<=I[1] and (t-a*s)%N==0)
        assert (x,y) in out;count+=1
    print('prescribed-prefix smooth completion comparisons',count,'early factors',fac_count)
    # Search for a small partial-relation cancellation, with no individual smooth ratio.
    for N in (77,143,221,899,1763,47053):
        H=isqrt(N)+1;B=max(2,2*H*H//N);P=primes(B)
        for a in range(1,min(N,5000)):
            if gcd(a,N)>1:continue
            d,pairs,_=primitive_pairs(N,a,H,H)
            if d or not pairs or any(peel(x,P)[0]==peel(y,P)[0]==1 for x,y in pairs):continue
            c=cancel_large(pairs,P)
            if c is None:continue
            C=sum(c);x=prod(abs(s)**j for (s,t),j in zip(pairs,c));y=prod(abs(t)**j for (s,t),j in zip(pairs,c));g=gcd(x,y)
            assert peel(x//g,P)[0]==peel(y//g,P)[0]==1
            sign=prod((-1 if t<0 else 1)**j for (s,t),j in zip(pairs,c))
            assert (pow(a,C,N)*x-sign*y)%N==0
            print('large-prime cancellation fixture',N,'a',a,'H',H,'cutoff',B,'pairs',pairs,'coefficients',c,'reduced signed ratio',sign*(y//g),x//g)
            return
    raise AssertionError('no cancellation fixture')


if __name__=='__main__':tests()
