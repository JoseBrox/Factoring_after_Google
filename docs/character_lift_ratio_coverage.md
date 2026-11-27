# Jacobi character-lift obstruction and uniform labelled ratio coverage

**Status (27 November 2026): proved an exact character-lift
extraction theorem and a uniform labelled short-ratio coverage
theorem for a specified class of inputs.** The analytic theorem
uses the project's already verified Dirichlet/zeta zero-free
strip and its written uniform prime-character estimate.
The resulting randomized progress theorem does not require
integer residual-span membership or known modular roots of
the individual short ratios. It does **not** give uniform
deterministic selection or a new general factoring exponent.
The one-third program remains deferred.

This continues [squareclass pooling](squareclass_ratio_pool.md)
and [primitive short-ratio aggregation](primitive_ratio_lattice_aggregation.md).
A useful distinction is that the old parity search required
known square roots of individual residues. The new search
instead maintains a hypothetical character lift on a fixed
small factor base, and uses **two differently labelled
representations of an arbitrary common residue**.

## 1. An exact finite character-lifting system

Let N be odd, let G=(Z/NZ)^*, and let eta denote the Jacobi
character (./N) on G. Fix e>=1 and M=2^e. Take a prime base
F of m primes coprime to N. Put epsilon_p=0 or 1 according
as eta(p)=1 or -1.

A candidate lift is the multiplicative function xi on
positive rational F-smooth numbers defined by
\[
 \xi(p)=\exp\left(\frac{2\pi i}{2M}
                     (\epsilon_p+2z_p)\right),
 \qquad z_p\in\mathbb Z/M\mathbb Z .
\]
Thus xi^M=eta on these rational numbers; no claim is made
that xi descends to a character of G. All operations with
xi use integer labels modulo 2M, not floating-point values.

For any collected actual exponent relation v in Z^m with
\(\prod_p p^{v_p}=1\bmod N\), the integer epsilon dot v
is even. Requiring xi to be one on this relation is exactly
\[
 v\cdot z=-\frac{\epsilon\cdot v}{2}\pmod M.             \tag{1}
\]
Keep a system of these constraints. Signed relations can be
doubled first; the short-ratio driver below produces actual
relations with residue 1.

**Theorem 1.** If (1) becomes inconsistent, one can compute
in polynomial bit time in the relation description, e and
log N a unit u with
\[
 u^{2^e}=1\bmod N,\qquad \eta(u)=-1.                     \tag{2}
\]
If e<v_2(N-1), deterministic successive squaring and gcds
give a proper factor of N.

Proof. Let A be the matrix of original rows and
h=-A epsilon/2 its integral right-hand side.
An inconsistent system A z=h modulo M has a dual certificate
c with c^T A=0 mod M but c^T h!=0 mod M.
The following explicit elimination constructs either a
solution or this certificate without enumerating M.

In the remaining rows and unused columns choose a nonzero
entry of smallest 2-adic valuation. After swapping rows
and scaling by an odd unit modulo M, its value is a power
d of two. Every remaining entry, including all entries in
the chosen pivot row, is divisible by d; earlier pivot
columns are zero in that row. If the transformed right
side is not divisible by d, multiply this transformed row
by M/d. Tracking its row operations gives the asserted
dual certificate. Otherwise subtract multiples of the
pivot row to eliminate its column below. A zero row with
nonzero right side also gives a certificate. If no
obstruction occurs, choose unused variables zero and solve
backwards, dividing by the pivot powers of two. At every
pivot all remaining coefficients and the right side are
divisible by d, so the backward congruence is solvable.
This proves both alternatives. Row arithmetic uses residues
modulo M, so the cost is polynomial in matrix dimensions
and log M; track the row operation matrix modulo M to
recover c.

Take representatives for c in [0,M-1] and put w=c^T A
over the integers. Every entry of w is divisible by M.
Moreover -epsilon dot w/2 is nonzero modulo M. Therefore
epsilon dot (w/M) is odd (since M is even). With
\[
 u=\prod_p p^{w_p/M}\bmod N
\]
the genuine modular relation for w proves (2).
Negative exponents are computed by unit inverses.
All exponent bit lengths are polynomial in the input.

