# Depth-independent character rigidity and a general labelled rank driver

**Status (27 November 2026).** Proved a depth-independent improvement
of the labelled ratio coverage theorem and a general uniform randomized
rank-increase theorem using two short-ratio fibres. No uniform
deterministic hitter is proved, no new general factoring complexity
exponent is claimed, and no new Lean milestone is counted.

This continues [character-lift ratio coverage](character_lift_ratio_coverage.md).
The previous gap bound of order 1/M^2 restricted its analytic
coverage to small lifting depth. We remove that restriction by using
approximate character rigidity simultaneously over powers of the
proposed labels. A second application gives a rank driver with no
hypothesis about the two-adic valuations of the hidden primes.

The only analytic input below is the uniform prime-character estimate
already established in writing from the project's fixed Dirichlet/zeta
zero-free result; see [the prime-character proof](qrh_deterministic_progressions.md)
and [the half-scale moment estimates](positive_smooth_relation_coverage.md).

## 1. Approximate character rigidity

Let G be a finite abelian group and let P be a finite sample of
elements of G with its uniform probability measure. Suppose the
restrictions of every two distinct characters chi, psi of G satisfy
\[
 |\mathbb E_P\chi\overline\psi|\le\delta\le1/2 .
 \tag{1}
\]
Let f:P -> mu_D take values among the D-th roots of unity, with
D an arbitrary positive integer. No independence or randomness is
assumed in the choice of f. Put epsilon=1/128 and call a power
t in Z/DZ good if there exists a character chi of G such that
\[
 |\mathbb E_P f^t\overline\chi|\ge1-\epsilon .
\]
Use the L2 norm with the normalized sample measure.

**Lemma 1 (rigidity).** If more than half the powers are good,
there is a homomorphism
\[
 t\longmapsto\chi_t,\qquad
 \mathbb Z/D\mathbb Z\longrightarrow\widehat G,
\]
such that for each t a unit scalar alpha_t exists with
\[
 \|f^t-\alpha_t\chi_t\|_2\le1/4 .                 \tag{2}
\]
In particular chi_t=chi_1^t.

Proof. A good power admits an approximation of the stated form
with error sqrt(2 epsilon)=1/8: choose the unit scalar aligning
the correlation. If the good set has size greater than D/2,
every t is a difference of two good powers u,v, because the
good set intersects its translate by t. Multiplication of unit
functions is an isometry, and the triangle inequality gives
\[
 \|f^{u-v}-\alpha_u\overline{\alpha_v}
                         \chi_u\overline{\chi_v}\|_2\le1/4.
\]
Thus (2) is available for every t. Any two distinct characters,
even after multiplication by arbitrary unit scalars, have
L2 distance at least sqrt(2(1-delta))>=1 by (1).
The character in (2) is therefore unique. Comparing the
approximation of f^(t+s) with the product of those of f^t and
f^s shows that the characters chi_(t+s) and chi_t chi_s,
up to scalar phases, are at distance at most 3/4. They must
be equal. This proves the homomorphism assertion, including
the reduction of indices modulo D. End proof.

The argument is exact: complex notation expresses a proof
about the finite distribution, and no floating-point character
calculation or enumeration of D powers is required by the
eventual algorithm.

## 2. Remove the depth restriction in the Jacobi lifting theorem

Use the notation of the previous labelled coverage theorem:
M=2^e, D=2M, and f(p)=xi(p) with f(p)^M=eta(p), where eta is
the known Jacobi character. Assume that no character of G
has M-th power eta. For every narrow prime interval P_i,
the previously proved prime-character bound gives (1) with
delta=B^(-1/100).

