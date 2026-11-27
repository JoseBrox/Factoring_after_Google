# Prime-primary pooling, faithful common orders, and batch-affine separation

**Status (27 November 2026).** Proved three further unconditional
extraction theorems: complete prime-primary readout of the saturated
relation span; a common-order small-root endpoint at half scale; and
a batch-affine strengthening of adaptive exponent separation. Uniform
coverage of one of these sufficient endpoints remains open.
In particular, no subexponential upper bound on cumulative independent
residual directions is established. One-third work remains deferred.

This continues [residual-support budgets and 2-primary extraction](support_budget_and_two_saturation.md)
and [adaptive rank-or-residual separation](adaptive_rank_or_residual.md).

## 1. Complete primary readout, including odd primes

Use the power-free gcd-free basis of the preceding note. All bases
are units modulo odd N, and its embedding into true rational-prime
valuation coordinates is saturated in its rational span. Write
\[
 \varphi:\mathbb Z^s\longrightarrow(\mathbb Z/N\mathbb Z)^\times
\]
for modular evaluation of the integer exponent vectors.

Choose a rationally independent subset of the collected signed relation
rows, double them to remove signs, and let L be their integer row
lattice. Thus phi(L)=1. Put W=(Q L) intersect Z^s and for a prime ell
\[
 L_\ell=\{v\in\mathbb Z^s:\ell^j v\in L
                       \text{ for some }j\ge0\}.
\]

**Theorem 1.** phi(L_ell) is the entire ell-primary subgroup of phi(W).
The lattice L_ell can be computed deterministically in polynomial
bit time in the original integer relation description and log ell.

Proof. One inclusion is immediate from phi(L)=1. For the other,
given w in W whose image has ell-power order, choose d>0 with dw in L.
Write d=ell^j t with gcd(ell,t)=1. Then tw is in L_ell; powering
its image by an inverse of t modulo the order of phi(w) recovers
phi(w). This is the same elementary argument as for ell=2.

For the computation, while the current independent rows have a
nonzero linear dependence modulo ell, take coefficients
c_i in [0,ell-1], with one chosen coefficient c_j=1 (scale the
dependence by a nonzero field element). Replace row j by
\[
 \frac{1}{\ell}\sum_i c_i v_i.
\]
Its coordinates are integral. The new integer lattice contains the
old lattice and lies in its ell-saturation, because the replaced
old row equals ell times the new one minus the other terms.
The rational span is unchanged and every maximal minor is divided
by ell. A fixed original nonzero maximal minor D therefore bounds
the number of replacements by v_ell(D). Hadamard's bound makes
this polynomial in the input bit length. In a replacement the
entry bound grows by at most a factor r, where r is the number of
rows, since |c_i|<ell. All intermediate entry bit lengths stay
polynomial. Dependencies modulo ell are found by exact Gaussian
elimination over F_ell.

When the rows are independent modulo ell, their integer row lattice
is ell-saturated: if ell v is an integer combination of these rows,
reducing modulo ell forces every coefficient of the combination
to be divisible by ell, whence v already lies in the lattice.
Induction removes every ell-power. Together with the previous
inclusions this proves that the procedure computes exactly L_ell.
End proof.

Every nonzero maximal minor D of the original doubled independent
rows annihilates phi(W): solving in its pivot columns by Cramer
gives D w in L for every w in W. Thus the primary parts to be
processed need only have primes dividing one explicitly computed
D. No factorization of D is needed to process all ell<=Z: sieve
these primes and test divisibility. A proper gcd with N is already
a factor. At the conclusion, if the remaining cofactor of D after
removing all such primes is 1, every primary part has been processed.
Otherwise the unprocessed large-prime parts are not certified by
this readout.

### Complete primary-group extraction with a local-faithfulness certificate

Fix a prime ell coprime to N. Let z_1,...,z_t be the computed
generator images of L_ell, all killed by ell^h. The number h of
saturation steps is one such certified bound: at each replacement
the ell-th power of the new image is a product of previous images.

**Theorem 2.** In bit time polynomial in ell, h, log N and t,
one can either find a proper factor of N or give an exact cyclic
description of the generated ell-group H_ell, including its order.
In the no-factor case, reduction modulo **each** prime divisor
p of N is injective on H_ell. In particular
\[
 |H_\ell|\mid p-1\quad\text{for every prime }p\mid N.       \tag{1}
\]
The procedure finds a factor whenever H_ell contains a nonidentity
element whose reduction modulo some prime divisor of N is 1.