For completeness, suppose the square chain fails to split.
The exact local orders of u at the distinct prime divisors
of N must then all have the same order 2^j, with
1<=j<=e (the negative Jacobi symbol excludes u=1).
By cyclicity modulo an odd prime p, the Legendre sign of
u at p is negative exactly when v_2(p-1)=j.
Write N=prod p_i^{a_i}. The negative Jacobi symbol says
that the sum of the a_i over those primes is odd.
Every other p_i is 1 modulo 2^{j+1}, while these primes
are 1+2^j modulo 2^{j+1}. Multiplying gives
N=1+2^j modulo 2^{j+1}. This contradicts j<=e<v_2(N-1).
End proof.

If the restriction e<v_2(N-1) is not met, (2) is still a
verified torsion certificate but need not split. In that
case use the existing primary-group readout; a locally
faithful cyclic group may instead give a common divisor of
all p-1. In particular this theorem does not claim that
every negative-Jacobi 2-power root is a mixed root.

### Progress measure

For a solvable system the solutions are a coset of a subgroup
of (Z/MZ)^m. Each appended relation that violates the current
solution either makes the system inconsistent or cuts the
number of possible solutions by a factor at least two.
There are at most em strict nonempty cuts, followed by one
inconsistent step if such cuts continue. This is an exact
bounded progress resource. It concerns **all candidate
character lifts**, not the ordinary rational rank, and uses
only the fixed small prime base. There are no residual
columns in (1).

## 2. Which inputs have the required character obstruction?

Suppose there is no character chi on G satisfying
\[
 \chi^M=\eta.                                           \tag{3}
\]
A sufficient condition is that N have a prime divisor p
of odd multiplicity with v_2(p-1)<=e. Indeed CRT separates
the p-primary prime-power factor. Its unit group has
a cyclic 2-primary subgroup of order 2^{v_2(p-1)}, on
whose generator eta is negative, whereas every M-th
power of a character is trivial there. This uses the
ordinary cyclicity theorem for units of odd prime powers,
or equivalently the cyclicity of F_p^* and the fact that
the kernel of reduction has odd order.

For a squarefree semiprime N=pq with
\[
 v_2(p-1)=v_2(q-1)=e ,
\]
one has v_2(N-1)>e, and (3) is impossible. This includes
the case p=q=3 modulo 4 for distinct p,q and e=1.
More generally the theorem applies when the specified
odd-multiplicity obstruction occurs and e<v_2(N-1).
The algorithm can test several e without knowing the
factorization. We do not claim the obstruction at an
arbitrary tested e. In particular the common unequal
two-adic-valuation case is not covered by this sufficient
condition with e<v_2(N-1).

The next analytic theorem is stated with (3) impossible.
The finite linear-system theorem did not require it.

## 3. Uniform label disagreement in short-ratio fibres

Use the earlier half-scale parameters, with binary lengths:
\[
 n=\operatorname{len}_2 N,\quad
 b=\lceil\sqrt{n\lceil\log_2(n+2)\rceil}\rceil,\quad
 B=2^b,\quad k=\lfloor(n-2)/b\rfloor,\quad L=k+2000 .
\]
Work at sufficiently large n and first sieve to B, returning
a proper factor if one is found. Divide
\((B(1-1/(8L)),B]\) into L disjoint equal-width intervals.
Let P_i be their respective prime sets and m_i their sizes.
All band primes are units.

The [narrow-band prime-character estimate](narrow_band_streaming_atoms.md)
gives uniformly in the intervals
\[
 m_i\gg \frac{B}{L^2\log B},\qquad
 \left|\mathbb E_{p\in P_i}\chi(p)\right|\le
       \delta_B=B^{-1/100}\quad(\chi\ne1).              \tag{4}
\]
This is the previously written consequence of the verified
fixed Dirichlet strip, not a new assumption about distribution
of smooth values. We only use (4), ordinary finite Fourier
analysis and exact small-product collisions.

