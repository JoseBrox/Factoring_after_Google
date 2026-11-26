# Factor-refinement extraction and a larger half-scale mark family

**Status (26 November 2026): proved reduction and search-cost bound
using a published unconditional polynomial-time theorem.**
Uniform target coverage is not proved. No smoothness heuristic is
required to compute the complete relation space of the searched
family, even at primes dividing the discriminants.

This supersedes the computational need for smoothness pruning in
[targeted_half_scale_search.md](targeted_half_scale_search.md).
The [small-unit/rank obstruction](half_scale_unit_rank_obstruction.md)
explains why the larger search must retain many finite-valuation
directions to produce large compact units.

## 1. Published ideal factor refinement

Use Guoqiang Ge, "Recognizing Units in Number Fields",
Mathematics of Computation 63 (1994), 377–387, especially
Propositions 6.2 and 6.3, with Algorithm 5.6 and Proposition 5.7.
[Paper](https://cr.yp.to/bib/1994/ge.pdf).
The theorem and proposition numbers refer to the printed article.

Ge's result is uniform in the field degree. The input is an
order A specified by its integral multiplication table and a list
of nonzero elements gamma_j in A in that basis. In deterministic
time polynomial in the bit length of this input, it supplies an
overorder C of A, pairwise comaximal proper invertible ideals J_t
of C, and nonnegative integer entries F_(t,j) such that
\[
 \gamma_j C=\prod_t J_t^{F_{t,j}} .
\]
These J_t need not be prime ideals. Nevertheless the column matrix
has the exact property
\[
 \prod_j\gamma_j^{c_j}\in O_K^\times
                 \quad\Longleftrightarrow\quad Fc=0
                 \qquad(c_j\in\mathbb Z).                 \tag{1}
\]
The reason is that the extensions of the J_t to O_K remain
proper and pairwise comaximal. Each has a nonempty prime-ideal
support disjoint from every other support. Taking the valuation
at one ideal in each support detects its exponent. This is also
the substance of Ge's Proposition 6.3.

In particular this is not a call to an algorithm for factoring
norms or finding the maximal order. The overorder enlargements
make ideal divisors invertible when needed; intersections and
colon ideals are rational integer-lattice operations.
The printed polynomial-time bound is in the length of the
multiplication table and element coordinates, not merely a
fixed-degree arithmetic-operation bound. It therefore applies
to the varying degrees in our construction.

## 2. Exact two-field relation space without factoring norms

Let f_1,f_2 be distinct monic irreducible totally real integer
polynomials with a known common root m modulo N. Use the orders
A_i=Z[theta_i]. Given any finite list of polynomial marks g_j,
discard those that vanish in either field. At each mark test
gcd(g_j(m),N); a proper gcd terminates successfully, and a mark
whose gcd is N cannot be used for this unit-evaluation procedure.
The remaining marks have evaluable inverses modulo N.

Reduce all marks modulo f_i by exact monic polynomial division.
Include a target element gamma_0=ell in the first field and 1
in the second field. Apply Ge to both orders and their full
element lists. Denote by F the vertically concatenated
exponent matrices from the two calls, and by F_0,F_m its target
column and mark submatrix.

By (1), for every integer E and every integer mark coefficient
vector c the following equivalence is exact:
\[
 F_m c=-E F_0
 \quad\Longleftrightarrow\quad
 \left(\ell^E\prod_j g_j(\theta_1)^{c_j},
             \prod_j g_j(\theta_2)^{c_j}\right)
                 \in O_{K_1}^\times\times O_{K_2}^\times . \tag{2}
\]
No assumption about the residue degrees, ramification or
discriminants enters. We do not evaluate the computed
overorders modulo N. They are used only for (2).

If F_0 does not lie in the rational image of F_m, reject the
target; (2) proves impossibility of the required relation.
Otherwise use exact rational elimination and denominator
clearing to obtain an integral c_0 and positive E_0 with
F_m c_0=-E_0 F_0, and a rational kernel basis cleared to
integral vectors k_j.

The projected log images L(c_0),L(k_j) all lie in the
product log-unit lattice by (2). The rational scalar ell
has zero projected log vector. Apply the exact rank-deficient
target criterion of the earlier note: decide whether
-L(c_0) lies in the real span of L(k_j), using the strictly
positive Gram-determinant gap for independent lattice vectors.
If it does, rational coordinate reconstruction and denominator
clearing give a positive E and integral c satisfying both
(2) and L(c)=0. The corresponding pair of algebraic units
is a sign pair. Clearing the negative powers gives
identities in A_i (not arbitrary identities in an overorder),
and evaluation proves ell^(2E)=1 modulo N.

All matrix, norm-bound, logarithm-approximation, determinant
and continued-fraction complexity bounds from the rank-deficient
extractor apply without change to the new F. The entries of F
have polynomial bit length by Ge's output-length bound.
The degrees, coefficient heights, multiplication-table
entries and reduced polynomial coordinates can all be encoded
with bit lengths polynomial in the actual field/mark input
sizes. The positive-integral-norm argument bounds individual
nonzero conjugates of integer marks from below in terms of
their upper bounds; this does not require factoring the norm.
Certified root isolation and log approximations in the totally
real fields therefore have polynomial bit cost at the explicit
precision required by the determinant gap.

**Theorem 1.** Given two such field polynomials, the common
evaluation root, and any explicit finite mark list, there is
a deterministic algorithm, polynomial in the total bit
length of these data, that either returns a proper gcd or
decides the exact existence of a nonzero target exponent
in the allowed mark subgroup, and outputs a verified
exponent when one exists. The decision allows a relation
up to a sign in each field (squaring removes signs). It
neither factors any absolute norm nor discards a mark on
account of its finite valuations.

This is an ordinary mathematical reduction to Ge's theorem
and our proven finite-rank reconstruction, not a Lean certification.
A small exact ideal-refinement implementation is verified below;
the full combined extraction has not been implemented.

## 3. Reduce degree to permit full polynomial representatives

The earlier ramified-target construction took d of order
sqrt(n), with many prescribed linear marks. Its root stability
actually permits the smaller degree scale below, allowing
a full-degree mark family at the desired cost.

Let n be the bit length of N, z=floor(log_2 n), and choose d
as the least power of two with d^2 z>=256n. For sufficiently
large n, d>=4, and
\[
 16\sqrt{n/z}\le d<32\sqrt{n/z}.
\]
Take k=J=d/4, r=d/2 and m=2^ceil(n/k).
Thus m^k>=2^n>N, m is larger than every fixed polynomial
in n and m<N eventually, and
\[
 \log m\le(4n/d+1)\log2
             \le d\log n/64+\log2.                       \tag{3}
\]
Use exactly the centers, P,Q, constants c_1=ell,c_2=1,
h_{i,0}, base-m digit corrections T_i and polynomials f_i
from the ramified-target note. For completeness the definitions
are
\[
 R_j=3\ell(2j+1),\quad P=\prod_{j=1}^d(X-R_j),\quad
 Q=\prod_{j=1}^r(X-R_j),
\quad
 f_i=P+c_i+Q(h_{i,0}+4\ell T_i).
\]
Here h_{1,0}=0, h_{2,0} in {0,2ell} makes the second
constant coefficient 2 modulo 4, and T_i of degree <k
represents the least residue of
\[
 -(P(m)+c_i+Q(m)h_{i,0})(4\ell Q(m))^{-1}\pmod N
\]
in base m. The gcd guards ensure this inverse exists, or
return a proper divisor first.

All the exact congruences and norm identities of the previous
construction remain valid. In particular f_1 is Eisenstein
at ell, f_2 is Eisenstein at 2, and the two defining polynomials are
distinct because their prescribed mark values differ.
The first field has a unique degree-one prime over ell,
totally ramified, and the target valuation relation is
available from any of the first r linear marks.

For the real-root proof keep the sign brackets of radius
eta=1/[4(ell d)^floor(J/4)]. The same factorial lower bound
for P and upper bound on the correction give the logarithmic
margin
\[
 (3/4)J\log(\ell d)-\log m-O(d+\log(\ell d)).
\]
For ell polynomially bounded, log(ell d)=O(log n), and
log(ell d)>=log d>=(1/2-o(1))log n. The first term is
at least (3/32-o(1))d log n, whereas (3) bounds the digit
term by (1/64)d log n+O(1). The margin tends to infinity
uniformly. Thus all d simple roots of each field are real.
The bit heights and sign-bracket encodings are polynomial in n.
This proves the construction with degree
d=Theta(sqrt(n/log n)), not just with sqrt(n).

## 4. Full-degree half-scale search

Set A=Z[X]/(f_1 f_2). Monicity gives a free Z-basis of
size 2d, and rational CRT identifies A tensor Q with
K_1 times K_2. Every element of A has a unique integer
polynomial representative of degree <2d.

Fix a positive integer C sufficiently large that the
polynomially bounded centers R_j are smaller than n^C.
In the new smaller-degree construction, enumerate *all*
polynomials of degree <2d with each power-basis coefficient
in [-n^C,n^C]. The number of marks is at most
\[
 (2n^C+1)^{2d}
       =\exp(O_C(\sqrt{n\log n})).
\]
The entire family, including all original prescribed linear
marks and all nonzero rational constants in its bound, is
available at half scale. The modular gcd check must now be
performed even when g(m) has size >=N; no assumption
g(m)<N is necessary. A gcd=N rejects the mark, a proper
gcd returns the factor. Theorem 1 decides the complete
target relation space of the surviving family in time
polynomial in this list size and the field sizes. Its
overall bit complexity is therefore L_N[1/2,O(1)].

We may also use other integral bases of A with polynomial
bit size, for example the Newton basis consisting of 1 and
successive products of the linear center polynomials, using
two interlaced lists of d centers (or a length-2d list of
arbitrary bounded integer centers). These monic polynomials
of consecutive degrees form a unimodular triangular basis
of A. Enumerating bounded coefficient boxes in any fixed
number of such bases has the same cost, while ordinary
power-basis heights may be substantially larger.

More generally any deterministically constructed explicit
list with at most exp(O(sqrt(n log n))) bits in total can
be added to the search, even if individual elements have
very large coefficient bit lengths. Ge's theorem and the
finite-rank reconstruction are polynomial in the *total*
input length. This allows targeted additional high-degree
marks and compact-unit factors. It is not necessary to
factor the marks themselves into irreducible integer
polynomials.

The older small-degree/high-coefficient-height search can
be run alongside this variant, as neither family necessarily
contains the other. Both have the claimed budget for the
certificate search, including negative answers. The outer
loop over polynomially many target primes is still allowed.

## 5. Exact coverage statement in the product order

Let A^* be the actual unit group of the product order A.
It has full log rank 2d-2. Indeed A has finite index in
O_{K_1} times O_{K_2}, and units congruent to 1 modulo
that index times the maximal product order belong to A
with their inverses. Every unit of A has identical modular
images in the two fields, since it is represented by a
single polynomial with evaluation at m. Its image is a
unit by evaluating its inverse.

Let G be the multiplicative subgroup generated by the
surviving mark pairs. A sufficient coverage condition is
\[
 \operatorname{span}_{\mathbb R}
       \log(G\cap A^*)=\mathbb R^{2d-2}.                 \tag{4}
\]
Indeed the initial particular target from the ramified
linear mark gives a unit log vector in the full product
unit lattice. By (4) it is in the span of the available
valuation-kernel logs, and Theorem 1 returns an exponent.
The true criterion remains weaker: only membership of
that one target vector is necessary. We do not need the
group generated by the marks to equal the full unit group
or to have a computed index.

Dirichlet's unit theorem proves (4) for the infinite
family of *all* representatives of A^*. It does not prove
it for any of the bounded coefficient boxes above.
Moreover, the new [rank/height obstruction](half_scale_unit_rank_obstruction.md)
shows that for most balanced inputs one cannot obtain (4)
by merely exhibiting 2d-2 individual shared units of
polynomially bounded logarithmic norm. Compact products
with much larger logs are required, and a successful
small-mark certificate needs joint valuation/log rank
Omega(n/log n).

A general compact-representation theorem for units in
number fields is also insufficient by itself: it must
supply the required factors in the *common* polynomial
order or in the allowed localized order, with unit modular
images, and in a list constructible within the half-scale
budget. Choosing a representation after being given an
unknown large unit does not meet this requirement.

## 6. Actual boundary of progress

We have removed the algorithmic dependence on factoring
norms, computing maximal orders, or obtaining small-prime
smoothness in advance. We have also expanded the degree
range to cover the whole common order's polynomial basis
at polynomial digit height. These are proved search and
construction improvements.

The unresolved step is now the following precise existence
problem: for every sufficiently large surviving composite,
prove that at some separating target prime the bounded
family generates enough compact shared-unit relations
for the particular target membership. No estimate in
this note proves that assertion. In particular an
unconditional general L_N[1/2,O(1)] factoring result
cannot yet be claimed. The one-third program remains
deferred.

## 7. Exact finite implementation check

The [research prototype](../verification/research/factor_refinement.py)
implements the ideal lattice sum/product/colon operations and the
factor-refinement/overorder loop with rational HNF arithmetic.
It never calls an integer factorization or prime-ideal decomposition
routine. All final principal-ideal product identities and pairwise
comaximality assertions are checked exactly.

The exact checked source is Git blob
`1841decf37f7e7cda89fc60e2e394e5d36543a61` (SHA-256
`528ab6aedc2ad146d3ed609420a7a7e5bac4f46a87d5efb85f40341a111d2017`).
Run with SymPy installed:

```
python verification/research/factor_refinement.py
```

Observed output:

```
nonmaximal order: overorder index 2 refinement steps 2 enlargements 1 matrix rank 3
field 1 : 9 elements, 8 refined ideal rows, 11 refinements, 0 enlargements
field 2 : 9 elements, 7 refined ideal rows, 6 refinements, 0 enlargements
joint matrix: (15, 9) rank 8 ; exact target certificate 2^4=1 mod 15, factor 3
```

The first fixture starts with Z[2 sqrt(2)] and exercises the
noninvertible-sum/overorder enlargement. The second uses the
manufactured N=15 target relation of the previous note, together
with six additional marks. It tests the exact relation matrix and
modular certificate, not the existence of relations on arbitrary
inputs. The proof of polynomial bit complexity uses the published
algorithm, not measured running times of this SymPy implementation.
