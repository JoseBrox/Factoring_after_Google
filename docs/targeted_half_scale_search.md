# Exact targeted certificate search at the half scale

**Status (26 November 2026): proved written algebraic and complexity
results for the certificate search; general-factorization coverage is
still open.** This note weakens and partly bypasses the COV hypothesis
in [the polynomial-mark construction](monic_polynomial_mark_factorer.md).
In particular, an exact decision of the target relation is possible
without a full unit-rank hypothesis, a squarefree restriction or any
probabilistic approximation. It does not prove that a successful
certificate exists for every sufficiently large input.

The objective here is the actual \(L_N[1/2,O(1)]\) scale, not just
the family of powers \(1/2+\varepsilon\). We do not advance to the
one-third target until uniform worst-case coverage at the half scale
is proved.

## 1. The precise target, and why COV is excessive

Let \(f_1,f_2\) be monic irreducible totally real integer polynomials,
of degrees \(d_1,d_2\), with distinct simple real roots and a common
known evaluation root \(m\bmod N\). Use the fields
\(K_i=\mathbb Q(\theta_i)\). Let \(\ell\nmid N\) be a known prime.
For simplicity retain the split/inert condition of the earlier
construction at \(\ell\), and exclude \(\ell\) from both polynomial
discriminants. The target \(b\) has value 1 at every prime ideal over
\(\ell\) in the first field, and 0 everywhere else. More generally its
nonzero entries could be the ramification indices of \((\ell)\).

For each available nonzero polynomial mark \(g_j\in\mathbb Z[X]\)
assume its two field values are nonzero and \(g_j(m)\) is a unit
modulo \(N\). Allow arbitrary signed integral exponents, repeated
prime-ideal valuations and prime ideals of arbitrary residue degree.
Let
\[
 V_{(i,\mathfrak p),j}=v_{\mathfrak p}(g_j(\theta_i))\in\mathbb Z_{\ge0}
\]
with all nonzero rows included, together with the target rows.
Define the matrix \(L\) of the two orthogonally projected real
logarithm vectors as in the earlier note. Set
\(D=d_1+d_2-2\). The exact relation sought is
\[
 Vc=-E b,\qquad Lc=0,\qquad
 c\in\mathbb Z^{M},\quad E\in\mathbb Z_{>0}.                 \tag{T}
\]
Here \(M\) is the number of marks. For this target the first equation
makes
\[
 \ell^E\prod_j g_j(\theta_1)^{c_j},\qquad
 \prod_j g_j(\theta_2)^{c_j}
\]
units in the full rings of integers. Their logs are the projected logs
\(Lc\), because their norms have absolute value one and the rational
scalar has constant log vector. Hence (T) makes them signs. Clearing
negative powers gives identities in the two monic orders
\(\mathbb Z[\theta_i]\). Evaluating those identities at \(m\bmod N\),
and using the unit guards, proves
\[
 \ell^{2E}=1\bmod N.                                       \tag{1}
\]
In particular the proof never evaluates an arbitrary element of the
maximal order modulo \(N\).

The earlier condition (E) required that \(b\) lie in the rational
valuation image and the projected log map of the integral kernel span
all of \(\mathbb R^D\). Only the first assertion and **one particular
log-vector membership** are needed.

### Theorem 1 (exact target criterion)

If \(b\notin\operatorname{im}_{\mathbb Q}V\), (T) is impossible.
Otherwise find an integral particular vector \(c_0\) with
\(Vc_0=-E_0 b,\ E_0>0\), and a finite list \(k_j\) of integral
vectors spanning the rational kernel of \(V\). Put
\[
 x=-Lc_0,\quad U_j=Lk_j,\quad S=\operatorname{span}_{\mathbb R}\{U_j\}.
\]
Then (T) holds if and only if \(x\in S\).

**Necessity.** If \(c,E\) satisfy (T),
\(E_0c-Ec_0\) is an integral valuation-kernel vector, and its log
image is \(Ex\). Hence \(x\in S\).