Proof. Obtain the ell-power order of each z_i by successive
ell-th powers, checking gcd(current-1,N) at every stage.
If a proper gcd occurs, stop. Otherwise select a generator g of
maximal order ell^k. The case k=0 is the trivial subgroup.
For k>0 let g_0=g^(ell^(k-1)). The gcd guard gives gcd(g_0-1,N)=1.
Since g_0 has order ell, its image has exact order ell at every
prime divisor p of N. Thus g itself has exact order ell^k at
each such p. The last statement uses only that ell is prime
and the order divides ell^k.

For another generator u, determine its discrete logarithm to base g
digit by digit. Initially v=u. At step j=0,...,k-1 maintain
v^(ell^(k-j))=1, and put
\[
 z=v^{\ell^{k-j-1}}.
\]
Then z^ell=1. Compute gcd(z-g_0^d,N) for each d=0,...,ell-1.
At every hidden prime p, all ell-th roots in F_p are powers of
the reduction of g_0: those powers are ell distinct roots of a
degree-ell polynomial. Hence some gcd in this list is >1.
If any is a proper gcd, return the factor. Otherwise at least
one is N, so z=g_0^d modulo N for a known d. Replace
v by v*g^(-d ell^j). Its next tested power is 1, maintaining
the invariant. After k steps v=1; the accumulated digits
express u as a power of g. This shows H_ell=<g> exactly.
The earlier order certificate proves injectivity at every p,
not just cyclicity. It also handles nonsquarefree N: the gcd
test operates modulo N itself and may return a proper divisor
even if it includes only part of a prime power. All loops
and modular exponent bit lengths obey the stated cost.

Conversely if no factor is returned, local injectivity implies
that no nonidentity element of H_ell is 1 at any hidden prime.
This proves the asserted completeness for this subgroup. End proof.

For ell<=Z=B^O(1), this is within the half-scale budget for a
half-scale pool. It strictly extends the earlier complete
2-primary extraction. It does not find all possible factors
using arbitrary information outside the represented primary
subgroups.

## 2. No mixed root can still be useful: a certified common order

Run the preceding readout for every prime ell<=Z. In the absence
of a factor, each certified primary group has order ell^k_ell,
and the groups commute (they are subgroups of the abelian unit
group). Their product is cyclic, of known order
\[
 C=\prod_{\ell\le Z}\ell^{k_\ell}.
\]
Its reduction at every prime divisor of N is injective, since
the primary components have relatively prime orders and each
is locally injective. Hence C divides p-1 for every prime
p|N. In particular gcd(C,N)=1: a prime divisor of N cannot
divide both C and p-1.

The value C is an exact order of the represented, processed
primary subgroup, not an arbitrary multiple of an order or
an upper bound from a saturation index. This distinction is
essential to what follows. If all prime divisors of the
maximal minor D were processed, the subgroup is the whole
phi(W); otherwise it is exactly the product of the processed
primary parts, without a claim about large primes.

## 3. A common-order half-scale factoring endpoint

Let n=bit_length(N) and
\[
 b=\left\lceil\sqrt{n\lceil\log_2(n+2)\rceil}\right\rceil,
 \qquad B=2^b.
\]
Fix a nonnegative constant D_0 (it suffices to use an integer
upper bound on a desired constant).

**Theorem 3.** Given an arbitrary composite N and an integer
C>1 certified to divide p-1 for every prime divisor p of N,
if
\[
 C\ge 2^{\lfloor n/4\rfloor-D_0 b},                        \tag{2}
\]
one can deterministically obtain a proper factor of N in
exp(O_{D_0}(b)) bit operations. No balanced-semiprime
assumption is needed.

This is a sufficient endpoint for the existing pooled search
even when no mixed primary root has occurred. It is an explicit
small-root application of LLL, rather than a new claim about
finding C. Here is a proof with a variable-slack parameter
schedule so that the half-scale exponent in (2) is charged
correctly.

### Linear small-root lemma with explicit slack

