# Deterministic dyadic balancing and global cofactor pooling

**Status (27 November 2026): proved polynomial-bit-time balancing for
every target multiplier, a constructive local CRT completion theorem,
and exact global cofactor-elimination/rank criteria.** The combined
method produces a full-rank relation system in a finite experiment
where every separate target system has rank zero. Uniform deterministic
half-scale coverage remains open. No new Lean milestone is counted.
The one-third program remains deferred.

This continues
[primitive-ratio lattice aggregation](primitive_ratio_lattice_aggregation.md).
We address two limitations of that construction: an adversarially
collinear target lattice, and the requirement that every target
separately supply a smooth relation or a compatible large-prime
component. Both can now be removed from the *search and extraction*
algorithm. The missing theorem is uniform success of the enlarged
search, not mere exactness of its tests.

## 1. A smooth shift eliminates the short-rational obstruction

Let \(N\ge5\) be odd, \(a\in(\mathbb Z/N\mathbb Z)^\times\), and
\[
 h=\left\lfloor\sqrt{(N-1)/3}\right\rfloor,\qquad
 J=\operatorname{len}_2(h^2),\qquad S=\lfloor\sqrt N\rfloor+1.
\]
Then \(3h^2<N\), \(h+1>\sqrt N/2\), and
\(h^2<2^J\le2h^2<N\).
Write
\[
 \Lambda_c=\{(x,y)\in\mathbb Z^2:y=cx\bmod N\}.
\]
Every \(\Lambda_c\) with \(c\) a unit has determinant \(N\).

**Theorem 1 (dyadic escape).** At least one
\(j\in\{0,\ldots,J\}\) has
\[
 \Lambda_{2^j a}\cap[-h,h]^2=\{0\}.
\]
Such a shift can be found deterministically in polynomial bit time.
One may instead return a verified proper factor if one of the
short vectors exposes a nonunit coordinate.

Proof. Suppose every shift has a nonzero vector in the box.
Both coordinates must be nonzero, since an axis vector in this
lattice has its nonzero coordinate divisible by \(N\). Change
the sign if necessary to write these vectors as \((x_j,y_j)\)
with \(1\le x_j\le h\), \(0<|y_j|\le h\).
The congruence
\[
 y_{j+1}x_j-2y_jx_{j+1}\equiv0\bmod N
\]
and the absolute bound \(3h^2<N\) make this an actual integer
identity. Therefore
\[
 y_J/x_J=2^J(y_0/x_0).
\]
The two rational absolute values lie between \(1/h\) and \(h\),
contradicting \(2^J>h^2\).
To find a shift, apply the exact signed-rectangle floor-sum
count of the AP note to each \(2^j a\bmod N\), updating the
multiplier by one modular doubling. There are only \(O(\log N)\)
iterations. The count is zero precisely when the short square
contains no nonzero vector. A positive count permits a short
vector to be recovered by binary search and one modular
remainder, with the gcd guard if desired. No enumeration of
\(\sqrt N\) integers is used. End proof.

This theorem is unconditional and applies to **arbitrary** unit
multipliers, including any prescribed \(q^T\), or
\(q^T U/V\) after fixing partial smooth factors. More generally
the same argument works with an integer shift base \(d\ge2\)
coprime to \(N\) and any \(h\ge1\) satisfying
\((d+1)h^2<N\), using the least \(J\) with \(d^J>h^2\).
The dyadic choice is particularly useful because \(2^j<N\)
and 2 belongs to the enlarged small-prime base.

### A uniformly bounded basis

