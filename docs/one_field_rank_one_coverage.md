# Forced coupled valuations and a one-field, rank-one coverage problem

**Status:** new proved algebraic constructions and an exact finite
factoring certificate. Uniform deterministic half-scale coverage is
still open. The one-third program is deferred.

This continuation changes two features of the preceding search:
rather than merely adding marks with private prime rows, we construct
large coupled valuation systems with independent unit relations; and
rather than demanding an entire shared-unit span in two fields, we
construct a full unit system in one field with prescribed modular
images. The latter reduces the remaining search to a single scalar
functional on its congruence-unit relations.

## 1. Many forced coupled relations, with no private prime rows

Let n be the bit length of an odd N, and let
s=floor(n/(1000 log_2(n+2))). Work for sufficiently large n
so s>=1. Take s distinct odd primes p_i<=n^2, coprime to N,
by sieving and gcd tests. If a proper gcd is found, stop.
Such primes exist for large n by the ordinary PNT; even excluding
every prime divisor of N removes at most n primes.

Let the distinct odd integers t_j be
\[
 p_1,p_1^2,\ldots,p_s,p_s^2,p_1^3.
\]
Set d=2s+2, a_j=(t_j-1)/2, g_j(X)=1+a_jX,
and C=2N prod_i p_i. Define
\[
 f(X)=X^{d-1}(X-2)+C\prod_{j=1}^{d-1}g_j(X).
 \tag{1}
\]
This is monic of even degree d, Eisenstein at 2 (all the
nonleading coefficients are even and the constant is C),
and f(0)=0 mod N. Its coefficient bit lengths are O(n)
because all t_j<=n^6 and d log n=O(n).
The second field may be taken as Q, with the common evaluation
root 0. Each mark evaluates to 1 there and modulo N.

### All roots are real

The reciprocal polynomial is
\[
 F(U)=U^d f(-1/U)=1+2U+C U\prod_j(U-a_j).
\]
Use the centers 0,a_1,...,a_(d-1), with radius
eta=2^(-floor(n/4)). They are distinct integers.
At either endpoint of a bracket the product term has absolute
value at least C eta 2^(-(d-1)), whereas |1+2U|=O(n^6).
Since C>=2^n and d=O(n/log n), the product dominates
uniformly for large n. Opposite signs persist at the endpoints.
The d disjoint brackets contain all d roots, one each; none is
zero since F(0)=1. The roots theta=-1/U of f are all real and
simple. The brackets and signs can be computed exactly with
polynomial bit complexity.

### Exact norms and actual prime ideals

At the rational root -1/a_j of g_j, the correction in (1)
vanishes. The homogeneous resultant formula gives
\[
 \operatorname{Norm}(g_j(\theta))
   =a_j^d f(-1/a_j)=1+2a_j=t_j.
 \tag{2}
\]
For every p_i, the reduction of f is X^(d-1)(X-2).
The root 2 is simple, so it lifts to exactly one unramified
degree-one local component of K tensor Q_(p_i). All the other
components reduce to the root 0. These assertions follow by
coprime Hensel factorization of (X-2) and X^(d-1); they do not
require that the whole power order be p_i-maximal.
If p_i divides t_j, then g_j vanishes only at the component
reducing to 2; in the other components its reduction is 1.
Thus the valuation at that unique prime ideal is v_(p_i)(t_j),
by (2), and no other prime ideal has a nonzero valuation.
If p_i does not divide t_j, all those valuations are zero.

Consequently the **true** valuation matrix of the marks has
rank s, with a separate row for each p_i and the entries
1,2 (and, for p_1, also 3). Every row has at least two
nonzero entries. No row or mark is removed by private-prime
peeling. Its integral kernel contains the s+1 independent
vectors corresponding to
\[
 g_{p_i^2}(\theta)/g_{p_i}(\theta)^2,\qquad
 g_{p_1^3}(\theta)/g_{p_1}(\theta)^3.
 \tag{3}
\]
These are genuine algebraic units and evaluate to 1 modulo N
in the localized power order.

### Independence of the unit relations

Use the d-1 real embeddings indexed by roots of F near a_i.
For g_j the absolute value there is |U_i-a_j|/|U_i|.
On the diagonal it is at most 2 eta; off the diagonal
the absolute value lies between 1/(4n^6) and 4n^6.
The diagonal log has absolute value at least
(n/4-O(1)) log 2, whereas the sum of the absolute
off-diagonal logs in a row is at most
(d-2) log(4n^6). Our explicit choice of s makes the
latter strictly smaller for large n.
The square matrix of these d-1 log columns is therefore
invertible by strict diagonal dominance.

