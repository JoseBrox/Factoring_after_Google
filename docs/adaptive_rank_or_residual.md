# Adaptive exponent separation and residual recycling

**Status (27 November 2026): proved an unconditional adaptive
rank-or-residual dichotomy, not a uniform half-scale rank-increase
theorem.** The next target is preventing indefinitely many independent
residual directions. The more ambitious assertion remains open.
The one-third program is deferred.

This continues [dyadic balancing and global cofactor pooling](power_shift_pooled_relations.md).
All rank tests use exact rational arithmetic and gcd-free refinement.

## 1. Normalized relations and adaptive recycling

Let N be odd, let F be the finite prime base (including 2, with every
base prime a unit), and put m=|F|. Write
\[
 P(A)=\prod_{p\in F}p^{A_p}\pmod N,\qquad A\in\mathbb Z^m .
\]
Store a normalized row (A,x',y',sigma), where x',y' are positive
integers <=H<N, coprime to N, stripped of all base primes,
and
\[
 P(A)x'/y'=\sigma\pmod N,\qquad \sigma\in\{1,-1\}.
 \tag{1}
\]
For the analysis write R for its vector of true outside-base rational
prime valuations of x'/y'. The algorithm need not factor x',y': a
common gcd-free basis computes the same rational dependence kernel.
Indeed each basis element has prime support disjoint from all other
basis elements, and its valuations are not all zero. Thus the map
from basis coordinates to true prime coordinates is injective.

Keep a list of r rows whose residual vectors R_i are independent over Q,
and a list of d independent pure base relations (possible signs allowed).
Assume d<m, and let w be a nonzero rational annihilator of the pure
relations. Normalize it so max_p |w_p|=1 and choose q with w_q=1,
negating w if needed.

For any chosen integer combination c of previous normalized rows set
\[
 A_0=\sum_i c_i A_i,\quad R_0=\sum_i c_i R_i,\quad
 \rho_0=\prod_i(x_i'/y_i')^{c_i},\quad
 \sigma_0=\prod_i\sigma_i^{c_i}.
\]
Then P(A_0) rho_0 = sigma_0 mod N. In particular rho_0 is a compact
unit rational product; all modular operations can be performed by
binary powering without expanding that integer numerator/denominator.

For a chosen positive T take multiplier
\[
 a=q^T\rho_0^{-1}\pmod N.
\]
Apply the dyadic balancing theorem to find j<=J=O(log N).
If it finds a factor, stop. Otherwise obtain a unit pair
0<x<=H, 0<|y|<=H with 2^j a x=y mod N. The original balancing
basis supplies at least one such pair for H>=floor(sqrt N)+1.
One may enumerate all primitive pairs, or choose by the previous
local CRT completion theorem when its explicit height guard fits H.
If any relevant coordinate has a proper gcd with N, return it.

Combining this new equation with the old equations with coefficients c
cancels the entire prescribed residual rho_0^{-1}. The resulting
normalized row is
\[
 A=A_0+T e_q+j e_2+\nu_F(x)-\nu_F(|y|),\qquad
 R=\nu_{\bar F}(x)-\nu_{\bar F}(|y|).
 \tag{2}
\]
It has sign sigma_0 sign(y) and satisfies (1) for the stripped
coordinates. In particular the newly retained residual integers
are still <=H, independently of the size of the recycled product.

This allows prescription of arbitrary *known* residual products
in a raw relation without enlarging the enumeration area of the
new cofactors. It is algebraic recycling, not a theorem about
small-coordinate CRT constraints. Indeed
rho_0^{-1}=sigma_0 P(A_0) mod N, so the adjusted multiplier is
just a known multi-base power up to sign. Recycling by itself
cannot imply that the new residual vector lies in the old span.

## 2. Uniform adaptive separation theorem

Let ell_H=ceil(log_2(H+1)), and suppose r residual rows are independent.
In a gcd-free basis of old residual integers, solve the exact system
\[
 R_i\lambda=A_i\cdot w\qquad(1\le i\le r).
 \tag{3}
\]
Here the left side denotes the row of gcd-free exponents, not the
unknown true-prime row. Since the rows are independent, a rational
solution exists, and it can be computed using a pivot submatrix.
Put Lambda=||lambda||_infty, taking Lambda=0 for an empty pool.

**Theorem 1.** In (2), choose the integer T to satisfy
\[
 T>\|A_0\|_1+J+2\ell_H+2\ell_H\Lambda.             \tag{4}
\]
Then for **every** resulting normalized row (2), either:

