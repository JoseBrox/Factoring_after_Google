"""Quadratic rank-one certificate: exact 2-adic exponent recovery.
No real logarithm calculations or factorization of N.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt, lcm, prod


def primes(B):
    a = bytearray(b'\x01')*(B+1)
    a[:2] = b'\x00\x00'
    for p in range(2,isqrt(B)+1):
        if a[p]: a[p*p:B+1:p] = b'\x00'*((B-p*p)//p+1)
    return [p for p in range(2,B+1) if a[p]]


def v2(n):
    if not n: raise ValueError('zero valuation')
    n=abs(n)
    return (n & -n).bit_length()-1


class Quadratic:
    """Z[X]/(X^2+bX+c) in the basis 1, X."""
    def __init__(self,b,c):self.b,self.c=b,c
    def mul(self,x,y,m=None):
        a,t=x; r,s=y; z=t*s
        v=(a*r-self.c*z,a*s+t*r-self.b*z)
        return tuple(i%m for i in v) if m else v
    def norm(self,x):
        a,t=x
        return a*a-self.b*a*t+self.c*t*t
    def inv(self,x,m):
        a,t=x; w=pow(self.norm(x),-1,m)
        return ((a-self.b*t)*w%m,-t*w%m)
    def pow(self,x,k,m):
        if k<0:x=self.inv(x,m); k=-k
        z=(1,0)
        while k:
            if k&1:z=self.mul(z,x,m)
            k//=2
            if k:x=self.mul(x,x,m)
        return z


def unit_coordinate(K,a,ell,relation):
    return compact_coordinate(K,a,ell,[(1,t,1,e) for t,e in relation.items()])


def compact_coordinate(K,a,ell,factors):
    """Recover k with alpha^(4Q)=u^(4k), for an actual unit alpha.
    Caller verifies the valuation equations. Return k, Q, precision.
    u=(1+a theta)/ell must be an algebraic unit of infinite order.
    Factors are (r,t,den,e), representing ((r+t theta)/den)^e.
    Each numerator and denominator must be invertible modulo 2.
    """
    assert ell%2 and K.b%2==0 and K.c%4==2
    assert K.norm((1,a))==ell*ell
    # R=2+max(|b|,|c|) bounds every conjugate |theta|.
    R=2+max(abs(K.b),abs(K.c))
    # Norm-one u: conjugate absolute values are reciprocal. Each <=1+|a|R.
    # Thus |log |sigma(u)|| < J/5 for J=6 * bit_length(1+|a|R).
    J=6*(1+abs(a)*R).bit_length()
    Q=lcm(*range(1,J+1))
    # Norm separation > 1/3 in two embeddings implies |log |u||>1/5.
    # For nonzero integral marks, both abs(log) <= bit_length(1+|t|R).
    assert factors and all(den>0 and den%2 and K.norm((r,t))%2 for r,t,den,e in factors)
    H=max(max(1,abs(r)+abs(t)*R).bit_length()+den.bit_length()
          for r,t,den,e in factors)
    A=sum(abs(e) for r,t,den,e in factors)
    bound=5*Q*H*A
    bits=(2*bound+1).bit_length()+1
    # v=u^4 in the 2-local power order. Compute the exact valuation of v-1.
    num=K.mul(K.mul((1,a),(1,a)),K.mul((1,a),(1,a)))
    diff=(num[0]-ell**4,num[1])
    t0=min(v2(z) for z in diff if z)
    assert t0>=2
    m=1<<(t0+bits)
    v=tuple(z*pow(ell**4,-1,m)%m for z in num)
    alpha=(1,0)
    for r,t,den,e in factors:
        inverse=pow(den,-1,m)
        alpha=K.mul(alpha,K.pow((r*inverse%m,t*inverse%m),e,m),m)
    y=K.pow(alpha,4*Q,m)
    residual=y
    # Bit lifting in cyclic <v> with exact order 2^bits modulo m.
    r=0; step=v
    for j in range(bits):
        small=1<<(t0+j+1)
        if (residual[0]%small,residual[1]%small)!=(1,0):
            r+=1<<j
            residual=K.mul(residual,K.inv(step,m),m)
        assert (residual[0]%small,residual[1]%small)==(1,0)
        step=K.mul(step,step,m)
    assert residual==(1,0) and K.pow(v,r,m)==y
    k=r if r<(1<<(bits-1)) else r-(1<<bits)
    assert abs(k)<=bound
    return k,Q,t0+bits


def fixture(N=77,ell=5,B=1000,T=200000):
    q=2*ell**2; r=(-4*pow(q,-1,N))%N
    if r%2==0:r+=N
    C=q*r; a=(ell-1)//2; b=C*a-4; c=C+4
    D=b*b-4*c
    K=Quadratic(b,c)
    assert c%N==0 and c%4==2 and b%2==0 and D>0
    assert K.norm((1,a))==ell**2
    assert (b+4)%ell==0 and (4+2*b+c)%ell**2==0
    ps=primes(B); cols=[]; rows=set()
    for t in range(1,T+1):
        z=abs(K.norm((1,t)))
        if not z or gcd(z,D)>1:continue
        v=z; col={}
        for p in ps:
            if p>v:break
            if v%p==0:
                e=0
                while v%p==0:v//=p;e+=1
                rr=(-pow(t,-1,p))%p
                assert (rr*rr+b*rr+c)%p==0 and (2*rr+b)%p!=0
                col[p,rr]=e
            if v==1:break
        if v==1:
            assert z==prod(p**e for (p,rr),e in col.items())
            cols.append((t,col)); rows.update(col)
        if len(cols)>len(rows)+2:break
    before=(len(cols),len(rows))
    active=set(range(len(cols))); inc=defaultdict(set)
    for j,(t,col) in enumerate(cols):
        for rr in col:inc[rr].add(j)
    while True:
        gone=set()
        for ss in inc.values():
            ss=ss&active
            if len(ss)==1:gone|=ss
        if not gone:break
        active-=gone
    cols=[cols[j] for j in sorted(active)]
    rows=sorted(set().union(*(set(v) for t,v in cols)))
    print('before/after peeling',before,(len(cols),len(rows)))
    def sub(x,y,t):
        for j,z in y.items():
            x[j]=x.get(j,0)-t*z
            if not x[j]:del x[j]
    piv={}
    for j,(t,v) in enumerate(cols):
        x={rr:Fraction(e) for rr,e in v.items()}; y={j:Fraction(1)}
        while x:
            rr=max(x)
            if rr not in piv:
                e=x[rr];piv[rr]=({k:w/e for k,w in x.items()},{k:w/e for k,w in y.items()});break
            e=x[rr];p,py=piv[rr];sub(x,p,e);sub(y,py,e)
        else:
            den=lcm(*(v.denominator for v in y.values()))
            coef={j:int(v*den) for j,v in y.items()}
            assert all(sum(k*cols[j][1].get(rr,0) for j,k in coef.items())==0 for rr in rows)
            relation={cols[j][0]:e for j,e in coef.items()}
            moment=sum(t*e for t,e in relation.items())
            print('relation support',len(relation),'first jet mod c',moment%c,'gcd with N',gcd(moment,N))
            k,Q,precision=unit_coordinate(K,a,ell,relation)
            if not k:continue
            x=Fraction(k,Q)
            E=2*abs(x.numerator)
            # Reducing k/Q is sound because Q0=den(x) is also a unit-lattice
            # denominator; alpha^Q0 and u^numerator have the same real logs.
            assert pow(ell,E,N)==1
            z=E
            while z%2==0:z//=2
            while z<=E:
                h=gcd(pow(ell,z,N)-1,N)
                if 1<h<N:
                    print('exact 2-adic recovery',x,'precision',precision,'bits','E',E,'factor',h)
                    return x,E,h
                z*=2
    raise AssertionError('no transverse relation in the tested list')


def known_coordinate_checks():
    tests=0
    for N,ell in [(77,5),(143,7),(221,3),(899,11),(1000036000099,5)]:
        assert gcd(ell,N)==1
        q=2*ell**2; r=(-4*pow(q,-1,N))%N
        if r%2==0:r+=N
        a=(ell-1)//2
        while True:
            C=q*r; b=C*a-4; c=C+4
            if b*b>4*c:break
            r+=2*N
        K=Quadratic(b,c)
        assert c%N==0 and c%4==2 and b%2==0
        assert K.norm((1,a))==ell**2
        assert (b+4)%ell==0 and (4+2*b+c)%ell**2==0
        for exponent in (0,1,-1,17,-123456789,2**250+137,-2**301+11):
            for sign in (0,1):
                k,Q,_=compact_coordinate(K,a,ell,[(1,a,ell,exponent),(-1,0,1,sign)])
                assert k==Q*exponent
                tests+=1
    print('signed compact-coordinate checks:',tests)


def norm_gap_checks():
    N=1000036000099; ell=5; a=(ell-1)//2
    q=2*ell**2;r=(-4*pow(q,-1,N))%N
    if r%2==0:r+=N
    C=q*r; K=Quadratic(C*a-4,C+4)
    H=100
    assert C>=N-4 and C-9*H**2>N//2
    count=0
    for r in range(-H,H+1):
        for t in range(-H,H+1):
            z=K.norm((r,t))
            assert z==(r+2*t)**2+C*t*(t-a*r)
            if t*(t-a*r):
                assert abs(z)>=C-9*H**2>N//2
                count+=1
    print('exact norm-gap checks:',count)


if __name__=='__main__':
    assert fixture()==(Fraction(-2064690),4129380,11)
    known_coordinate_checks()
    norm_gap_checks()