Let 1<=m<d be integers, X>=1 an integer, and f(z)=z+c monic
with c an integer in [0,N). Suppose an unknown divisor p|N
satisfies p>=2^h and f(z_0)=0 mod p with 0<=z_0<X.
Consider d integer polynomial coefficient rows, with the
coefficient of z^j scaled by X^j, from
\[
 N^{m-i} f(z)^i\quad(0\le i<m),\qquad
 z^j f(z)^m\quad(0\le j<d-m).
\]
Every row polynomial at z_0 is divisible by p^m. The same
is true for every integral combination. The coefficient
matrix is triangular by increasing degree, with determinant
\[
 \Delta=N^{m(m+1)/2}X^{d(d-1)/2}.
\]
Classical deterministic LLL with parameter 3/4 returns a
nonzero vector of Euclidean norm at most
2^((d-1)/4) Delta^(1/d). Recover its polynomial g by
undoing the column scales (exact division). By Cauchy-Schwarz
at |z_0|<X, its absolute value is at most sqrt(d) times that
norm. Consequently if
\[
 \sqrt d\,2^{(d-1)/4}\Delta^{1/d}<2^{hm},                  \tag{3}
\]
then g(z_0) is an integer multiple of p^m of absolute value
strictly smaller than p^m. Thus g(z_0)=0 over the integers.
The polynomial is nonzero, so all integer roots can be
obtained by factoring it over Q and taking its linear
factors. The standard polynomial-bit-cost LLL and rational
polynomial factorization theorems are from Lenstra, Lenstra
and Lovasz,
[Factoring polynomials with rational coefficients (1982)](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1982f/art.pdf).
The determinant, scaling, and Cauchy-Schwarz argument above
prove precisely the small-root statement we need; we do not
invoke a fixed-slack version of Coppersmith with unspecified
dependence on the slack.

All coefficient sizes of this construction are polynomial in
n,m,d,log X. Condition (3) can also be certified by the exact
integer comparison
\[
 d^{2d}2^{d(d-1)}\Delta^4<2^{4dhm}.                      \tag{4}
\]

### Bucket search and exact parameters

Let p be a smallest prime divisor of N, for the proof only.
Then C+1<=p<=sqrt(N). For sufficiently large n in (2),
guess its binary logarithm in a bucket [h,h+b), with h
a multiple of b, by enumerating h between n/8 and n/2.
The correct bucket is included: h>=n/4-(D_0+1)b-O(1)
eventually exceeds n/8. There are polynomially many buckets.
At that bucket p=1+C k with k>=1 and
\[
 \log_2 k<h+b-\log_2 C
 \le h-\frac n4+(D_0+1)b+1
 \le \frac{h^2}{n}+(D_0+1)b+1 .                         \tag{5}
\]
The last inequality is exactly (h-n/2)^2>=0.

Choose
\[
 m=\lceil n/b\rceil,\quad
 d=\lceil mn/h\rceil,\quad
 X=2^{\lfloor h^2/n\rfloor-4b}.
\]
For sufficiently large n the exponent of X is positive
uniformly over the guessed h. We have d>=2m and d<=8m+1.
Write beta=h/n. Since d>=m/beta and d-1<m/beta,
\[
 \begin{aligned}
 \log_2(\sqrt d\,2^{(d-1)/4}\Delta^{1/d})
 &\le \frac12\log_2 d+\frac{d-1}{4}
    +\frac{nm(m+1)}{2d}
    +\frac{d-1}{2}(h^2/n-4b)\\
 &\le mh+\frac h2-2b(d-1)+\frac{d-1}{4}
                       +\frac12\log_2 d\\
 &<mh .
 \end{aligned}
\]
Indeed h/2<=n/4, b(d-1)>=bm>=n, and d=O(n/b).
Thus (3) holds with explicit margin, uniformly. Every
lattice call and rational polynomial factorization has
polynomial bit cost in n.

For a guessed bucket, enumerate blocks of k values
[k_0,k_0+X-1], with k_0 nonnegative multiples of X
through floor((2^(h+b)-1)/C). For each block use
\[
 f(z)=z+c,\qquad c=(k_0+C^{-1})\bmod N,
\]
which is well-defined because gcd(C,N)=1. In the
correct block f(k-k_0)=0 mod p. Recover all integer
roots of the short polynomial and test
gcd(1+C(k_0+z),N) for roots in [0,X). The true root
returns p as a proper divisor. Every claimed output is
checked by integer gcd and divisibility.

By (5) the number of blocks at any h is at most
2^((D_0+5)b+O(1)). This proves exp(O_{D_0}(b)) bit time
for the complete splitting search. Finitely many bounded
lengths before these explicit inequalities hold can be
handled by trial division. This establishes Theorem 3
on arbitrary composite inputs, including those with
more than two prime factors. End proof.

