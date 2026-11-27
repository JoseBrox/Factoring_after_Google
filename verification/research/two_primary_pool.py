"""Factor-free 2-saturation of signed pooled integer relations.
Standard library; prior lattice/row generation routines used in finite tests.
No uniform coverage or runtime guarantee for finding sufficient relations.
"""
from math import gcd, isqrt, prod
from itertools import combinations
from fractions import Fraction as Q
from random import Random
from primitive_ratio_lattice import factorfree_columns, peel, primes, primitive_pairs
from pooled_shift_relations import exact_eliminate, collect, pool


def kth_root(x,k):
    lo,hi=1,1<<((x.bit_length()+k-1)//k)
    while lo<hi:
        t=(lo+hi+1)//2
        if t**k<=x:lo=t
        else:hi=t-1
    return lo


def powerfree(x):
    assert x>=2
    for e in range(x.bit_length()-1,1,-1):
        r=kth_root(x,e)
        if r**e==x:return r,e
    return x,1


def normalized_basis(values):
    # Distinct bases are pairwise coprime and not proper powers.
    out={}
    for d,v in factorfree_columns(values).items():
        r,e=powerfree(d);assert r not in out
        out[r]=[a*e for a in v]
    assert all(prod(d**v[i] for d,v in out.items())==x for i,x in enumerate(values))
    return out


def image(N,bases,row):
    z=1
    for p,e in zip(bases,row):
        if e:z=z*pow(p,e,N)%N
    return z


def mod2_dependence(rows):
    piv={}
    for i,row in enumerate(rows):
        v=sum((a&1)<<j for j,a in enumerate(row));c=1<<i
        while v:
            j=v.bit_length()-1
            if j not in piv:piv[j]=v,c;break
            w,d=piv[j];v^=w;c^=d
        else:return c
    return 0


def involution(N,z):
    assert z*z%N==1
    if z in (1,N-1):return None
    g=gcd(z-1,N);assert 1<g<N and N%g==0
    return g


def two_group(N,values,max_k):
    if not values:return None,0
    orders=[]
    for z in values:
        w=z;k=0
        while w!=1:
            assert k<max_k
            nxt=w*w%N;k+=1
            if nxt==1:
                d=involution(N,w)
                if d:return d,None
            w=nxt
        orders.append(k)
    h=max(range(len(values)),key=lambda i:orders[i]);k=orders[h];g=values[h]
    if k==0:return None,0
    top=pow(g,1<<(k-1),N);assert top==N-1
    for u in values:
        v=u;exp=0
        for j in range(k):
            z=pow(v,1<<(k-j-1),N)
            assert z*z%N==1
            if z==1:continue
            d=involution(N,z)
            if d:return d,None
            assert z==top
            exp+=1<<j;v=v*pow(g,-(1<<j),N)%N
        assert v==1 and pow(g,exp,N)==u
    return None,k


def sat_split(N,bases,signed_rows,stop=True,minor_check=False):
    assert all(gcd(p,N)==1 for p in bases)
    assert all(image(N,bases,r) in (1,N-1) for r in signed_rows)
    r=len(bases)
    # Choose a rationally independent subset; its saturation has the same Q-span.
    piv={};ind=[]
    for row in signed_rows:
        v={j:Q(a) for j,a in enumerate(row) if a}
        while v:
            j=min(v);a=v[j]
            if j not in piv:
                piv[j]={i:z/a for i,z in v.items()};ind.append(row);break
            for i,z in piv[j].items():
                v[i]=v.get(i,0)-a*z
                if not v[i]:del v[i]
    rows=[[2*a for a in row] for row in ind]
    if minor_check:
        g=0
        # Small-test oracle only: enumerate all maximal minors by a different
        # exact determinant algorithm. This is NOT in the asymptotic procedure.
        for cols in combinations(range(r),len(rows)):
            g=gcd(g,abs(det_fraction([[v[j] for j in cols] for v in rows])))
        assert g>0
        expected=(g&-g).bit_length()-1
    # 2-saturation of their integer row lattice. Each replacement divides a fixed
    # nonzero maximal minor by 2, so only polynomially many replacements.
    steps=0
    while (c:=mod2_dependence(rows)):
        sel=[j for j in range(len(rows)) if c>>j&1]
        v=[sum(rows[i][j] for i in sel) for j in range(r)]
        assert all(a%2==0 for a in v)
        rows[sel[0]]=[a//2 for a in v];steps+=1
        z=image(N,bases,rows[sel[0]])
        # All current row images are killed by 2**steps.
        assert pow(z,1<<steps,N)==1
        if stop:
            d,k=two_group(N,[z],steps)
            if d:return d,len(rows),steps,None
    if minor_check:assert steps==expected
    vals=[image(N,bases,row) for row in rows]
    d,k=two_group(N,vals,steps)
    return d,len(rows),steps,k


def encode(N,P,raw):
    # raw row: q**T * 2**j * x = y mod N.
    m=len(raw);xx=[];yy=[];base=[]
    for q,T,j,x,y in raw:
        assert (pow(q,T,N)*pow(2,j,N)*x-y)%N==0 and gcd(x*y,N)==1
        a,u=peel(x,P);b,v=peel(y,P);xx.append(a);yy.append(b)
        base.append([T*(p==q)+j*(p==2)+u.get(p,0)-v.get(p,0) for p in P])
    R=normalized_basis(xx+yy);keys=list(R)
    rows=[base[i]+[R[d][i]-R[d][i+m] for d in keys] for i in range(m)]
    return list(P)+keys,rows


def test_powerfree():
    for x in range(2,1000):
        d,e=powerfree(x);assert d**e==x and powerfree(d)==(d,1)
    ds=normalized_basis([3**8*5**12,7**6,3**2*5**3,7**3])
    assert set(ds)=={3**2*5**3,7}
    print('power-free gcd basis: 998 integer checks and grouped composite fixture')


def test_group():
    # Exhaustive unit subgroup check for pairs of generators of 2-power order.
    count=0
    for N in [15,21,35,45,65,77,105,221]:
        vals=[z for z in range(1,N) if gcd(z,N)==1 and pow(z,256,N)==1]
        for u in vals:
            for v in vals:
                H={pow(u,i,N)*pow(v,j,N)%N for i in range(16) for j in range(16)}
                bad=any(z not in (1,N-1) and z*z%N==1 for z in H)
                d,k=two_group(N,[u,v],8)
                assert (d is not None)==bad
                if d:assert 1<d<N and N%d==0
                else:assert len(H)==1<<k
                count+=1
    print('2-group extraction comparisons:',count)


def det_fraction(A):
    A=[list(map(Q,row)) for row in A];n=len(A);ans=Q(1)
    for i in range(n):
        k=next((k for k in range(i,n) if A[k][i]),None)
        if k is None:return 0
        if k!=i:A[i],A[k]=A[k],A[i];ans=-ans
        a=A[i][i];ans*=a
        for k in range(i+1,n):
            b=A[k][i]/a
            for j in range(i,n):A[k][j]-=b*A[i][j]
    assert ans.denominator==1
    return int(ans)


def test_saturation():
    rng=Random(10287);count=0
    # Construct guaranteed relation matrices by taking random integer vectors
    # multiplied by a known annihilator only for this independent unit test.
    for _ in range(150):
        N=77;P=[2,3,5,13,17];r=rng.randrange(1,6)
        V=[[rng.randrange(-5,6) for _ in P] for j in range(r)]
        rows=[[30*2**rng.randrange(4)*a for a in row] for row in V]
        assert all(image(N,P,row)==1 for row in rows)
        d,rank,steps,k=sat_split(N,P,rows,stop=False,minor_check=True)
        if d:assert 1<d<N and N%d==0
        count+=1
    print('2-saturation index comparisons by maximal-minor gcd:',count)


def search():
    # Select small prime bases and modest rectangles, compare on real raw pools.
    tested=0
    for N in [77,143,221,899,1763,2491,3233,10403,47053,100160063,1000036000099]:
        for H in [isqrt(N)+1,2*(isqrt(N)+1),3*(isqrt(N)+1)]:
            if H>=N:continue
            P=primes(max(2,2*H*H//N))
            if any(N%p==0 for p in P):continue
            d,data=collect(N,H,P)
            if d:continue
            raw=sum(data.values(),[])
            # Look at prefixes where ordinary residual-free rank is still zero.
            for cap in sorted(set([1,2,3,4,6,10,20,40,min(80,len(raw)),len(raw)])):
                if cap>len(raw):continue
                selected=raw[:cap];rank,_,_=pool(N,selected,P)
                if rank:break
                bases,rows=encode(N,P,selected)
                d,R,steps,k=sat_split(N,bases,rows);tested+=1
                if d:
                    assert 1<d<N and N%d==0
                    print('zero-pure-rank saturation fixture:',N,'H',H,'P',P,'raw rows',selected,'rank',R,'2-steps',steps,'factor',d)
                    # The fourth raw row alone gives the square root, despite
                    # zero pure rank; explicitly verify the compact witness.
                    assert N==10403
                    rr=[selected[-1]];assert pool(N,rr,P)[0]==0
                    bb,vv=encode(N,P,rr);assert all(a%2==0 for a in vv[0])
                    z=image(N,bb,[a//2 for a in vv[0]])
                    assert z==102 and z*z%N==1 and gcd(z-1,N)==101
                    assert sat_split(N,bb,vv)[0]==101
                    print('single-row half exponent root:',z,'factor',gcd(z-1,N))
                    print('zero-rank prefixes checked:',tested);return
    print('zero-rank prefixes checked:',tested,'no factor by saturation')


if __name__=='__main__':
    test_powerfree();test_group();test_saturation();search()


def check_adaptive_pools():
    # Reproduce two earlier stalled local-CRT pools using their actual
    # adaptive algorithm, not the unknown factorization of either input.
    from adaptive_pooled_rank import step
    for N in (100160063,1000036000099):
        P=primes(7);H=min(N-1,5000*(isqrt(N)+1));old=[];pure=[]
        for attempt in range(25):
            d,result=step(N,P,H,old,pure,attempt,local=True,dual=True)
            assert d is None
            row,dep,gain,stats=result
            if gain is None:old.append(row)
            else:pure.append(gain)
        m=len(old)
        R=normalized_basis([x for A,x,y,s in old]+[y for A,x,y,s in old]);keys=list(R)
        rows=[A+[R[d][i]-R[d][i+m] for d in keys] for i,(A,x,y,s) in enumerate(old)]+[v+[0]*len(keys) for v in pure]
        assert len(old)==25 and not pure
        d,rank,steps,k=sat_split(N,P+keys,rows,stop=False)
        assert d is None and rank==25 and steps==25 and k==1
        print('adaptive saturation:',N,'residual rank',len(old),'pure rank',len(pure),'2-saturation steps',steps,'cyclic order',1<<k,'factor',d)


if __name__=='__main__':check_adaptive_pools()