Split the slots into two sides of lengths floor(L/2) and
ceil(L/2). Choose one prime independently from each slot
and form a positive rational ratio r of the two products.
Their prime supports are disjoint, so r is primitive.
Each coordinate is <=sqrt(N) B^O(1), and the product of
their upper bounds is B^L<=N B^2000. Use the uniform
distribution on the tuples, and let
\[
 \pi(a)=\Pr[r=a\bmod N],\qquad
 \mu(a)=\mathbb E[\xi(r)1_{\{r=a\bmod N\}}].
\]
Here xi is **any** choice of candidate labels satisfying
xi(p)^M=eta(p). No distribution, independence, or
computability assumption on those labels is needed for
the following analytic estimates. The search chooses
them by (1).

The ordinary unweighted short-ratio theorem already gives
\[
 |G|\sum_a|\pi(a)-|G|^{-1}|^2\le B^{-34}.               \tag{5}
\]
We now control mu, uniformly over all label assignments.

### Twisted prime coefficients have a gap

For each interval define
\[
 \lambda_{i,\chi}=\mathbb E_{p\in P_i}\xi(p)\chi(p).
\]
Since (3) is impossible, the character eta chi^M is
nonprincipal for every chi, including the principal one.
(The inverse of a character whose M-th power equals eta
has the same M-th power.) Thus (4) gives
\[
 \left|\mathbb E_{p\in P_i}(\xi(p)\chi(p))^M\right|
 \le\delta_B .
\]
For a unit complex random variable Z of mean m, choose a
unit scalar z_0 in the direction of m (arbitrary if m=0).
Then E|Z-z_0|^2=2(1-|m|).
The telescoping identity for Z^M-z_0^M gives
\[
 1-\delta_B\le \mathbb E|Z^M-z_0^M|
       \le M\sqrt{2(1-|m|)}.
\]
Consequently, for all sufficiently large n,
\[
 |\lambda_{i,\chi}|\le1-\gamma,\qquad
 \gamma=\frac{1}{8M^2}.                                \tag{6}
\]
For e=1 a sharper fixed gap follows from the real-part
variance argument, but (6) suffices.

### Counting the large spectrum

The functions xi(p)chi(p) on P_i for distinct chi have
absolute inner product <=delta_B by (4), since |xi(p)|=1.
If R of their means have absolute value >=x, align them
by unit scalars and apply Cauchy-Schwarz against the
constant function. This yields
\[
 R^2x^2\le R+\delta_B R(R-1).
\]
Thus for x^2>=2delta_B their number is <=2/x^2.
This bound is uniform in i and xi and has no |G| factor.

### Exact high moment in each individual interval

Use k independent primes from a **single** interval,
allowing repetitions. Character orthogonality shows
\[
 \sum_\chi|\lambda_{i,\chi}|^{2k}
     \le |G|\,k!/m_i^k\le B^8                          \tag{7}
\]
eventually. Indeed the products of k primes are smaller
than N, so a congruence of two such products is actual
equality of their prime multisets. The xi phases in the
two products cancel exactly when the multisets agree.
Each tuple has at most k! permutations. For the last
bound, n-kb<b+2, k<=n/b, and the binary logarithm of the
loss in m_i and k! is at most
k(2 log_2 L+log_2 log B+log_2 k+O(1)).
The relation b^2>=n log_2(n+2) gives the stated conservative
B^8 bound for large n. This is a different use of the
small-product moment from the original disjoint-slot
identity.

