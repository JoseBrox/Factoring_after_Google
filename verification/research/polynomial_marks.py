"""Exact algebraic checks; numerical log solve only proposes a certificate.
Requires SymPy and mpmath. Run: python verification/research/polynomial_marks.py
"""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, lcm
import sympy as sp
import mpmath as mp


def eval_poly(c, x):
    z = 0
    for a in reversed(c):
        z = z*x+a
    return z


def root_poly(roots):
    p = [1]
    for r in roots:
        q = [0]*(len(p)+1)
        for i, a in enumerate(p):
            q[i] -= r*a
            q[i+1] += a
        p = q
    return p


def sign_at(c, x_num, x_den):
    z, scale = c[-1], 1
    for a in reversed(c[:-1]):
        scale *= x_den
        z = z*x_num+a*scale
    return (z > 0)-(z < 0)


def check_construction():
    N, ell = 1000036000099, 227
    n = N.bit_length()
    d = 2
    while d*d < 64*n:
        d *= 3
    m = 1 << ((4*n+d-1)//d)
    assert sp.isprime(ell) and ell > 4*d and ell % 9 in (2, 5)
    assert gcd(2*ell, N) == 1
    D = d//2
    den = 4*(ell*d)**(d//8)
    u = 1 << isqrt(n)
    for i in (1, 2):
        centers = [12*ell*j+(2*j if i == 1 else 6*ell)
                   for j in range(1, d+1)]
        p = root_poly(centers)
        f = p[:]
        f[0] += ell if i == 1 else 1
        f[D] += ell if i == 1 else 1
        c = (-eval_poly(f, m)*pow(2*ell, -1, N)) % N
        for j in range(D):
            c, a = divmod(c, m)
            f[j] += 2*ell*a
        assert c == 0
        f[0] -= 2*ell*m*u
        f[1] += 2*ell*(u+m*u)
        f[2] -= 2*ell*u
        assert f[-1] == 1 and eval_poly(f, m) % N == 0
        assert [a % 2 for a in f] == [int(j in (0, D, d)) for j in range(d+1)]
        assert [a % ell for a in f] == ([a % ell for a in p] if i == 1 else
                                        [int(j in (0, D, d)) for j in range(d+1)])
        assert all(sign_at(f, r*den-1, den)*sign_at(f, r*den+1, den) == -1
                   for r in centers)
    print('monic construction: N=%d d=%d ell=%d all %d sign brackets verified' % (N,d,ell,2*d))


def check_extraction():
    x = sp.symbols('x')
    N, m, ell, H, B = 77, 6, 5, 40, 199
    F = [(0,-19,-25), (-1,-5,4)]
    def pol(f):
        A, B0, C = f
        return x**3+A*x*x+B0*x+C
    def norm(f, g):
        A, B0, C = f
        a,b,c = g
        h = (-c*C,a-c*B0,b-c*A)
        k = (-h[2]*C,h[0]-h[2]*B0,h[1]-h[2]*A)
        return abs(a*(h[1]*k[2]-h[2]*k[1])-b*(h[0]*k[2]-h[2]*k[0])+c*(h[0]*k[1]-h[1]*k[0]))
    assert all(sp.Poly(pol(f),x).is_irreducible and pol(f).subs(x,m)%N == 0 for f in F)
    assert all(sp.discriminant(pol(f),x)>0 for f in F)
    D = abs(int(sp.discriminant(pol(F[0]),x)*sp.discriminant(pol(F[1]),x)*sp.resultant(pol(F[0]),pol(F[1]),x)))
    P = [int(p) for p in sp.primerange(2,B+1) if D%int(p)]
    def squarefree(n):
        if not n: return None
        a = []
        for p in P:
            if n%p == 0:
                n //= p
                if n%p == 0: return None
                a.append(p)
            if n == 1: return a
        return a if n == 1 else None
    roots = {(i,p):[r for r in range(p) if (r**3+f[0]*r*r+f[1]*r+f[2])%p==0]
             for i,f in enumerate(F) for p in P}
    assert len(roots[0,ell]) == 3 and not roots[1,ell]
    cols, used = [], set()
    for g in product(range(-H,H+1), repeat=3):
        # Deliberately suppress direct GCD hits to test the exponent mechanism.
        if next((v for v in g if v),0)<=0 or gcd(eval_poly(g,m),N)!=1: continue
        L = [squarefree(norm(f,g)) for f in F]
        if any(z is None for z in L): continue
        c = []
        for i, l in enumerate(L):
            assert norm(F[i],g) == abs(int(sp.resultant(pol(F[i]),sum(g[j]*x**j for j in range(3)),x)))
            for p in l:
                rr = [r for r in roots[i,p] if eval_poly(g,r)%p==0]
                assert len(rr) == 1
                c.append((i,p,rr[0]))
        cols.append((g,c)); used.update(c)
    target = {(0,ell,r) for r in roots[0,ell]}
    rows = sorted(used|target)
    V = sp.Matrix([[int(r in c) for g,c in cols] for r in rows])
    b = sp.Matrix([int(r in target) for r in rows])
    _, pivot = V.rref()
    assert len(pivot) == len(rows)
    W = V[:,list(pivot)]
    den = abs(int(W.det(method='domain-ge')))
    W_inv = W.inv()
    C0 = -den*W_inv*b
    free = [j for j in range(len(cols)) if j not in pivot]
    K = -den*W_inv*V[:,free]
    assert all(z.q==1 for z in C0) and all(z.q==1 for z in K)
    # Numerical log solve is merely a candidate generator. Its rank and errors
    # are NOT certified. The integer relation and modular result below are exact.
    mp.mp.dps = 160
    rootsR = [[mp.mpf(str(r)) for r in sp.nroots(pol(f),n=155,maxsteps=500)] for f in F]
    logs = mp.matrix(4,len(cols))
    for j,(g,c) in enumerate(cols):
        vals = [mp.log(abs(eval_poly(g,r))) for rr in rootsR for r in rr]
        for i,(a,b0) in enumerate([(0,2),(1,2),(3,5),(4,5)]):
            logs[i,j] = vals[a]-vals[b0]
    Lp = mp.matrix([[logs[i,j] for j in pivot] for i in range(4)])
    c0 = [int(z) for z in C0]
    targetL = -(Lp*mp.matrix(c0))
    A = Lp*mp.matrix([[int(K[i,j]) for j in range(len(free))] for i in range(len(pivot))])+den*mp.matrix([[logs[i,j] for j in free] for i in range(4)])
    selected, basis = [], []
    for j in range(A.cols):
        z = A[:,j]; orig = mp.norm(z)
        for v in basis: z -= v*(v.T*z)[0]
        t = mp.norm(z)
        if t > mp.mpf('1e-80')*max(1,orig):
            basis.append(z/t); selected.append(j)
        if len(basis)==4: break
    assert len(selected)==4
    M = mp.matrix([[A[i,j] for j in selected] for i in range(4)])
    sol = mp.lu_solve(M,targetL)
    rat = [Fraction(mp.nstr(z,155)).limit_denominator(10**8) for z in sol]
    Q = lcm(*(r.denominator for r in rat))
    E = den*Q
    cc = [0]*len(cols)
    for i,j in enumerate(pivot):
        cc[j] = Q*c0[i]+sum(int(Q*r)*int(K[i,k]) for r,k in zip(rat,selected))
    for r,k in zip(rat,selected): cc[free[k]] = den*int(Q*r)
    assert V*sp.Matrix(cc) == -E*b
    M = 2*E
    assert pow(ell,M,N)==1
    print('polynomial marks: retained=%d rows=%d exact rational rank=%d' % (len(cols),len(rows),len(pivot)))
    print('exponent certificate: base=%d M=%d modular power=%d' % (ell,M,pow(ell,M,N)))
    h = M
    while h%2==0: h//=2
    while h<=M:
        z = pow(ell,h,N); g = gcd(z-1,N)
        if 1<g<N:
            print('split: gcd(%d-1,%d)=%d' % (z,N,g)); return
        h *= 2
    raise AssertionError('no split')


if __name__ == '__main__':
    check_construction()
    check_extraction()
