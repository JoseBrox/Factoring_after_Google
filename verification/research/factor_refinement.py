"""Exact prototype of Ge's ideal factor refinement over monic power orders.

Requires SymPy. This deliberately small reference implementation verifies
ideal equalities and comaximality; no integer or ideal prime factorization
is used. It is not a bit-complexity benchmark or a coverage experiment.
"""
from itertools import combinations
from math import gcd, lcm
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form


def lattice(M):
    M = S.Matrix(M)
    den = lcm(*(int(x.q) for x in M))
    assert all((x*den).q == 1 for x in M)
    H = hermite_normal_form((M*den).applyfunc(S.Integer))
    assert H.rows == H.cols == M.rows and H.det() != 0
    return H/den


class Order:
    def __init__(self, coefficients):
        # ascending coefficients, monic polynomial
        self.f = list(map(S.Integer, coefficients))
        self.d = len(self.f)-1
        assert self.f[-1] == 1
        self.A = S.eye(self.d)
        self.one = self.A[:, 0]

    def reduce(self, coeffs):
        a = list(map(S.Rational, coeffs))
        a += [S.Integer(0)] * max(0, self.d-len(a))
        for i in range(len(a)-1,self.d-1,-1):
            for j in range(self.d):
                a[i-self.d+j] -= a[i]*self.f[j]
        return S.Matrix(a[:self.d])

    def mul(self, a, b):
        c = [S.Integer(0)]*(2*self.d-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                c[i+j] += x*y
        return self.reduce(c)

    def matrix(self, a):
        return S.Matrix.hstack(*(self.mul(a,self.A[:,i]) for i in range(self.d)))

    def principal(self, a, C):
        return lattice(self.matrix(a)*C)

    def product(self, I, J):
        return lattice(S.Matrix.hstack(*(self.mul(I[:,i],J[:,j])
            for i in range(self.d) for j in range(self.d))))

    def sum(self,I,J):
        return lattice(S.Matrix.hstack(I,J))

    def colon(self,I,J):
        # xJ subset I iff I^{-1} M_{j} x is integral for every basis vector j.
        # The solution lattice is the dual of the row lattice of the stacked system.
        inverse = I.inv()
        rows = S.Matrix.vstack(*(inverse*self.matrix(J[:,j]) for j in range(self.d)))
        return lattice(lattice(rows.T).inv().T)

    def norm_index(self,C,J):
        v = abs(J.det()/C.det())
        assert v.q == 1 and v >= 1
        return int(v)

    def contains(self, I, J):
        return all(x.q==1 for x in I.inv()*J)

    def make_invertible(self,C,J):
        steps = 0
        while True:
            inverse = self.colon(C,J)
            C1 = self.colon(inverse,inverse)
            assert self.contains(C1,C)
            if C1==C:
                assert self.product(J,inverse)==C
                return C,J,steps
            steps += 1
            assert self.norm_index(C1,C)>=2
            J = self.product(J,C1)
            C = C1

    def refine(self, values):
        C = self.A
        ideals = [self.principal(a,C) for a in values]
        k = len(values)
        rows = [(J,S.eye(k)[i,:]) for i,J in enumerate(ideals) if J!=C]
        steps = enlargements = 0
        # Ge's refinement: all starting principal ideals are invertible.
        def merge(rows,C):
            merged=[]
            for J,v in rows:
                if J==C: continue
                for i,(K,w) in enumerate(merged):
                    if J==K:
                        merged[i]=(K,w+v)
                        break
                else:
                    merged.append((J,v))
            return merged
        rows = merge(rows,C)
        while True:
            found=None
            indices=[self.norm_index(C,J) for J,_ in rows]
            for i,j in combinations(range(len(rows)),2):
                if gcd(indices[i],indices[j])==1: continue
                H=self.sum(rows[i][0],rows[j][0])
                if H!=C:
                    found=(i,j,H);break
            if found is None: break
            i,j,H=found
            C1,H,t=self.make_invertible(C,H)
            if C1!=C:
                rows=[(self.product(J,C1),v) for J,v in rows]
                C=C1;enlargements+=t
            J,v=rows[i];K,w=rows[j]
            J1,K1=self.colon(J,H),self.colon(K,H)
            assert self.product(J1,H)==J and self.product(K1,H)==K
            rows=merge([r for h,r in enumerate(rows) if h not in (i,j)]
                       +[(J1,v),(H,v+w),(K1,w)],C)
            steps+=1
        for (J,_),(K,_) in combinations(rows,2):
            assert self.sum(J,K)==C
        for i,a in enumerate(values):
            Z=C
            for J,v in rows:
                for _ in range(int(v[i])): Z=self.product(Z,J)
            assert Z==self.principal(a,C)
        F=S.Matrix.vstack(*(v for _,v in rows)) if rows else S.zeros(0,k)
        return C,F,steps,enlargements


def nonmaximal_fixture():
    K=Order([-8,0,1]) # theta=2 sqrt(2), initial discriminant 32
    values=[K.reduce(a) for a in [[2],[0,1],[3],[1,1]]]
    C,F,steps,enlargements=K.refine(values)
    assert enlargements>=1
    assert C.det()==S.Rational(1,2)
    assert F*S.Matrix([-3,2,0,0])==S.zeros(F.rows,1) # theta^2 = 2^3
    print('nonmaximal order: overorder index',1/C.det(),
          'refinement steps',steps,'enlargements',enlargements,'matrix rank',F.rank())


def target_fixture():
    # Manufactured rank-deficient example; N=15 is deliberately known.
    # The first two marks satisfy exact product 16 in field 1, 1 in field 2.
    # Additional composite-norm marks are present; their norms are not factored.
    fields=[Order([30,-47,1]),Order([45,-47,1])]
    polys=[[-1,1],[-46,1],[-2,1],[-4,1],[-7,1],[1,2],[7,2,1],[-11,1]]
    N=15
    assert all(gcd(g[0],N)==1 for g in polys)
    mats=[]
    for i,K in enumerate(fields):
        vs=[K.reduce([2 if i==0 else 1])]+[K.reduce(g) for g in polys]
        C,F,steps,enlargements=K.refine(vs)
        mats.append(F)
        assert K.mul(vs[1],vs[2])==(16 if i==0 else 1)*K.one
        print('field',i+1,':',len(vs),'elements,',F.rows,'refined ideal rows,',
              steps,'refinements,',enlargements,'enlargements')
    F=S.Matrix.vstack(*mats)
    v=S.Matrix([4,-1,-1]+[0]*(len(polys)-2))
    assert F*v==S.zeros(F.rows,1)
    assert pow(2,4,N)==1 and gcd(pow(2,2,N)-1,N)==3
    print('joint matrix:',F.shape,'rank',F.rank(),'; exact target certificate 2^4=1 mod 15, factor 3')


if __name__=='__main__':
    nonmaximal_fixture()
    target_fixture()