Let x_0=2 sqrt(delta_B). For sufficiently large n,
x_0^2<=B^(-1/200). From (7),
\[
 \sum_{|\lambda_{i,\chi}|<x_0}|\lambda_{i,\chi}|^{2L}
 \le B^8 (x_0^2)^{2000}\le B^{-2}.
\]
For the remaining coefficients, integrate the tail count
2/x^2 from x_0 to 1-gamma. When the interval is empty
the sum is zero; otherwise it is bounded by
\[
 2x_0^{2L-2}
  +\frac{4L}{2L-2}(1-\gamma)^{2L-2}
 \le 6(1-\gamma)^{2L-2}\quad (L\ge2).
\]
Thus every interval has the same upper bound
\[
 \sum_\chi|\lambda_{i,\chi}|^{2L}
 \le \Delta_\xi:= B^{-2}+6(1-\gamma)^{2L-2}.           \tag{8}
\]
The Fourier coefficients of mu are products of these
lambda's or their conjugates, according to the side.
Hölder's inequality over the L slots gives
\[
 \sum_\chi|\widehat\mu(\chi)|^2\le
 \prod_{i=1}^L\left(\sum_\chi
             |\lambda_{i,\chi}|^{2L}\right)^{1/L}
 \le\Delta_\xi.                                      \tag{9}
\]

**Theorem 2 (uniform label-disagreement coverage).**
If no character lift (3) exists, the proportion of unit
residues a for which the specified disjoint short-ratio
family has two representations with **different xi
labels** is at least
\[
 1-4 B^{-34}-4\Delta_\xi.                             \tag{10}
\]
In particular this proportion is 1-o(1) for fixed e, or
more generally when \(M^2=o(L)\). The estimate is uniform
over all choices of the candidate lift, including
adaptively chosen labels.

Proof. By (5), at most 4 |G| B^-34 residues have
pi(a)<1/(2|G|). At every other residue with only one
xi label, all terms defining mu have the same complex
phase, hence |mu(a)|=pi(a)>=1/(2|G|). Parseval in (9)
bounds the number of these residues by 4 |G| Delta_xi.
This proves (10), including empty fibres in the first
exceptional set. Finally
(1-gamma)^{2L-2}<=exp(-(L-1)/(4 M^2)).
End proof.

The use of complex-valued labels is essential to the
statement for larger e. We do not assert that every
possible one of the 2M labels occurs at each good residue.
Two distinct labels suffice. Nor do we assert pointwise
coverage of any prescribed residue; (10) is a density
bound.

## 4. Exact oracle and adaptive progress

For any unit a, enumerate all primitive unit pairs in
the determinant-scale rectangle with the two side
bounds, using [the exact lattice enumeration theorem](primitive_ratio_lattice_aggregation.md).
This either returns a proper factor or takes
\[
 \operatorname{poly}(n)(1+B^L/N)
\]
bit time. Filter the pairs by positivity and the
specified disjoint-band factorization, using trial
division by the explicit prime band. For each accepted
pair its label is computed modulo 2M using the known
candidate labels. This gives an exact half-scale decision
of whether the fibre contains two different labels and
recovers such representations when it does. One may
also allow all F-smooth positive primitive pairs in a
slightly larger rectangle: the disjoint-band family is
then a sufficient subfamily for the coverage proof.

Suppose the oracle gives \(r_1,r_2\) at the same residue
and with different labels. The exponent vector of
\(r_1/r_2\) is an actual modular relation with residue 1,
and its label under xi is not 1. It therefore violates
the current solution of (1). Append it. This reduces
the solution set of (1), or obtains (2) immediately.
No root of either individual residue is required.

For an input satisfying the obstruction and e<v_2(N-1),
choose a uniformly random unit target a at each attempt.
The success probability is 1-o(1), **conditional on
every earlier history**, by (10). One can instead sample
a uniform n-bit integer, reduce modulo N, and return
any proper gcd; reject zero. Its unit residue multiplicities
are at most two, and after the initial sieve the nonunit
fraction is at most O(n/B). This gives the same uniform
high-probability bound. Uniform sampling can use exact
rejection or fixed extra random bits; no character evaluation
at the hidden primes is performed.

