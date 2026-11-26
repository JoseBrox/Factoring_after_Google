# Disjoint narrow prime bands and exact streaming divisibility atoms

**Status (26 November 2026).** Proved uniform narrow-band coverage,
a simplified arithmetic search predicate, an exact fresh-randomness
streaming implementation of its atoms, and a deterministic exact
conditional-expectation oracle for bounded-degree combinations of
those atoms. The full uniform deterministic half-scale search remains
open. No new complete Lean milestone is counted. The one-third
program remains deferred.

This continues the [common-anchor construction](common_anchor_derandomization.md)
and the [derandomization audit](prime_word_derandomization_audit.md).
The objective is to simplify the arithmetic predicate enough to
permit an actual derandomization, rather than invoke a theorem about
a stronger randomness model than we have implemented.

## 1. A narrower product family still covers almost all residues

Let n be the binary length of odd N, use the existing
\(b=\lceil\sqrt{n\lceil\log_2(n+2)\rceil}\rceil\), \(B=2^b\),
\(k=\lfloor(n-2)/b\rfloor\), and \(L=k+2000\).
Work for sufficiently large n, so \(B<N\), \(L\ge1\), and
\(k\to\infty\). As before, sieve for a factor up to B and handle
primes and prime powers. The remaining band primes are units.

Replace the full dyadic band by the interval
\[
 (B(1-1/(8L)),B].
\]
Divide it into L consecutive intervals of equal length
\(B/(8L^2)\), open at the left endpoint and closed at the right.
Let \(P_i\) be the primes in interval i, and \(m_i=|P_i|\).
All endpoints are rational and can be used by exact integer
comparisons. The full band \(P=\bigcup P_i\) is enumerated
in time polynomial in B.

The uniform sharp-interval prime-character estimate from
[the previous contour proof](qrh_deterministic_progressions.md)
applies to each of these intervals. Specifically, its weighted
error \(O(B^{61/64}\log(2N)+B^{63/64}\log B+
\sqrt B\log^2 B)\) is negligible relative to the interval length
\(B/(8L^2)\). Partial summation, with the actual interval endpoints,
gives, uniformly in i,
\[
 m_i\gg B/(L^2\log B),\qquad
 \left|\lambda_{i,\chi}\right|\le B^{-1/100},\qquad
 \lambda_{i,\chi}=\frac1{m_i}\sum_{p\in P_i}\chi(p)
 \quad(\chi\ne1).
 \tag{1}
\]
The principal estimate uses the corresponding zeta zero-free
input and its pole contribution. The fixed seven-eighths
Dirichlet/zeta strip is the same previously verified input;
the short-interval loss is only polynomial in n.

Let \(\pi\) be the distribution of the residue of the product
of **one independent uniformly chosen prime from each** \(P_i\).
Its support \(D\) consists of those residues with such a product
representative. Unlike the earlier full-band independent-word
model, every product is squarefree, and its ordered tuple
in the specified interval order is unique.

For the first k intervals, distinct tuples give distinct
positive integers, each at most \(B^k<N\). Thus they give
distinct residues modulo N. If \(G=(\mathbb Z/N\mathbb Z)^\times\),
character orthogonality gives the exact moment identity
\[
 \sum_\chi\prod_{i=1}^k|\lambda_{i,\chi}|^2
       = |G|/\prod_{i=1}^k m_i\le B^6 .
 \tag{2}
\]
For the bound, taking binary logs gives
\(n-kb+k(2\log_2 L+\log_2\log B+O(1))\).
Here \(n-kb<b+2\), \(L=O(n/b)\), and
\(k\log_2 n\le b\) for large n. Hence the displayed log
is at most \(6b\) eventually. The disjoint intervals avoid
even the factorial factor of the older moment bound.

For the remaining 2000 intervals use (1). It follows that
\[
 \Delta=\sum_{\chi\ne1}|\widehat\pi(\chi)|^2
       \le B^{6-40}=B^{-34}.
 \tag{3}
\]
Parseval shows that every missing residue contributes
\(1/|G|\) to \(\Delta\), so
\[
 |G\setminus D|\le |G|B^{-34}.                       \tag{4}
\]
This is a uniform support theorem, not an assertion
of pointwise positivity at every residue.

Every represented integer x satisfies
\[
 (7/8)B^L\le B^L(1-1/(8L))^L <x\le B^L,
 \tag{5}
\]
by Bernoulli's inequality and the strict lower band endpoint.
Also \(B^L/N>B^{1999}/4\). In particular the represented
integers are much larger than N, but remain within the
half-scale AP search limit.

