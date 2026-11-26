# Primitive-ratio lattice aggregation and factor-free large-prime cancellation

**Status (27 November 2026): proved a new exact compressed suffix
aggregation algorithm and a necessary-and-sufficient graph criterion
for cofactor cancellation within each enumerated lattice.** The
character-moment input proves dense short-ratio coverage, but not
uniform selection at the prescribed target powers. Uniform
deterministic half-scale factoring remains open. No new complete
Lean milestone is counted. The one-third program remains deferred.

This continues [the shared-AP lattice count](ap_lattice_conditional_counting.md)
and [narrow-band coverage](narrow_band_streaming_atoms.md).
Instead of aggregating one floor-sum term per unknown prime tuple,
we change the enumeration variables to the remaining primitive
integer pair. We also allow cancellation of large residual factors
across multiple pairs, without requiring any individual smooth pair.

## 1. Primitive rectangular lattice enumeration

Let N>=3, gcd(a,N)=1, and 1<=X,Y<N be integers. Define
\[
 \Lambda_a=\{(x,y)\in\mathbb Z^2:y=ax\bmod N\}.
\]
Its index in Z^2 is N, by the surjective homomorphism
(x,y) -> y-ax mod N. Consider the signed rectangle
\[
 1\le x\le X,\qquad 0<|y|\le Y.
\]
We call a pair primitive if gcd(x,y)=1, and a unit pair if
gcd(xy,N)=1.

**Theorem 1.** There is a deterministic algorithm which either
returns a verified proper divisor of N, or enumerates every primitive
unit pair in this rectangle. Its bit cost is
\[
 \operatorname{poly}(\log N)\bigl(1+XY/N\bigr),
\]
including skew lattices. In particular it does not depend on the
number of nonprimitive multiples on a short lattice line.

Proof. Use the exact rectangular floor-sum count from the AP note.
Since a is a unit and X<N, any vector with x>0 in the signed
rectangle automatically has y!=0. If the count is zero, return
the empty list. Otherwise binary search in x obtains a vector
u=(u_x,u_y) in the rectangle, with u_x>0. The least y>=-Y in
the required residue class is computed by one remainder. Check
gcd(u_x,N) and gcd(u_y,N); a nonunit coordinate gives a proper
factor because its nonzero absolute value is less than N.
If both are units, divide u by gcd(u_x,u_y). That integer is
invertible modulo N, so the divided vector remains in Lambda_a,
remains inside the rectangle, and is primitive in Z^2.

Find integers r,s with r u_x+s u_y=1 by extended gcd. The vector
v=N(-s,r) belongs to Lambda_a and det(u,v)=N. Since the index
of Lambda_a is N, u,v are a Z-basis of the full lattice.
Every vector in the symmetric box [-X,X] times [-Y,Y] is
uniquely j u+t v. The coefficient t satisfies
\[
 |t|\le K=\left\lfloor
            (|u_x|Y+|u_y|X)/N\right\rfloor .
\]
Indeed det(u,j u+t v)=Nt.

If K=0, every vector of the box is a multiple of u. Its only
primitive vector with positive first coordinate is u itself.
This is the case in which direct enumeration of all points
might have been exponentially expensive.

If K>=1, put rho=max(|u_x|/X,|u_y|/Y), so 0<rho<=1.
For each of the 2K+1 possibilities for t, intersect the two
integer intervals for j obtained from the coordinate bounds.
Their intersection contains at most 2/rho+1 integers.
Since K<=2rho XY/N, the total number of visited points is
at most
\[
 (2K+1)(2/\rho+1)
 \le 3K(3/\rho)\le18XY/N .
\]
There are no hidden loops over empty lines: 2K+1 obeys the
same bound. All coordinate and coefficient bit lengths are
polynomial in log N by the extended-gcd and determinant
bounds. Check the proper-gcd guard, sign and primitive
condition on each point. Every primitive unit point is
enumerated exactly once. The initial count/binary search
cost is polynomial in log N. End proof.

We did not need LLL or even Gauss reduction here. The short
vector is obtained by the already proved floor-sum oracle,
and the collinear case is handled algebraically.

