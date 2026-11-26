# Scalar-free target relations and the common-order obstruction

**Status:** proved algebraic and necessary-rank refinements of the
deterministic half-scale search. The desired uniform target coverage
is still unproved. These results do not give a new general factoring
time bound. The one-third program remains deferred.

We work with the [full-degree factor-refinement search](full_degree_factor_refinement.md)
and its prescribed ramified target. This note distinguishes exact
target coverage from three insufficient substitutes: large rank
(including rational constants), generation of units in the separate
fields, and short vectors in the common-order embedding lattice.

## 1. Quotient out diagonal rational elements exactly

Write \(K_i=\mathbb Q(\theta_i)\), \(A_i=\mathbb Z[\theta_i]\),
\(d_i=[K_i:\mathbb Q]\). The defining polynomials are monic,
irreducible and totally real and have the known common root \(m\)
modulo \(N\). Let \(A_i^{\mathrm{loc}}\) be the localization at the
multiplicative set of polynomial-order elements whose evaluations at
\(m\bmod N\) are units. The evaluation maps extend to these
localizations. We use only pairs of invertible elements of them.

Put \(d=d_1\). For a pair \(\alpha=(\alpha_1,\alpha_2)\) of nonzero
field elements define the multiplicative homomorphism
\[
 \Phi(\alpha)=
 \left(\frac{\alpha_1^d}{\operatorname{Norm}_{K_1/\mathbb Q}\alpha_1},
       \frac{\alpha_2^d}{\operatorname{Norm}_{K_1/\mathbb Q}\alpha_1}\right).
\]
Use the signed rational norm. For every nonzero rational \(a\),
\(\Phi(a,a)=(1,1)\). The first component of \(\Phi(\alpha)\)
has norm 1. If \(\Phi(\alpha)\) is a sign pair, then
\[
 \alpha_1^{2d}=\alpha_2^{2d}
      =(\operatorname{Norm}_{K_1/\mathbb Q}\alpha_1)^2\in\mathbb Q^\times,
\]
where the two equalities are identities in their respective fields.
Conversely, modulo the finite sign group, this construction detects
the diagonal rational subgroup up to power saturation.

Let \(\tau=(\ell,1)\) for a known prime \(\ell\nmid N\).
For every admitted mark \(g_j\) put \(a_j=(g_j(\theta_1),g_j(\theta_2))\),
so that its two modular evaluations agree and are units. Notice
\(\Phi(\tau)=(1,\ell^{-d})\).

**Proposition 1 (normalized target extraction).** If there exist
\(E>0\) and integral \(c_j\) with
\[
 \Phi(\tau)^E\prod_j\Phi(a_j)^{c_j}\in\{1,-1\}^2,
 \tag{NT}
\]
then \(\ell^{2dE}=1\bmod N\).

Proof. Apply the preceding norm identity to
\(\alpha=\tau^E\prod a_j^{c_j}\). Its components are invertible in
the localized orders. The common rational scalar \(r^2\) on the
right of the identity must be a unit in each localization.
For a rational prime \(p\mid N\), reduce the evaluation map further
modulo \(p\). Its kernel in \(A_i\) is a maximal ideal. By lying
over for the integral extension \(A_i\subseteq\mathcal O_{K_i}\),
choose a prime ideal over it. Every inverted denominator avoids
this prime ideal, and hence every unit of the localization has
valuation zero there. Applying this to the rational \(r^2\) proves
\(v_p(r)=0\). Thus \(r\) has numerator and denominator coprime to
\(N\). Evaluating the two equalities and dividing gives the assertion.
There is no evaluation of \(\Phi(a_j)\) itself: its rational norm
denominator may be a nonunit modulo \(N\).

In particular, a mark whose norm is divisible by \(N\) is not
automatically rejected if its modular evaluation is a unit.
A proper gcd of a computed norm with \(N\) can of course be
returned immediately.

