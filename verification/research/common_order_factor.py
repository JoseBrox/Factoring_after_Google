"""Exact finite tests of a common-congruence small-root endpoint.
Uses SymPy for integer LLL and polynomial roots. The theorem is in
primary_pool_extraction.md. No claim of uniform subgroup-order coverage.
"""
from math import gcd, comb
import sympy as S
from primary_pool import primary_readout
from two_primary_pool import powerfree


def determinant_bound(N,h,m,d,X):
    # Exact fourth-power inequality for sqrt(d)*2^((d-1)/4)*det^(1/d) < 2^(hm).
    det=N**(m*(m+1)//2)*X**(d*(d-1)//2)
    return d**(2*d)*2**(d*(d-1))*det**4 < 2**(4*d*h*m)


def small_roots(N,c,h,m,d,X):
    """All roots z in [0,X) of z+c modulo any divisor >=2^h.
    Assumes the exact determinant guard. Integer roots of one LLL vector suffice.
    """
    assert 1<=m<d and 0<=c<N and X>=1 and determinant_bound(N,h,m,d,X)
    B=[]
    for i in range(m):
        row=[0]*d
        for j in range(i+1):row[j]=N**(m-i)*comb(i,j)*c**(i-j)*X**j
        B.append(row)
    for i in range(d-m):
        row=[0]*d
        for j in range(m+1):row[i+j]=comb(m,j)*c**(m-j)*X**(i+j)
        B.append(row)
    A=S.Matrix(B)
    # SymPy 1.14's PythonMPQ fallback can round large fractions through
    # float in math.floor. Use exact integer division for this local call.
    import sympy.polys.matrices.lll as lllmod
    old_floor=lllmod.mfloor
    try:
        lllmod.mfloor=lambda q:int(q.numerator)//int(q.denominator)
        R,T=A.lll_transform(delta=S.Rational(3,4))
    finally:
        lllmod.mfloor=old_floor
    assert T*A==R and abs(T.det())==1
    v=list(map(int,R[0,:]));assert any(v)
    assert d*sum(a*a for a in v)<2**(2*h*m)
    assert all(a%X**i==0 for i,a in enumerate(v))
    coeff=[a//X**i for i,a in enumerate(v)]
    z=S.Symbol('z');f=S.Poly.from_list(coeff[::-1],z,domain=S.ZZ)
    roots=[int(t) for t in f.ground_roots() if t.q==1 and 0<=t<X]
    assert all(f.eval(t)==0 for t in roots)
    return sorted(roots),d


def finite_factor(N,C,step=4,m=5):
    """Finite version using a guessed divisor-bit bucket and exact LLL guard.
    The asymptotic theorem uses different explicit parameters.
    """
    assert 1<C<N and gcd(C,N)==1
    n=N.bit_length();blocks=0;dims=[]
    for h in range((C.bit_length()-1)//step*step,n//2+1,step):
        if h<1:continue
        d=(m*n+h-1)//h
        z=h*h//n
        while z>=0 and not determinant_bound(N,h,m,d,1<<z):z-=1
        if z<0:continue
        X=1<<z
        K=((1<<(h+step))-1)//C
        for k in range(0,K+1,X):
            c=(pow(C,-1,N)+k)%N
            rr,_=small_roots(N,c,h,m,d,X)
            blocks+=1;dims.append(d)
            for r in rr:
                g=gcd(1+C*(k+r),N)
                if 1<g<N:return g,blocks,max(dims),X
    return None,blocks,max(dims,default=0),None


def next_p(C,k):
    while not S.isprime(C*k+1):k+=1
    return C*k+1


def test_common_modulus():
    C=1<<24
    # Construct inputs with a supplied known common divisor of p-1. Factors
    # are used ONLY for construction and independent verification, not recovery.
    tests=[(next_p(C,1031),next_p(C,1<<18)),
           (next_p(C,1<<14),next_p(C,(1<<14)+100)),
           (next_p(C,11),next_p(C,100),next_p(C,300))]
    for fs in tests:
        N=1
        for p in fs:N*=p
        d,calls,dim,X=finite_factor(N,C)
        assert d and 1<d<N and N%d==0
        print('common-modulus LLL fixture: bits',N.bit_length(),'C bits',C.bit_length(),'factors',len(fs),'LLL calls',calls,'max dim',dim,'X',X,'proper factor',d)


def test_faithful_endpoint():
    C=1<<24;p=next_p(C,1031);q=next_p(C,1<<18);N=p*q
    # Manufactured subgroup to exercise the readout->LLL interface ONLY.
    # Do not use this fixture as evidence for construction of the subgroup.
    gp=pow(int(S.primitive_root(p)),(p-1)//C,p)
    gq=pow(int(S.primitive_root(q)),(q-1)//C,q)
    g=(gp+p*((gq-gp)*pow(p,-1,q)%q))%N
    assert powerfree(g)==(g,1)
    assert pow(g,C,N)==1
    factor,report=primary_readout(N,[g],[[C]],13)
    assert factor is None
    D=1
    for ell,h,k in report:D*=ell**k
    assert D==C
    d,calls,dim,X=finite_factor(N,D)
    assert d and N%d==0 and 1<d<N
    print('faithful-subgroup endpoint: report',report,'C',D,'factor',d,'LLL calls',calls)


if __name__=='__main__':
    test_common_modulus();test_faithful_endpoint()