If more than half the powers were good on P_i, Lemma 1
would give (2) for t=M. But f^M is exactly eta on P_i,
and distinct characters have distance at least one even
up to phase. Hence chi_M=eta and chi_1^M=eta, a contradiction.
It follows that for each interval at least half the powers t
have
\[
 \sup_\chi|\mathbb E_{P_i} f^t\chi|\le1-\epsilon.       \tag{3}
\]
(A strict inequality for a nongood power only strengthens this
weak bound.) Average the number of intervals satisfying (3)
over t. There is a **single** t for which at least half the
L intervals satisfy (3). It is not necessary to compute t.

For this common power define mu_t(a)=E[f(r)^t 1_(r=a)]
on G, using the same random disjoint-slot ratio r as the
previous note. Each slot obeys the previous single-interval
moment bound B^8, and the large-spectrum counting inequality
2/x^2. Those bounds use only unit modulus of the labels,
not their order or independence. Splitting at x_0=2sqrt(delta)
as in that proof shows
\[
 \sum_\chi |\mathbb E_{P_i} f^t\chi|^{2L}
 \le B^{-2}+6\theta_i^{2L-2},
\]
where theta_i=1-epsilon for a slot satisfying (3) and
theta_i=1 otherwise. To spell out the constant 6, the large
coefficients have cardinality at least-threshold x bounded
by 2/x^2. Integrating the tail from x_0 to theta gives
2 x_0^(2L-2)+(4L/(2L-2)) theta^(2L-2), at most
6 theta^(2L-2) for L>=2; the interval is empty if theta<x_0.
The small coefficients use the previous B^8 moment and
L-k=2000, yielding B^(-2).

Put D_* = B^(-2)+6(1-epsilon)^(2L-2). By Holder over the
slots, and at least L/2 good-gap slots for the common t,
\[
 \sum_\chi|\widehat\mu_t(\chi)|^2
 \le \sqrt{7D_*}.                                      \tag{4}
\]
The slots with inverse primes use conjugated coefficients,
so do not change the bound. This argument is uniform in e,
even when e grows with the input.

The unweighted distribution pi still satisfies
|G| sum_a |pi(a)-1/|G||^2 <= B^(-34).
Except for at most 4 |G| B^(-34) residues, pi(a)>=1/(2|G|).
At such a residue, if all representations have the same
original xi label, their powered labels f(r)^t are also
equal, so |mu_t(a)|=pi(a). Parseval in (4) bounds these
remaining bad residues by 4 |G| sqrt(7D_*).

**Theorem 2 (depth-free coverage).** Under the no-lift
hypothesis of the previous Jacobi theorem, the fraction of
residues with two differently labelled short-ratio
representations is at least
\[
 1-4B^{-34}-4\sqrt{7(B^{-2}
                         +6(1-1/128)^{2L-2})}.
\]
This tends to one uniformly in every positive integer e.
The extraction algorithm only uses the original labels
modulo 2M and never enumerates the powers t used in the proof.
Their bit length is e+1.

In particular the former requirement M^2=o(L) is removed.
For every e of at most polynomial bit-size in the algorithm's
resource bound, the exact linear-system and fibre operations
retain their cost. To get the previous direct Jacobi root
split, its separate necessary extraction hypothesis
e<v_2(N-1) is still imposed. We have not changed that
hypothesis or asserted that a Jacobi-negative faithful
common subgroup always splits N.

## 3. A two-translation theorem for arbitrary annihilator labels

The rigidity lemma also allows a general rank driver which
does not start with the Jacobi character or any character
lifting obstruction.

Use n=bit_length(N), b=ceil(sqrt(n ceil(log_2(n+2)))),
B=2^b, k=floor((n-2)/b), and now take
L=2 ceil((k+2000)/2) even, h=L/2. Work for sufficiently
large n and sieve through B first. Use the full dyadic prime
band P=(B/2,B] intersect the primes, of size m. Let
G=(Z/NZ)^*. The already proved uniform estimate is
\[
 |\mathbb E_{p\in P}\chi(p)|\le\delta=B^{-1/100}
            \qquad(\chi\ne1).                         \tag{5}
\]
Thus m>=B/(4 log B) eventually and (1) holds.