1. its residual vector is independent of the existing residual
   vectors, and it increases the residual rank by one; or
2. an integral combination of the old rows and the new row
   cancels the residuals and gives a new base relation whose
   dot product with w is strictly positive.

Thus every completed attempt increases the sum of the residual
rank and pure base rank, unless it already returns a factor.
The theorem permits arbitrary adaptive local prescriptions,
any of the allowed dyadic shifts, and arbitrary candidate
selection within the height bound.

Proof. The new row has
\[
 A\cdot w \ge T-\|A_0\|_1-J-2\ell_H
                >2\ell_H\Lambda.
 \tag{5}
\]
The valuation bound uses sum_p nu_p(z)<=log_2 z.

We must ensure that (3) provides a legitimate linear functional
on the true prime coordinates of **new** residuals, including
those that split an old composite gcd-free basis element.
For each old gcd-free basis element d_j, choose in the proof
one prime p_j|d_j, and put weight lambda_j/v_{p_j}(d_j) on
p_j, with weight zero on every other prime. The supports of
the d_j are disjoint. The resulting functional on true-prime
valuations agrees with (3) on every old row, and all its
weights have absolute value <=Lambda. No selection of these
prime factors is needed computationally. Equivalently one can
refine the old basis together with the new integers and extend
the weight by the same argument on a factor of each d_j.

Consequently the absolute value of the functional on the
new residual row is <=2 ell_H Lambda. If R is dependent, solve
R=sum_i beta_i R_i exactly by gcd-free refinement and rational
linear algebra. The agreement on old rows gives
\[
 \left|\sum_i\beta_i A_i\cdot w\right|
   \le2\ell_H\Lambda.
\]
By (5), A-sum beta_i A_i has strictly positive dot product
with w. Clear denominators of the beta_i using a positive
integer. This produces an integral combination whose actual
residual product cancels. Its base relation holds up to a
sign; doubling removes that sign. Since w annihilates all old
pure relations, this gives a strict pure-rank increase.

If the new residual row is independent, append it to the
independent residual list. This proves both branches. All
computations use gcd-free integer factor refinement and
rational linear algebra; the true-prime functional was only
a proof device. End proof.

### Explicit Cramer version and cost

A conservative version avoids solving (3) in advance.
For r independent old residual rows, choose an invertible
r by r pivot submatrix. Its entries and the entries of a
new bounded residual row have absolute values <=2 ell_H,
also in a refined gcd-free basis. By Cramer's rule, any
coefficients of a dependent row have
\[
 |\beta_i|\le D_r,\qquad
 D_r=(r+1)!(2\ell_H+1)^{r+1}.
\]
Thus it suffices to replace the term 2 ell_H Lambda in (4)
by D_r sum_i ||A_i||_1. This gives the same theorem. The
dual version is generally much tighter, and avoids making
the target exponent unnecessarily large.

There is a polynomial bit bound over a prescribed number M
of adaptive attempts. Take for recycling coefficients with
l1 norm <=poly(M), for example recycle one old row or no row.
Use the least integer T satisfying the indicated bound.
For the Cramer variant the l1 norm of a new base row is at
most poly(M,log N) D_r times the maximum old l1 norm plus
a polynomial-in-log N additive term. The log of D_r is
O((r+1) log((r+1)(ell_H+1))). Hence over M calls the bit
length of every normalized base row is
O((M+1)^2 log((M+2)(log N+2))) up to the fixed polynomial
recycling bound. Denominator clearing for a pure relation
has polynomial bit cost in the same parameters, by the
minor bounds. The pivot solution in (3) has
Lambda<=D_r sum_i||A_i||_1 (choose zero nonpivot weights),
so the dual variant obeys the same type of bound, with a
further factor 2 ell_H in the multiplier norm estimate.

Computing w by exact elimination on the accumulated pure
rows costs polynomial time in these bit lengths. Its
normalization ||w||_infty=1 means that the preceding bound
does not multiply recursively by its denominator sizes.
All modular powers are charged their actual exponent
bit lengths. No succinct exponent evaluation is assumed.

For H<=sqrt(N) B^C, M<=B^D, |F|<=B^E, and fixed C,D,E,
the primitive rectangle enumeration and all the stated
linear algebra, gcd refinement, modular powers, and
candidate tests cost exp(O(log B)). For the local CRT
version choose its modulus subject to the prior
completion bound and include the cost of its guaranteed
gcd search. All algorithms return a factor if a verified
proper gcd appears.