Every vector in the integral valuation kernel gives a unit
whose full log vector has sum zero. Its restriction to these
embeddings still determines the vector; the preceding
invertibility proves that the s+1 unit relations in (3)
are independent modulo torsion.

**Proposition 1.** In deterministic polynomial bit time one
can construct a totally real field with a known modular
evaluation and an explicit mark family of polynomial bit
height having both valuation rank and independent
congruence-unit rank Omega(n/log n), with no private-prime
peeling loss.

This is stronger than the previous private-prime rank
construction, but it is not a target certificate: all the
marks here evaluate to 1. We must not infer a nontrivial
modular order relation from their rank.

## 2. A simple way of adjoining the target fails exactly

The following calculation screens a natural modification.
Choose a target ell among the p_i. Use the 2s marks with
t_j=p_i,p_i^2, and replace the extra cube mark by
\[
 h(X)=\ell+\frac{1-\ell}{2}X.
\]
Keep d=2s+2 and include h as one more factor of the
correction product in (1). The polynomial is still monic,
Eisenstein at 2, and has f(0)=C ell divisible by N.
All the previous norm identities remain true; additionally
\[
 \operatorname{Norm}(h(\theta))
   =\ell^{d-1}(\ell+2(1-\ell)/2)=\ell^{d-1}.
\]
The reciprocal polynomial has the additional center
(1-ell)/(2ell), between -1/2 and -1/3, instead of the
positive cube-mark center. The same sign-bracket argument
works (using the lower spacing bound 1/4 rather than 1/2).
Hence this field is also totally real for large n.

Modulo ell the simple root 2 is unchanged and the remaining
components reduce to 0. The old marks have no valuations
at any of the latter components, whereas h has all of its
ell-adic norm valuation, d-1, there. The rational scalar
ell also has total residue-degree-weighted valuation d-1
on these components: the simple root 2 contributes 1
to the total degree d.

In the paired formulation with second field Q and target
tau=(ell,1), allow arbitrary diagonal rational scalars
evaluable modulo N, and suppose a target relation has
target exponent E, coefficient c_h on h and total
ell-adic valuation z of the diagonal scalars.
The second-field valuation equation gives c_h+z=0,
since h(0)=ell and the old marks evaluate to 1.
The sum of the first-field valuation equations over
the root-0 components, weighted by residue degree, gives
(d-1)(E+c_h+z)=0. Therefore E=0.

So even with a large coupled relation system and a
norm-controlled target mark, this interpolation scheme
cannot supply a target certificate. This is an exact
valuation obstruction, not a failure of logarithm precision.
It does not exclude other choices of the defining polynomial.

## 3. A full unit system with a prescribed modular image

There is a more useful alternative using just one field.
Fix any odd N, odd prime ell coprime to N, and even d>=2.
Take
\[
 a_j=(\ell^j-1)/2,\quad g_j(X)=1+a_jX,\quad 1\le j<d,
\]
and set A=1+ell^(d-1), eta=(16 A)^(-4d).
Choose a positive integer C satisfying
\[
 C\equiv-2^d\bmod N,\quad v_2(C)=1,\quad
 \ell^{d(d-1)}\mid C,\quad C\ge(16A)^{10d}.
 \tag{4}
\]
This is an elementary CRT construction:
write C=2 ell^(d(d-1)) r, solve for r modulo N,
and add multiples of N until r is odd and the lower
bound holds. Choose the least such positive representative
above the lower bound. The bit length is
O(n+d^2 log ell). Define
\[
 f(X)=(X-2)^d+C\prod_{j=1}^{d-1}(1+a_jX).
 \tag{5}
\]

**Proposition 2.** In polynomial bit time in n,d,log ell
this constructs a monic irreducible totally real polynomial
of degree d, with f(0)=0 mod N, together with d-1
multiplicatively independent units
\[
 u_j=\frac{1+a_j\theta}{\ell^j}.
 \tag{6}
\]
They belong to the localization of Z[theta] at the
elements evaluating to units modulo N, and
\[
 u_j\longmapsto\ell^{-j}\pmod N.
 \tag{7}
\]

Proof. Monicity, f(0)=0 mod N and the Eisenstein condition
at 2 follow from (4) and even d>=2. The reciprocal polynomial
is
\[
 F(U)=(1+2U)^d+C U\prod_{j=1}^{d-1}(U-a_j).
\]
At the endpoints of the eta brackets of the d distinct
integer centers, the product term has magnitude at least
C eta 2^(-(d-1))>(4A)^d, whereas |1+2U|^d<=(4A)^d.
Thus all roots are real and simple as above.