Every original target certificate gives (NT). Conversely, (NT)
is equivalent to an original target certificate if we also allow
all diagonal rational scalars that are units modulo \(N\).
This apparent infinite enlargement is computationally finite:
include the absolute first-field norms of all marks, \(\ell\),
and \(N\) in an ordinary integer gcd-free basis computation.
These inputs are positive integers of known bit lengths; pairwise
coprime bases and all exponent vectors can be computed without
prime factorization. If a basis element has a proper gcd with \(N\),
return that factor. Otherwise, after perfect-power preprocessing,
the only nontrivial basis element sharing a prime factor with
\(N\) is \(N\) itself: the basis elements used in the representation
of \(N\) divide \(N\), and pairwise coprimality forces the claim.
The rational scalar in the proof of (NT) uses exponent zero on
that basis element. All remaining bases are unit-evaluable
rational marks. Their finite list suffices to cancel the rational
scalar exactly after squaring the relation and raising to the
degree \(d\). This proves the equivalence, without requiring
prime factorization of the norms.

### Exact polynomial-cost extraction

Use Ge's ideal-refinement theorem (Propositions 6.2–6.3 of
[Recognizing units in number fields](https://doi.org/10.1090/S0025-5718-1994-1242057-X))
on the original mark values, the rational first-field norms
\(\nu_j=\operatorname{Norm}_{K_1/\mathbb Q}g_j(\theta_1)\), and
\(\ell\) in each field. All of these are integral in the power orders.
If \(F_{i,g_j}\), \(F_{i,\nu_j}\), \(F_{i,\ell}\) are the resulting
refined valuation columns, use normalized columns
\[
 M_{i,j}=dF_{i,g_j}-F_{i,\nu_j},\qquad
 t=(0,-dF_{2,\ell}).
\]
Ge's equivalence for integer exponent vectors gives the exact
unit condition \(Mc=-Et\). The projected log columns are simply
\(dL(g_j)\); the rational denominators disappear from projection.
The target projected log is zero. All norm, matrix and log data
have polynomial bit cost in the total mark list and field input.
The [rank-deficient extraction](targeted_half_scale_search.md)
decides (NT) using the same lattice separation and determinant
bounds. No ideal or integer prime factorization is needed.

Thus normalizing, and adjoining the needed rational gcd-free
bases if desired, costs only polynomial overhead in the list
size. It is within the existing \(L_N[1/2,O(1)]\) search budget.
It does not increase the actual logarithmic unit span.

## 2. The genuinely non-diagonal necessary rank

Apply the valuation/projected-log lattice of
[the earlier obstruction](half_scale_unit_rank_obstruction.md)
to the elements \(\Phi(a_j)\) and \(\Phi(\tau)\).
Each nonzero vector has norm greater than \(1/3\):
a nonzero integer valuation has absolute value at least one,
and zero finite valuations leave a unit log vector with the
norm-of-\(u^2-1\) separation. These vectors are consequently
contained in a discrete lattice in their real span.

Suppose the normalized mark vectors have lengths at most \(H\),
and their joint rank is \(k\). If (NT) holds, the normalized
target vector lies in their real span. The small-span denominator
lemma in the earlier note gives an integral relation after
multiplying the target by some \(Q\le(3H\sqrt{k})^k\).
Proposition 1 then gives
\[
 \operatorname{ord}_p(\ell)\le 2dQ
       \le 2d(3H\sqrt{k})^k\qquad(p\mid N).
 \tag{1}
\]
The zero-rank case cannot contain the nonzero normalized target.

For the fields and marks of polynomial bit height in the
half-scale proposal, all normalized vector lengths are
polynomial in \(n=\operatorname{len}_2(N)\): multiplying a valuation
or log by \(d\) and subtracting the valuations of a rational norm
preserves a polynomial bound. The earlier elementary prime-divisor
count gives a density-one set of balanced semiprimes on which
every polynomially bounded target has order at least
\(\exp(cn)\), for some fixed \(c>0\). Consequently on these inputs
(1) implies
\[
 k=\Omega(n/\log n),\qquad
 \operatorname{rank}_{\mathbb Q}(M)=\Omega(n/\log n).
 \tag{2}
\]
Indeed the archimedean dimension \(d_1+d_2-2\) is \(o(n/\log n)\).
The second rank is the *normalized* finite-valuation rank, not
the rank inflated by arbitrarily many rational scalar columns.
It equals the rank of the true normalized prime-ideal matrix
because Ge preserves the rational kernel. Every diagonal rational
mark has zero column.

This applies to every successful subfamily of polynomial-bit-height
marks, independently of the number of rational primes included
as constants. In particular, adding many rational primes cannot
meet the necessary rank condition in (2).

## 3. High normalized rank is not target coverage

Even the normalized rank condition is only necessary. Here is
an explicit existence construction, within polynomial bit height,
which shows why a proof must control the support of relations.

Use the actual smaller-degree ramified fields of
full_degree_factor_refinement.md, with \(r=d/2\) prescribed linear
marks \(X-R_j\), \(1\le j\le r\). Their norms are \(\ell,1\) in the
two fields, respectively. Their initial ideal target is available
and their second-field log columns are independent by the same
diagonal-dominance argument as in ramified_target_construction.md
(the margin is stronger when \(d-r=d/2\)).

Fix any constant \(A>0\). For every sufficiently large such field
pair one can append \(\lfloor n^A\rfloor\) more linear marks of
polynomial bit height, increasing normalized rank by at least
that number, without making (NT) solvable.

First prove that enough distinct private primes are available.
Let \(D_0\) be the positive integer
\[
 N\ell\,(2d)!\,
 |\operatorname{disc}(f_1)\operatorname{disc}(f_2)
              \operatorname{Res}(f_1,f_2)|,
\]
whose bit length is polynomial in \(n\). Set \(J=D_0^2\) and
\(K=2^{n^2}\). Consider \(f_1(R_1+Jj)\) for \(1\le j\le K\).
These values are congruent to \(\ell\bmod D_0^2\), so among
the primes dividing \(D_0\) their only divisor is \(\ell\), with
valuation one. For sufficiently large \(n\) all the values are
positive, and the logarithm of every one is at most a polynomial
\(U\) in \(n\) by the coefficient-height bound and Horner evaluation.
For \(K/2\le j\le K\), the root bound gives
\(\log f_1(R_1+Jj)\ge d(\log K-O(1))\).

For any prime \(p\nmid D_0\), the polynomial is squarefree modulo
\(p\), and Hensel lifting gives at most \(d\) roots modulo \(p^h\)
for each \(h\ge1\). Since \(J\) is a unit modulo \(p\), its total
logarithmic contribution to all \(K\) values is at most
\[
 dK\frac{\log p}{p-1}+dU .
\]
If at most \(n^A\) distinct primes outside \(D_0\) occurred, summing
this inequality would give
\(O(dK(\log n)^2+d n^A U)\), plus \(K\log\ell\) from the bad primes.
Here \(\log p/(p-1)\) decreases for \(p\ge2\), and even comparison
with all integers up to \(n^A+1\) gives \(O((\log n)^2)\).
This contradicts the lower bound \(\Omega(dK\log K)\).
Thus choose \(t=\lfloor n^A\rfloor\) such primes \(p_j\).
Their individual log sizes are at most \(U\), and each has a root
\(a_j\) of \(f_1\), not a root of \(f_2\), since the prime avoids
the resultant.

At every \(p_j>2d\) choose also a residue \(b_j\) avoiding all roots
of both polynomials. For \(1\le j\le t\), prescribe an integer \(u_j\)
by CRT:
\[
 u_j\equiv R_1\bmod N,\qquad
 u_j\equiv a_j\bmod p_j,\qquad
 u_j\equiv b_h\bmod p_h\quad(h\ne j).
\]
Use the least nonnegative representative. The coefficient bit length
of each mark \(X-u_j\) is \(O(n+tU)\), polynomial in \(n\).
Its modular evaluation is a unit by the original gcd guard.
The first norm is divisible by \(p_j\), the second is not;
no other added or prescribed mark has either norm divisible by \(p_j\).

After normalization, at every second-field prime ideal above
\(p_j\) its column has the nonzero valuation of the reciprocal
first norm. All other normalized marks and the target have
zero entries at those ideals. The new columns are therefore
independent in the normalized finite matrix and every solution
of \(Mc=-Et\) uses coefficient zero on all of them. The projected
second-field logs of the remaining prescribed marks are independent
(their normalization only multiplies them by \(d\)). Log cancellation
forces their coefficients to be zero as well. The target remains
nonzero. Hence there is no (NT), regardless of the added rank.

This is an existence counterexample to a **rank-only criterion**,
not a counterexample to the entire polynomial-digit box. The
private primes were obtained by a counting argument over a very
long range, not an algorithm charged to the half-scale budget.
The new marks are polynomial-bit-height, not necessarily in the
fixed smaller power-basis digit box. They belong to the more
general type of polynomial-size additions permitted by the search.
The point is that a large rank observed in a mark family can all
be contributed by isolated finite valuations; it does not imply
that any of the required unit relations exist.

### Exact peeling

For the normalized refined matrix, if a row has a single nonzero
mark entry and zero target entry, force that mark coefficient
to zero and delete it. Repeat with the restricted matrix.
This is a finite induction on the number of marks: at each step
every possible normalized target relation vanishes on the removed
column. If the nonzero target row becomes unsupported, reject.
No rank inflation from removed columns may enter a coverage proof.
Ge's normalized matrix is sufficient; no prime-ideal factorization
is needed. The previous resultant cutoff is another way to
identify some such obstructions. Peeling is an exact preprocessing
step, not an assertion that the surviving core contains the target.

## 4. The target in the shared-order unit quotient

There is also an exact algebraic description of the special
target, not merely an index lower bound.

Let \(f_1,f_2\) be the ramified polynomials, and write
\[
 A=\mathbb Z[X]/(f_1f_2),\qquad
 D=\mathbb Z[X]/(f_1,f_2).
\]
The natural map from \(A\) into \(A_1\times A_2\) identifies it
with the fiber product over \(D\): pairs with identical residues
in \(D\). Indeed \((f_1)\cap(f_2)=(f_1f_2)\), by coprimality over
\(\mathbb Q\) and monic division over \(\mathbb Z\), and the usual
exact sequence for two ideals proves the image assertion.

The ring \(D\) has finite additive order \(|\operatorname{Res}(f_1,f_2)|\).
One way to see this is to identify it with the quotient of \(A_1\)
by the image of multiplication by \(f_2(\theta_1)\); the determinant
of that multiplication is the resultant. Write \(C=\operatorname{char}D\).
Then \(C\) is the least positive integer in the principal ideal
\(f_2(\theta_1) A_1\), and \(N\mid C\), since the common evaluation
induces a surjective ring homomorphism \(D\to\mathbb Z/N\mathbb Z\).
Compute \(C\) exactly by solving
\(f_2(\theta_1)u=1\) in the rational power basis of \(K_1\)
and taking the lcm of the denominators of \(u\). This is polynomial
bit complexity in the field descriptions. Equivalently use the
Smith normal form of the multiplication matrix.
If its invariant factors give a proper gcd with \(N\), return it.
There is no proof that such a gcd must occur.

For our ramified construction \(f_1\equiv X^d\bmod\ell\) and
\(f_2\equiv X^d+1\bmod\ell\). Thus \(\ell\) is coprime to
the resultant and to \(C\). With \(g=X-R_1\), define
\[
 \xi=(g(\theta_1)^d/\ell,\ g(\theta_2)^d).
\]
This pair actually belongs to \(A_1^\times\times A_2^\times\),
not only to the maximal-order units. In the first component
\(g(X)^d-f_1(X)\) is coefficientwise divisible by \(\ell\)
because \(R_1\equiv0\bmod\ell\). The quotient has integral
power-basis coordinates, and its norm is one. The second
component has norm one already. An element of a finite free
integer order with norm one is a unit in that order, by the
integer adjugate of its multiplication matrix.

The unit group of \(A\) is the subgroup of \(A_1^\times\times
A_2^\times\) with equal residues in \(D^\times\); inverses of
equal residues also agree, proving the converse. The residue
of \(g^d\) is a unit in \(D\) by the second component. Consequently
\[
 \xi^j\in A^\times \quad\Longleftrightarrow\quad
       \ell^j=1\text{ in }D
 \quad\Longleftrightarrow\quad
       \ell^j\equiv1\bmod C .                            \tag{3}
\]
Thus the exact order of the coset of \(\xi\) in the quotient
of the two individual order-unit groups by the common order-unit
group is \(\operatorname{ord}_C(\ell)\).
In the quotient of their log lattices, the corresponding order
is the least positive \(j\) with \(\ell^j\equiv\pm1\bmod C\):
two unit pairs have equal projected logs precisely when they
differ by independent signs.

Equation (3) explains why an explicit full-rank unit system in
each individual field does not solve the shared-unit problem.
The congruence quotient contains the precise order obstruction
at a known modulus divisible by \(N\). Dirichlet's theorem proves
that some power of \(\xi\) belongs to the full common-order unit
group, but provides no half-scale method to express it as a
product of the enumerated marks.

## 5. Why a direct common-lattice Minkowski argument is insufficient

In the \(D_e=d_1+d_2\) real embedding coordinates, the covolume
of the power-basis lattice of \(A\) is
\[
 \operatorname{covol}(A)=
 |\operatorname{Res}(f_1,f_2)|
       \sqrt{|\operatorname{disc}(f_1)\operatorname{disc}(f_2)|}
 \ge N .
\]
This is the Vandermonde determinant, or the discriminant
identity for a product of coprime monic polynomials. Let \(I\)
be any finite-index ideal of \(A\). Its covolume is
\([A:I]\operatorname{covol}(A)\).

A symmetric embedding box with coordinate bounds \(W_i>0\)
has volume \(2^{D_e}\prod_iW_i\). The usual Minkowski
existence guarantee needs \(\prod_iW_i>\operatorname{covol}(I)\).
Even if it produces a regular element \(\alpha\) (nonzero in
both fields; this is not automatic in a product algebra),
the bound on the index of its principal ideal inside \(I\)
is
\[
 [I:\alpha A]=\frac{|\operatorname{Norm}\alpha_1
                           \operatorname{Norm}\alpha_2|}{[A:I]}
 \le\frac{\prod_iW_i}{[A:I]}.
\]
The smallest value of the right side supplied by this guarantee
is \(\operatorname{covol}(A)\ge N\), not
\(\exp(O(\sqrt{n\log n}))\). This is an uncontrolled cofactor
on the exponential scale. For a stronger full-rank statement,
if \(D_e\) linearly independent elements of \(I\) lie in the
same embedding box, their determinant is at least
\(\operatorname{covol}(I)\); rowwise Hadamard gives at most
\(D_e^{D_e/2}\prod_iW_i\). Thus a full-rank box would still
have residual bound at least
\(\operatorname{covol}(A)/D_e^{D_e/2}=\exp(\Omega(n))\)
in our degree regime.

These inequalities do not forbid special elements of much
smaller norm or adapted non-box searches. They forbid claiming
the desired cofactor bound just from the ordinary covolume
and Minkowski estimates. Using the separate-field lattices
removes the resultant factor, but loses the common-residue
condition (3); one cannot then evaluate the two resulting
elements as the same modular mark.

## 6. Check of the relevant literature

The December 2025 paper by K. de Boer, A. Pellet-Mary and
B. Wesolowski, [Rigorous methods for computational number theory](https://koendeboer.com/publication/rigorousmethods/RigorousMethods.pdf),
Theorems 1.3 and 12.1, is relevant to the missing compact-unit
generation. It gives rigorous **probabilistic** class-group
and S-unit lattice algorithms under ERH. Its runtime depends
also on the Dedekind zeta residue, and it assumes an LLL-reduced
maximal-order basis as input. The random-walk theorem (6.4 and
discussion in Section 21.6) uses Hecke L-functions over the
number field, not only Dirichlet L-functions over \(\mathbb Q\).
It does not establish uniform deterministic generation in the
common polynomial order at our budget. Our verified rational
Dirichlet/zeta zero-free results do not imply this Hecke ERH.
Even a separate-field compact unit basis would still require
the shared congruence constraint (3).

## 7. Remaining coverage problem

The exact finite search can now discard diagonal scalar rank,
peel isolated ideal directions, and test target membership
in the normalized lattice. The algebraic target in the
full common-order unit group is fully characterized by (3).
The required **new theorem** is that enough compact shared
unit relations generated by the half-scale list survive
peeling to contain that particular log class in the real
span, for at least one separating prime on every large
composite input. Neither the previous rank condition nor
the new stronger condition (2) proves this. No unconditional
half-scale general factoring bound is claimed.

The finite script normalized_target.py checks the normalization,
the gluing characteristic, a manufactured positive certificate,
and a private-prime negative fixture. It uses exact integer
and rational arithmetic and the earlier Ge prototype, not a
numerical rank test. It is not an asymptotic coverage experiment.