For the shifted multiplier \(c=2^j a\bmod N\), one can find
a lattice vector of smallest positive sup-norm \(s\) in
polynomial bit time, with
\[
 h<s\le S.
\]
The upper bound follows from the elementary signed Dirichlet
approximation/pigeonhole argument of the AP note. Binary search
on the exact square count finds \(s\), followed by binary
search for a positive first coordinate and recovery of the
second. If a coordinate is not a unit modulo \(N\), its gcd
is a proper divisor (both absolute values are nonzero and
less than \(N\)). Otherwise the vector \(u=(u_x,u_y)\) is
primitive in \(\mathbb Z^2\): dividing by an integer common
divisor would remain in the lattice since the divisor is a
unit, contradicting minimality of \(s\).

Choose integers \(r,t\) with \(r u_x+t u_y=1\).
Then \(v=N(-t,r)\) belongs to the lattice and
\(\det(u,v)=N\), so \(u,v\) are an actual integer basis.
Subtract an integral multiple of \(u\) from \(v\) to put
its coordinate in the dominant coordinate direction of \(u\)
in the interval of radius \(s/2\). The other coordinate has
absolute value at most \(N/s+s/2\), by the determinant identity.
Thus, with the original notation for the adjusted basis,
\[
 \|u\|_\infty\le S,\qquad
 \|v\|_\infty\le N/s+s/2<3S.                      \tag{1}
\]
This proves an exact deterministic normalization of the lattice
with no need for a numerical lattice-reduction algorithm.
In particular for any \(H\ge6S\) with \(H<N\), the box
\([-H,H]^2\) contains two independent vectors. The old
collinear obstruction for a multiplier with small nonsmooth
rational height is not an obstruction after allowing this
short list of dyadic shifts.

If \(K=\lfloor H/(6S)\rfloor\), every vector \(i u+jv\)
with \(1\le i,j\le K\) lies in the box. For coprime \(i,j\),
any common coordinate divisor of the vector divides \(N\):
this follows by applying the adjugate of the basis matrix.
There are at least \(K^2/4\) such coprime coefficient pairs,
since the number with a common divisor is bounded by
\[
 K^2\sum_{m\ge2}m^{-2}\le 3K^2/4
\]
(using the elementary bound \(1/4+\int_2^\infty x^{-2}dx\)).
The vectors are distinct and nonzero and none lies on an
axis if \(H<N\). Every one therefore gives a primitive
unit pair, or one exposes a proper factor. This shows
abundance of genuinely different primitive candidates,
not just many scalar multiples on one line.

## 2. Constructively complete arbitrary small local prime prescriptions

The bounded basis also gives a useful deterministic
local-to-global completion procedure.

**Theorem 2.** Let \(u,v\) be the basis from (1). Let \(D\ge1\),
\((D,N)=1\), and let \((\alpha,\beta)\bmod D\) satisfy
\(\gcd(\alpha,\beta,D)=1\).
Define the computable integers
\[
 w_*(D)=\max\{w\ge0:(w+1)!\le D\},\qquad
 L_D=(w_*(D)+1)2^{w_*(D)}+1 .
\]
In polynomial bit time in \(\log N,\log D,L_D\) (and hence
\(D^{o(1)}\operatorname{poly}(\log N)\) as \(D\to\infty\))
one can find a vector \((x,y)\in\Lambda_c\) with
\[
 (x,y)=(\alpha,\beta)\bmod D,\qquad
 \max(|x|,|y|)\le3S D(1+L_D),\qquad
 \gcd(x,y)\mid N .                                      \tag{2}
\]
The vector is nonzero. If its bound is smaller than \(N\),
the gcd guard either factors \(N\) or certifies a primitive
unit pair.

Proof. The basis matrix is invertible modulo \(D\) since
its determinant is \(N\). Solve for its coefficient residues
\((i_0,j_0)\) and choose representatives in \([1,D]\).
They satisfy \(\gcd(i_0,j_0,D)=1\).
Fix \(i=i_0\) and take \(j=j_0+Dk\) for
\(0\le k<L_D\).