The exact norm identity is now
\[
 \operatorname{Norm}(g_j(\theta))=\ell^{jd}.
\]
The element y=(theta-2)/ell^(d-1) is integral because
f(2+ell^(d-1)Y)/ell^(d(d-1)) is monic integral by (4).
Then u_j=1+a_j ell^(d-1-j)y is integral, has norm 1,
and is an algebraic unit. Both u_j and its inverse
belong to the evaluation localization: the inverse
of g_j is obtained from its norm and multiplication
adjugate, with denominator ell^(jd), coprime to N.
Equation (7) is immediate.

At the embedding indexed by the root U_i near a_i,
\[
 |u_j|=\frac{|U_i-a_j|}{|U_i|\ell^j}.
\]
For i!=j this lies between 1/(4A^2) and 4A, so the
off-diagonal log entries are bounded by log(4A^2).
The diagonal absolute value is at most 2 eta.
Our eta guarantees 2 eta (4A^2)^(d-2)<1, which is
the strict diagonal-dominance inequality for the
(d-1)-by-(d-1) log matrix in these embeddings.
It is invertible. Thus the unit logs are independent,
and, being unit logs of a totally real degree-d
field, form a basis of the real sum-zero subspace.
All heights, rational brackets, and exact construction
steps have polynomial bit complexity in the indicated
parameters. End proof.

The explicit units therefore have **full archimedean rank**;
no regulator oracle or class-group computation is needed
to obtain a spanning unit lattice. They need not generate
the entire unit group integrally.

The d-2 units
\[
 w_j=u_j/u_1^j,\qquad 2\le j<d
 \tag{8}
\]
evaluate to 1 and have independent logs. Their span is
exactly a codimension-one subspace. In the free group
generated by the u_j the kernel of the modular evaluation
is the integer lattice
\[
 \{(c_1,\ldots,c_{d-1}):\ \sum_j j c_j
                      \equiv0\bmod\operatorname{ord}_N(\ell)\}.
\]
The displayed w_j generate its sublattice with exact
sum zero. The missing cyclic direction is the order itself.
Thus full rank of the ordinary unit system does not by
itself prove coverage for the congruence-unit system.

## 4. Exact rank-one extraction and its coverage condition

Let L be the projected log map in K. Define the linear
functional Lambda on its (d-1)-dimensional real
sum-zero subspace by
\[
 \Lambda(L(u_j))=j .
\]
The earlier exact rational-reconstruction argument applies
to the full-rank lattice basis L(u_j): any actual unit
alpha has rational coordinates x_j in this basis.
Their denominators divide a single index bounded by the
covolume ratio. The lattice separation >1/3 and
Hadamard bounds provide an explicit denominator bound.
For a compact product of elements of polynomial bit
height, whose integer exponent bit lengths are given,
root bisection and certified log computations give
the required precision in polynomial bit complexity in
the total compact description and field data.

**Proposition 3.** Given any compact unit alpha
represented by a product of marks whose modular
evaluations are all 1, compute its exact rational
Lambda-value. If it is nonzero, a positive order
multiple for ell modulo N is computable at polynomial
bit cost in the compact description.

Indeed, for positive Q clearing the x_j denominators,
the unit equality
\[
 \alpha^Q=\pm\prod_j u_j^{Qx_j}
\]
follows from equality of all absolute embedding logs,
since the field is totally real. Evaluation gives
ell^(2 Q Lambda(L(alpha)))=1 mod N, and the absolute
value of this nonzero integer exponent is positive.
Verify the modular power explicitly. If ell is a
separating target (different local two-adic orders),
the previously proved odd-part squaring scan returns
a proper divisor.

For any finite list of marks g with g(0)=1, Ge's ideal
factor refinement produces an exact valuation-kernel
basis k_a as in the earlier two-field work, now using
only one order. All integer kernel products are actual
units with modular image 1. For each basis vector
compute Lambda(L(k_a)) exactly by Proposition 3.
If any is nonzero the algorithm succeeds; if every
value is zero the entire log span of the searched
valuation kernel lies in the span of (8). Thus this
is an exact rank-one decision, not a numerical guess
about a small singular value.

Equivalently, failure for a fixed list means that the
real row vector with entries Lambda(L(g)) lies in the
real row span of its finite valuation matrix. This
is the ordinary annihilator identity for the rational
kernel, whose integral basis spans the real kernel.
The projected logs of nonunit marks are used here
only to define a linear row, not as unit lattice points.

Take d=2 (or a polynomially growing d, for example
Theta(n/log n)), and enumerate marks of constant
coefficient 1, degree at most s, and other coefficients
in [-H,H] with s log(2H+1)=O(sqrt(n log n)).
The list can include other targeted marks and the
known w_j represented compactly. Every mark has
unit modular evaluation; none can vanish in the
field because f(0)=0 mod N. All coefficient sizes
in (5)-(6) are polynomial in n for polynomial d
and polynomial ell. The exact search has deterministic
worst-case bit cost L_N[1/2,O(1)] including failure,
by Ge's uniform polynomial-time factor refinement
and our certified unit-coordinate recovery.
It is not necessary to enumerate the full degree-d
coefficient cube when d is large.