Choose h independent uniform primes for the numerator
and h for the denominator, all from P. Let r be their
positive rational ratio. Repetitions and common factors
are allowed; reduction to lowest terms preserves both
its residue and its formal multiplicative label. Its
primitive coordinates are <=H=B^h, with H<N for large
n and H^2=B^L<=N B^2001.

Set D=2^(n+1). Assign an arbitrary integer label z_p
modulo D to every p in P, requiring at least one odd
coordinate. Choose such a prime q0, and put
f(p)=exp(2 pi i z_p/D).
Extend f multiplicatively to positive rational numbers
supported on P.

For a unit residue a define the combined labelled fibre:
\[
 {\cal F}(a)=
 \{r:r\bmod N=a\}
 \ \cup\
 \{q_0 r:r\bmod N=a/q_0\},                             \tag{6}
\]
where the r's in both terms are ratios from the balanced
word family just described. A word with a common factor
is still valid; the second term need not itself fit the
original coordinate bounds. We enumerate its underlying
r, not its translated numerator.

We prove that almost every a has two members of (6)
with different f labels, uniformly in every assignment
z and every odd-labelled q0.

### Fourier estimates for balanced ratios

For any t in Z/DZ set
\[
 \lambda_{\chi,t}=\mathbb E_{p\in P} f(p)^t\chi(p),\quad
 \mu_t(a)=\mathbb E[f(r)^t 1_{\{r=a\bmod N\}}].
\]
The balance of the slots gives the exact identity
\[
 \widehat\mu_t(\chi)=|\lambda_{\chi,t}|^{L}.
\]
Indeed the h inverse slots each contribute the complex
conjugate of the corresponding numerator coefficient.
For t=0 this is the ordinary ratio distribution pi.

The moment bound at k is
\[
 \sum_\chi|\lambda_{\chi,t}|^{2k}
 \le |G|\,k!/m^k \le B^4 .                             \tag{7}
\]
Character orthogonality compares two integer products of
k primes each, less than N; equality modulo N is equality
of integers and hence of their multisets. Label phases
then cancel exactly. This bound is independent of t and
D. The last numerical bound is the elementary estimate
from positive smooth-relation coverage, using
n-kb<b+2 and k log_2 n=O(b) with the chosen constants.

From (5), (7), and L-k>=2000 we obtain
\[
 \sum_{\chi\ne1}|\widehat\pi(\chi)|^2\le B^{-36}.
                                                               \tag{8}
\]
For any set of characters on which |lambda_(chi,t)|
<=theta<=1, the same almost-orthogonality counting argument
as in Section 2 and (7) give
\[
 \sum_{\chi\ {\rm in\ that\ set}}
             |\lambda_{\chi,t}|^{2L}
 \le B^{-6}+6\theta^{2L-2}.                            \tag{9}
\]
Here x_0^2<=B^(-1/200), and B^4 (x_0^2)^2000<=B^(-6).
No restriction on the number of characters in that set
is needed. Define
\[
 \Delta=B^{-6}+6(1-\epsilon)^{2L-2}.
\]

### Case A: a nongood power exists

If some power t has no character approximation at the
threshold 1-epsilon, all its coefficients are bounded
by 1-epsilon. Equation (9) bounds the total Fourier
square sum of mu_t by Delta. As before, outside the
4 |G| B^(-36) low-mass fibres of pi, a monochromatic
original f fibre has |mu_t(a)|>=1/(2|G|).
There are at most another 4 |G| Delta such residues.
Therefore the first part of (6) already gives the
desired label disagreement for almost every a.

### Case B: all powers are good