### Smooth-ratio decision

Given an explicit prime base F of primes coprime to N, trial
divide the coordinates of the enumerated primitive pairs by F.
This decides whether a is represented by a signed F-smooth
ratio with nonzero numerator and denominator in the specified
box, or returns a factor. It is enough to consider primitive
pairs: any nonprimitive smooth representation can be divided
by its common divisor (which must be a unit under the unit
promise), without introducing a new prime or increasing either
coordinate. The complexity is polynomial in the base size,
log N and 1+XY/N. The enumeration itself does not count all
nonprimitive smooth pairs; that stronger counting assertion
is not needed or made.

## 2. Exact compressed aggregation of remaining prime products

Suppose the intended relation is a U x = V y mod N, with U,V
specified products of primes, and x,y the remaining products
of one prime from each of specified bands. Require all bands
across the two sides to be disjoint. In particular the residual
pair is automatically primitive. Let X and Y be the respective
products of the upper band endpoints, rounded down, and assume
X,Y<N and XY<=N B^C, with C fixed.

Apply Theorem 1 at multiplier a U V^(-1) mod N. For every
primitive pair in the residual rectangle, test positivity and
the required factorization pattern by trial division through
the remaining bands: one prime from each, exponent one, no
remaining cofactor. A further anchor interval condition on
Ux mod N can be checked by exact modular reduction. Each
complete witness pair is accepted exactly once.

**Corollary 2.** In the stated area range one can count and
extract all complete smooth product pairs, including an
arbitrary prescribed anchor interval, in deterministic
exp(O(b)) bit time, where B=2^b and the number of bands and
input bit sizes are polynomial in n=bit_length(N). Alternatively
a proper factor is returned.

This is compressed aggregation over *all* unknown remaining
prime choices, not just counting one specified conjunction.
The number of unknown primes may grow as Theta(n/b). A direct
expansion of those choices could be exponentially large in n;
we enumerate at most 18XY/N lattice points instead. The
disjoint-band restriction ensures that the exact count does
not require counting nonprimitive multiples. One can replace
the previous same-band-on-both-sides search by disjoint
intervals without loss of its character-moment coverage, as
proved below. The area constraint is essential: the old
unconditioned full-size rectangle has area about N^2 B^O(1),
which does not fit the budget.

## 3. Dense short-ratio coverage

Use the binary scales of the previous narrow-band note:
\[
 n=\operatorname{len}_2(N),\quad
 b=\lceil\sqrt{n\lceil\log_2(n+2)\rceil}\rceil,\quad
 B=2^b,\quad k=\lfloor(n-2)/b\rfloor,\quad L=k+2000.
\]
After the initial sieve every band prime is a unit. Divide
(B(1-1/(8L)),B] into L disjoint equal-width prime intervals.
Split them into sets of h=floor(L/2) and L-h slots. Take
independent uniform primes in the slots, let U,V be their
respective products, and consider the law pi of V/U mod N.

For each slot, the previously established uniform prime
character bound from the fixed Dirichlet/zeta zero-free strip
gives
\[
 |\lambda_{i,\chi}|\le B^{-1/100}\quad(\chi\ne1),
 \qquad m_i\gg B/(L^2\log B).
\]
For any k slots, including slots on both sides, two signed
products have the same residue only if they have identical
tuples. Cross multiplication gives equality modulo N of two
positive integer products of k primes each, smaller than N.
Unique factorization and the disjoint intervals imply actual
tuple equality. Orthogonality therefore gives exactly
\[
 \sum_\chi\prod_{i=1}^k|\lambda_{i,\chi}|^2
     = |G|/\prod_{i=1}^k m_i\le B^6.
\]
The logarithmic bound is the same elementary bound as in the
narrow-band coverage proof. For inverse slots the Fourier
coefficient is conjugated; its absolute value is unchanged.
Using the remaining 2000 slots,
\[
 \sum_{\chi\ne1}|\widehat\pi(\chi)|^2\le B^{-34}.
\]
Consequently the set D of actual short-ratio residues satisfies
\[
 |G\setminus D|\le |G| B^{-34}.
 \tag{1}
\]
The two coordinate bounds are X=B^h and Y=B^(L-h).
Both are less than N for sufficiently large n, and
XY/N=B^L/N<=B^2000. Both coordinates are of size at most
sqrt(N) B^O(1). Thus **membership in this dense set, and the
exact number of its specified disjoint-product representations,
can be computed deterministically in half-scale time**, by
Corollary 2 (or a proper factor is returned).