**Remaining sufficient theorem for general factoring.**
For every sufficiently large surviving composite N,
at some separating prime ell of the polynomial-size
interval provided by the established Dirichlet witness
argument, prove that an admissible half-scale mark
family has a valuation-kernel product alpha with
Lambda(L(alpha))!=0.
The whole ordinary unit span, and d-2 congruence
directions, now hold unconditionally by construction.
The missing theorem is a single transverse unit
relation. We do not yet know how to prove its uniform
existence.

This is a genuinely different reduction from the
simultaneous smoothness and covariance of two resultants.
It can use one-field norm-smoothness estimates if
available, or entirely non-smooth ideal refinement.
It must not count the known ratios (8) as transverse
relations. In fact the original g_j have principal
ideals equal to (ell^j); their integral valuation
kernel is exactly sum j c_j=0, so they alone provably
do not meet the criterion.

## 5. Finite exact verification

The script coupled_norm_marks.py checks the degree-ten
forced-coupling construction, the obstructed target
modification, and two full unit-system constructions:
N=77, ell=5, d=6 and N=143, ell=7, d=8. It verifies
Eisenstein and real-root signs, the resultant norms,
the integral scaled-root polynomials, and the exact
diagonal dominance inequality. These checks verify
the algebraic construction, not uniform success.

A separate script one_field_certificate.py uses only
Python's standard library and demonstrates a complete
rank-one extraction with N=77, ell=5, d=2. It uses
a smaller C=150 satisfying the requisite CRT and
integrality conditions for this finite example; the
quadratic polynomial is X^2+296X+154, of discriminant
87000. It enumerates linear marks 1+tX with t<=200000
and collects norms smooth up to 1000, excluding the
discriminant primes. At every allowed prime the
simple root of the mark identifies the actual ideal
valuation. It uses no factorization of N to generate
the marks or relations.

The exact integer valuation matrix has 147 columns
and 144 rows before peeling, and 107 columns and
102 rows afterwards. Sparse rational column
elimination gives an integral kernel relation
supported on 91 marks, with maximum coefficient
bit length 22. The coefficient of this unit in the
rank-one lattice basis u_1 is exactly -2064690.
The script certifies this by directed rational
interval bounds on the roots and log series at
96 bits, not a floating-point approximation:
the coordinate interval has width <1/10000 and
contains precisely one possible rational of
denominator at most 100. The denominator bound
follows from the >1/3 unit-lattice separation and
the explicit norm bound on L(u_1).
The verified exponent is 4129380, and the odd-part
square scan produces the proper gcd 11.

This is a finite algorithmic success on the new
one-field construction, unlike the earlier manufactured
certificate fixtures that began with a known order.
It does not establish that smooth linear marks,
or any other half-scale mark list, always contain
the transverse unit relation. The general half-scale
factoring bound remains unsecured.

## 6. Next mathematical task

The one-field rank-one criterion should be attacked
before revisiting full two-field covariance.
For instance, for linear marks the norm is the
reciprocal polynomial F(t), and the finite ideal
rows and the scalar log functional are precisely
specified. We need a single nonzero residual of
that row modulo the valuation row span, after
peeling. A mere lower bound for valuation rank,
a mere large kernel, or an estimate for the
unconditional local congruence probabilities
does not establish the residual.

At fixed small degree the field height is exp(O(n)),
which puts ordinary smoothness density benchmarks
in the half-scale range; however a uniform
deterministic smooth-value or residual theorem
for these polynomials is not supplied by the
classical randomized class-group algorithms.
At high degree the field and explicit units remain
polynomial-bit-height, but the norm growth makes
ordinary small-prime smoothness less attractive.
Both choices remain candidates for the unresolved
existence step. No new Lean milestone is counted.

## Subsequent exact extraction and coverage obstruction

The [2-adic quadratic extractor](padic_rank_one_extraction.md) eliminates real logarithms from the degree-two decision, proves an integer first-jet sufficient criterion, and identifies the unavoidable smoothness and exponent-size conditions for the bounded linear family. The [adverse-parameter theorem](adversarial_rank_one_parameter.md) gives valid choices of C forcing trivial valuation-kernel products for any predetermined bounded polynomial family on balanced inputs. This excludes a proof uniform over arbitrary admissible C, without refuting the canonical small-C choice or adaptive C-dependent marks. The existence of a successful transverse unit at a separating target remains open.