Lemma 1 provides a homomorphism chi_t. Its image has
order dividing D and the exponent of G. Since D/2>|G|,
and D is a power of two, chi_(D/2)=1. Consequently the
parity function u=f^(D/2), which takes values +/-1,
is within L2 distance 1/4 of a constant phase.
In particular |E_P u|>=31/32, so there is a sign sigma
with E_P |u-sigma|<=1/32.
For every nonprincipal chi,
\[
 |\mathbb E_P u\chi|\le \delta+1/32\le1-\epsilon
\]
eventually. Thus (9) for t=D/2 bounds all nonprincipal
Fourier squares of mu_t by Delta. Its principal
coefficient beta=(E_P u)^L is nonnegative because
L is even. Parseval gives
\[
 |G|\sum_a|\mu_t(a)-\beta/|G||^2\le\Delta.            \tag{10}
\]

Except on at most 8 |G| B^(-36) residues, both pi(a)
and pi(a/q0) are >=1/(2|G|), by (8) and translation.
If the combined fibre (6) has no disagreement in
the original labels, every member has the same
powered label as well. Since u(q0)=-1, the powered
labels of the underlying ratios at a and a/q0 must
be opposite constant signs. Hence at least one of
mu_t(a),mu_t(a/q0) is <=-1/(2|G|). Equation (10)
bounds the number of such negative values by
4 |G| Delta, using beta>=0. Counting the two
translations gives at most 8 |G| Delta further
bad residues.

**Theorem 3 (arbitrary-label fibre/translate coverage).**
For every assignment with an odd coordinate, the
proportion of unit residues where (6) has unequal
labels is at least
\[
 1-8B^{-36}-8\Delta = 1-o(1).
\]
This is uniform in the assignment, the selected odd
coordinate and the modulus N under (5). It has no
hypothesis about the Jacobi character, its lift,
or the local two-adic valuations of the prime
divisors of N. The proof does not need to decide
which of the two analytic cases holds.

## 4. Exact rank increase and its cost

Keep a matrix A of verified integer exponent relations
on P with product 1 modulo N. If its rational rank is
less than m, compute any nonzero rational annihilator
and clear denominators. Divide the resulting integer
vector by the gcd of its coordinates to obtain w with
gcd(w_p)=1 and A w=0. Some coordinate is odd. Set
z_p=w_p mod D and choose an odd q0 as in Theorem 3.

For a candidate a, enumerate the primitive unit
congruence-lattice points of height at most H at
multipliers a and a/q0. A proper coordinate gcd
immediately returns a factor. Filter positive pairs by
trial division through P, keeping all P-smooth ratios
in the boxes. This includes the whole balanced word
family after rational cancellation. Compute their
integer label modulo D. In the second list add the
exponent coordinate of q0, equivalently add its label.
Compare against one representative from the combined
list. A disagreement gives a relation v of residue 1
with v dot w nonzero modulo D. In particular v dot w
is a nonzero integer, so v strictly increases the
ordinary rational rank of A.

All label comparisons are exact integer calculations
of O(n) bits modulo D. The determinant-scale enumeration
has cost polynomial(n)*(1+H^2/N), including skew
lattices, and both trial division and relation matrix
operations have polynomial bit cost in the explicit
list sizes. Thus one query has exp(O(b)) bit cost.
The theorem proves that for each chosen annihilator,
an independent uniform unit query succeeds with
probability 1-o(1), conditional on the entire previous
history. At most m successful queries are needed.
The full-rank determinant annihilates every prime in P
by the adjugate identity, and the character bound
(5) proves that P generates G. The previous order
chain then factors a composite with two distinct prime
factors, with primes and perfect powers preprocessed.
As usual deterministic recursion gives complete
factorization. This is a uniform randomized half-scale
algorithm with a bounded rank resource, using only two
short-ratio fibres and a one-prime shift.

**This is not a stronger randomized complexity exponent or
an improved nonuniform advice bound.** The previous
common-anchor theorem already gave a uniform randomized
half-scale algorithm, a stronger numerical hole bound,
and polynomial advice. The new benefits are depth-independent
label coverage, freedom from the restricted Jacobi
input class, and a different exact rank-increase predicate.