**Sufficiency.** All \(U_j\) and \(x\) belong to the discrete lattice
\(\mathcal L\) of projected logs of the product of the two unit
groups. Choose independent columns \(U_{j_1},\ldots,U_{j_k}\)
spanning \(S\). They generate a full-rank sublattice of
\(\mathcal L_S=\mathcal L\cap S\), of finite positive integral index.
The coordinates of \(x\in\mathcal L_S\) in their basis are therefore
rational, say \(t_i\). Clear their positive denominators by \(Q\).
Then \(c=Qc_0+\sum_i(Qt_i)k_{j_i}\), \(E=QE_0\) satisfy (T).
The zero-rank case is included: \(S=\{0\}\) requires only \(x=0\),
and then \(Q=1\) works. This proves the equivalence.

Thus even a highly rank-deficient mark family can be sufficient.
It is unnecessary to prove a lower eigenvalue for the entire
normalized covariance matrix if one can prove the target membership
directly. This is a strictly weaker mathematical requirement than
(E), not a proof of the missing membership.

## 2. Certified finite-rank membership, without a full-rank promise

Theorem 1 has an effective exact decision algorithm using certified
approximations. The determinant argument in
[effective number-field recovery](effective_number_field_recovery.md)
can be strengthened to all ranks as follows.

Every nonzero vector of \(\mathcal L\) has Euclidean length greater
than \(1/3\). Indeed a non-torsion unit in either totally real field
with all \(|\log|\sigma(u)||\le1/3\) would have
\(0<|\operatorname{Norm}(u^2-1)|<1\), since
\(0<e^{-2/3}\le|\sigma(u)|^2\le e^{2/3}<2\).
This contradicts integrality of that nonzero norm. A zero log vector
corresponds to signs; projection of the logs of a unit is an isometry
on the sum-zero subspace. The product inherits the same lower bound.

For any \(k\) independent lattice vectors, the lattice that they
generate in their \(k\)-dimensional real span has no nonzero point in
the open cube of side \(2/(3\sqrt k)\) in orthonormal coordinates.
Minkowski's convex body theorem gives covolume at least
\((3\sqrt k)^{-k}\). Consequently, for the matrix \(A\) of these
columns,
\[
 \det(A^TA)\ge (3\sqrt k)^{-2k}.                             \tag{2}
\]
Dependent columns have Gram determinant exactly zero. Crucially,
(2) does not require extension to a full basis of \(\mathcal L\).
The same covolume bound applies to \(\mathcal L\cap S\).

Suppose all the vectors, including \(x\), have Euclidean norm
at most \(H_0\ge2\), and approximate them by rational vectors to
Euclidean error at most \(2^{-P}\). Gram entries are bounded by
\(4H_0^2\); their entry errors are at most \(3H_0 2^{-P}\).
Telescoping each product in the Leibniz determinant expansion
bounds the Gram determinant error by
\[
 k!\, k(4H_0^2)^{k-1}\,3H_0\,2^{-P}.                       \tag{3}
\]
Use the lower threshold \(\gamma=(3\max(1,D))^{-2D}\).
Choose \(P\) so (3) is at most \(\gamma/4\) for all
\(1\le k\le D\), then an approximate determinant above
\(\gamma/2\) is equivalent to independence. This chooses \(P\)
using \(D\) and an explicit upper bound on \(\log_2 H_0\), not
by testing convergence of an unknown real rank.

Greedily select independent columns. Applying the same test to
\(x\) appended to the selected list decides \(x\in S\). At rank
\(D\), membership is automatic; at rank zero, use the length gap
directly. If membership holds, write \(A=(U_{j_1},\ldots,U_{j_k})\).
The index bound and Cramer's rule in \(S\) give both
\[
 \operatorname{den}(t_i)\le H_0^k(3\sqrt k)^k,\qquad
 |t_i|\le H_0^k(3\sqrt k)^k.                                \tag{4}
\]
For the first bound, the common denominator divides the index
\([\mathcal L_S:A\mathbb Z^k]\). For the second, replace one column
by \(x\) and compare \(k\)-volumes. The numerator bound uses
Hadamard's inequality and the denominator uses (2).

