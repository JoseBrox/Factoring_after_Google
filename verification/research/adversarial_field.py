"""Finite exact check of a deliberately adverse quadratic field parameter.
The proof does not factor any resultant norm; SymPy is used for polynomial gcds.
"""
from math import gcd, prod
from itertools import combinations
import sympy as S
X,Z=S.symbols('X Z')


def polynomial_basis(marks):
    """Pairwise coprime constant-one basis and its exact exponents."""
    k=len(marks)
    rows=[(S.Poly(g,X,domain=S.ZZ),S.eye(k)[i,:]) for i,g in enumerate(marks)]
    def merge(rows):
        out=[]
        for h,v in rows:
            assert h.eval(0)==1
            if h.degree()==0:continue
            for j,(p,w) in enumerate(out):
                if h==p:
                    out[j]=(h,w+v);break
            else:out.append((h,v))
        return out
    rows=merge(rows)
    splits=0
    while True:
        for i,j in combinations(range(len(rows)),2):
            h,v=rows[i];p,w=rows[j]
            g=S.gcd(h,p)
            if g.degree()==0:continue
            assert abs(g.eval(0))==1
            if g.eval(0)==-1:g=-g
            rows=merge([row for t,row in enumerate(rows) if t not in (i,j)]+
                [(h.exquo(g),v),(g,v+w),(p.exquo(g),w)])
            splits+=1;break
        else:break
    for h,p in combinations([g for g,v in rows],2):assert S.gcd(h,p).degree()==0
    for i,g in enumerate(marks):
        assert S.Poly(prod(h.as_expr()**int(v[i]) for h,v in rows),X)==S.Poly(g,X)
    return [h for h,v in rows],splits


def strip(z,M):
    while True:
        q=gcd(z,M)
        if q==1:return z
        z//=q


def fixture():
    N=1000036000099; ell=5; a=(ell-1)//2
    special=1+a*X
    marks=[1+t*X for t in range(-8,9) if t]+[1+X+X**2,1-3*X+2*X**2,1+5*X+6*X**2,1+X**3,special]
    assert all(g.subs(X,0)==1 and gcd(int(g.subs(X,2*(ell+1))),N)==1 for g in marks)
    basis,splits=polynomial_basis(marks)
    assert S.Poly(special,X) in basis
    results={}
    for i,j in combinations(range(len(basis)),2):
        q=abs(int(S.resultant(basis[i],basis[j],X)))
        assert q>0; results[i,j]=q
    R=ell*prod(results.values())
    R0=strip(R,2*N)
    assert R0%2 and gcd(R0,N)==1 and R0%ell==0
    K=2*max(abs(int(h.eval(2))).bit_length() for h in basis)+1
    fZ=(X-2)**2+Z*special
    lower=100
    for h in basis:
        if h==S.Poly(special,X):continue
        P=S.Poly(S.resultant(fZ,h.as_expr(),X),Z)
        assert P.degree()==h.degree() and P.LC()!=0
        assert P.eval(0)==h.eval(2)**2
        lower=max(lower,2*(sum(abs(int(z)) for z in P.all_coeffs()[1:])+abs(int(h.eval(2)))**2)+2)
    q=2*ell**2*R0**K
    r=(-4*pow(q,-1,N))%N
    if r%2==0:r+=N
    r+=2*N*max(0,(lower-q*r+2*N*q-1)//(2*N*q))
    C=q*r; f=S.Poly((X-2)**2+C*special,X)
    assert C>=lower and C%4==2 and C%ell**2==0 and (C+4)%N==0
    assert f.is_irreducible and S.discriminant(f)>0
    cert=0
    for i,h in enumerate(basis):
        norm=abs(int(S.resultant(f,h,X)))
        if h==S.Poly(special,X):assert norm==ell**2;continue
        assert norm>abs(int(h.eval(2)))**2 and gcd(norm,2*N)==1
        # Remove every prime supported on R0, without factoring it.
        residual=strip(norm,R0)
        assert residual>1 and norm//residual<=abs(int(h.eval(2)))**2
        assert gcd(residual,ell)==1
        assert all(gcd(residual,q)==1 for (j,k),q in results.items() if i in (j,k))
        cert+=1
    print('mark polynomials',len(marks),'gcd-free factors',len(basis),'refinements',splits)
    print('C bit length',C.bit_length(),'private-support certificates',cert,'of',len(basis)-1)
    print('all nonexceptional factor exponents forced to zero; remaining norm ell^2 forces trivial unit')

if __name__=='__main__':fixture()
