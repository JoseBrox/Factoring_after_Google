# Effective exact number-field certificate reconstruction

**Status:** independent written derivation of the precision and output-size
bounds in TryPair, assuming the exact valuation and unit-lattice facts of
the manuscript. Determinant clearing, determinant heights and binary
modular powering are already verified components. This note does not
claim that the ideal-valuation construction or the full extractor has
been kernel-certified.

Use the manuscript's \(D=D_{\rm row}\ge d+1\ge10\), \(L_0\ge10\),
\(K=DL_0\), \(n=2d-2\), \(P=64d^3K\).
The valuation matrix V has integral 0/1 entries, at most \(L_0\)
nonzero entries per column. The target vector b is integral 0/1 with
exactly d nonzero entries. Assume \(b\in\operatorname{im}_{\mathbb Q}V\)
and that the archimedean map of the integral valuation kernel spans
\(\mathbb R^n\), as in the extractor promises.

## 1. Integral pivots and bounded columns

Choose a nonsingular pivot submatrix A of order r=rank(V), with
determinant \(\Delta\ne0\), by exact fraction-free elimination.
Every k-square minor has absolute value at most \(L_0^{k/2}\)
by Hadamard, since each restricted column has Euclidean norm
at most \(\sqrt{L_0}\). This also bounds the adjugate entries by
\(L_0^{D/2}\).

Let \(E_0=|\Delta|\). On the pivot coordinates define
\(c^{(0)}=-\operatorname{sgn}(\Delta)\operatorname{adj}(A)b_I\),
zero elsewhere. Since the pivot rows span the row space, the
pivot-row equality implies \(Vc^{(0)}=-E_0b\).
For each free column \(v_j\), put \(c^{(j)}_j=\Delta\),
put its pivot coordinates equal to
\(-\operatorname{adj}(A)(v_j)_I\), and put other free coordinates
zero. These are in the integral kernel and are a rational basis
of the rational kernel, because their free-coordinate matrix is
\(\Delta I\). Their support sizes are at most \(D+1\), and their
l1 norms are bounded by
\[
 C_0=(D+1)L_0^{D/2+1}+d(D+1)L_0^{D/2}
 \le 2d(D+1)L_0^{D/2+1}.
\]
The inequality also covers c(0). For example
\(\log_2(2d(D+1))\le D+1\) for \(D\ge10\), and
\(\log_2 L_0\le.35L_0\). Thus
\(\log_2 C_0< K/2\). The exact matrix can be computed by fraction-free
elimination with intermediate entries bounded by minors (or by
rational elimination with reduced fractions); every operation
has polynomial bit cost in the dimensions and K.

## 2. Lattice separation and uniform archimedean heights

The actual normalized root distances lie in \([2^{-L_0},1]\),
so their logarithms have absolute value at most \(L_0\log2<L_0\).
The Helmert map has orthonormal rows, hence each combined
archimedean vector has Euclidean norm at most \(\sqrt{2d}L_0\).
Since \(D,L_0\ge10\), \(\log_2(\sqrt{2d}L_0)<K/2-1\).
All images
\[
 u_0=U_{\rm arch}c^{(0)},\qquad m_j=U_{\rm arch}c^{(j)}
\]
have norm at most \(H=2^K\) (in fact smaller by a fixed factor).

They lie in the product of the two projected log-unit lattices.
For each totally real field, if a unit not equal to \(\pm1\) had
all log embeddings of absolute value at most \(1/3\), then
all its squared absolute embeddings would be less than 2
(\(e^{2/3}<2\)). The absolute norm of its nonzero algebraic
integer \(\epsilon^2-1\) would be a product of numbers smaller
than 1, impossible. Hence its log vector has Euclidean norm
greater than \(1/3\). Helmert projection preserves this norm
on the sum-zero hyperplane by the unit norm identity.
Minkowski applied to the open cube of side
\(2/(3\sqrt{d-1})\) gives covolume at least
\((3\sqrt{d-1})^{-(d-1)}\) for each unit lattice.
For their product lattice \(\mathcal L\),
\[
 \det\mathcal L>(9d)^{-d}>2^{-dK}.
 \tag{1}
\]
This is a geometric lower bound, not a procedure computing a
fundamental unit basis.

## 3. Certified approximations, rank selection and determinant bounds

Bisection of the d disjoint rational isolating intervals with
opposite signs produces approximations to all normalized roots to
absolute error \(2^{-2P}\), using \(O(P)\) exact sign tests per root.
The cleared-denominator integers in each sign test have
\(O(dP+dL_0)\) bits. The distance guard ensures every logarithm
can be approximated by evaluating it at the rational root
approximation, with additional error at most \(2^{L_0+1-2P}\)
by the mean value theorem. Compute logs and Helmert entries to
dyadic precision \(2^{-2P-16}\); multiplication and summation
give approximations to the archimedean vectors, including the
pivot combinations, with Euclidean error at most \(2^{-P/2}\)
after rounding to \(P\) bits. This much weaker bound than the
source's \(2^{-.99P}\) suffices for every test below.
For a direct elementary log routine, reduce a positive rational
to \(2^k t\) with \(1\le t<2\) by exact comparisons, and use
\[
 \log t=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1},
 \quad z=(t-1)/(t+1)\in[0,1/3].
\]
The tail after m terms is bounded by
\(2(1/3)^{2m+1}/(1-1/9)\); the same series for \(\log2\)
handles the scaling. Taking \(O(P+\log(1+|k|))\) terms and
using exact rationals (or controlled dyadic rounding) costs
polynomial bit operations. Rational square-root bisection
suffices for the Helmert entries. None of this invokes a
precision oracle.