To recover the coordinates, solve the rational approximate normal
equations \(\widehat A^T\widehat A\,\widehat t
=\widehat A^T\widehat x\). By (2)-(3) its determinant is at least
\(\gamma/2\). Cofactor bounds give each entry of the inverse at
most \(2(k-1)!(4H_0^2)^{k-1}/\gamma\).
Writing the exact equations as \(Gt=h\), subtract to obtain
\(\widehat G(\widehat t-t)=(\widehat h-h)
-(\widehat G-G)t\). Each entry of the right side is bounded
by \(3H_0\,2^{-P}(1+kD_*)\), with \(D_*\) an integer upper
bound in (4). Thus increasing \(P\) by an explicitly computed
amount polynomial in \(D,\log H_0\) makes every coordinate error
strictly less than \(1/(2D_*^2)\).
Legendre's continued-fraction theorem and the cross-multiplication
separation of bounded-denominator rationals recover exactly the
unique \(t_i\) meeting the bound. This works also at non-full rank.

Exact rational elimination on \(V\) gives \(c_0,k_j\) with
bit lengths polynomial in the dimensions and the maximum input
entry bit length, by determinant clearing. Their log images have
an explicit norm upper bound \(H_0\) obtained from the integer
coefficient bounds and the individual mark log bounds. For any
nonzero mark of integer norm, if every conjugate absolute value
is at most \(H_g\ge1\), each is at least \(H_g^{-(d_i-1)}\).
Certified bisection in the given real-root brackets, followed by
the range-reduced log series, therefore computes all projected
logs with the required precision in polynomial bit time in the
dimensions, field/mark height bit lengths and \(P\). The same
is true for the Helmert projection. All approximations can be
performed as rational intervals before dyadic rounding.

This proves exact membership or nonmembership in (T), and an
explicit exponent if membership holds, with polynomial bit
complexity in the list size, field data and valuation-entry sizes.
Modular verification of (1) is an additional independent exact
check. Failure is not an appeal to a precision cutoff chosen by
experimentation.

## 3. A large-prime elimination theorem