## 3. The exact remaining rank-growth gap

After M completed attempts without factoring, let r_M
be the number of independent residual rows and d_M the
pure base rank. Theorem 1 gives exactly
\[
 r_M+d_M=M
\]
if one appends precisely the independent rows and pure
rank gains of the construction. Thus if d_M<m there
must be at least M-m+1 independent residual directions.

In particular, if it is independently established that
all residuals encountered have their true valuations in
a rational subspace of dimension <=R_*, then full base
rank follows in at most R_*+m attempts. This is a uniform
rank-increase theorem under a *dimension* bound, not a
smoothness assumption on any individual ratio. For
example it suffices that the union of outside-base prime
supports contains at most R_* primes, even if no single
ratio is smooth. Full rank supplies a common exponent
after denominator clearing and removal of signs. The
verified small-prime generation and earlier splitting
arguments then apply if the base is the designated
generating base.

The trivial unconditional choice R_*<=pi(H) follows from
the size of the retained residual integers. It yields a
finite algorithm, but at H near sqrt N the number of
iterations and their bit costs do not give the half-scale
bound. The number of *currently* exposed gcd-free basis
elements is not a uniform bound on the number that will
be exposed later. An independent residual row can
overlap many old prime factors and nevertheless introduce
a new direction. A bound on the number of rows per
lattice, or a proof of local primitive completion, does
not bound this cumulative dimension.

This identifies the precise missing mathematical step:
prove a uniform exp(O(log B)) bound on the residual
dimensions encountered by a suitable adaptive selection,
or directly force a residual dependence within that
budget. Theorem 1 eliminates the need to prove
nonvanishing of an additional base projection after a
dependence is found. It does not force the dependence.

## 4. Two limitations on using local prescriptions to close the gap

### A rigidity identity across nearby multipliers

Let two unit multipliers a,a' have a'/a=u/v mod N, where
u,v are positive coprime integers, both units modulo N.
Let primitive unit pairs (x,y),(x',y') be in their respective
signed boxes of bounds H, with positive first coordinates.
If a prime p divides both first coordinates or both
second coordinates, then
\[
 pN\mid vxy'-u x'y.
\]
If p>(u+v)H^2/N, the integer on the right has absolute
value less than pN and hence is zero. Therefore
\[
 y'/x'=(u/v)(y/x)\quad\text{in Q},
\]
not just modulo N. If the formal target exponent
difference is exactly the base valuation of u/v
(and u/v is base-smooth), the two raw exponent rows
are identical as formal valuation vectors.
Such a shared large factor cannot yield a new rank
gain by subtracting the two rows.

Similarly, if aa'=u/v mod N and a prime p divides one
first coordinate and the other second coordinate, then
pN divides vyy'-u xx'. Above the same cutoff this is
an integer identity. If the formal target sum is the
base valuation of u/v, adding the rows is formally
trivial. Both statements require the exact formal
target exponent correspondence, not merely equality
of modular images. Signs can be tracked separately.

Thus useful large-prime overlaps from nearby smooth
shifts cannot be inferred merely from observing shared
factors. The original private-prime lemma is the
special same-multiplier case.

### Counting obstruction for forcing a large known factor

Fix N and a list of K unit shifts independent of an
arbitrary unit multiplier a. For a specified unit
integer d>1, consider finding a unit pair with d|x,
1<=x<=X, 0<|y|<=Y, y=s a x mod N for a shift s.
Every triple (s,x,y) determines at most one a.
Consequently the number of covered multipliers is
at most 2K Y floor(X/d). Dividing by phi(N)>=N/(n+1)
gives relative size at most
\[
 \frac{2K(n+1)XY}{dN},\qquad n=\operatorname{len}_2(N).
\]
With XY<=N B^C, K<=B^D, and d>=N^delta for fixed
delta>0, this tends to zero. This holds even if the
search through the specified shifts is exhaustive,
and additional local congruences cannot enlarge
the covered set.

Thus a uniform theorem for *arbitrary* multipliers
that forces an existing large residual factor into
a coordinate of the original determinant-scale
box, by a fixed half-scale menu of smooth shifts,
is false. This counting statement does not cover
an adaptive choice of shift depending on a or the
specific prime-power targets. Nor does it forbid
the compact recycling operation in Section 1,
which changes the size of the raw prescribed
coordinate but bounds the newly retained residual.