This differs from the original long-product support theorem:
both halves now have sizes around sqrt(N) rather than N.
In particular the *single* ratio query is a complete compressed
aggregation of all its prime tuples.

For arbitrary target a, take two such dense sets D_1,D_2
from disjoint collections of bands (using 2L equal-width
intervals in the same narrow band instead of L changes only
the fixed polynomial loss in their counts). By (1),
D_1 intersects a D_2^(-1). Thus every a is a product of
two short smooth ratios, and almost every unit intermediate
multiplier r works. Two calls to the exact ratio oracle,
at r and a/r, recover the complete representation. This
is another exact half-scale suffix/search formulation of
the original full-size congruence. It does not yet provide
a uniform deterministic choice of the intermediate r.

Similarly, if prescribed prefixes have total log size
at least log N-O(log B) and leave both residual bounds
below N, their residual area fits Corollary 2. Splitting the
2L bands into a balanced prefix collection and a balanced
suffix collection of L bands each, the ratio law of the
prefix is itself near uniform by the same moment calculation.
For each target, a fraction 1-o(1) of uniformly chosen
prefix tuples admit a smooth suffix completion. This gives
a uniform randomized one-shot prefix search with exact
compressed suffix counting. We have not proved deterministic
selection of the first prefix, or compressed aggregation for
the unrestricted 2L-slot pair sum.

## 4. A private-prime property of the primitive lattice

The next result gives a different way to complete the
remaining cofactors. Fix X,Y and a unit multiplier a as in
Theorem 1. Put
\[
 Z\ge\max(2,\lfloor 2XY/N\rfloor)
\]
and take F to contain every prime <=Z not dividing N.
If one of the excluded primes divides N properly, return it.
One may enlarge Z further within exp(O(b)).

**Lemma 3.** For distinct primitive unit pairs in the
rectangle, a rational prime p>Z can divide at most one
first coordinate and at most one second coordinate.

For example, if p divides both x_i,x_j, then their
determinant x_i y_j-x_j y_i is divisible by p. It is also
divisible by N, as both pairs are in Lambda_a. Since p
divides unit coordinates, gcd(p,N)=1. But its absolute
value is at most 2XY, strictly smaller than pN. Hence
the determinant is zero. The primitive integer pairs
with positive first coordinate are then identical,
contradiction. The proof for the second coordinate is
identical. This also holds for signed y. No analytic
hypothesis is used.

Let x_i',y_i' be the positive residuals of x_i,|y_i| after
removing every prime in F. Lemma 3 says the x_i' are
pairwise coprime, and the y_i' are pairwise coprime. There
is no need to factor the residuals themselves.

## 5. Exact nonnegative cofactor cancellation

Compute a gcd-free basis of the list of all residuals:
a pairwise coprime list of integers d_j>1 and their
nonnegative integral exponents in each residual. This
is a polynomial-bit-cost operation in the total list
description. For example repeatedly split two active
distinct bases A,B by their gcd g, replacing them by
A/g, B/g and g, adding exponent vectors as appropriate
and merging equal bases. The product of the distinct
active bases decreases by at least a factor of two at
each nontrivial split, so the number of steps is bounded
by the initial total bit length. All exponent entries
are bounded by the bit lengths of the original residuals.
This is exact integer gcd refinement, not prime factorization.

For each basis d_j, at most one x_i' and at most one
y_i' have nonzero exponent on it, by pairwise coprimality
on each side. Thus cancellation of the residual primes in
a product of ratios, with coefficient vector c, imposes
only equations of the following two kinds:
\[
 c_i=0 \quad\hbox{or}\quad e_i c_i=f_j c_j
                         \quad(e_i,f_j>0).
 \tag{2}
\]
A missing opposite occurrence imposes c_i=0. A shared
occurrence gives a positive rational ratio constraint.
Draw a graph on the pairs, with an edge for every shared
basis and its rational ratio; mark vertices forced zero.