At most em+1 successful constraint additions suffice
before inconsistency, where m=|F|<=B (include the union of
all bands). For fixed e, or e with M^2=o(L), this yields a
rigorous randomized half-scale **rank-progress and
extraction mechanism** on the stated class of inputs,
without unknown residual columns or a smoothness
assumption beyond the proved prime-character estimate.
Expected cost is exp(O(b)); at small bounded input lengths
one may dovetail trial division as in the previous notes.
This is not a new best randomized factoring algorithm,
and the earlier common-anchor algorithm already gives
a uniform randomized half-scale bound without this
restricted input condition.

The new deterministic target is nevertheless different:
find a residue where a **given explicit lift assignment
fails to be consistent on the short-ratio fibre**. Every
successful query gives provable progress in a bounded
resource (the number of solutions of (1)). There is no
second uncontrolled residual-rank budget and no need
to prove that a squareclass dependency has a nontrivial
root afterwards. When the constraints are inconsistent,
the dual certificate already has the required Jacobi
sign.

A uniform deterministic way of selecting this residue
in half-scale time is not established. In particular,
(10) cannot be converted into a claim about one fixed
list of prime powers or dyadic shifts just by counting
its density. The error contribution in (8) for the
largest twisted coefficients is exp(-Omega(L/M^2)),
not exp(-Omega(n)); even making it very small does
not imply that a half-scale-size predetermined list
meets the good set. This is precisely the unresolved
arithmetic-specific selection problem, not a
polynomial-space or fresh-randomness claim.

## 5. Exact finite tests

The standard-library script
[character_lift_pool.py](../verification/research/character_lift_pool.py)
was executed locally. Tested and committed source match
byte-for-byte:

Git blob: 5b49764c90466545c66bec78942e8441aabb8ce2

SHA-256:
8699d46141cba332eb4571c57f17da389286fd90a85527deb6ccdc840206d416

Observed output:

    2-power system: 2000 brute-force comparisons, 1085 dual certificates; 100 large-modulus solvable checks
    Jacobi-labelled root split: 380 exhaustive cases
    label-lift split: 47053 depth 1 base 15 H 650 relations 13 queries 110 ignored gcd exits 13 root 7806 factor 223
    label-lift split: 11009 depth 2 base 14 H 312 relations 14 queries 36 ignored gcd exits 5 root 10606 factor 101
    label-lift split: 31921 depth 3 base 19 H 540 relations 19 queries 42 ignored gcd exits 2 root 4796 factor 137
    label-lift split: 27233 depth 4 base 19 H 495 relations 18 queries 44 ignored gcd exits 7 root 13977 factor 241

The small systems are compared to brute-force enumeration
over Z/2^e, including explicit dual witnesses for failures.
The additional 100 solvable systems have moduli of 50--249
power-of-two bits, and test that the algorithm does not
enumerate the modulus. The 380 root checks exhaust the
stated small-input Jacobi/order conditions. The four
factoring fixtures use the actual primitive lattice
enumerator and trial division of short coordinates with
a small factor base; the input factors are not used by
the algorithm. The finite harness intentionally ignores
reported proper coordinate gcds to exercise the new
labelled extraction instead, and uses seeded random
target choices. A production algorithm would return the
coordinate factor immediately. Every modular relation,
inconsistency witness, root order upper bound, Jacobi
sign, and final divisor is verified exactly.

These finite runs use all positive base-smooth primitive
pairs in their small rectangles, not the asymptotic
narrow-band schedule. They test the arithmetic solver and
the extraction interface, not the uniform Fourier
inequalities or their asymptotic thresholds.

## 6. Research boundary

The exact character-lift system gives a new useful dual
target with a bounded number of successful progress steps.
Uniform **label-disagreement density** in short-ratio
fibres is now proved for the specified input class, and
each fibre has an exact deterministic half-scale
membership/extraction oracle. The unresolved step is a
uniform deterministic hitter for that predicate. We also
need a replacement label or a different exit for cases
where the Jacobi character has the required lift, or the
inequality e<v_2(N-1) fails. Keep the general pooled rank
and primary extraction methods in parallel.

**Uniform deterministic L_N[1/2,O(1)] general factoring
remains open.** No uniform subexponential upper bound
on the old residual directions has been proved. No new
Lean milestone is counted.
