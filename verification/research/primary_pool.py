"""Exact small-prime saturation of signed relation pools, standard library.
No assumption of uniform coverage. See primary_pool_extraction.md.
"""
from math import gcd,isqrt
from itertools import combinations
from random import Random
from fractions import Fraction
from two_primary_pool import image,encode,sat_split,det_fraction,normalized_basis
from primitive_ratio_lattice import primes,primitive_pairs
from pooled_shift_relations import pool


def independent_rows(rows):
    piv={};ind=[];cols=[]
    for row in rows:
        v={j:Fraction(a) for j,a in enumerate(row) if a}
        while v:
            j=min(v);a=v[j]
            if j not in piv:
                piv[j]={i:z/a for i,z in v.items()};ind.append(list(row));cols.append(j);break
            for i,z in piv[j].items():
                v[i]=v.get(i,0)-a*z
                if not v[i]:del v[i]
    return ind,cols


def modular_dependency(rows,p):
    """Return nonzero coefficient vector in left kernel mod p, or None."""
    piv={}
    for i,row in enumerate(rows):
        v=[x%p for x in row];c=[0]*len(rows);c[i]=1
        for j in range(len(v)):
            x=v[j]
            if not x:continue
            if j not in piv:
                d=pow(x,-1,p);piv[j]=([z*d%p for z in v],[z*d%p for z in c]);break
            w,b=piv[j]
            v=[(z-x*t)%p for z,t in zip(v,w)]
            c=[(z-x*t)%p for z,t in zip(c,b)]
        else:
            assert any(c)
            return c
    return None