**Theorem 4.** A nonzero rational cancellation vector
exists if and only if some connected component contains
no forced-zero vertex and has consistent ratio constraints.
If one exists, a nonzero vector with *nonnegative integer*
coordinates exists and can be computed in polynomial bit
time. Equivalently, all nontrivial cancellations in a
component have one common sign.

Proof. Along an edge the two coordinates are positive
multiples of one another; zero propagates. A product
of ratios around an inconsistent cycle forces the
component to zero. Conversely, choose one vertex of a
component with no such obstruction, assign it one, and
propagate the rational ratios along a spanning tree.
Check every remaining edge; consistency is exactly
what is needed for a solution. Set all other components
to zero and clear denominators. Along a tree path the
ratio is a product of at most the number of vertices
many rational factors, each numerator/denominator
bounded by the input bit lengths. Hence all output
bit lengths are polynomial in the list size. This
proves both directions and the cost claim. Pairwise
coprimality of the gcd-free bases ensures that the
equations are equivalent to actual equality of the
two residual integer products, not just equality of
some aggregated valuations. End proof.

For C=sum_i c_i>0, cancellation gives
\[
 a^C=\sigma\prod_{p\in F} p^{z_p}\pmod N,\qquad
 \sigma\in\{-1,1\},\qquad
 \sum_{p\in F}|z_p|\log p\le C\log(XY).
 \tag{3}
\]
The last bound follows by adding the individual coordinate
log sizes, then using the triangle inequality for the
remaining small-prime valuation vector. The signs of y_i
are retained in sigma; the cofactors themselves are units.
Large integer products need never be expanded: the z_p
are computed by integer linear combinations of the trial
division exponent rows. Thus (3) is an efficiently
computed compact smooth relation for a positive power
of a, even if no single lattice pair is smooth.

### Rank consequence

Take a prime factor base F containing the narrow band,
with Z and XY/N of half-scale size. For each q in F
choose T_q>0 by integer comparisons with q^T_q>XY.
Run Theorems 1 and 4 at a=q^T_q mod N (an already verified
order relation or proper gcd can be used immediately).
If the cofactor cancellation succeeds, (3) gives an
integer row T_q C_q e_q-z with modular product a sign.
If it succeeds for every q, the rows form a nonsingular
matrix: for a kernel vector w choose q maximizing
|w_q|/log q=M. Then
\[
 T_q C_q M\log q\le M C_q\log(XY),
\]
impossible unless M=0. As usual twice the absolute
determinant is a common annihilator. The established
generation and deterministic splitting argument applies.

All of this is within exp(O(b)) deterministic bit time,
including unsuccessful searches; one may try a
half-scale-size list of exponents T_q satisfying the
strict inequality. The exact row-space method can also
use the rows that were obtained: if the row span contains
a coordinate e_q, clear denominators and verify the
resulting order multiple for that q, and run the
square-chain split. Full rank is sufficient, not
necessary for a proper gcd. No proof that enough
compatible components exist at the required targets
has been obtained.

## 6. A rigorous restriction: uniform short smooth ratios are false

It is not enough to seek a pointwise analogue of (1) for
all multipliers while retaining these short rectangle
sizes and a small factor base. In fact even the
relaxed signed-smooth-ratio/graph formulation cannot
cover every multiplier.