No lower bound on C generated by the previous relation
algorithm has been proved. In particular there exist
structural cases with gcd(p-1,q-1) small, where a locally
faithful subgroup cannot have order near N^(1/4).
The theorem is an extra sufficient exit, not a replacement
for uniform factoring coverage.

### Monotonicity for a growing pool

If the verified relation list is enlarged, its true-prime
rational valuation span grows. Its saturated integral
span also grows. The power-free gcd-free coordinates
represent this integral span exactly by the earlier
saturation lemma, even if subsequent gcd refinement
splits an old composite basis element. Thus the image
group grows. At a fixed cutoff Z the actual processed
primary subgroup grows as well. Unless a split is found,
the certified C can only increase by divisibility. Each
strict increase multiplies C by at least 2. Since
C<=min_(p|N)(p-1)<sqrt(N) on composite inputs, there are
only O(n) strict increases before the common-order bound
(2) is reached or growth stops.

This is a second bounded *successful-progress* resource.
It suggests selecting raw rows by actual primary-image
growth in addition to pure-base rank gain. Growth of the
saturation index without growth of its modular image
must not be counted as such progress. We have not proved
a uniform bound on the number of attempts with neither
kind of gain.

## 4. Batch-affine adaptive exponent separation

Return to the adaptive setting of the prior note.
Let R_i, A_i denote the independent old residual
vectors and their integer base rows, i=1,...,r.
Let w be a rational annihilator of the old pure
base relation span, normalized to max |w_p|=1.
Choose q with w_q=1. Let A_0 be the base contribution
from any chosen fixed compact recycled residual product,
and use target q^T times its inverse residual image.

At a single chosen exponent T, collect a batch of at
most M new normalized rows. Each raw candidate may
come from any of the admissible shifted lattices,
and any local prescription subject to its height
guard. After normalization write
\[
 A'_j=A_0+T e_q+C_j,\qquad
 \|C_j\|_1\le J+2\ell_H,\qquad
 \|R'_j\|_1\le 2\ell_H .
\]
Here ell_H=ceil(log_2(H+1)); J is an upper bound on
the allowed dyadic shifts. The old residuals satisfy
the same residual-height bound.

Compute the old dual solution R_i lambda=A_i dot w
in its gcd-free basis and put Lambda=||lambda||_infty.
As proved in the prior note, it extends to a functional
on all true prime valuations with norm at most Lambda.
Thus it remains valid if new residuals split old
composite bases.

Set K=r+M, D=2 ell_H+1 and choose
\[
 T>\|A_0\|_1+
       K D^K(J+2\ell_H+2\ell_H\Lambda).                  \tag{6}
\]
For a positive-coefficient dependence the earlier smaller
bound already suffices; the new bound allows arbitrary
signed affine combinations. A deterministic upper bound
on M is known before choosing T: each shifted lattice
contributes at most 1+floor(18 H^2/N) primitive unit
pairs in the square, or a proper factor. For half-scale
H and at most half-scale many shifts, M has half-scale
size. Formula (6) charges exponent bit length
O(K log D) in addition to the previous dual and recycling
terms; binary modular powering with that integer is
within the half-scale budget. Over a prescribed half-scale
number of batches, the same multiplicative bit-height
accounting as in the adaptive note gives polynomial
bit lengths in the total number of retained rows and n.