In particular a deterministic uniform selector for a
label-disagreeing a in (6) for arbitrary primitive
annihilator labels suffices for deterministic half-scale
factoring. No such selector has been proved. The proof
of Theorem 3 uses a density estimate, not a pointwise
guarantee at arbitrary prescribed target powers. It does
not permit replacing uniform residues by a predetermined
half-scale list without an additional hitting argument.
We have not established a new uniform residual-rank
bound in the separate adaptive pooling route either.

## 5. Exact finite verification

The standard-library test
[depth_free_labels.py](../verification/research/depth_free_labels.py)
was run locally with Python 3.13.5. The tested script
and both local dependencies were checked against the
committed Git blobs. The new script's Git blob is
48471087777030f01e8a516b935a710dc9037a26 and its SHA-256
is 1cba52e0580db68e631a74f840a2c2a9d92643fbd544bdbd468f43018369d180.

Observed output:

    fibre/translate query comparisons: 177 factor exits 602 internal disagreements 126 translated disagreements 28
    primitive annihilator checks: 300
    rank driver: 47053 v2(N-1) 2 base 15 H 650 rank 15 queries 39 ignored gcd exits 3 internal 12 translated 3 exponent bits 16 factor 223
    rank driver: 11009 v2(N-1) 8 base 14 H 312 rank 14 queries 24 ignored gcd exits 5 internal 14 translated 0 exponent bits 14 factor 109
    rank driver: 100160063 v2(N-1) 1 base 19 H 60048 rank 19 queries 872 ignored gcd exits 10 internal 12 translated 7 exponent bits 30 factor 10007
    rank driver: 3233 v2(N-1) 5 base 11 H 300 rank 11 queries 61 ignored gcd exits 49 internal 11 translated 0 exponent bits 12 factor 61
    rank driver: 1333 v2(N-1) 2 base 10 H 148 rank 10 queries 40 ignored gcd exits 30 internal 10 translated 0 exponent bits 11 factor 31

The query comparisons use an independent enumeration of
primitive positive ratios on small rectangles, trial
division, and exact labels. They compare whether the
combined fibre has a disagreement; early gcd exits
are verified separately. The annihilator tests check
the exact integer kernel equations and primitivity.

Each actual relation in the rank experiments has
verified modular product one and nonzero dot product
with the current annihilator, with independent exact
rank checks. The final exponent is computed by an
exact Bareiss determinant, verified at every base,
and checked by the gcd scan. The harness intentionally
ignores early coordinate factors to exercise the
rank driver, and uses a fixed seed for random residue
queries. It permits all positive base-smooth ratios
with its small illustrative heights, not the actual
asymptotic balanced word distribution. It does not use
the factorization of the inputs to construct relations.
These are exact tests of the arithmetic algorithm;
the uniform analytic statements are the proofs above,
not conclusions extrapolated from these small trials.

Dependency blobs: primitive_ratio_lattice.py
446b6eb7e1c46388db7109d4f73b61665c071e59 and
pooled_shift_relations.py 2c232588e5f6304a96c456e35245171be6a2f21a.

## 6. Remaining target

The depth restriction was a real limitation of the prior
Fourier argument and is now removed. The general
annihilator formulation turns every successful exact
label query into a rank increase with no need for a
second residual-support budget or an additional test of
a reconstructed root's nontriviality.

The outstanding deterministic problem is still selecting
a label-disagreeing residue uniformly, without enumerating
the full residue domain. The two-translation formulation
only requires a small prime shift, and all constraints
are explicit integer labels. Future work should exploit
the arithmetic structure of these fibres rather than
infer a hitting theorem from their density. Retain the
other exact exits, including primary saturation and
common-order recovery, in parallel.

**Uniform deterministic L_N[1/2,O(1)] factoring remains
open.** The one-third investigation remains deferred.