Every prime dividing both \(i_0\) and \(D\) is automatically
coprime to \(j\). Each of the other \(w\) distinct primes
dividing \(i_0\) excludes exactly one residue class of \(k\).
Their number is at most \(w_*(D)\), since the product of
\(w\) distinct primes is at least \((w+1)!\) and \(i_0\le D\).
By elementary CRT inclusion-exclusion, the number of allowed
\(k\) is at least
\[
 L_D\prod_{p\mid i_0,\ p\nmid D}(1-1/p)-2^w
 \ge L_D/(w+1)-2^w>0.
\]
The product lower bound follows by ordering the distinct
primes \(p_i\ge i+1\) and telescoping.
No factorization of \(i_0\) is required by the algorithm:
try successive \(k\), computing only \(\gcd(i_0,j_0+Dk)\).
The explicit bound proves termination. Since
\(\gcd(i,j)=1\), the adjugate argument yields the divisor
claim in (2); the norm bound is immediate from (1).
Finally the elementary factorial lower bound gives
\(w_*(D)=O(\log D/\log\log D)\), so
\(L_D=D^{o(1)}\). End proof.

For the half-scale box \(H=\lfloor\sqrt N B^C\rfloor\),
with \(B=\exp(\Theta(\sqrt{\log N\log\log N}))\) and fixed
\(C>0\), this proves that one can force any primitive
coordinate residue prescription modulo
\(D\le B^{C-\varepsilon}\) for fixed \(0<\varepsilon<C\)
for all sufficiently large \(N\). In particular disjoint
collections of required prime powers in the numerator and
denominator can be prescribed, together with avoidance of
those primes in the opposite coordinate, by taking
\((0,1)\) or \((1,0)\) modulo the relevant prime powers.
This can force a growing number of small prime factors.
It does **not** ensure smoothness of the remaining large
cofactor: the logarithm of the allowed prescribed product
is \(O(\log B)\), rather than order \(\log N\).

All this arithmetic is deterministic and uses the actual
lattice determinant. It does not depend on an independence
heuristic for divisibility in an ill-conditioned box.

## 3. Preserve the rank argument after dyadic shifts

Let \(\mathcal F\) be a small-prime base containing 2 and
the generating prime band, all coprime to \(N\).
For each \(q\in\mathcal F\), choose a positive integer \(T_q\)
with \(q^{T_q}>NH^2\). The shifted lattice at
\(a=q^{T_q}\bmod N\) provides rows
\[
 q^{T_q}2^j x\equiv y\pmod N,\qquad
 0<x\le H,\quad0<|y|\le H,\quad 0\le j\le J.
 \tag{3}
\]
In the presence of fixed prescribed smooth factors on the two
sides, increase the exponent threshold by their product.
The unprescribed version suffices here.

Suppose we can combine finitely many such rows for the
same target \(q\), with nonnegative integer coefficients,
not all zero, so that every outside-base prime valuation
cancels. Write \(C_q\) for their coefficient sum,
\(J_q\) for the weighted sum of the shifts, and \(z_q\)
for the combined base valuation row of \(x/|y|\).
Then the actual exponent relation (up to a sign) is
\[
 T_q C_q e_q+J_q e_2+z_q .
\]
Here \(J_q\le J C_q\) and
\(\sum_p |z_{q,p}|\log p\le 2 C_q\log H\).
If such a row exists for every target, the matrix is
nonsingular. Indeed for an annihilator \(w\ne0\), let
\(M=\max_p|w_p|/\log p\) and choose an attaining \(q\).
Its row equation would give
\[
 T_q C_q M\log q
 \le C_q M(J\log 2+2\log H)
 < C_q M(\log N+2\log H),
\]
contradicting the exponent threshold. This includes \(q=2\),
for which both the principal and shift terms occupy the
same column. Signs are removed by doubling each row.
Exact integer elimination and the usual verified exponent
scan then yield a factor.

Thus allowing dyadic shifts never forces a loss of the
previous strict rank inequality. In fact one can allow
different positive target exponents in a nonnegative
combination, provided each satisfies the displayed strict
threshold. This is a sufficient coverage criterion, not
a proof of the required cancellations.

