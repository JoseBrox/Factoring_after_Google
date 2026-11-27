"""Factor-free squareclass membership, square-target lattices and parity extraction.
Exact standard-library finite tests. No uniform coverage claim.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt, prod
from random import Random
from primitive_ratio_lattice import primitive_pairs, rect_count, primes, peel, factorfree_columns
from two_primary_pool import normalized_basis, image, sat_split


def is_square(x):
    return x >= 0 and isqrt(x)**2 == x


def support_part(x,d):
    rem=x
    while (g:=gcd(rem,d))>1:
        rem//=g
    return x//rem,rem


def squareclass_coordinates(x,y,bases):
    """Signed rational x/y, y>0. Return bits, or None outside basis span.
    Bit zero is the sign; other bits encode pairwise coprime nonsquare bases.
    Even valuations outside the basis are allowed. No factorization.
    """
    assert x and y>0
    z=abs(x)*y;v=int(x<0)
    for j,d in enumerate(bases,1):
        part,z=support_part(z,d)
        if is_square(part):continue
        if not is_square(part*d):return None
        v|=1<<j
    return v if is_square(z) else None


def gf2_insert(piv,v,c):
    """Insert binary vector retaining a row-combination bitset."""
    while v:
        k=v.bit_length()-1
        if k not in piv:
            piv[k]=(v,c);return None
        u,d=piv[k];v^=u;c^=d
    return c


def gf2_solve(piv,v):
    c=0
    while v:
        k=v.bit_length()-1
        if k not in piv:return None
        u,d=piv[k];v^=u;c^=d
    return c


class SquarePool:
    """Keep independent squareclasses of ratios with known modular roots.
    Compare all first-level squareclass dependencies as they arrive.
    """
    def __init__(self,N):
        assert N>2 and N%2
        self.N=N;self.rows=[];self.bases=[];self.piv={};self.dependencies=0

    def rebuild(self):
        # gcd-free basis of all retained numerators and denominators. Perfect
        # power normalization makes each basis nonsquare.
        D=normalized_basis([abs(y) for x,y,t in self.rows]+[x for x,y,t in self.rows])
        self.bases=list(D);self.piv={}
        for i,(x,y,t) in enumerate(self.rows):
            v=squareclass_coordinates(y,x,self.bases)
            assert v is not None
            assert gf2_insert(self.piv,v,1<<i) is None
        assert len(self.piv)==len(self.rows)

    def add(self,x,y,t):
        N=self.N
        assert x>0 and y and gcd(x*y,N)==1 and gcd(t,N)==1
        assert (t*t*x-y)%N==0
        v=squareclass_coordinates(y,x,self.bases)
        c=None if v is None else gf2_solve(self.piv,v)
        if c is None:
            self.rows.append((x,y,t));self.rebuild();return None
        self.dependencies+=1
        sel=[(x,y,t)]+[row for i,row in enumerate(self.rows) if c>>i&1]
        z=Q(1);w=1
        for a,b,r in sel:z*=Q(b,a);w=w*r%N
        assert z>0 and is_square(z.numerator) and is_square(z.denominator)
        root=isqrt(z.numerator)*pow(isqrt(z.denominator),-1,N)%N
        h=root*pow(w,-1,N)%N
        assert h*h%N==1
        if h in (1,N-1):return None
        d=gcd(h-1,N);assert 1<d<N and N%d==0
        return d


def parity_keys_batch(ratios):
    """Incremental gcd splitting for parity only; pairwise coprime nonsquare
    bases with bit masks indicating odd exponents in each input ratio.
    No integer factorization and no repeated global gcd refinement.
    """
    active=[]
    for i,r in enumerate(ratios):
        bit=1<<i
        for z in (abs(r.numerator),r.denominator):
            if is_square(z):continue
            nxt=[]
            for d,mask in active:
                if z==1:nxt.append((d,mask));continue
                if gcd(z,d)==1:nxt.append((d,mask));continue
                t,z=support_part(z,d)
                if is_square(t):nxt.append((d,mask));continue
                if is_square(t*d):
                    if mask^bit:nxt.append((d,mask^bit))
                    continue
                # Refine just these two overlapping integers. Other supports
                # are disjoint and never enter this gcd refinement.
                for e,(u,v) in factorfree_columns([d,t]).items():
                    m=(mask if u%2 else 0)^(bit if v%2 else 0)
                    if m and not is_square(e):nxt.append((e,m))
            if z>1 and not is_square(z):nxt.append((z,bit))
            active=nxt
    keys=[int(r<0) for r in ratios]
    for j,(d,mask) in enumerate(active,1):
        while mask:
            k=mask&-mask;keys[k.bit_length()-1]|=1<<j;mask-=k
    return keys


def extract_batch(N,raw,report=False):
    """Check a basis of every binary dependency of a pool with known roots.
    Returns (proper factor or None, independent raw rows, dependency count).
    """
    ratios=[Q(y,x) for x,y,t in raw]
    keys=parity_keys_batch(ratios);piv={};ind=[];deps=0
    for i,(r,key) in enumerate(zip(ratios,keys)):
        x,y,t=raw[i];assert x>0 and gcd(x*y*t,N)==1 and (t*t*x-y)%N==0
        c=gf2_insert(piv,key,1<<i)
        if c is None:ind.append(raw[i]);continue
        deps+=1;support=c.bit_count();z=Q(1);w=1
        while c:
            k=c&-c;j=k.bit_length()-1;c-=k
            z*=ratios[j];w=w*raw[j][2]%N
        h=square_root_of_ratio(N,z)*pow(w,-1,N)%N
        assert h*h%N==1
        if h not in (1,N-1):
            d=gcd(h-1,N);assert 1<d<N and N%d==0
            if report:
                print('parity certificate:',N,'support',support,'product bits',z.numerator.bit_length(),z.denominator.bit_length(),'known root',w,'involution',h)
            return d,ind,deps
    return None,ind,deps


def test_batch():
    rng=Random(9371);count=0;factors=0
    for N in (15,21,77,91,143,221,899,1763):
        for _ in range(60):
            raw=[]
            for i in range(15):
                t=rng.randrange(1,N);x=rng.randrange(1,N)
                if gcd(t*x,N)!=1:continue
                y=t*t*x%N
                if rng.randrange(2):y-=N
                raw.append((x,y,t))
            rr=[Q(y,x) for x,y,t in raw]
            new=parity_keys_batch(rr);old=ratio_keys(rr)
            # Compare dependency spaces, not arbitrary coordinate labels.
            p1={};p2={}
            for i,(u,v) in enumerate(zip(new,old)):
                assert gf2_insert(p1,u,1<<i)==gf2_insert(p2,v,1<<i)
            d,ind,dep=extract_batch(N,raw)
            P=SquarePool(N);f=None
            for x,y,t in raw:
                f=P.add(x,y,t)
                if f:break
            assert (d is None)==(f is None)
            if d:assert N%d==0 and 1<d<N;factors+=1
            else:assert len(ind)==len(P.rows) and dep==P.dependencies
            count+=1
    print('incremental parity refinement and batch extraction:',count,'comparisons,',factors,'factor exits')


def ratio_keys(ratios):
    """Factor-free exact parity keys of arbitrary signed rational ratios."""
    D=normalized_basis([abs(r.numerator) for r in ratios]+[r.denominator for r in ratios])
    bases=list(D);keys=[squareclass_coordinates(r.numerator,r.denominator,bases) for r in ratios]
    assert all(k is not None for k in keys)
    return keys


def square_root_of_ratio(N,r):
    assert r>0 and is_square(r.numerator) and is_square(r.denominator)
    return isqrt(r.numerator)*pow(isqrt(r.denominator),-1,N)%N


def same_residue_collision(N,ratios,arity=1):
    """All ratios must be equal modulo N. Search equal squareclasses of
    products of arity one or two; compare to one representative per key.
    """
    ratios=list(dict.fromkeys(ratios));keys=ratio_keys(ratios)
    assert arity in (1,2)
    if ratios:
        a=ratios[0].numerator*pow(ratios[0].denominator,-1,N)%N
        assert all(r.numerator*pow(r.denominator,-1,N)%N==a for r in ratios)
    tab={};collisions=0
    words=((i,) for i in range(len(ratios))) if arity==1 else ((i,j) for i in range(len(ratios)) for j in range(i,len(ratios)))
    for w in words:
        k=0;r=Q(1)
        for i in w:k^=keys[i];r*=ratios[i]
        if k not in tab:tab[k]=r;continue
        s=tab[k]
        if r==s:continue
        collisions+=1
        z=square_root_of_ratio(N,r/s);assert z*z%N==1
        if arity==1 and max((r/s).numerator,(r/s).denominator)<= (N//2)**2:
            # The height bound is on the *reduced square root*, not the ratio.
            rr=r/s;u,v=isqrt(rr.numerator),isqrt(rr.denominator)
            assert u!=v and u+v<N
            assert z not in (1,N-1)
        d=gcd(z-1,N)
        if 1<d<N:return d,collisions,len(tab),(r,s,z)
    return None,collisions,len(tab),None


def square_shift_pairs(N,t,H,J=None):
    """Known square roots retained under dyadic root shifts."""
    if J is None:J=N.bit_length()
    rows=[];shifts=0
    for j in range(J+1):
        root=t*pow(2,j,N)%N
        d,ps,_=primitive_pairs(N,root*root%N,H,H)
        if d:return d,rows,shifts
        rows.extend((x,y,root) for x,y in ps);shifts+=1
    return None,rows,shifts


def true_squareclass(x,y):
    # Finite independent oracle by trial division, used only in tests.
    z=abs(x)*y;bits={-1} if x<0 else set();p=2
    while p*p<=z:
        while z%p==0:
            z//=p
            if p in bits:bits.remove(p)
            else:bits.add(p)
        p+=1
    if z>1:bits.add(z)
    return frozenset(bits)


def test_membership():
    rng=Random(8794);count=0
    for bases in ([12,75], [12,175,11], [18,35,13], [2,3,5,7], []):
        # use only pairwise coprime nonsquare bases
        if any(gcd(a,b)!=1 for i,a in enumerate(bases) for b in bases[i+1:]):continue
        table={}
        for s in product((0,1),repeat=len(bases)+1):
            z=(-1 if s[0] else 1)*prod(d**e for d,e in zip(bases,s[1:]))
            table[true_squareclass(z,1)]=sum(a<<j for j,a in enumerate(s))
        for _ in range(500):
            x=rng.randrange(-10000,10001) or 1;y=rng.randrange(1,10001)
            assert squareclass_coordinates(x,y,bases)==table.get(true_squareclass(x,y));count+=1
        for k in table.values():
            d=(-1 if k&1 else 1)*prod(a for i,a in enumerate(bases,1) if k>>i&1)
            assert squareclass_coordinates(d*101**2,103**2,bases)==k;count+=1
    print('factor-free squareclass membership:',count,'exact comparisons')


def test_pool():
    rng=Random(55331);count=0;factor_count=0;dep=0
    # Compare streaming extractor with independent full binary kernel test.
    for N in (15,21,35,77,91,143,221,899):
        for _ in range(30):
            P=SquarePool(N);raw=[];full_piv={};reference=False
            for i in range(10):
                t=rng.randrange(1,N);x=rng.randrange(1,N)
                if gcd(t*x,N)!=1:continue
                y=t*t*x%N
                if rng.randrange(2):y-=N
                raw.append((x,y,t))
                f=P.add(x,y,t)
                cs=[true_squareclass(y,x) for x,y,t in raw]
                allp=sorted(set().union(*cs));piv={};bad=False
                for j,c in enumerate(cs):
                    v=sum(1<<k for k,p in enumerate(allp) if p in c)
                    h=gf2_insert(piv,v,1<<j)
                    if h is not None:
                        r=Q(1);s=1
                        for k,(a,b,t) in enumerate(raw):
                            if h>>k&1:r*=Q(b,a);s=s*t%N
                        z=square_root_of_ratio(N,r)*pow(s,-1,N)%N
                        if z not in (1,N-1):bad=True
                assert (f is not None)==bad
                if f:assert 1<f<N and N%f==0;factor_count+=1;break
                assert len(P.rows)==len(piv);count+=1
            dep+=P.dependencies
    print('online parity kernel:',count,'independent comparisons,',factor_count,'factor exits,',dep,'dependencies')


def search():
    # All exact ratios at square shifts of known t; no input factorization.
    for N in (77,143,221,899,1333,1763,2491,3233,10403,47053,100160063,1000036000099):
        S=isqrt(N)+1
        for H in (S,2*S,3*S):
            if H>=N//2:continue
            for q in (2,3,5,7):
                if gcd(q,N)!=1:continue
                t=pow(q,N.bit_length(),N)
                # only even shifts, normalized by the small square shift
                rr=[];raw=[];failed=False
                K=8
                for s in range(1,K+1):
                    if gcd(s,N)>1:failed=True;break
                    root=t*s%N
                    d,vs,_=primitive_pairs(N,root*root%N,H,H)
                    if d:failed=True;break
                    for x,y in vs:
                        rr.append(Q(y,x*s*s));raw.append((x,y,root))
                if failed or not rr:continue
                d,nc,nk,witness=same_residue_collision(N,rr,1)
                if d:
                    print('bounded square-shift collision:',N,'H',H,'q',q,'rows',len(raw),'distinct',len(set(rr)),'root',witness,'factor',d)
                    return
    print('No bounded square-shift collision fixture found')


def stalled():
    # Different square-target family on two inputs where earlier greedy
    # rational-rank/primary searches had stalled. The input factors are not
    # used. Retain an independent squareclass basis after each batch.
    for N in (100160063,1000036000099):
        H=3*(isqrt(N)+1);P=primes(7);old=[];count=deps=0;d=None;attempt=0
        for T in range(N.bit_length(),N.bit_length()+4):
            for q in P:
                t=pow(q,T,N);d,rows,j=square_shift_pairs(N,t,H)
                if d:break
                count+=len(rows);attempt+=1
                d,old,nc=extract_batch(N,old+rows,report=True);deps+=nc
                if d:break
            if d:break
        if d:assert 1<d<N and N%d==0
        print('square-target pool:',N,'H',H,'target batches',attempt,'rows',count,'parity rank',len(old),'dependencies',deps,'factor',d,flush=True)


if __name__=='__main__':
    test_membership();test_pool();test_batch();search();stalled()