def l_saturate(rows,p):
    """Input integer Q-independent rows, p prime; return exact p-saturation."""
    rows=[list(v) for v in rows];steps=0
    while (c:=modular_dependency(rows,p)) is not None:
        i=next(i for i,a in enumerate(c) if a)
        d=pow(c[i],-1,p);c=[a*d%p for a in c]
        assert c[i]==1
        z=[sum(c[j]*rows[j][h] for j in range(len(rows))) for h in range(len(rows[0]))]
        assert all(a%p==0 for a in z)
        rows[i]=[a//p for a in z];steps+=1
    return rows,steps


def primary_group(N,vals,p,bound):
    """Factor or exhibit a cyclic p-group with faithful projection modulo every r|N.
    vals are units killed by p**bound. p must be prime, coprime to N.
    Returns (factor, order exponent, cyclic discrete-log coordinates).
    """
    d=gcd(N,p)
    if 1<d<N:return d,None,None
    assert d==1
    orders=[]
    for z in vals:
        assert gcd(z,N)==1
        a=z;k=0
        while a!=1:
            d=gcd(a-1,N)
            if 1<d<N:return d,None,None
            assert k<bound
            a=pow(a,p,N);k+=1
        orders.append(k)
    k=max(orders,default=0)
    if k==0:return None,0,[0]*len(vals)
    g=vals[orders.index(k)];top=pow(g,p**(k-1),N)
    assert top!=1 and pow(top,p,N)==1 and gcd(top-1,N)==1
    # top has exact order p at each prime divisor of N.
    powers=[1]
    for j in range(1,p):powers.append(powers[-1]*top%N)
    assert len(set(powers))==p
    logs=[]
    for u in vals:
        v=u;e=0
        for j in range(k):
            z=pow(v,p**(k-j-1),N)
            assert pow(z,p,N)==1
            # At every prime divisor r of N, z is one of these p powers.
            found=None
            for t,w in enumerate(powers):
                d=gcd(z-w,N)
                if 1<d<N:return d,None,None
                if d==N:found=t;break
            assert found is not None
            e+=found*p**j
            v=v*pow(g,-found*p**j,N)%N
            assert pow(v,p**(k-j-1),N)==1
        assert v==1 and pow(g,e,N)==u
        logs.append(e)
    return None,k,logs


def primary_readout(N,bases,signed_rows,limit):
    """Check every p-primary part for primes p<=limit of a saturated row span."""
    assert all(gcd(N,z)==1 for z in bases)
    assert all(image(N,bases,row) in (1,N-1) for row in signed_rows)
    ind,cols=independent_rows(signed_rows)
    rows=[[2*a for a in row] for row in ind]
    minor=abs(det_fraction([[row[j] for j in cols] for row in rows]))
    assert minor>0 # det(empty)=1
    report=[]
    for p in primes(limit):
        d=gcd(p,N)
        if 1<d<N:return d,report
        if minor%p:continue
        assert d==1
        m=minor;bound=0
        while m%p==0:m//=p;bound+=1
        sat,h=l_saturate(rows,p)
        assert h<=bound
        vals=[image(N,bases,v) for v in sat]
        assert all(pow(z,p**h,N)==1 for z in vals)
        d,k,_=primary_group(N,vals,p,h)
        report.append((p,h,k))
        if d:return d,report
    return None,report


def test_groups():
    count=0
    for N in (15,21,35,45,49,63,65,77,91,105,117,133,143,171,189,217,221,273,341):
        for p in (2,3,5,7):
            if gcd(p,N)>1:continue
            vs=[z for z in range(1,N) if gcd(z,N)==1 and pow(z,p**5,N)==1]
            for u in vs:
                for v in vs:
                    H={1};todo=[1]
                    for z in todo:
                        for x in (u,v):
                            w=z*x%N
                            if w not in H:H.add(w);todo.append(w)
                    # A locally faithful cyclic subgroup iff no nonidentity element
                    # becomes 1 mod a proper factor. Independent exhaustive oracle.
                    bad=any(1<gcd(z-1,N)<N for z in H)
                    d,k,logs=primary_group(N,[u,v],p,5)
                    assert (d is not None)==bad
                    if d:assert 1<d<N and N%d==0
                    else:assert len(H)==p**k
                    count+=1
    print('prime-primary subgroup comparisons:',count)


def test_indices():
    rng=Random(1109);count=0
    for p in (2,3,5,7,11):
        for _ in range(60):
            m=rng.randrange(1,7);r=rng.randrange(1,m+1)
            raw=[[p**rng.randrange(4)*rng.randrange(-9,10) for j in range(m)] for i in range(r)]
            ind,cols=independent_rows(raw);r=len(ind)
            g=0
            for cs in combinations(range(m),r):g=gcd(g,abs(det_fraction([[v[j] for j in cs] for v in ind])))
            assert g>0
            h0=0
            while g%p==0:g//=p;h0+=1
            sat,h=l_saturate(ind,p)
            assert h==h0 and modular_dependency(sat,p) is None
            # Every original row belongs to final lattice, solve against pivot columns.
            if r:
                # Independent exact determinant/Cramer verification of lattice inclusion.
                F=[[v[j] for v in sat] for j in cols]
                D=det_fraction(F);assert D!=0
                for v in ind:
                    c=[]
                    for i in range(r):
                        C=[row[:] for row in F]
                        for j,k in enumerate(cols):C[j][i]=v[k]
                        c.append(Fraction(det_fraction(C),D))
                    assert all(z.denominator==1 for z in c)
                    assert all(sum(c[i]*sat[i][j] for i in range(r))==v[j] for j in range(m))
            count+=1
    print('prime-saturation maximal-minor comparisons:',count)


def search_actual():
    # Predetermined enumeration of small odd composite test inputs. Trial
    # division here only selects composite test cases; no factors are passed
    # to the lattice relation generator or the extractor.
    tested=0
    for N in range(35,2000,2):
        if not any(N%d==0 for d in range(3,isqrt(N)+1,2)):continue
        if N%3==0:continue
        P=[2];H=min(N-1,4*(isqrt(N)+1))
        T=1
        while 2**T<=N*H*H:T+=1
        for t in range(T,T+20):
            d,pairs,_=primitive_pairs(N,pow(2,t,N),H,H)
            if d:continue
            for x,y in pairs:
                raw=[(2,t,0,x,y)];bases,rows=encode(N,P,raw)
                if not any(rows[0][1:]):continue
                h=0
                for a in rows[0]:h=gcd(h,abs(a))
                if h%3 and h%5 and h%7:continue
                d,_,_,_=sat_split(N,bases,rows,stop=False)
                if d:continue
                tested+=1
                d,report=primary_readout(N,bases,rows,3)
                if d:
                    assert 1<d<N and N%d==0 and pool(N,raw,P)[0]==0
                    assert (N,H,raw,bases,rows,d)==(1333,148,[(2,32,0,54,-125)],[2,3,5],[[33,3,-3]],43)
                    z=image(N,bases,[a//3 for a in rows[0]])
                    w=z*z%N
                    assert z==429 and pow(z,3,N)==N-1 and w==87 and pow(w,3,N)==1
                    assert gcd(w-1,N)==43
                    print('odd-primary-only raw fixture:',N,'H',H,'row',raw,'bases',bases,'valuations',rows,'report',report,'factor',d,'tested',tested)
                    print('cube root of sign',z,'order-three component',w,'gcd',d)
                    return
    raise AssertionError('expected fixture absent')


def stalled_pools():
    # Reconstruct the prior 25-call stalled local-CRT pools, with the same
    # adaptive algorithm and parameters, independently of their factors.
    from adaptive_pooled_rank import step
    for N in (100160063,1000036000099):
        P=primes(7);H=min(N-1,5000*(isqrt(N)+1));old=[];pure=[]
        for attempt in range(25):
            d,res=step(N,P,H,old,pure,attempt,local=True,dual=True)
            assert d is None
            row,dep,gain,stats=res
            if gain is None:old.append(row)
            else:pure.append(gain)
        assert len(old)==25 and not pure
        m=len(old);R=normalized_basis([x for A,x,y,s in old]+[y for A,x,y,s in old]);keys=list(R)
        rows=[A+[R[d][i]-R[d][i+m] for d in keys] for i,(A,x,y,s) in enumerate(old)]
        d,report=primary_readout(N,P+keys,rows,1000)
        if d:assert 1<d<N and N%d==0
        print('stalled pool prime-primary readout:',N,'rank',len(old),'report',report,'factor',d)


if __name__=='__main__':
    test_groups();test_indices();search_actual();stalled_pools()