For the square case let H satisfy sqrt(N)<=H<N and
H=sqrt(N) exp(O(b)). Suppose the entire factor base is
bounded by Z'=exp(O(b)), which can be larger than
2H^2/N. For all sufficiently large n there exist primes p
with
\[
 Z'<p< N/(2H),\qquad p\le H.
\]
For example apply Bertrand's postulate above an integer
bound max(Z',2); 2Z'=o(N/H) at these scales. Either
gcd(p,N) is a proper factor or p is a unit. At multiplier
a=p, all points with 1<=x<=H, |y|<=H obey y=p x as
an actual integer equality: |px-y|<N because
pH<N/2 and H<N/2 for large n. The only primitive pair
is (1,p), whose large prime p is private. There is
no smooth ratio and the graph has no nonzero
cancellation vector. The analogous obstruction works
with p^-1 by exchanging the coordinates and signs.
If desired there are many such unit primes by the
ordinary prime number theorem, since at most n primes
divide N. This is fully compatible with the density
bound (1), which permits a much larger exceptional set.

Even the disjoint-band ratio support alone misses every
positive integer a with aX<N and gcd(a,N)=1:
for a positive product pair with x>1, y<N,
the congruence forces y=ax, which contradicts the
disjoint-band coprimality. This includes all sufficiently
small band primes at the stated split sizes. Dense
coverage cannot simply be used to certify a fixed short
list of such multipliers.

These obstructions are for *arbitrary* multipliers and
specified rectangles; they do not prove failure for a
well-chosen power q^T, or for an adaptive choice of
rectangles, or for a product of two ratios. A small
finite fixture demonstrates failure at an actual target
power for one box: N=77, H=9, F={2}, T=7,
a=2^7 mod 77=51. The only primitive signed pair in the
box is (3,-1), and its outside-base prime is private.
The exact test rejects; this is not an asymptotic
counterexample to choosing other exponents/boxes.

## 7. Verified finite computations

The new standard-library script
[primitive_ratio_lattice.py](../verification/research/primitive_ratio_lattice.py)
was executed locally with Python 3.13.5. Exact tested
source: Git blob 446b6eb7e1c46388db7109d4f73b61665c071e59,
SHA-256
75c2ed71e403da3e599b66c593a9ae41133e00c7138c65e60da0273ea07bb204.

Observed output:

    rectangle comparisons 1581 early factors 363 empty 291 collinear 741 noncollinear 549
    graph versus exact rational kernel: 1583 comparisons
    all-target disjoint product counts 34 early factors 806
    prescribed-prefix smooth completion comparisons 100 early factors 0
    large-prime cancellation fixture 77 a 9 H 9 cutoff 2 pairs [(1, 9), (8, -5), (9, 4)] coefficients [1, 0, 1] reduced signed ratio 4 1

The rectangle comparisons enumerate signed boxes directly as
an independent oracle on small inputs; returned early factors
are checked by exact divisibility. The graph is compared with
an independent exact rational rank computation, including
a consistent and an inconsistent weighted cycle. The disjoint
product counts and prefix-conditioned counts are compared
with exhaustive finite tuple products, not with another
lattice implementation.

In the cancellation fixture, none of the individual
primitive pairs is 2-smooth on both sides, but the
first and third yield 9*9=81=4 mod 77 after cancellation
of the shared large residual 9. The input factorization
is not used in the algorithm. All finite congruences
and residual products are verified exactly. The
additional N=77, a=51 negative example was checked
separately by the same primitive enumeration and
graph routine. These finite examples do not establish
uniform graph coverage or factoring complexity.

## 8. Next precise targets

The new algorithm has removed the need to enumerate
unknown prime tuples in a determinant-scale rectangle,
and the graph criterion can convert multiple nonsmooth
pairs into a valid small-base relation. Two concrete
remaining targets are:

- a deterministic selection of a prefix/intermediate
  ratio, using the dense short-ratio membership oracle
  and the actual multiplicative structure of the
  two ratio sets; or
- a theorem supplying compatible residual graph
  components for a sufficient collection of large
  target powers q^T, possibly after varying T,
  box shape, or prescribed small factors within the
  half-scale budget.

The literal uniform one-ratio smoothness theorem is
false at the short scale, by Section 6. Density alone
and the previous average smooth-AP literature do not
give the needed target-specific conclusion.
No new generic derandomization assumption is being
substituted for it. The verified fixed zero-free strip
is used only for the density theorem; Theorems 1 and 4
and the obstruction are unconditional elementary
arithmetic and lattice results.

**Uniform deterministic L_N[1/2,O(1)] factoring remains
open.** This continuation has not started the one-third
program.