### A direct cycle search across shifts

Previously, the weighted residual graph concerned only
one lattice, using the within-lattice private-prime lemma.
We can now pool rows even at *different* shifted multipliers.

For a fixed unshifted target \(q^{T_q}\), strip all base
primes from \(x,|y|\) in each row (3), obtaining positive
residual integers \(X',Y'\). Draw a directed edge
\(X'\longrightarrow Y'\), labelled by the complete row,
for every enumerated pair at every shift.
Every directed cycle cancels the whole residual integers
exactly, with nonnegative coefficients equal to one for
each occurrence on the cycle. The cycles can be found
deterministically by ordinary graph search; no factorization
of the residuals is required. A self-loop corresponds to
one already smooth primitive ratio.

This sufficient cycle test is not the old necessary-and-
sufficient single-lattice weighted graph test. It can
succeed by joining edges from different shifts, where
the old uniqueness of outside-prime occurrences need
not hold. Conversely it may miss cancellations between
partially overlapping residual integers. The exact
global elimination below includes both kinds of
cancellation and is more general.

## 4. Exact global cofactor pooling across all targets

The requirement that each target separately produce a
nontrivial relation is unnecessarily restrictive. There
is an exact and efficient way to pool *all* partial
ratios, across shifts, target exponents, and distinct
target primes.

For every collected row
\(q_i^{T_i}2^{j_i}x_i\equiv y_i\bmod N\), check unit
coordinates and the modular congruence. Remove all primes
of the chosen base from \(x_i,|y_i|\).
Compute a **single** gcd-free basis \(d_1,\ldots,d_s>1\)
for the entire list of residual integers, across every
row. These are pairwise coprime integers, not necessarily
primes. The elementary gcd splitting construction of the
previous note has polynomial bit cost in the total
description size. Its representation of each residual
is checked by exact integer products in the finite tests.
All \(d_j\) are units modulo \(N\).

Let \(R\) be the integer matrix of residual exponent
differences (numerator minus denominator). Let \(A\)
be the integer matrix of base exponent rows
\[
 A_{i,*}=T_i e_{q_i}+j_i e_2+
                 \nu_{\mathcal F}(x_i)-\nu_{\mathcal F}(|y_i|).
\]
An integral combination \(c\) of the rows whose residual
product is one is characterized exactly by \(c^T R=0\):
the pairwise coprimality of the gcd-free bases proves
both directions, even without knowing any of their prime
factors.

**Theorem 3 (global rank criterion).** The rational span
of all small-base relations obtainable by exact cofactor
cancellation in the collected list has dimension
\[
 \boxed{\operatorname{rank}_{\mathbb Q}[\,R\mid A\,]
                   -\operatorname{rank}_{\mathbb Q}R.}    \tag{4}
\]
In this formula a rational combination represents a genuine
integral exponent relation after clearing the denominators
of the combination and removing its possible sign.

Proof. Project the row space of the augmented matrix onto
its residual coordinates. Its image is exactly the row
space of \(R\), and its kernel consists of the vectors
\((0,z)\) from residual-zero combinations. Rank-nullity
proves (4). Conversely every vector of the kernel has
a rational representation as a combination of the
original rows. Clear the denominators of those coefficients
(not merely the denominators of \(z\)) to obtain an actual
integral combination. Its residual factors cancel exactly,
and its modular product is a sign. Doubling removes that
sign. End proof.

To implement this, order the residual columns before the
base columns and perform exact rational elimination,
retaining the representation of each pivot in the
original rows. The pivots in the base block form a basis
of the residual-free subspace. Equivalently compute an
integer basis of the residual kernel and then do the base
elimination. Exact integer/rational linear algebra with
polynomial bit bounds on minors and Cramer denominators
has polynomial bit cost in the dimensions and input
entry lengths.