**Theorem 4 (batch-affine rank gain).** If the new residuals
satisfy
\[
 0\in\operatorname{aff}_{\mathbb Q}
       \{R'_j+\operatorname{span}_{\mathbb Q}(R_i)\},
                                                               \tag{7}
\]
then a pure-base rank gain can be constructed by exact
rational linear algebra under (6). This does not require
any single new residual to lie in the old span, or any
nonnegative cancellation of the new residuals.

Proof. Condition (7) gives a rational combination of old
and new rows with total residual zero and new coefficients
summing to 1:
\[
 \sum_i \beta_i R_i+\sum_j\gamma_j R'_j=0,\qquad
 \sum_j\gamma_j=1.
\]
Encode the residual integers in a single gcd-free basis
for old and new. In that basis the l1 norm bounds hold
unchanged or improve: every basis integer is at least 2.
Solve the system with target column (0,1) using columns
(R_i,0),(R'_j,1). Choose an independent subset of at
most K columns spanning the target, and a corresponding
nonzero square minor. Every such column has Euclidean
length at most D; the target length is 1. By Cramer and
Hadamard there is a solution supported on this subset
with each absolute coefficient <=D^K (the denominator
is a nonzero integer). Hence sum_j |gamma_j|<=K D^K.
This solution is computable by exact Gaussian elimination
and uses no factorization of residuals.

The dual equation on old rows makes the base dot product
of the combination
\[
 \sum_i\beta_i A_i\cdot w+\sum_j\gamma_j A'_j\cdot w
 =T+A_0\cdot w+\sum_j\gamma_j(C_j\cdot w-R'_j\lambda).
\]
Its last sum is at least
-K D^K(J+2 ell_H+2 ell_H Lambda), so (6) makes it
strictly positive. Clearing denominators produces an
actual integer residual-cancelling relation; doubling
removes any sign. Since w annihilates the previous
pure base space, this is a strict new pure-rank gain.
End proof.

For the exact test, append a column of zeros to the
old residual matrix and ones to the new rows. Then
(7) holds if and only if this appended column increases
the rank by one. Row elimination with the last column
as the last pivot produces the desired rational
combination. If (7) fails, there is an exact dual
functional zero on the old residual span and equal
to 1 on every new residual. This is an affine-separation
certificate, stronger than merely finding that no
individual new row is in the old span.

The new test can be run alongside full pooled elimination.
Failure of (7) does not rule out other dependencies with
new coefficient sum zero that give actual rank gain for
the specific base rows. The full row-space test is still
needed to decide those. If no rank gain is obtained from
a nonempty batch, its residual rank increases by at least
one; all independent new residual rows can be retained.
This is a stronger adaptive sufficient condition, not
a uniform subexponential bound on the number of affine
separations or residual-support escapes.

### A concrete signed-only dependence

Modulo 77 with base {2}, T=14, H=9, consider the two
actual lattice rows
\[
 2^{21}\cdot4=-3,\qquad 2^{16}\cdot1=9\pmod {77}.
\]
They have base entries 23 and 16 and residuals 1/3
and 1/9. Each residual is nonzero, and no nonzero
nonnegative combination cancels them: their valuation
at 3 is strictly negative. The affine combination
(2,-1) cancels exactly and gives base exponent 30.
This modular power is 1; gcd(2^15-1,77)=7.
The example has no old pool, and illustrates why
the signed affine test is stronger than the
nonnegative cancellation criterion. Its particular
T does not need to satisfy the conservative
general separation bound because the resulting
base exponent is checked directly.

## 5. Exact finite tests and remaining failures

Three new research scripts were executed locally with Python
3.13.5. Their committed source blobs were checked byte-for-byte
against the tested files. No uniform coverage theorem is
inferred from these examples.

### Prime-primary saturation

[verification/research/primary_pool.py](../verification/research/primary_pool.py)

Git blob: e8bc23b5ca2431d7e2b159e0418a8e6038f771f7

SHA-256: a90e1a3b5e014be1a157bdd787aabecb03ef16747d20c71b0afc57b67ee6d5a0

Observed output:

    prime-primary subgroup comparisons: 7052
    prime-saturation maximal-minor comparisons: 300
    odd-primary-only raw fixture: 1333 H 148 row [(2, 32, 0, 54, -125)] bases [2, 3, 5] valuations [[33, 3, -3]] report [(2, 1, 1), (3, 1, None)] factor 43 tested 2
    cube root of sign 429 order-three component 87 gcd 43
    stalled pool prime-primary readout: 100160063 rank 25 report [(2, 25, 1), (3, 0, 0)] factor None
    stalled pool prime-primary readout: 1000036000099 rank 25 report [(2, 25, 1)] factor None

The 7,052 group tests compare with independent exhaustive group
enumeration on small moduli, including prime powers. The 300
saturation tests compare the computed indices against the gcd
of all maximal minors, and check original-row membership in the
new lattice by independent Cramer determinants. Enumerating
all minors is only a finite-test oracle. In the N=1333 example
the actual raw congruence gives
(2^11*3/5)^3=-1 modulo N, and the square of that cube root of
sign has order three, equals 87 modulo N, and yields gcd(86,N)=43.
The ordinary residual-free rank is zero and the 2-primary group
is the sign group. Trial division selected small composite
test inputs only; their factors were not passed to the relation
generator or extractor.

The last two cases reconstruct the earlier stalled 25-row
local-CRT adaptive pools. Even all prime-primary checks up to
1000 give no split and C=2. Thus this improved endpoint does
not solve those stalls.

### Common-congruence LLL endpoint

[verification/research/common_order_factor.py](../verification/research/common_order_factor.py)

Git blob: 840546f7b7a8e5536cc8db113e565bd1e31e023f

SHA-256: e7b87139b54a6ab2df173fd05b79f4c8c47cfff068b13763ca22af6882671317

Observed output:

    common-modulus LLL fixture: bits 77 C bits 25 factors 2 LLL calls 3 max dim 17 X 2048 proper factor 17314086913
    common-modulus LLL fixture: bits 77 C bits 25 factors 2 LLL calls 6 max dim 17 X 16384 proper factor 275364446209
    common-modulus LLL fixture: bits 92 C bits 25 factors 3 LLL calls 2 max dim 20 X 64 proper factor 469762049
    faithful-subgroup endpoint: report [(2, 25, 24)] C 16777216 factor 17314086913 LLL calls 3

These are constructed instances with a supplied common
congruence modulus, and the last subgroup is constructed with
known CRT factors solely to check the interface from faithful
primary readout to LLL recovery. They do not test construction
of a large C by the factoring relation pool. The finite
lattice parameters use the exact determinant guard (4), not
the deliberately asymptotic slack schedule. All returned
factors, row transformations, unimodularity and vector norm
inequalities were checked exactly.

In the available SymPy 1.14 PythonMPQ backend, math.floor
on a large rational can round through floating point.
The initial LLL run exposed this problem via an assertion.
The test script replaces that local LLL floor function
with exact numerator//denominator during the call and
restores the original afterwards. The certified
transformation and norm checks are independent of this
rounding workaround. The proof's algorithmic complexity
uses the published exact LLL and rational polynomial
factorization algorithms; it does not rely on timing
claims about the finite SymPy implementation.

### Batch-affine rank tests

[verification/research/batch_affine_rank.py](../verification/research/batch_affine_rank.py)

Git blob: 3d4cb1a265081ce05b550af8838799763953a5a9

SHA-256: 0669210f62e83a71afe33253deabc220030046fd67fde39f3af0c51370d67024

Observed output:

    batch affine rank comparisons: 250 positive cases 3
    signed-only batch: 77 raw [(7, 4, -3), (2, 1, 9)] residual [(1, 3), (1, 9)] coefficients ['2', '-1'] E 30 factor 7
    separated full batch: 47053 factor/rows/residual rank/T bits/gain support and bits (223, 0, 0, 10756, None)
    separated full batch: 100160063 factor/rows/residual rank/T bits/gain support and bits (None, 310, 122, 21014, None)
    separated full batch: 1000036000099 factor/rows/residual rank/T bits/gain support and bits (None, 407, 148, 35826, None)

In the full-batch tests the target exponent is actually selected
by (6) for an empty old pool, base {2}, and the explicit upper
bound on candidate rows. The test discards individually smooth
rows deliberately to evaluate the new affine condition. The
two larger fixtures have many residual dependencies, but none
with nonzero sum of the new coefficients. Additional full
pooled rank and primary checks on these very same retained
batches gave respectively pure ranks 0 and 0, with processed
common order C=2 at cutoff 100; the first had an early factor
by lattice gcd. These supplementary checks were run interactively
using the existing exact pool and primary routines rather than
included in the three script outputs. They are not a
counterexample to every exponent or batch selection rule.
They show that even a large number of residual dependencies
does not ensure an affine dependence with the required
nonzero target label, or growth of the primary image.

## 6. Next research boundary

The search now has three sufficient exits: a pure base
relation at a separating prime (or full pure rank), any
mixed primary subgroup, or a locally faithful certified
common order satisfying (2). A batch-affine dependence
is enough to force the first kind of progress by
separated exponents. Both the number of pure rank gains
and the number of strict common-order gains are bounded;
neither bounds the attempts that produce only independent
residual directions.

The next promising task is therefore to exploit the actual
affine-separation functional from failed batches to choose
subsequent targets, or to prove a uniform bound on rounds
with no gain in any of the three exits. The exact support
budget of the previous note still identifies a sufficient
condition, but its uniform smallness remains unproved.
Retain broad pooled searches in parallel with adaptive
selection, since the negative experiments demonstrate
that some individually reasonable rules stall.

**Uniform deterministic L_N[1/2,O(1)] factoring remains
open.** The results here are extraction theorems, exact
arithmetic improvements, and finite checks. No new
Lean milestone is claimed.
