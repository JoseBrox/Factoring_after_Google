"""Support-aware adaptive rank search using a power-free gcd-free residual basis.
Standard library; no uniform bound on support escapes is assumed.
"""
from fractions import Fraction as Q
from math import gcd,isqrt,lcm,prod
from random import Random
from primitive_ratio_lattice import primitive_pairs,peel,primes,matrix_rank
from two_primary_pool import normalized_basis,sat_split
from pooled_shift_relations import exact_eliminate,sub
from adaptive_pooled_rank import annihilator,base_image,dot,dual_solution,recover,dependency


def prepare(old):
    """old is list of coprime positive residual ratios (x,y)."""
    m=len(old)
    D=normalized_basis([x for x,y in old]+[y for x,y in old])
    bases=list(D)
    rows=[{j:Q(D[d][i]-D[d][i+m]) for j,d in enumerate(bases) if D[d][i]!=D[d][i+m]} for i in range(m)]
    piv=exact_eliminate(rows)
    return bases,piv


def member(x,y,bases,piv):
    """Exact membership in old rational valuation span, no new gcd refinement."""
    g=gcd(x,y);x//=g;y//=g
    v={}
    for j,d in enumerate(bases):
        z=0
        while x%d==0:x//=d;z+=1
        while y%d==0:y//=d;z-=1
        if z:v[j]=Q(z)
    if x!=1 or y!=1:return None
    c={}
    while v:
        j=min(v);a=v[j]
        if j not in piv:return None
        r,z=piv[j];sub(v,r,a);sub(c,z,-a)
    return c


def outside(x,S):
    """Remove every prime divisor of S, without factoring S or x."""
    while (g:=gcd(x,S))>1:x//=g
    return x


def step(N,P,H,old,pure,attempt,recycle=True):
    q,w=annihilator(pure,len(P));J=(isqrt((N-1)//3)**2).bit_length()
    A0=[0]*len(P);mult=1;sig0=1
    if old and recycle:
        A0,u,v,sig0=old[attempt%len(old)];mult=v*pow(u,-1,N)%N
    sep=2*H.bit_length()*dual_solution(old,w)
    T=1+(sum(map(abs,A0))+J+2*H.bit_length()+sep)//1
    a=pow(P[q],T,N)*mult%N
    oldres=[(x,y) for A,x,y,s in old]
    bases,piv=prepare(oldres);assert len(piv)==len(old)
    S=prod(bases);best=None;best_score=None
    # ALL shifts, not only the first balanced shift. The collinear case is
    # cheap by the primitive-rectangle theorem; no heuristic sampling needed.
    for j in range(J+1):
        c=a*pow(2,j,N)%N
        d,pairs,_=primitive_pairs(N,c,H,H)
        if d:return d,None
        for x,y in pairs:
            rx,vx=peel(x,P);ry,vy=peel(y,P)
            dep=member(rx,ry,bases,piv)
            A=[A0[i]+T*(i==q)+j*(p==2)+vx.get(p,0)-vy.get(p,0) for i,p in enumerate(P)]
            sig=sig0*(1 if y>0 else -1)
            assert base_image(N,P,A)*rx*pow(ry,-1,N)%N==sig%N
            row=(A,rx,ry,sig)
            if dep is not None:
                den=lcm(*(v.denominator for v in dep.values()))
                gain=[den*A[i]-sum(int(den*z)*old[k][0][i] for k,z in dep.items()) for i in range(len(P))]
                assert dot(gain,w)>0 and base_image(N,P,[2*g for g in gain])==1
                # independent exact valuation dependency test (expensive; only for test)
                ref,_=dependency(oldres,(rx,ry));assert ref==dep
                return None,(row,gain,1,T.bit_length())
            score=outside(rx,S)*outside(ry,S)
            if best_score is None or (score,rx*ry)<(best_score,best[1]*best[2]):
                best=row;best_score=score
    assert best is not None
    # Validate negative membership by the earlier global refinement routine.
    ref,_=dependency(oldres,(best[1],best[2]));assert ref is None
    return None,(best,None,best_score,T.bit_length())


def run(N,P,H,limit,recycle=True):
    old=[];pure=[];escaped=0;support_preserving=0;bits=0;d=None;reason=None;mass=1
    for i in range(limit):
        d,z=step(N,P,H,old,pure,i,recycle)
        if d:reason="lattice gcd";break
        row,gain,score,Tbits=z;bits=max(bits,Tbits)
        if gain is None:
            old.append(row)
            escaped+=score>1;support_preserving+=score==1;mass*=score
        else:pure.append(gain)
        d,rank,coords=recover(N,P,pure)
        if d or rank==len(P):
            if d:reason="pure relation"
            break
    R=normalized_basis([x for A,x,y,s in old]+[y for A,x,y,s in old]);keys=list(R);m=len(old)
    raw=[A+[R[p][i]-R[p][i+m] for p in keys] for i,(A,x,y,s) in enumerate(old)]+[v+[0]*len(keys) for v in pure]
    d2,rank,steps,k=sat_split(N,P+keys,raw,stop=False)
    if d2 and not d:d=d2;reason="2-saturation"
    if d:assert 1<d<N and N%d==0
    print('support-aware:',N,'P',P[-1],'H',H,'recycle',recycle,'residual rank',len(old),'pure rank',len(pure),'support escapes',escaped,'support-only directions',support_preserving,'new support log2 upper bound',mass.bit_length()-1 if mass==1 else mass.bit_length(),'max exponent bits',bits,'factor',d,'method',reason,flush=True)
    return d,len(old),len(pure)


def tests():
    # Composite bases with nontrivial powers; an integer supported on the
    # same primes need not be in the old span (e.g. 3 versus 3^2*5^3).
    old=[(3**4*5**6,7**4),(3**2*5**3,11**2)]
    B,piv=prepare(old)
    count=0
    for x in [1,3,5,7,9,11,49,121,3**2*5**3,3**4*5**6,3**6*5**9]:
        for y in [1,3,5,7,11,49,121,3**2*5**3,3**4*5**6]:
            z=member(x,y,B,piv);w,_=dependency(old,(x,y));assert z==w;count+=1
    rng=Random(319)
    for _ in range(100):
        old=[]
        for i in range(5):
            u,v=rng.randrange(1,2000),rng.randrange(1,2000);g=gcd(u,v);u//=g;v//=g
            if dependency(old,(u,v))[0] is None:old.append((u,v))
        B,piv=prepare(old)
        for i in range(10):
            x,y=rng.randrange(1,2000),rng.randrange(1,2000)
            g=gcd(x,y);x//=g;y//=g
            z=member(x,y,B,piv);w,_=dependency(old,(x,y));assert z==w;count+=1
        c=[rng.randrange(-3,4) for _ in old];x=y=1
        for (u,v),e in zip(old,c):
            if e>=0:x*=u**e;y*=v**e
            else:x*=v**(-e);y*=u**(-e)
        g=gcd(x,y);x//=g;y//=g
        z=member(x,y,B,piv);assert z is not None and all(z.get(i,0)==c[i] for i in range(len(c)));count+=1
    print('factor-free membership comparisons:',count,flush=True)
    for N in (100160063,1000036000099):
        for recycle in (False,True):run(N,primes(17),3*(isqrt(N)+1),40,recycle)

if __name__=='__main__':tests()