For each \(p\in\mathcal F\) whose coordinate vector lies
in the residual-free row space, solve for an explicit
rational combination of the original rows representing
\((0,e_p)\). Clear its denominators \(E_p>0\). Then
\[
 p^{2E_p}\equiv1\bmod N.
\]
This is checked independently by binary modular powering.
The 2-adic chain can already split \(N\) if a base with
a separating local order has been covered. If the rank
in (4) equals \(|\mathcal F|\), then all bases are covered.
The lcm of the checked exponents has polynomial bit
length in the total description. As the prime band
generates the group by the established Dirichlet estimate,
this lcm is a common group annihilator, and the earlier
deterministic splitting theorem applies.

The exact span is independent of the chosen gcd-free
basis: its residual-zero constraint is equality of
positive rational residual products after clearing
denominators. Adding more rows and recomputing a common
basis cannot decrease the true small-base relation space.
Pooling can increase it strictly beyond the sum of all
separate-target relation spaces, because new cross-target
cancellations become possible.

For any fixed half-scale box parameter \(H\le\sqrt N B^C\)
with \(H<N\), and any list of at most \(B^{O(1)}\) target
powers of polynomial-in-\(B\) bit length, enumerating
all primitive pairs at all \(O(\log N)\) dyadic shifts
costs \(\exp(O(\log B))\), by the previous primitive-lattice
enumeration theorem. All matrix entries, raw list lengths,
gcd refinement and exact rank/certificate computations
therefore stay within that budget. One may restrict to
the balanced shifts or retain every shift. No claim is
made that the pooled rank always becomes full.

### A weaker sufficient target for rank increase

The signed elimination criterion (4) is exact and need
not use positive combinations. Positivity gives a useful
sufficient condition when designing a collection adaptively.

Suppose the current base relation row space is proper,
and take a nonzero rational annihilator \(w\). Choose
target primes with nonzero \(w_q\) of the same sign
(negate \(w\) if necessary). Put
\(W=\max_p|w_p|\).
For each such \(q\), choose a positive integer \(T_q\)
satisfying the exact rational comparison
\[
 T_q |w_q|>(J+2\lceil\log_2 H\rceil)W.                    \tag{5}
\]
This is computable with polynomial bit length, even if the
exponent value itself is much larger than \(\log N\);
binary powering charges its bit length. Each raw row (3)
then has base part with strictly positive dot product
with \(w\) (for the chosen positive sign). Indeed the
shift and coordinate valuations contribute in absolute
value at most the right side of (5).
A nonzero **nonnegative** rational combination of any
of these raw rows whose residuals cancel therefore gives
a strict rank-increasing relation, regardless of which
targets occur in that combination. The existence of such
a combination in a finite pool is an exact rational
linear feasibility problem \(c^T R=0,\ c\ge0,\sum c_i=1\),
solvable in polynomial bit time by standard rational
linear programming. The previous directed-cycle test
is a special case; the signed span computation is more
general for the actual extraction. This reduces the
sufficient coverage assertion to finding a cancellation
somewhere in a suitably sign-selected pooled family,
rather than requiring every target independently to
have a smooth representation.

No uniform theorem supplying this positive combination
or the corresponding signed rank increase has been
established. In particular, a lower bound on the number
of primitive candidates alone cannot prove that their
outside-base valuations cancel.

## 5. Exact finite verification

The two scripts below were run locally with Python 3.13.5,
using only standard-library integer/rational arithmetic and
the earlier exact primitive-ratio lattice routines.
Their committed Git blobs were checked to match the tested
local files byte-for-byte.

### Balancing, local completion and cross-shift cycles

[verification/research/target_power_balance.py](../verification/research/target_power_balance.py)

Git blob: `deb87f2c10bd889c3e905a4c58a4def66f13d33b`
SHA-256: `df47aa204715ee680db567eb83e4f93d2727f175e14a92423d516b7a11962462`