Let \(\mathcal G\) consist of primitive positive-leading-coefficient
irreducible integer polynomials of degree at most \(s\) and
coefficient absolute value at most \(H'\), together with rational
prime constants at most \(H'\). Assume \(s<\min(d_1,d_2)\).
Take the rational-prime cutoff
\[
 R_*=\big((s+1)H'\big)^{2s}.
\]
For two distinct nonconstant marks \(g,h\in\mathcal G\), their
resultant is nonzero (they are nonassociate primitive
irreducibles) and Hadamard's inequality for the Sylvester matrix
gives
\[
 0<|\operatorname{Res}(g,h)|\le R_* .                        \tag{5}
\]
Indeed there are at most \(2s\) rows, each of Euclidean norm at
most \(\sqrt{s+1}H'\). The slightly weaker bound above avoids
any square-root rounding. For a prime ideal \(\mathfrak p\) over
a rational prime \(p\), if both \(g(\theta_i)\) and \(h(\theta_i)\)
lie in \(\mathfrak p\), their polynomials have a common root
in its residue field, so \(p\mid\operatorname{Res}(g,h)\).
This follows either from the resultant Bezout identity or
from its defining Sylvester determinant; monicity of \(g,h\)
is not required. It remains true at bad primes.

For \(p>R_*\), no two distinct nonconstant marks therefore have
nonzero valuation at the same prime ideal in a fixed field.
The rational constant marks cannot have any valuation over \(p\)
either, since they are at most \(H'\le R_*\).
If a mark has a rational prime divisor \(p>R_*\) of either
absolute norm, some prime ideal above \(p\) has positive valuation
on that mark. Its row is supported on that mark alone. For a target
\(\ell\le R_*\), that row of \(b\) is zero. The valuation equation
in (T) forces the coefficient of this mark to be zero.

**Theorem 2.** For the entire family \(\mathcal G\), deleting every
mark having a prime divisor \(p>R_*\) of either absolute norm
does not change existence of (T). This assertion uses neither
squarefreeness nor a density theorem. It is valid even when the
same rational prime appears at different ideals in several marks:
the proof uses equality of the prime *ideal*, not merely equality
of the rational prime.

For good primes the bound refines to residue degree: if two
polynomials vanish at the same degree-\(f\) prime ideal, their
common irreducible factor modulo \(p\) has degree \(f\), and the
Sylvester matrix has nullity at least \(f\) modulo \(p\).
Elementary row operations lifted modulo powers of \(p\) then show
\(p^f\mid\operatorname{Res}(g,h)\). One cannot use this stronger
cutoff indiscriminately in the presence of rational constant marks:
a small constant \(p\) has nonzero valuation at every prime over
\(p\), including high-residue-degree primes. Theorem 2 uses only
the safe rational-prime cutoff.

### Including all factors of the original marks

The original family permits reducible or nonprimitive polynomials
with degree at most \(s\) and height at most \(2H\). Every
primitive irreducible factor has coefficient height at most
\[
 H'=2^{s+1}(s+1)H.
\]
To see this, write \(M(g)\) for the Mahler measure. Its multiplicative
formula in terms of roots implies \(M(h)\le M(g)\) for each
nonconstant integer factor \(h\), because the complementary
integer factor has Mahler measure at least one. Jensen's formula,
followed by the concavity of the logarithm and Parseval, gives
\(M(g)\le\|g\|_2\le2\sqrt{s+1}H\). The elementary symmetric
coefficient bounds in terms of roots give
\(\|h\|_\infty\le2^s M(h)\). The stated \(H'\) is a safe integer
upper bound. Every prime factor of the content is at most \(2H\).

Expand the columns of a relation for the original family into
their irreducible factors and constant primes. Valuations and
projected logs add, and a sign has no effect. A unit guard for
\(g(m)\) implies the corresponding guard for each factor.
If the original norms avoid the field polynomial discriminants,
so do those of the factors. Thus any original (T) survives in
the enlarged irreducible family, and Theorem 2 eliminates all
large rational primes from that enlarged certificate. The
converse claimed here is only for the enlarged family, not for
the original, smaller height box.

This explains why simply factoring *all* resultant norms would
not by itself prove the desired existence: the very large
prime-ideal rows may be single-column obstructions. The relation
search is nevertheless complete within the specified enlarged
family.

## 4. Deterministic computation of the retained valuation columns

There is no need to factor a large leftover norm. Trial-divide the
two absolute norms by the rational primes at most \(R_*\) and
discard the mark if a remainder greater than one is left.
Theorem 2 proves that this cannot remove a possible certificate.
For the following local arithmetic implementation also require
that retained norms be coprime to
\(\operatorname{disc}(f_1)\operatorname{disc}(f_2)\).
This is a separate restriction: it permits the exact use of the
unramified power order. We do not claim that bad-small-prime
marks can all be deleted without loss. The earlier squarefree
family already imposed this restriction, and also excluded
the cross-resultant primes, which are not needed here.

At a good rational prime \(p\le R_*\), factor
\(\bar f_i\) over \(\mathbb F_p\) deterministically in
time polynomial in \(p,d_i,\log p\). One elementary implementation
is Berlekamp's algorithm: compute the fixed subspace of Frobenius
on \(\mathbb F_p[X]/\bar f_i\). Under its squarefree CRT
decomposition this subspace is exactly the product of the
constant fields \(\mathbb F_p\). A basis separates every pair of
components, so successive gcds with the basis elements minus
each scalar in \(\mathbb F_p\) split all factors. Binary
polynomial powering and linear algebra give the indicated cost.

For the lifted factorization modulo \(p^k\), use elementary
coprime Hensel lifting. If factors are known modulo \(p^j\),
the degree-bounded corrections at the next level solve the
linear equation
\(\sum_t \delta_t\prod_{u\ne t}\bar F_u=\mathrm{error}\)
in polynomials of degree below \(d_i\) over \(\mathbb F_p\).
It is invertible by CRT, since the factors are pairwise
coprime. This constructs the factors to any requested precision
in polynomial bit time in \(d_i,k,\log p\).

Because \(p\nmid\operatorname{disc}(f_i)\), the \(p\)-local
order is maximal: the index of \(\mathbb Z[\theta_i]\) in the
full integer ring is prime to \(p\). The lifted factor quotient
is the unramified local component, with \(p\) a uniformizer.
The valuation of \(g(\theta_i)\) at the corresponding prime
ideal is exactly the largest \(k\) for which \(g\) has zero
remainder modulo that lifted factor at precision \(p^k\).
The rational norm valuation is \(\sum_t \deg(\bar F_t)v_t\).
It supplies both a finite upper bound for the lift length
and an exact consistency test. Thus repeated valuations and
higher residue degrees cost only polynomially many operations
beyond the allowed enumeration of \(p\). No assumption of
efficient deterministic factoring over exponentially large
finite fields in \(\log p\) alone is being made.

## 5. The exact half-scale search

Take the monic field family of the earlier note, with
\(n\) the bit length of \(N\), \(d_i=\Theta(\sqrt n)\),
polynomial-size \(\ell\), and four perturbation coordinates
in a box of cardinality \(\exp(O(\sqrt n))\).
The construction, brackets and coefficients have polynomial
bit length. Fix any computable integer \(s,H\) satisfying
\[
 s<\min(d_i),\qquad s(s+\log H+\log(s+1))
                = O(\sqrt{n\log n}).
\]
For instance \(s=\lceil n^{1/4}\rceil\), \(H=2^s\) is valid
and gives the smaller search budget \(\exp(O(\sqrt n))\).
Enlarging the height by the factor in Section 3 still gives
\(\log R_*=O(s(s+\log H+\log(s+1)))\).
All nonzero norms have polynomial bit size, since the roots
and the logarithms of coefficient bounds do. If
\(\log H'=o(\log m)\) and \(s\log m=o(n)\), as in this
example, nonzero marks have \(0<|g(m)|<N\); any nonunit
therefore gives a proper gcd. Other marks are checked directly.

Enumerate the entire bounded irreducible family and the
constants. Irreducibility can even be tested by exhaustive
possible integer factors with the same Mahler coefficient
bound (with another factor \(2^s(s+1)\)); this has the same
exponential scale, so a sophisticated polynomial factorization
routine is unnecessary for this cost assertion.
Compute and prune the norms, construct the exact valuations
as in Section 4, and perform Theorem 1 including its
rank-deficient case. All these loops, their products and the
polynomial-time exact arithmetic on their output matrices have
bit cost \(L_N[1/2,O(1)]\). For the explicit example they
have cost \(\exp(O(\sqrt{\log N}))\).
The bound is a true worst-case bound for the certificate search,
including rejection and failure; it does not include a
trial-division fallback on \(N\) itself.

For the original \(s=n^{1/4+o(1)},\ \log H=n^{1/4+\eta+o(1)}\)
family the same method gives a search bound
\(\exp(O(n^{1/2+\eta}))\). In particular it dominates the
original squarefree COV-based certificate search (with the
stated enlargement). It also searches genuinely half-scale
families with a larger prime cutoff and no squarefree or
full-rank condition.

Using the previously established QRH witness argument, enumerate
a polynomial-sized dyadic prime interval in the specified
congruence classes. Some such prime has different local
two-primary orders at two hidden prime divisors. Every accepted
certificate is checked by binary powering and gcd scans.
If the enlarged search succeeds at a separating target for
every sufficiently large surviving composite, this proves
complete deterministic \(L_N[1/2,O(1)]\) factoring, with
polynomial recursion overhead. But **that uniform coverage is
not proved**. The deterministic certificate-search theorem
does not imply that the prime-ideal relations needed by (T)
exist in these restricted height families.

## 6. A stricter screen for deterministic constructions from linear units

For a nonconstant integer polynomial \(f\) of degree \(d\), the
integer unit marks \(a\) with \(f(a)=\pm1\) satisfy a simple
obstruction. If both signs occur at \(a,b\), then
\(a-b\mid f(a)-f(b)=\pm2\), so \(|a-b|\le2\).
In particular any pair of widely separated integer unit marks
must have the same sign. If all marks have mutual distances
greater than 2, there are at most \(d\), because they are roots
of one fixed degree-\(d\) polynomial \(f-1\) or \(f+1\).
If both signs occur, all such marks lie in the union of two
bounded integer intervals (each same-sign mark is within 2
of any fixed opposite-sign mark), regardless of the degree.
For the monic real-field construction using \(f=P\pm1\) and
\(d\) separated marks, their product is already a rational
sign, so they supply at most \(d-1\) independent unit log
directions. Simply adding more such widely separated linear
unit marks cannot resolve the missing joint unit rank.
This is only an obstruction for that specific construction,
not for higher-degree polynomial marks or all unit constructions.

## 7. Exact finite checks and next task

The [targeted mark experiment](../verification/research/targeted_marks.py)
checks a deliberately manufactured rank-deficient fixture:
\(N=15,\ \ell=2,\ m=0,\ P=(X-1)(X-46)\),
\(f_1=P-16,\ f_2=P-1\).
Both fields are irreducible and totally real, the first splits
at 2 and the second is inert. The two marks have exact valuation
matrix \(4I_2\) on the two target prime ideals, and zero
valuations in the second field. The valuation kernel has rank
zero, whereas the product log-unit lattice has rank two.
Nevertheless the product of the two marks is exactly 16 in
the first field and 1 in the second, so \(c=(-1,-1),E=4\)
satisfy (T), and a gcd of the modular square chain gives 3.
This shows the strict weakness of Theorem 1's condition for
a given mark list. The fixture was constructed using a known
exponent, so it is not evidence of general target coverage.

The separate resultant fixture enumerates 34 primitive
irreducible linear/quadratic marks of height at most two,
checks all 561 pair resultants exactly (maximum 64, general
cutoff 1296), and finds 56 good large-prime incidences in
a translated cubic field. It checks the required lack of
common prime-ideal factors. The experiment is a finite
arithmetic check, not evidence for the asymptotic density
of successful marks.

The next research task is now to prove target coverage or
construct target relations directly, rather than proving a
full covariance lower bound for its own sake. The target is
the precise membership in Theorem 1 for a half-scale mark
family, including cancellation of all surviving ideal rows.
The large-prime theorem identifies a rigorous barrier to
naively adding arbitrary fully factored norms. A promising
way to investigate this further is to allow *targeted*
additional marks of larger coefficient height and use the
small field defined by an irreducible mark to construct
resultant relations; the cost and descent on residual ideals
must be proved, not assumed. No general successful descent
or unconditional \(1/2\) factoring theorem is supplied here.

## Subsequent exact search improvement

[Ge factor refinement and full-degree marks](full_degree_factor_refinement.md)
eliminates the need to factor norms or restrict bad primes in the
finite relation search. It also supplies a smaller-degree ramified
construction with all full-degree polynomial representatives of
polynomial digit height searchable at the half scale. The
[necessary rank and unit-height bounds](half_scale_unit_rank_obstruction.md)
rule out completing the target by ordinary small shared units on
most balanced semiprimes. These are advances in exact search and
necessary conditions, not a uniform success proof.