## 5. Exact finite experiments, including negative results

The local standard-library prototype
[adaptive_pooled_rank.py](../verification/research/adaptive_pooled_rank.py)
uses the earlier primitive enumeration, dyadic balance, CRT
completion, and gcd-free rank routines. It checks actual
modular relations for every normalized row. In the dependent
case it independently verifies the cleared residual
combination and the resulting base-only modular power.

The script implements both Cramer separation and actual
dual separation. At each iteration it recycles one old
residual row (round-robin). The enumeration variant searches
the whole balanced rectangle for a dependence, preferring
large gcd overlap if none is found. The local variant
chooses an old exposed gcd-free factor when the proven CRT
budget allows, and otherwise a small base prime. It does
not factor the residuals. One hundred exact dependency
examples also check the Cramer bound.

Observed local output:

    Cramer dependency checks: 100
    adaptive Cramer 47053 base 17 H 651 rows 2 residual rank 0 base rank 2 CRT 0 shared CRT 0 max exponent bits 6 factor 223
    adaptive Cramer 100160063 base 17 H 30024 rows 40 residual rank 40 base rank 0 CRT 0 shared CRT 0 max exponent bits 6802 factor None
    adaptive Cramer 1000036000099 base 17 H 3000054 rows 40 residual rank 40 base rank 0 CRT 0 shared CRT 0 max exponent bits 7243 factor None
    adaptive Cramer 100160063 base 7 H 50040000 rows 25 residual rank 25 base rank 0 CRT 25 shared CRT 16 max exponent bits 2754 factor None
    adaptive Cramer 1000036000099 base 7 H 5000090000 rows 25 residual rank 25 base rank 0 CRT 25 shared CRT 19 max exponent bits 2864 factor None
    adaptive dual 47053 base 17 H 651 rows 2 residual rank 0 base rank 2 CRT 0 shared CRT 0 max exponent bits 6 factor 223
    adaptive dual 100160063 base 17 H 30024 rows 40 residual rank 40 base rank 0 CRT 0 shared CRT 0 max exponent bits 199 factor None
    adaptive dual 1000036000099 base 17 H 3000054 rows 40 residual rank 40 base rank 0 CRT 0 shared CRT 0 max exponent bits 221 factor None
    adaptive dual 100160063 base 7 H 50040000 rows 25 residual rank 25 base rank 0 CRT 25 shared CRT 20 max exponent bits 144 factor None
    adaptive dual 1000036000099 base 7 H 5000090000 rows 25 residual rank 25 base rank 0 CRT 25 shared CRT 21 max exponent bits 153 factor None

These unsuccessful fixtures are important. The previous
pooled-shift experiment did obtain full rank at N=100160063;
the different adaptive exponent selection tested here
does not reproduce that success in the allotted 40 calls.
In the local variants many prescribed factors are genuinely
reused, yet every new row adds an independent residual
direction. The dual rule improves exponent bit sizes
substantially in these runs, not the observed base rank.
The negative results are not counterexamples to every
possible adaptive selection rule.

The executed local source had Git hash
deeb5dd9dac85799e21d753853ef6d883327182d and SHA-256
d1ae63faff5cd45f6c48394b96fc6908c116334b966470a293fac74e9f3e8e31.
The source was subsequently committed and its final comment
normalized. A byte-for-byte identity of the tested local
file and the current remote blob was not established;
the displayed executable source was compared and the
local run is the evidence reported here, rather than a
claimed remote CI receipt.

## 6. Research decision

Do not treat target-exponent separation as a solution of
the half-scale coverage theorem. It is valuable because
it makes **any** residual dependence rank-increasing
and gives an exact accounting of failed calls. The
current negative tests indicate that greedily maximizing
gcd overlap or prescribing an old factor is insufficient
as a standalone strategy.

Next investigate a structural bound on the cumulative
residual space under adaptive target selection, or a
constructive method forcing residual-span membership
rather than a single shared factor. Retain the previous
broad pooled search in parallel because it succeeds on
fixtures where the present greedy selection stalls.
Theorem 1 may be used as a certificate-producing
subroutine when such membership is found.

**Uniform deterministic L_N[1/2,O(1)] factoring is still
open.** The requested uniform rank increase in the pure
base, within the half-scale time budget, has not been
proved. No new Lean milestone is counted.
