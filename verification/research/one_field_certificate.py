"""Exact finite extraction for the rank-one field, using only the stdlib.
All log bounds are directed rational/integer interval calculations.
This is a finite fixture, not a worst-case coverage experiment.
"""
from math import gcd, isqrt, lcm
from fractions import Fraction as Q
from collections import defaultdict


def primes(B):
    a=bytearray(b'\x01')*(B+1)
    a[:2]=b'\0\0'
    for p in range(2,isqrt(B)+1):
        if a[p]:a[p*p:B+1:p]=b'\0'*((B-p*p)//p+1)
    return [p for p in range(2,B+1) if a[p]]


def ceildiv(a,b):return -((-a)//b)


PREC=96
S=1<<PREC


def unit_log(z):
    """Enclose 2 atanh(z), 0<=z<=1/3, in integer units of 1/S."""
    assert 0<=z<=Q(1,3)
    l=(z.numerator*S)//z.denominator
    h=ceildiv(z.numerator*S,z.denominator)
    l2=l*l//S; h2=ceildiv(h*h,S)
    L=H=0
    for j in range(PREC):
        L+=2*l//(2*j+1)
        H+=ceildiv(2*h,2*j+1)
        l=l*l2//S;h=ceildiv(h*h2,S)
    # Exact omitted tail <= 2*3^(-2PREC-1)/(1-1/9) < 1/S.
    assert 2*S*9<8*3**(2*PREC+1)
    return L,H+1


LOG2=unit_log(Q(1,3))


def logq(v):
    assert v>0
    k=v.numerator.bit_length()-v.denominator.bit_length()
    def two(k):return Q(2**k) if k>=0 else Q(1,2**(-k))
    while v<two(k):k-=1
    while v>=two(k+1):k+=1
    w=v/two(k)
    L,H=unit_log((w-1)/(w+1))
    if k>=0:return L+k*LOG2[0],H+k*LOG2[1]
    return L+k*LOG2[1],H+k*LOG2[0]


def sub(v,w,t):
    for k,z in w.items():
        v[k]=v.get(k,0)-t*z
        if not v[k]:del v[k]


def main():
    N,ell=77,5
    # d=2: f=X^2+b X+c=(X-2)^2+C(1+aX).
    # A small valid C is enough for this finite fixture, rather than
    # the uniform generous real-root bound of the general construction.
    q=2*ell**2;r=(-4*pow(q,-1,N))%N
    if r%2==0:r+=N
    C=q*r;a=(ell-1)//2;b=C*a-4;c=C+4;D=b*b-4*c
    assert c%N==0 and b%2==0 and c%4==2 and D>0
    assert C%ell**2==0 and 1-b*a+c*a*a==ell**2
    # u=(1+a theta)/ell=1+a (theta-2)/ell is integral:
    assert (4+b)%ell==0 and (4+2*b+c)%ell**2==0
    # Its norm is 1 by the preceding norm identity.
    print('field:',b,c,'discriminant',D)
    B,T=1000,200000
    ps=primes(B);cols=[];rows=set()
    for t in range(1,T+1):
        z=abs(1-b*t+c*t*t)
        if not z or gcd(z,D)>1:continue
        v=z;row={}
        for p in ps:
            if p>v:break
            if v%p==0:
                e=0
                while v%p==0:v//=p;e+=1
                # p cannot divide t since the norm is 1 mod p then.
                rr=(-pow(t,-1,p))%p
                assert (rr*rr+b*rr+c)%p==0 and (2*rr+b)%p!=0
                row[(p,rr)]=e
            if v==1:break
        if v==1:
            assert z==__import__('math').prod(p**e for (p,rr),e in row.items())
            cols.append((t,row));rows.update(row)
        if len(cols)>len(rows)+2:break
    print('before peeling:',len(cols),'marks',len(rows),'rows')
    active=set(range(len(cols)));inc=defaultdict(set)
    for j,(t,v) in enumerate(cols):
        for rr in v:inc[rr].add(j)
    while True:
        gone=set()
        for ss in inc.values():
            ss=ss&active
            if len(ss)==1:gone|=ss
        if not gone:break
        active-=gone
    cols=[cols[j] for j in sorted(active)]
    rows=sorted(set().union(*(set(v) for t,v in cols)))
    print('after peeling:',len(cols),'marks',len(rows),'rows')
    # Choose the more negative real root, bounded with exact integer sqrt.
    w=isqrt(D*S*S)
    th_lo=Q(-b*S-w-1,2*S);th_hi=Q(-b*S-w,2*S)
    def abslog(t,den=1):
        lo=-(1+t*th_hi)/den;hi=-(1+t*th_lo)/den
        assert 0<lo<=hi
        return logq(lo)[0],logq(hi)[1]
    UL,UH=abslog(a,ell)
    # The rank-one unit lattice has shortest vector >1/3. In the
    # two-real-embedding coordinates the basis vector has length
    # sqrt(2)*log|u|. Its lattice index is <3 sqrt(2) log|u|<100.
    assert 0<UL<=UH and 6*UH<100*S
    piv={}
    for j,(t,v) in enumerate(cols):
        x={rr:Q(z) for rr,z in v.items()};y={j:Q(1)}
        while x:
            rr=max(x)
            if rr not in piv:
                z=x[rr]
                piv[rr]=({k:w/z for k,w in x.items()},
                         {k:w/z for k,w in y.items()})
                break
            z=x[rr];p,py=piv[rr];sub(x,p,z);sub(y,py,z)
        else:
            den=lcm(*(v.denominator for v in y.values()))
            coef={j:int(v*den) for j,v in y.items()}
            # Exact ideal valuations at unramified simple roots.
            assert all(sum(k*cols[j][1].get(rr,0) for j,k in coef.items())==0 for rr in rows)
            L=H=0
            for j,k in coef.items():
                lo,hi=abslog(cols[j][0])
                if k<0:lo,hi=hi,lo
                L+=k*lo;H+=k*hi
            endpoints=[Q(z,w) for z in (L,H) for w in (UL,UH)]
            lo,hi=min(endpoints),max(endpoints)
            if lo<=0<=hi:continue
            x=((lo+hi)/2).limit_denominator(100)
            assert lo<=x<=hi
            # A rational of denominator <=100 is unique within this
            # interval, since distinct such rationals differ >=1/100^2.
            assert hi-lo<Q(1,10000)
            E=2*abs(x.numerator)
            assert E and pow(ell,E,N)==1
            z=E
            while z%2==0:z//=2
            while z<=E:
                h=gcd(pow(ell,z,N)-1,N)
                if 1<h<N:
                    print('certified relation:',len(coef),'marks, coefficient bits',max(abs(k).bit_length() for k in coef.values()),'coordinate',x)
                    print('interval width < 1/10000; exact exponent',E,'factor',h)
                    return
                z*=2
    raise AssertionError('no verified nontrivial unit relation')

if __name__=='__main__':main()