## 2. Independent anchors also suffice for full rank

One need not solve the common-anchor problem simultaneously
over the entire prime band. Set \(T=2L+1\).
For each prime p in P, independently seek a residue r
with \(r,p^T r\in D\). By (4) the proportion of such
residues in G is at least \(1-2B^{-34}\), uniformly in p.
Their representations give exponent vectors u_p,v_p of
coordinate sum L and a row
\[
 A_{p,*}=Te_p+u_p-v_p .
\]
The anchor and hence u_p may vary with the row.

**Lemma.** Every such matrix A is nonsingular.
If Aw=0, choose an index p with maximal |w_p|.
Then
\[
 T|w_p|=|(v_p-u_p)\cdot w|
       \le 2L\|w\|_\infty .
\]
As \(T>2L\), this forces w=0. The old sharper \(T>L\)
threshold still holds with a single common anchor; the
present slightly larger T eliminates its common-anchor
requirement. It does not increase the asymptotic search
cost.

Every row is an exact signed exponent relation modulo N.
Consequently \(|\det A|>0\) annihilates the full band,
which generates G by (1) and quotient character
orthogonality. The earlier deterministic supplied-exponent
splitting argument applies unchanged. It suffices, therefore,
to deterministically solve the dense *two-translation*
predicate separately for each p. There are at most B
targets, so an \(\exp(O(b))\) algorithm per target would
still give the desired bound. Alternatively retain a
common anchor and solve all translations at once.

## 3. Exact streaming atoms by a truncated quotient trick

The obstacle in the previous verifier was storing
\(aR\bmod N\), where R is a random n-bit anchor and a is
a known target multiplier (1 or \(p^T\bmod N\)). Even
one-pass exact residue computation can require nearly
n bits. It is unnecessary for the following narrower
divisibility tests.

Let \(R=\sum_{h=0}^{n-1}r_h2^h\) be the raw n-bit
anchor; do not require \(R<N\). Put
\[
 K=2^{\lceil\log_2(2n)\rceil},\quad
 c_{a,h}=a2^h\bmod N\in[0,N),\quad
 w_{a,h}=\lfloor Kc_{a,h}/N\rfloor,\quad
 s_a(R)=\sum_h r_hw_{a,h}.
\]
All the c and w are deterministic constants depending
only on N,a,n. They can be precomputed in the allowed
time, and made available on the ordinary read-only
input of a randomized verifier. Define the integer
\[
 y_a(R)=\sum_h r_hc_{a,h}-N\lfloor s_a(R)/K\rfloor .
 \tag{6}
\]
It is congruent to aR modulo N and satisfies \(0\le y_a<2N\).
Indeed the difference between
\(\sum r_h c_{a,h}/N\) and \(s_a/K\) is in \([0,n/K)\),
which is contained in \([0,1/2)\). After subtracting
\(\lfloor s_a/K\rfloor\), the result lies in \([0,3/2)\).
There is no need to resolve close-to-integer rounding
cases or to store an n-bit remainder. Formula (6)
specifies the same shifted representative for all
auxiliary primes.

Put \(M=\lfloor B^L/N\rfloor\). For a lift index
\(1\le j\le M\) and \(q\in P\) define the Boolean atom
\[
 A_{a,j,q}(R)=\mathbf1_{\{q\mid y_a(R)+jN\}}.
 \tag{7}
\]
It is evaluated **exactly** in one pass over the fresh
bits of R by retaining only two integers:
\[
 s\leftarrow s+r_hw_{a,h},\qquad
 z\leftarrow z+r_hc_{a,h}\pmod q .
\]
The first is at most nK, so uses O(log n) bits, the
second at most b+1 bits. At the end test
\(z+N(j-\lfloor s/K\rfloor)=0\bmod q\).
There is no error probability, no repeated access to
a random bit, and no need for random-access arithmetic
on the anchor. Precomputing the deterministic constants
or reducing them modulo q takes at most polynomial
time in B,n and is independent of R. A fixed prefix
can simply be processed using its prescribed bits
before drawing fresh completion bits.

### Exact divisibility-only representation test

For a fixed multiplier a define
\[
 F_a(R)=
   \bigvee_{j=1}^M\ \bigwedge_{i=1}^L\
                      \bigvee_{q\in P_i} A_{a,j,q}(R).
 \tag{8}
\]
Then \(F_a(R)=1\) if and only if \(aR\bmod N\in D\).