Observed output:

    balanced lattice checks: 2496 proper factor exits 82 nonzero shifts 1061 max shift 9
    local primitive CRT completion checks: 16425 additional 201-bit balanced lattices 98
    cross-shift-only fixture: 47053 q 2 T 40 H 434 base bound 7 shifts 15 rows 61 cycle [(0, 50, 177), (9, 354, -185), (14, 222, 275), (1, 264, -13), (14, 364, 27)]

The small-lattice tests independently enumerate all possible
first coordinates in the short square to verify the escape
condition. The local completion checks verify the prescribed
residues and coprime basis coefficients; some deliberately
small test moduli permit local vectors larger than \(N\),
so those checks do not assert the bounded-box unit conclusion
without its explicit size guard. The 201-bit examples
test the balancing and the local construction without
large-coordinate enumeration.

In the cycle fixture the full primitive lists at each
of the 15 shifts were checked by the earlier exact
necessary-and-sufficient weighted graph cancellation
routine: none has a cancellation. The displayed cycle
uses five distinct rows from four shifts and cancels
the large residuals as actual positive integers. The
signed modular congruence of the product is checked.
The parameters are illustrative finite values, not
the asymptotic \(B\)-schedule.

### Pooled relation rank

[verification/research/pooled_shift_relations.py](../verification/research/pooled_shift_relations.py)

Git blob: `2c232588e5f6304a96c456e35245171be6a2f21a`
SHA-256: `fb833c62c15ae48f0636ca747ca955d9c52910b6b1f86234fad140741230c58d`

Observed output:

    pool gain: 100160063 H 30024 base [2, 3, 5, 7, 11, 13, 17] rows 1915 separate rank 0 pooled rank 7 residual rank 579 factor 10007
    pooled versus separate exact rank: 6 comparisons, 1 strict gains, 18 proper-factor exits
    full-rank fixture: (100160063, 30024, [2, 3, 5, 7, 11, 13, 17], 1915, 0, 7, [0, 0, 0, 0, 0, 0, 0], 10007)
    unshifted 74 pooled rank 0 residual rank 74 certificate exponent bits 0 factor None
    balanced_only 1377 pooled rank 7 residual rank 521 certificate exponent bits 34 factor 10007

This fixture has **zero** residual-free rank for every
individual target, even after pooling all of that target's
dyadic shifts. Pooling across different target primes gives
full rank seven. Restricting to balanced shifts alone also
gives full rank. For every recovered coordinate relation,
the script explicitly checks the integer combination of
original exponent rows after clearing denominators, and
checks the resulting modular power. The factor is verified
by the exact gcd chain. The input factorization is never
used to construct the relations. This is a strict finite
improvement over independent-target processing; it is not
evidence of a proved asymptotic probability or uniform
coverage bound.

## 6. Remaining task

The earlier collinear short-ratio counterexample does not
block the dyadically normalized target search. The lattice
is uniformly well-conditioned after an admissible smooth
shift, local congruences of subexponential product size
can be forced, and global elimination allows cross-target
cancellation without factoring the residuals or obtaining
an individually smooth ratio.

The most promising next mathematical task is a uniform
rank-increase theorem for the **pooled** family, or a
constructive selection of local prescriptions and shifted
target powers giving the required cancellation. One can
seek the positive residual-kernel witness in (5), or
directly prove a nonzero projection rank gain in (4).
Neither follows from the previous character-moment density
of short smooth ratios or from the balancing theorem.
In particular no new assertion about simultaneous smooth
values of two large linear forms in short boxes has been
proved. The explicit local product budget in (2) is not
enough to account for the entire coordinate height.

**The uniform deterministic \(L_N[1/2,O(1)]\) factoring
bound remains open.** These are unconditional arithmetic
and exact-search improvements, plus finite verification;
no new complete formalization milestone is counted.
