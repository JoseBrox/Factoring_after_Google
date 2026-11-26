# Shared arithmetic progressions: exact high-degree counting and forced partial relations

**Status (27 November 2026).** Proved an exact polynomial-bit-cost
oracle for arbitrary conjunctions of specified prime divisibility
conditions on two translated progressions, a uniform partial-sieve
count, and deterministic construction of signed partial relations with
prescribed factors. A weighted rank lemma removes the requirement that
the residual factors have exactly the original narrow-band form.
Uniform deterministic half-scale factoring remains open. The
one-third program remains deferred. No additional Lean milestone is
counted.

This addresses the remaining arithmetic-specific search from
[narrow-band streaming atoms](narrow_band_streaming_atoms.md).
The key change is to combine the prime conditions by CRT before
counting, rather than multiplying the individual streaming state
spaces. The unresolved operation is aggregation over unspecified
prime choices, not evaluation of a specified conjunction.

## 1. Notation and canonical lifts

Use the parameters of the narrow-band note: n is the binary length
of N, b=ceil(sqrt(n ceil(log_2(n+2)))), B=2^b,
k=floor((n-2)/b), L=k+J with J=2000, and X=B^L.
Put M=floor(X/N), so for sufficiently large n,
\[
 B^{J-1}/8 \le M\le B^J.
\]
The primes P_i belong to L disjoint narrow intervals with all
their primes in (B(1-1/(8L)),B]. We assume the initial sieve has
not found a factor, so these primes are units modulo N. In
particular every full product Q of one prime from each interval
satisfies 7X/8<Q<=X.

For the counting oracle we use canonical representatives
r in [0,N-1] and y=ar mod N in [0,N-1], where a is a fixed unit.
For each prime q, multiplier 1 or a, and integer lift index j,
the divisibility atom is q|(r+jN) or q|(y+jN).
These are the canonical-lift versions of the shifted streaming
atoms. They do not require a small-state streaming implementation
when used in the deterministic count below.

Full product membership can equivalently be tested using these
canonical atoms, with 0<=j<=M and the integer lift in [7X/8,X].
If the lift is divisible by one prime from every interval,
their product Q divides it; since both are positive and
the lift is at most X<2Q, the lift equals Q. Conversely
every such Q is one of these lifts. Thus the change of
representative does not change the desired success predicate.
It is important to distinguish the new canonical atoms from
the individually streamed shifted atoms, whose representative
depends on the truncated quotient of the raw anchor.

## 2. Exact rectangular congruence count

For integers m>0, H>=0, A,C, define the floor sum
\[
 S(H,m,A,C)=\sum_{i=0}^{H-1}\left\lfloor\frac{Ai+C}{m}\right\rfloor .
\]
It is computable in polynomial bit time in the binary lengths
of its four arguments, even when H is exponentially large
and A,C have either sign.