Let \(\varepsilon=2^{-P/2}\).
For a candidate matrix of k selected columns
\(M\in\mathbb R^{n\times k}\), \(k\le n\), each column norm is
at most H and each approximating column has error at most
\(\varepsilon\). Every entry of the two Gram matrices is
bounded by \(4H^2\); their entrywise difference is at most
\(3H\varepsilon\) by Cauchy–Schwarz.
The Leibniz formula and the telescoping product difference
\(\prod a_i-\prod b_i=
 \sum_j(a_j-b_j)\prod_{i<j}a_i\prod_{i>j}b_i\)
give the explicit Gram determinant error bound
\[
 |\det(\widehat M^T\widehat M)-\det(M^TM)|
 \le k!\,k(4H^2)^{k-1}\,3H\varepsilon
 <\tfrac12\,2^{-5dK}.
 \tag{2}
\]
The last inequality follows, for \(k\le2d\), from
\(K\ge10(d+1)\), \(\log_2(k!k)\le(k+1)\log_2 k\le 2dK\),
and \(P/2=32d^3K\). This leaves a substantial margin.

Inductively extend any linearly independent k-1 columns by
one of the remaining m_j to a full n-column independent list.
For the full matrix M_full, its lattice index is a positive
integer and \(|\det M_{\rm full}|\ge\det\mathcal L\).
Hadamard in the orthogonal complement of the first k columns
(or Gram–Schmidt) gives
\[
 \det(M^TM)\ge
 (\det\mathcal L)^2/H^{2(n-k)}
 >2^{-2d\log_2(9d)-(4d-6)K}>2\,2^{-5dK}.
\]
The last comparison uses
\(2d\log_2(9d)+1 < (d+6)K\) for the indicated parameters.
Thus selecting the largest approximate Gram determinant
and checking it exceeds \(2^{-5dK}\) always finds an independent
column under the hypotheses, by (2), and yields a full matrix
\(M_U\). All tests use rational matrices with \(O(P)\)-bit entries
and exact polynomial-time determinant arithmetic. There is no
test comparing floating-point rank to zero.

## 4. Rational coordinates, certified recovery and output exponent

Since all columns and u0 lie in \(\mathcal L\),
\(x=-M_U^{-1}u_0\) is rational in any integral basis of that
lattice. Integral Cramer clearing shows its reduced denominators
all divide the same integer index
\[
 E_1=|\det M_U|/\det\mathcal L
 \le H^n(9d)^d< D_*:=2^{3dK}.
 \tag{3}
\]
Cramer's rule and (1) bound \(\|x\|_\infty\le2^{4dK}\):
a numerator determinant has modulus at most \(n!H^n\)
by the Leibniz bound; \(\log_2(n!)\le n\log_2 n <dK\).
The same product-telescoping determinant estimate as in (2)
gives \(|\det\widehat M_U|\ge\frac12|\det M_U|\),
since the entry error is at most \(\varepsilon\) and
\(|\det M_U|>2^{-dK}\).
Cofactor bounds then give every entry of
\(\widehat M_U^{-1}\) absolute value at most \(2^{4dK}\).
Compute the exact rational
\(\widehat x=-\widehat M_U^{-1}\widehat u_0\) by rational elimination.
Subtracting the two systems yields the rigorous error bound
\[
 \|\widehat x-x\|_\infty
 \le n\,2^{4dK}(\varepsilon+n\varepsilon\,2^{4dK})
 <\frac1{2D_*^2}.
\]
The strict inequality follows from \(P/2=32d^3K\) and \(n\le2d\).
For each coordinate, two distinct reduced rationals with positive
denominators at most \(D_*\) have separation at least \(D_*^{-2}\),
by cross multiplication. Legendre's continued-fraction theorem
implies that the unique rational within \(1/(2D_*^2)\) of
\(\widehat x_i\) is a convergent. List the convergents of the
exact rational approximation by the Euclidean algorithm and
select the one meeting the denominator and distance tests.
Its numerator/denominator input has polynomial bit length
by determinant/cofactor bounds after clearing dyadic denominators;
the Euclidean algorithm has a number of divisions linear in
the operand bit lengths (two remainder steps at least halve the
larger bound). Thus this reconstruction is polynomial in the
parameters, not a loop over \(D_*\) possible denominators.

Let Q be the lcm of the recovered denominators. By (3), \(Q\mid E_1\);
in particular \(Q<D_*\), not \(D_*^n\).
The integral combination
\(c=Qc^{(0)}+\sum_i (Qx_i)c^{(j_i)}\) has the prescribed valuation
vector and zero projected log vector. Under the manuscript's
ideal-valuation and localization hypotheses its two field products
are torsion units, hence signs, and the already verified modular
cancellation gives \(\ell^{2E_0Q}=1\bmod N\).
The returned exponent \(E=2E_0Q\) is positive even, and
\[
 \log_2 E\le1+K+3dK<P.
\]
The algorithm verifies the modular power by binary exponentiation.
All numeric guards and finite searches thus have polynomial
bit costs in \(A,B,d,D,P\), under the stated algebraic hypotheses.

## Remaining formal boundary

The verified determinant and unit-lattice clearing modules establish
the basic exact algebra. Mathlib already contains the Legendre
convergent theorem for the canonical continued fractions. The
remaining Lean work is to connect the exact valuation/norm and
localization construction to the actual polynomial number fields,
the projected lattice/covolume bound, perturbation and rank tests,
certified approximation algorithms, and the final finite bit
machine. A written precision bound is not a proof that all these
implementations have already been certified.