To prove the forward implication, the lift x=y_a+jN
is positive and \(x<B^L+2N\). Choosing a prime divisor
from each disjoint interval gives a divisor of x
strictly greater than \((7/8)B^L\). For large n,
\(B^L+2N<(7/4)B^L\). Hence the remaining positive
integer cofactor is less than 2, and equals 1.
In particular x is actually at most \(B^L\), with
exactly one distinct prime from each interval.
For the reverse implication, every product representative
x from (5) is congruent to y_a modulo N. Its index
\((x-y_a)/N\) is an integer between 1 and M, because
\(x>3N\) eventually and \(0\le y_a<2N\).
That lift passes all the tests.

Thus all of the previous exact integer-division,
large-prime-power valuation and product-equality checks
can be removed from the Boolean verifier. The only
non-Boolean gates are small-state streaming modular
tests. A full common-anchor predicate is the AND of
\(F_1\) and all \(F_{p^T\bmod N}\); the independent-row
version only uses \(F_1\land F_{p^T\bmod N}\).
The formula has depth at most four above the atoms,
with at most \(B^{2000+O(1)}\) occurrences and deterministic
constant-table bit size within \(\exp(O(b))\).
All represented products have unit residue, so acceptance
automatically implies the unit guard; no gcd calculation
is required inside (8).

It is essential to distinguish *each* atom's read-once
implementation from a read-once evaluation of the whole
formula. Evaluating (8) atom after atom by rerunning the
same random input would still use persistent randomness.
No such implementation is being counted as BPL.

## 4. Exact conditional expectations for bounded modular tests

There is a new, unconditional arithmetic-specific
moment oracle. For any fixed constant h, let H be
a list of at most h atoms (7), including repetitions,
negations, or any Boolean function of their outputs.
Their **joint** streaming state consists of one small
counter \(s_a\) for each distinct multiplier a and
one residue z for each distinct pair (a,q).
Atoms with different j but the same (a,q) reuse
the same residue. With h fixed, the work space is
O(h(b+log n))=O(b). The state set has size at most
\[
 (nK+1)^{h}(B+1)^{h}=\exp(O(b)).
\]
Given any prescribed prefix of the n anchor bits,
perform exact dynamic programming on this state space.
At each position take the single prescribed transition
or sum both transitions. Store integer counts of
paths to each state, of at most n+1 bits. On the final
layer apply the specified Boolean function and sum
the accepting counts. This yields the exact number
of accepting completions, in deterministic time
\(\exp(O(b))\), with no invocation of the new L=BPL
theorem and no approximation error. The full DP may
use subexponential memory; the original streaming
machine itself uses O(b) work bits.

Consequently expectations of any explicitly given
constant-degree rational polynomial in the atoms,
whose total description length is \(\exp(O(b))\),
can be computed exactly for *every* prefix in the
same budget. Expand into the explicitly supplied
monomials, use the preceding count oracle, and use
exact rational addition; the sum of denominator bit
lengths is at most the input length.

**Sufficient deterministic selection theorem.** If one
can uniformly construct, in \(\exp(O(b))\) time, such a
polynomial H with
\[
 H(R)\le F_1(R)F_a(R)\quad\text{for every }R,\qquad
 \mathbb E_{R\sim U_n}H(R)>0,
 \tag{9}
\]
then uniform deterministic half-scale factoring follows.
At each bit, compute the exact two conditional
expectations and keep the larger. Their mean is the
parent expectation, so positivity is preserved.
After n steps, the resulting anchor satisfies H(R)>0,
hence the exact Boolean predicate is 1. Recover both
representations by the ordinary AP scanner, assemble the
independent-anchor relation matrix of Section 2, and
split by the verified exponent. This gives a precise
pessimistic-estimator goal for the arithmetic-specific
derandomization program.

## 5. Why generic low-degree reasoning does not yet suffice

It would be incorrect to infer (9) from high density
and small-state atoms alone. There is a rigorous
obstruction to any generic constant-degree polynomial
lower bound based only on the OR-of-AND structure.

Let \(X_{j,i}\) be independent Bernoulli(p) variables,
\(0<p\le1/2\), for rows j and \(1\le i\le L\).
Consider \(F=\bigvee_j\bigwedge_i X_{j,i}\). With M rows
its density is \(1-(1-p^L)^M\), arbitrarily close to one.
For the product distribution P on one row, define
\[
 Q(x)=P(x)-p^L(-1)^{L-\sum_i x_i},
              \qquad x\in\{0,1\}^L .
 \tag{10}
\]
The probabilities are nonnegative: every P(x) is
at least \(p^L\), since p<=1/2. The parity sum
vanishes, so Q has mass one. It gives zero probability
to the all-one row. For every monomial of degree
strictly below L, its expectation under Q equals its
expectation under P, since at least one coordinate
does not occur in the monomial and the signed
correction cancels in that coordinate.