Here is an elementary proof of the recurrence used in the
implementation. First take quotient and remainder on division
of A and C by m, adding the corresponding
q_A H(H-1)/2+q_C H to the answer. Now 0<=A,C<m.
Put Y=floor((AH+C)/m) and C'=(AH+C) mod m.
If Y=0 the remaining sum is zero. Otherwise A>0, and counting
the lattice points by horizontal rows gives
\[
 \begin{aligned}
 S(H,m,A,C)
 &=\sum_{j=1}^Y\bigl(H-\lceil(jm-C)/A\rceil\bigr)\\
 &=\sum_{j=1}^Y\left\lfloor\frac{(Y-j)m+C'}A\right\rfloor\\
 &=S(Y,A,m,C').
 \end{aligned}
\]
The first sum includes a possible last row of size zero;
all terms are nonnegative because j<=Y. Each recursive call
performs the Euclidean interchange of the positive modulus and
its smaller remainder after normalization, so there are
O(log m) calls. All intermediate integer sizes are polynomially
bounded in the initial operand bit lengths.

For any signed integer intervals [s0,s1], [t0,t1], the
number of pairs with
\[
 t\equiv c s+d\pmod N
\]
equals
\[
 S(H,N,-c,t_1-cs_0-d)
 -
 S(H,N,-c,t_0-1-cs_0-d),\qquad H=s_1-s_0+1.       \tag{1}
\]
This follows by counting t for each s using two floors.
An empty interval gives zero. Formula (1) counts actual
pairs, not just residue classes, so no assumption that
either interval length is less than N is needed.

## 3. Arbitrarily many specified prime conditions

**Theorem 1.** Given a unit a modulo N, intervals I,I'
inside [0,N-1], and arbitrary finite lists of specified
prime divisibility atoms on the two canonical progressions,
one can compute exactly the number of anchors r in I
with ar mod N in I' satisfying every atom, in polynomial
bit time in the total description. In particular there is
no restriction to a constant number of atoms or to moduli
of product at most B^C.

Proof. On the first side, the condition q|r+jN requires
r=-jN mod q. Repeated q with inconsistent residues makes
the count zero. Otherwise CRT combines every distinct
prime condition on that side into
\[
 r=u+U s,\qquad 0\le u<U.
\]
Similarly the other side becomes
\[
 y=v+V t,\qquad 0\le v<V.
\]
Empty lists use U=1 or V=1 with residue zero. The four
interval endpoints give exact integer bounds for s,t
by ceilings and floors. Since gcd(V,N)=1, the remaining
congruence y=ar mod N is
\[
 t\equiv aU V^{-1}s+(au-v)V^{-1}\pmod N.
\]
Apply (1) to the two intervals. There is exactly one y
in [0,N-1] for each r, so the count is an anchor count.
The bit length of U or V is bounded by the sum of the
prime bit lengths in the list, and CRT, modular inversion,
integer division and the floor sum have the required cost.
End proof.

This also counts conditional completions of any prescribed
prefix of the n-bit raw anchor R: its possible values
form one integer interval in [0,2^n-1]. Reduction modulo
N splits this interval into at most two canonical intervals
(count each with its own multiplicity). The quotient/remainder
and CRT count are all exact. Upper and lower bounds on
lifts, such as 7X/8<=r+jN<=X, are simply additional
interval restrictions on r or y, so they are handled by
the same oracle.

Thus an explicitly supplied **sparse rational polynomial
of arbitrary degree** in the two collections of canonical
divisibility atoms has exact prefix-conditional expectations
within polynomial time in its expanded description length.
For this statement a monomial means a product of positive
Boolean atoms, with arbitrary signed rational coefficient;
repetitions of an atom are harmless. A list of negative
literals can be expanded by inclusion-exclusion, but no
polynomial cost is asserted for that expansion if the number
of negative literals grows. The previous constant-degree
streaming-DP oracle is therefore not the limit of exact
conditional computation in this arithmetic model.

A further extension to any **fixed** number of multipliers
follows from the fixed-dimensional integer-point-counting
theorem of Barvinok:
[A polynomial time algorithm for counting integral points
in polyhedra when the dimension is fixed, 1994](https://doi.org/10.1287/moor.19.4.769).
After CRT, write r=u+Us, y_i=v_i+V_i t_i and impose
a_i r-y_i=N w_i with integral w_i. The bounds on r,y_i
and these equations define a bounded rational polytope in
one plus twice the number of additional multipliers
variables. The w_i and t_i are unique for a feasible r;
hence the count is exactly the desired anchor count.
The dimension is fixed independently of n, even if the
prime lists are long. This extension uses the published
theorem; our finite implementation uses only the elementary
two-multiplier floor sums.

## 4. Count partial product pairs without specifying either lift

A related, more useful formulation avoids individual lift
indices altogether. Fix arbitrary prescribed products U,V
of allowed prime factors. Let x,y range in any two signed
integer intervals [X0,X1],[Y0,Y1]. We seek
\[
 U\mid x,\qquad V\mid y,\qquad y\equiv ax\pmod N.
 \tag{2}
\]
Writing x=Us, y=Vt immediately reduces the count to (1)
with c=aUV^{-1} mod N, d=0 and integer intervals obtained
by dividing their endpoints by U,V.

**Theorem 2.** The number of all partial witness pairs (2)
in the two given intervals is computable in polynomial
bit time in the description, without enumerating either
the integer range or its lifts. A further condition
x mod N in a given canonical anchor interval I can be
handled by splitting the x-range into its quotient
intervals [jN,(j+1)N-1] and applying (1) to their
intersections with jN+I. Only one lift index is enumerated,
not a pair of indices. For the half-scale box
[7X/8,X], there are at most M+2 such intervals. Thus the
prefix-conditioned partial-pair count takes half-scale
time for each prescribed U,V, no matter how many primes
are already prescribed.

This is a count with multiplicities of lifts, which is
exactly what is needed for a positive witness-count
potential. It need not be a count of distinct residues.
If desired, the anchor interval restriction can also be
handled in polynomial bit time without quotient enumeration,
using Barvinok in fixed dimension: impose Vt-aUs=Nw and
lo<=Us-Nj<=hi with four integer variables s,t,w,j.
For each feasible pair s,t, both w and j are unique.

Positive counts are self-reducible. Binary search on the
left integer interval using the counts finds the least
feasible s; for this s one modular residue and the lower
bound on t determine the least feasible t. The same
applies to a specified anchor interval using the restricted
counts. All of these are deterministic constructions of
actual partial witnesses, not estimates of an expected
number of smooth witnesses.

## 5. Uniform partial sieve: exact use of the common lift index

For a single fixed anchor r and the lift interval 1<=j<=M,
every specified collection Q of distinct band primes is
simultaneously hit exactly on one residue class modulo
D_Q=prod_{q in Q}q:
\[
 j\equiv-rN^{-1}\pmod {D_Q}.
\]
Consequently the number of hits is M/D_Q+O(1), with
absolute error at most one, uniformly in r, including
nonunit anchors. This is a direct integer count, not an
independence hypothesis. In particular **every** prescribed
tuple of at most J-2 primes can be forced deterministically
into a lift, since D_Q<=B^(J-2)<M. CRT gives the first
positive lift index directly.

There is also a uniform count when the prime in each of
several specified bands may vary. Let I be a set of h
distinct intervals, let
\[
 \sigma_i=\sum_{q\in P_i}1/q,\qquad
 C_i(j)=\sum_{q\in P_i}1_{q\mid r+jN}.
\]
Expanding and applying the preceding exact CRT count gives
\[
 \sum_{j=1}^{M}\prod_{i\in I} C_i(j)
 =M\prod_{i\in I}\sigma_i
   +O\left(\prod_{i\in I}|P_i|\right).
 \tag{3}
\]
Since |P_i|<=B sigma_i, the relative error is at most
B^h/M. The main term counts tuples with multiplicity.

To count distinct successful lifts instead, note for
nonnegative integer counts with all C_i>=1 that
\[
 0\le\prod C_i-1
   \le \sum_i {C_i\choose2}\prod_{\ell\ne i} C_\ell.
\]
When any C_i=0, the corresponding overcount is zero and
the same inequality bounds the overcount. The inequality
for positive counts follows by telescoping the product
after replacing the factors one at a time by one, and
using C_i-1<={C_i choose 2}.
For each term on the right, count two distinct primes
from the chosen interval and one from every other
interval. CRT again bounds it above by
\[
 \frac{M}{2}\sigma_i\prod_{\ell\in I}\sigma_\ell
 +\frac{B^{h+1}}2\sigma_i\prod_{\ell\in I}\sigma_\ell.
\]
Thus for h<=J-3 the number of lifts hitting every band in
I is
\[
 M\prod_{i\in I}\sigma_i
 \left(1+O\left(B^h/M+
       \sum_{i\in I}\sigma_i(1+B^{h+1}/M)\right)\right).
 \tag{4}
\]
The error is o(1) uniformly in r and the chosen h bands:
J is fixed, M>=B^(J-1)/8, and sigma_i=O(1/L^2)
even by counting all integers in a narrow interval.
This proves genuine local sieve equidistribution for the
shared progression, beyond the earlier abstract moment
obstruction.

It does not extend to all L bands by the same argument:
L grows unboundedly, whereas the lift range has fixed
power B^J. For a complete tuple its modulus is of order
X=N times the lift length; a complete-tuple count is zero
or one, and the relative error of the naive CRT main term
is uncontrolled. The logarithm of the unaccounted
cofactor after forcing only J-2 primes is still of order n.

## 6. Force a growing number of prime factors by varying the anchor

The preceding uniform local sieve can force only a fixed
number of primes at a prescribed anchor. The joint congruence
geometry allows much more if the anchor is free and signed
integer representatives are permitted.

**Theorem 3.** Suppose N>=5, a,U,V are units modulo N
and U,V are positive integers. Put H=floor(sqrt(N))+1.
There is a deterministic polynomial-bit-time algorithm
returning integers s,t with
\[
 1\le s\le H,\qquad 0<|t|\le H,\qquad
 aUs\equiv Vt\pmod N.                                  \tag{5}
\]
If a proper gcd of a cofactor with N occurs, it is a
factor; otherwise the relation is between units.

Proof. Put c=aUV^{-1} mod N. The H+1 distinct residues
c i mod N, 0<=i<=H, can be partitioned into H consecutive
integer intervals of length at most ceil(N/H)<=H.
Two are in the same interval. Subtract them and choose
the orientation to make the nonzero difference of indices
positive. This yields s,t satisfying (5), with t nonzero
since c is a unit and 0<s<N. We do not enumerate these
residues in the algorithm. Instead use the floor-sum
count (1) for [1,H] times [-H,H], then binary search for
the least s admitting t, and recover t by a modular
residue calculation. There are O(log N) count queries.
All calculations have polynomial bit cost in the data.
End proof.

Now take h=floor(k/2) and prescribe one prime from each
of h distinct original bands for U and one from each
of another h bands for V (they can be chosen disjoint).
Since U,V<=B^h<=sqrt(N/2), the constructed integers
x=Us,y=Vt have 0<|x|,|y|<N for large N. Thus for any
chosen target multiplier a, we can force roughly k
prescribed prime occurrences across the two sides of
a signed congruence in deterministic polynomial time.
No assertion of independence of their eventual valuation
columns is implied, since cofactors could cancel some
of the prescribed factors.

The residual cofactors have absolute values at most
sqrt(N)+1, rather than N B^J. This is an unconditional
partial-divisibility construction on every large input.
It does not guarantee that those cofactors are B-smooth.

There is a counting limitation to simply shrinking the
cofactor boxes further. For fixed U,V and bounds S,T,
each unit pair (s,t) with 0<|s|<=S, 0<|t|<=T determines
only one unit multiplier a=Vt/(Us) modulo N. Thus at
most 4ST unit multipliers can be covered. The same
bound adds over a predetermined list of product pairs
U,V. The elementary inequality phi(N)>=N/(n+1) follows
from the Euler product by ordering the distinct prime
factors p_j>=j+1. If the list size and both cofactor
bounds are exp(O(b)), then almost all unit multipliers
are not covered by such a list. This does not exclude
a target-dependent choice of U,V, nor a procedure
tailored to multipliers that are powers of band primes.
It does explain why the usual fixed-box lattice argument
cannot supply both subexponential cofactors uniformly.

## 7. Weighted rank extraction permits arbitrary smooth cofactors

The narrow-band count used exactly L prime occurrences
to force a nonsingular relation matrix. That rigidity
is no longer required if we use a weighted maximum norm.

Fix a finite prime base F containing the narrow band, all
of whose primes are units modulo N, and a positive
integer X0>1. For each q in F choose a positive integer
T_q with
\[
 q^{T_q}>X_0^2
\]
by exact integer comparisons. Suppose there is a relation
for every q,
\[
 q^{T_q}x_q\equiv y_q\pmod N,\qquad
 1\le |x_q|,|y_q|\le X_0,
\]
whose signed x_q,y_q are units and have all their prime
factors in F. Define the integer row
\[
 A_{q,*}=T_q e_q+\nu(|x_q|)-\nu(|y_q|),
\]
where nu denotes the factor-base valuation vector.

**Theorem 4.** Every such square matrix A is nonsingular.
If Aw=0, put C=max_{p in F}|w_p|/log p. For an attaining
q, the row equation gives
\[
 T_q C\log q
 \le C\bigl(\log|x_q|+\log|y_q|\bigr)
 \le 2C\log X_0.
\]
The choice of T_q makes this impossible for C>0.
Thus C=0 and w=0. This proof allows both signs, repeated
prime powers, and varying factor counts.

Each row represents a product equal to a rational sign
modulo N. Doubling it removes the sign. The adjugate
identity therefore proves that E=2|det A| annihilates
every prime in F. Since the narrow band generates the
unit group by the established character estimate, E
annihilates the unit group, and the previous deterministic
square-chain factorization applies.

If F consists of all primes <=B^C for a fixed C>=1,
X0=N or N B^J, and the appropriate smooth signed
relations are supplied, all factor-base generation,
verification, matrix and exponent bit costs are
exp(O(b)). The initial gcd sieve up to that bound
is within the same budget. In particular the partial
relations (5) can be used directly whenever both
cofactors are smooth in such an enlarged base. There
is no need to complete exactly the original interval
pattern. To get this endpoint we still need a uniform
deterministic method finding the smooth cofactors for
each target; the current partial construction does
not establish that.

## 8. The exact remaining aggregation problem

Let Q be the family of all complete products of one
prime from each narrow band. For a fixed target unit a,
define
\[
 C(I,a)=
 \sum_{U,V\in Q}
 1_{\{U\bmod N\in I,\ V\equiv aU\pmod N\}}.
 \tag{6}
\]
This is the exact count of smooth witness pairs with
anchor in I (including multiplicities). Equivalently
it is the sum of the partial-pair count from Theorem 2
with both integer intervals equal to [ceil(7X/8),X]
and the prescribed products U,V now complete.
Indeed any multiple of U in this interval equals U,
and the same holds for V.

The earlier Fourier coverage theorem proves
C([0,N-1],a)>0 for every unit a. If positivity in (6)
can be decided uniformly in half-scale time for any
binary prefix interval I, then binary search constructs
a successful anchor in at most n such queries. An
exact count or a multiplicative approximation that
distinguishes zero from positive counts is sufficient;
there is no need to estimate a conditional probability
with an additive inverse-polynomial error. This would
settle the deterministic search using the independent-
anchor or weighted rank driver.

The arithmetic-specific oracle handles **every term** of
(6) in polynomial time. It does not yet aggregate the
sum in subexponential time. The products from the first
k bands alone number at least exp(n log 2-O(b)), by
the disjoint-band prime counts; all these products are
distinct. In a fixed full quotient interval [jN,jN+N-1]
inside [7X/8,X] (such j exist for large n), every one
of those prefix tuples already admits a multiple because
its modulus is less than N. Hence exhaustive one-sided
tuple expansion with pruning only by partial CRT
feasibility has exponentially many surviving prefixes.
This is a barrier to that simple enumeration, not a
lower bound for joint lattice algorithms or all possible
compressed summations of (6).

We also reviewed the applicable smooth-progression
literature. Pascadi's
[Smooth numbers in arithmetic progressions to large moduli](https://doi.org/10.1112/S0010437X2500747X)
gives an averaged exponent of distribution of 66/107
(up to an epsilon loss), not pointwise control of our
modulus N=X^(1-o(1)). Nor does an averaged estimate
over moduli imply a uniform bound at our adversarially
specified N. We do not import a nonexistent uniform
short-progression smoothness theorem.

The next concrete target is therefore compressed evaluation
or positivity of (6), possibly through exact lattice counts
with a deterministic multiplicative descent on U,V. A
different sufficient route is a target-dependent choice
of prescribed products in Theorem 3 giving smooth
cofactors and the weighted rank endpoint. Both use the
actual shared arithmetic progression structure; neither
has yet been solved. The uniform deterministic
L_N[1/2,O(1)] factoring claim remains open.

## 9. Exact finite verification

The standard-library script
[ap_lattice_count.py](../verification/research/ap_lattice_count.py)
implements the Euclidean floor sum, arbitrary-degree
canonical-atom counts, raw-prefix conditional counts,
partial witness counts with optional anchor intervals,
and deterministic signed-pair construction by binary
search on floor-sum counts.

It was executed locally with Python 3.13.5. Exact tested
source: Git blob
fda85b8630b10ec56e98e13ae6ac6232d56e0774,
SHA-256
c9a90f94fefb096c16f7463c409b5c36d05b86fbfd977f6305a647a6c92746c5.

Observed output:

    floor sums: 130680 brute-force checks, 1000 large-integer identity checks
    CRT anchor counts: 1852 brute-force cases and 44-atom unique-anchor fixture
    partial witness counts: 656 brute-force cases (signed ranges and prefix intervals)
    forced signed pairs: 974 checks, including 201-bit moduli

The large-integer identities independently check splitting
a floor sum into two consecutive intervals and the signed
complement identity. The 44-atom fixture has CRT moduli
larger than N, and also checks incompatible repeated
prime conditions. The partial-pair counts are compared
to independent direct enumeration on signed intervals.
The forced-pair tests check actual integer bounds and
congruences, not factorization or smooth cofactor coverage.
All random choices in the tests use fixed seeds. None of
these finite tests is a substitute for the written
complexity and existence proofs, and the Barvinok extension
is not separately implemented or benchmarked.

**No uniform deterministic half-scale factorer has been
proved in this continuation.**