Use independent Q rows to form a new distribution.
It gives F=0 everywhere while preserving all moments
of total degree <L of the original independent
Bernoulli variables. Consequently any real polynomial
H of degree <L satisfying H<=F pointwise on this
Boolean domain has
\[
 \mathbb E_P H=\mathbb E_Q H\le0.
\]
This remains true even when the original density tends
to one, for instance with M>>p^(-L).
Thus a generic low-degree lower-certificate method
cannot treat the interval-hit predicates in (8) as
independent Boolean inputs. An arithmetic-specific
proof of (9) would have to exploit their actual
correlations, periodicity across lift indices, or some
other stronger structural property. This is **not**
a lower bound for the actual anchor function.

There is also a precision obstacle to using a PRG that
fools each full smooth-witness clause separately. For
the identity target, a clause specifying one particular
prime in every interval and a particular j has at most
one accepting residue in [0,N), by Section 3. As the
product tuples range over their support, every residue
in D has such a clause (using the shifted lift index).
Under uniform residues each nonempty clause has
probability exactly 1/N. A generator with support
\(\exp(O(b))\) must miss many of these clauses by (4).
It cannot approximate all their probabilities to error
strictly smaller than 1/N. This does not exclude a
hitter for their union, which is precisely what we want.

## 6. Applicability of recent derandomization results

The fixed-multiplier atom, or any bounded number of
atoms, now really is in the fresh-randomness workspace
model of the September 2026 L=RL=BPL result after
padding. The exact DP is already enough for that
restricted class.

The whole OR-AND-OR formula still reads the same anchor
bits in many different atoms. No constant-visit random
tape or random-independent auxiliary-stack realization
has been established. In particular, the September
2026 Doron-Lang [read-k branching program generators](https://eccc.weizmann.ac.il/report/2026/210/)
improve the dependence on k but do not provide the
required short seed for arbitrary exponentially many
reads. Krak's [optimal modular-sum generators](https://eccc.weizmann.ac.il/report/2026/130/)
concern a fixed modulus, with modulus-dependent
constants; our atoms have many growing prime moduli,
and the full Boolean composition is not a single
modular-sum test. The recent [persistent-randomness
characterization](https://eccc.weizmann.ac.il/report/2023/211/)
by Pass and Renard also makes explicit that general
polynomial-time read-many logspace search is a distinct
derandomization problem. These scopes do not rule
out an arithmetic-specific solution to (8).

## 7. Exact finite verification

The standard-library experiment
[verification/research/narrow_band_streaming.py](../verification/research/narrow_band_streaming.py)
checks the exact shifted representative, including raw
anchors at least N and zero; compares the one-pass
atom to full integer arithmetic; compares the entire
divisibility-only lift predicate to exhaustive narrow-band
product tables on a small fixture; and verifies the
conditional DP counts by brute force at several prefixes.
A separate independent-anchor relation matrix is checked
by exact Bareiss elimination and modular powering.
Product tables are used only for the finite checks,
not in the asymptotic search.

Tested source: Git blob c4315ed3d8ee8095fba7c551b4277d5aa7ea2f3b,
SHA-256 0aa15819bbbc0eb7906d4f6753842f9bcdb2aaa204903019b9c5423db68446c7.

Observed output:

    streaming atom checks 61440 shifted representatives 227 exact lift decisions 5120
    exact conditional DP checks 24
    independent-anchor rank fixture: N 21 band sizes [4, 3] rank 7 distinct anchors 2 determinant 108000 factor 7

The fixture parameters are small illustrative values,
not the asymptotic schedule with J=2000. All certificate
checks are exact integers.

## 8. Remaining goal

The whole half-scale construction is now expressible
using an especially simple Boolean combination of
exact one-pass linear-modular atoms, with separate
dense two-translation predicates sufficient. We can
compute conditional expectations of any constant
number of these atoms exactly. The missing step is
an efficient uniform hitter for their structured
composition, or an arithmetic-specific estimator (9).
The low-degree obstruction identifies a genuine
limitation of the generic method, not a proof that
such an estimator is impossible on the arithmetic
domain.

**Uniform deterministic half-scale factoring remains
open.** No assumption that read-many randomness is
free, or that full smooth witnesses can be counted
from bounded moments, is used. The one-third program
has not been started.
