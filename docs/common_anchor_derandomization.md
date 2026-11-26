# Common-anchor relations and the reduced-space verifier

**Status (26 November 2026):** proved common-anchor coverage, an
exact deterministic extraction conditional on one good anchor,
a polynomial-advice deterministic half-scale algorithm, and an
exact low-workspace verifier with reusable read-only anchor bits.
The uniform deterministic anchor search remains open. The read-only
randomness model is not the fresh-randomness model of L=BPL.
No new complete Lean milestone is claimed. The one-third program
remains deferred.

This continues [positive smooth-relation coverage](positive_smooth_relation_coverage.md)
and the [derandomization audit](prime_word_derandomization_audit.md).
The earlier adaptive sign-subset driver can be replaced entirely by
one full-band common anchor.

## 1. A common anchor simultaneously supplies all relations

Use the binary length \(n\) of \(N\), the integer
\(b=\lceil\sqrt{n\lceil\log_2(n+2)\rceil}\rceil\),
\(B=2^b\), and
\[
 P=\{p:B/2<p\le B,\ p\text{ prime}\},\quad m=|P|,
 \quad k=\lfloor(n-2)/b\rfloor,\quad L=k+J,\quad J=2000.
\]
Work at sufficiently large lengths; sieve through \(B\) and return
a proper divisor if one is found. Handle primes, even inputs and
perfect powers separately, as in the preceding note. Thus every
prime of \(P\) is a unit modulo the surviving \(N\).
Put \(G=(\mathbb Z/N\mathbb Z)^\times\).

Let \(\pi\) be the law of a product of \(L\) independent uniform
primes from \(P\), reduced modulo \(N\), and \(D=\operatorname{supp}\pi\).
Equivalently, \(r\in D\) exactly when a positive integer at most
\(B^L\) congruent to \(r\) is a product of exactly \(L\) primes of
\(P\), counting multiplicities.

The fixed Dirichlet zero-free theorem, using the uniform prime
estimate proved in the preceding note, gives
\[
 \left|\lambda_\chi\right|\le B^{-1/100},\qquad
 \lambda_\chi=m^{-1}\sum_{p\in P}\chi(p),\quad \chi\ne1.
\]
The small-product moment bound is
\[
 \sum_\chi|\lambda_\chi|^{2k}
 \le |G|k!/m^k\le B^4.
\]
Indeed \(B^k<N\), so equality of two product residues of length
\(k\) is actual integer equality, hence equality of their prime
multisets. The probability that the second word is such a
permutation of the first is at most \(k!/m^k\). The final
inequality is the elementary binary-length estimate in Section
3.3 of the previous note, using \(m\gg B/\log B\).

It follows that
\[
 \Delta=\sum_{\chi\ne1}|\lambda_\chi|^{2L}
 \le B^{4-2J/100}=B^{-36}.
\]
Parseval gives
\[
 |G|\sum_{r\in G}|\pi(r)-1/|G||^2=\Delta.
\]
Every residue missing from \(D\) contributes \(1/|G|\) to the
left side. In particular,
\[
 |G\setminus D|\le |G|B^{-36}.                     \tag{1}
\]
This is a bound on the number of holes, not just a bound on
the total variation distance of the product law.

Fix \(T=L+1\). Define the good-anchor set
\[
 {\cal A}=D\cap\bigcap_{p\in P}p^{-T}D.
\]
Each translation is a bijection of \(G\), so the union bound
and (1) give
\[
 |G\setminus{\cal A}|\le(m+1)|G|B^{-36}.           \tag{2}
\]
In particular \({\cal A}\) is nonempty for every sufficiently
large surviving composite, and its density in \(G\) is at least
\(1-2B^{-35}\). There is no choice of sign subsets, no dependence
on previous relations, and no need to compute an inverse of an
unknown prime product.

### The common-translation matrix lemma

For \(r\in{\cal A}\), let \(x_0\) represent \(r\), and \(x_i\)
represent \(p_i^T r\), with each integer representation a
product of \(L\) band primes. Let \(u,v_i\in\mathbb Z_{\ge0}^m\)
be their respective exponent vectors, all with coordinate sum
\(L\). Form the integer matrix with rows
\[
 A_{i,*}=T e_i+u-v_i.
\]
Each row is a genuine signed exponent relation modulo \(N\).
Every row sums to \(T\).

**Lemma.** For arbitrary such nonnegative vectors, \(A\) is
nonsingular whenever \(T>L\).

Suppose \(Aw=0\) over the reals. Choose indices \(i,j\) attaining
the largest and smallest coordinates of \(w\). Subtract the
two row equations:
\[
 T(w_i-w_j)=(v_i-v_j)\cdot w\le L(w_i-w_j).
\]
The inequality holds because each \(v_i\) is nonnegative of
sum \(L\). Since \(T>L\), all coordinates of \(w\) agree.
The row sums \(T\ne0\) then give \(w=0\). This argument is stronger
than ordinary row diagonal dominance, which would follow by
taking \(T>2L\). We use \(T=L+1\). The strict threshold is
sharp for unrestricted vectors: at \(T=L\) one can take
\(v_i=L e_i\) for all \(i\), obtaining identical rows \(u\).

Let \(E=|\det A|>0\). The integer adjugate identity implies
\[
 p^E=1\bmod N\qquad (p\in P).
\]
Hadamard gives \(E\le(T+2L)^m\), so the bit length of \(E\)
is polynomial in \(B,n\). Exact integer matrix elimination
therefore costs \(\exp(O(b))\) bit operations.

The full band generates \(G\): otherwise a nonprincipal
character lifted from the finite abelian quotient by the
generated subgroup would be identically one on the band,
contradicting the character bound. Hence \(E\) annihilates
\(G\). The CRT projection to each \((\mathbb Z/p\mathbb Z)^*\)
for \(p\mid N\) is surjective, so \(p-1\mid E\).

The supplied-exponent square-chain argument from the preceding
note now splits every surviving composite with two distinct
prime factors. In the equal local two-adic valuation case,
the product of the two distinct Legendre characters detects
opposite signs at a band prime; in the unequal valuation case,
a band nonresidue at the factor with larger valuation suffices.
Either follows from the nonprincipal-character bound. Scan all
band primes with the odd part of \(E\) and its successive
doublings. At the first level where one local power becomes
one but the other does not, the gcd with \(N\) gives a proper
factor. Primality and perfect powers are dealt with first.
Deterministic Miller testing may use the previously reviewed
full Dirichlet GRH witness bound.

### Deterministic verification and extraction

For any candidate \(r\) in \(1,\ldots,N-1\), compute its gcd
with \(N\) (a proper gcd already splits). For a unit residue,
scan \(r+jN\) through \(B^L\), and repeat for each
\(p_i^T r\bmod N\). There are at most \(B^J+1\) candidates
per scan because \(B^k<N\). Factor each candidate by trial
division through the explicit band, accepting precisely when
the cofactor is one and the exponent sum is \(L\).
This checks membership in \(D\) exactly and produces the
needed exponent rows. The number of scans is at most \(m+1\).
All these loops, their bit arithmetic, and the determinant
and gcd chain cost \(\exp(O(b))\), even when a candidate
fails. The search is over a single anchor, not a list of
independent words.

## 2. Uniform randomized and polynomial-advice consequences

Take \(R\) uniformly in \(0,\ldots,2^n-1\) and reduce it
modulo \(N\). Each residue has at most two preimages.
If the residue has a proper gcd with \(N\), return that
factor; if it is zero, reject; otherwise use the preceding
anchor check. The total probability of failure is at most
\[
 2(m+1)B^{-36}+2^{1-n}<B^{-2}
\]
for sufficiently large \(n\). Independent repetitions
therefore give the same uniform randomized half-scale
factoring bound as before, but with a single \(n\)-bit
random candidate and no adaptive rank-generation loop.

There is also a stronger nonuniform consequence. For fixed
length \(n\), sample \(t=\lceil n/b\rceil+1\) independent
\(n\)-bit candidate strings. For any particular surviving
\(N\) of that length, the probability that all fail is at
most \(B^{-2t}\). Union bound over fewer than \(2^n\)
inputs gives failure probability less than one. Thus there
exists one list of \(t\) candidates working for all inputs
of that length, including the allowed proper-gcd exit.
The advice length is \(nt=O(n^2/b)\) bits, which is
polynomial (rather than subexponential). With advice for
each smaller length, complete recursive factorization is
deterministic within the half-scale time budget. Finitely
many small lengths can be handled by trial division.
No uniform construction of the advice is asserted.

The hole bound alone cannot justify a short uniform list:
even when \(J\) is any fixed larger constant, its cardinality
bound on bad anchors has scale \(N B^{-O(1)}\).
Making the bound small enough by increasing \(J\) to
\(\Omega(n/b)\) forfeits the half-scale AP scan, whose
upper bound is \(B^J\) candidates. This is a limitation of
the present density-only guarantee, not a lower bound for
arithmetic-specific hitting sets or for all implementations
of the scan.

## 3. Priority 1: an exact verifier with small work space

The common anchor is an \(n\)-bit string. We can give an
exact acceptance predicate using \(O(b)\) work bits and
\(\exp(O(b))\) time, **if the anchor is on a reusable
read-only input tape**. This differs from storing an
\(n\)-bit product residue in streaming work space.

Use the uniform constant-depth threshold-circuit theorem
for integer division and iterated multiplication:
W. Hesse, E. Allender and D. A. M. Barrington,
[Uniform constant-depth threshold circuits for division
and iterated multiplication](https://doi.org/10.1016/S0022-0000(02)00025-9).
The uniform division and iterated multiplication results
are the arithmetic inputs here, not the additional claim
corrected in the 2014 corrigendum. In particular polynomial-size
uniform constant-depth threshold circuits on read-only
polynomial-bit-length operands have deterministic
logarithmic-workspace bit evaluation: enumerate a gate's
predecessors, count their Boolean outputs, and evaluate
recursively through a fixed depth, keeping gate identifiers
and counters. DLOGTIME uniformity allows gate descriptions
to be regenerated in logarithmic work space. Fixed
compositions of the arithmetic circuits retain this property.

The verifier reads the \(n\)-bit raw \(R\) repeatedly
as needed. Compute queried bits of \(r=R\bmod N\), and reject
if \(r=0\). For each target \(p\in P\), or the identity target,
the bits of \(a=p^T r\bmod N\) are computed using uniform
iterated multiplication and division. All intermediate integer
bit lengths are \(O(n+Jb)=O(n)\), since \(T=L+1\).
A counter of \(O(b)\) bits suffices to enumerate the possible
lifts \(x=a+jN\), \(0\le j\le B^J\). Discard zero or out-of-range
lifts. The bits of \(x\) are likewise accessed by arithmetic
circuits, not retained in work space.

To check whether a lift is exactly a product of \(L\) band
primes, enumerate \(q\in P\). Compute
\[
 e_q=\min(v_q(x),L)
\]
by testing divisibility by \(q^e\) for \(1\le e\le L\).
Each divisibility check is on polynomial-bit integers and
uses the same arithmetic bit evaluator. Record the sum of
these capped exponents, rejecting unless it is exactly \(L\).
The product \(W=\prod_{q\in P}q^{e_q}\) divides \(x\);
in particular \(1\le W\le x\le B^L\). To verify \(W=x\)
without storing either integer, enumerate auxiliary primes
\(t\le n^2\). For each \(t\), recompute the capped valuations,
accumulate \(W\bmod t\) with \(O(\log n)\)-bit registers,
and compare it with \(x\bmod t\). By the ordinary prime
number theorem the product of the auxiliary primes exceeds
\(B^L\) for large \(n\). Hence equality of these residues
is equivalent to actual equality. This is an exact test,
not a Monte Carlo equality fingerprint. The prime loops
can use the explicit read-only band, or trial division
with \(O(b)\)-bit counters. The number of nested loops
is fixed and all ranges are polynomial in \(B,n\), with
\(J\) a fixed constant. The arithmetic evaluator's fixed
depth also gives only fixed nesting overhead.

Accept if all \(m+1\) scans succeed. No gcd algorithm is
required inside this small-space predicate: success for
the identity target already implies that \(r\) is a unit,
since the band primes are units. The ordinary higher-space
gcd branch and extraction can still be used outside the
verifier. After the initial sieve, the proportion of
nonunits is at most \(n/B\), by the union bound over the
at-most-\(n\) prime divisors of \(N\), all larger than \(B\).
Since the raw \(R\) has at most two preimages per residue,
the strict acceptance predicate has probability
\(1-O(n/B)\), uniformly on surviving \(N\).

This proves the stated work-space and time bounds for an
exact read-only-input checker, including any fixed prefix
of the anchor and an independent uniform completion.
It does **not** prove the same bounds for a fresh-randomness
machine. An \(n\)-bit random string read repeatedly is a
persistent-randomness or multiple-access tape. The input
tape of the published L=BPL machine is deterministic data;
its random bits are fresh (or read once, with a cached
current bit). Moving the anchor to a reusable random tape
does not satisfy that hypothesis.

If a suitable polynomial-time probability approximation
theorem were available for this verifier model on inputs
padded to \(\exp(O(b))\), conditional probabilities of
success for prefixes could be estimated to \(o(1/n)\).
The greedy bit-fixing reduction in the preceding audit
would then yield a uniform deterministic half-scale factorer.
This is the precise missing access-model theorem or
implementation, not a missing smooth-number density
assertion.

## 4. Priority 2: bounded-access and auxiliary-stack constraints

Cheng and Wu's [SC derandomization result](https://arxiv.org/abs/2609.23603)
treats bounded visits to each random cell or a random-independent
auxiliary push/pop schedule. The abstract and scope were
reviewed; the full paper was not accessible in the present
audit. Its hypotheses must not be replaced by unrestricted
read-only access to random bits. The arithmetic verifier
above can re-query an anchor digit many times, so the
bounded-visit hypothesis is not established. A single
pushdown stack is also not a random-access tape. Merely
pushing the anchor does not give an implementation that
can read and restore it arbitrarily many times with small
work space. No qualifying oblivious-stack implementation
has been constructed.

There is a useful additional rigorous obstacle to the most
obvious exact verification strategies. In the full-band
word model, take the increasing words of \(k\) distinct
band primes. Their products are distinct and smaller
than \(N\). Their number is
\[
 K_0={m\choose k}\ge 2^{n-O(b)}
\]
(and \(K_0\ge 2^n/B^4\) eventually by the same elementary
estimates as the collision moment). By (1), at most
\(N B^{-36}\) of their inverse residues are missing from
\(D\). Choose the remaining \(K\ge K_0/2\) words and,
for each, a fixed length-\(L\) suffix word representing
its inverse. If these first and second words are used
as two input blocks, the exact joint-product congruence
predicate has an equality submatrix of order \(K\).
Every pair with matching index satisfies the congruence;
every mismatched pair does not.

For a deterministic two-way input-head verifier with
\(O(b)\) workspace, worst-case time \(\exp(O(b))\), and a
constant bound on visits to every cell, Alice can simulate
the first block and Bob the second. A crossing of the
block boundary transfers the work configuration and
head positions, at cost \(O(b)\) bits. There are only
constantly many crossings. This would give a deterministic
communication protocol of \(O(b)\) bits for equality on
\(K\) inputs, impossible: the diagonal \(K\) accepting
pairs must lie in distinct accepting rectangles of the
protocol. Its cost is at least \(\log_2 K=n-O(b)\).
Thus this exact two-block check does not give a qualifying
bounded-access implementation.

This communication argument is restricted to the exact
joint congruence predicate, not our dense anchor predicate,
and does not exclude constant-error randomized equality
checks or auxiliary-stack algorithms. For completeness,
if such an equality protocol has public randomness and
per-input error at most \(\delta\), a fixed public seed
with \(c\)-bit transcripts and \(a\) accepted diagonal pairs
accepts at least \(a^2/2^c-a\) off-diagonal pairs. Averaging
and using \(\mathbb E a\ge(1-\delta)K\) gives
\[
 c\ge\log_2\frac{(1-\delta)^2 K}{1+\delta(K-1)}.
\]
In particular the extremely small error \(\delta\le1/K\)
again requires \(n-O(b)\) communication. This does not
exclude low-space fingerprinting at much larger errors.

### A restricted positive one-pass fingerprint result

With a fixed known target residue \(r\) given as ordinary
read-only input, there *is* a small-workspace one-pass
randomized congruence test for a random length-\(L\) word.
Choose an auxiliary random prime in \((Q/2,Q]\) with
\(Q=B^{J+6}\), and accumulate the prime-word product
modulo this prime. Compare the result with every lift
\(r+jN\le B^L\), accepting if one matches. Both the stored
residue and all counters have \(O(b)\) bits. The test
accepts true congruences. For a false congruence, all
at most \(B^J+1\) differences from possible lifts are
nonzero integers bounded by \(B^L\). Each has
\(O(n/\log Q)\) prime divisors in the auxiliary band.
By the PNT, the false-acceptance probability is at most
\(O(n B^J/Q)=O(n B^{-6})\). Sampling the auxiliary prime
can use a bounded number of fresh bits, by taking a
uniform integer index modulo the band size with extra
bits so the statistical error is at most \(B^{-10}\).
The time is \(\exp(O(b))\).

This verifies a fixed-target event with small additive
error, but does not solve our dense search. Indeed
Parseval also gives the pointwise estimate
\(\pi(r)\le |G|^{-1}+\sqrt{\Delta/|G|}\),
which is exponentially small in \(n\), not in \(b\).
A fixed-target probability approximator with additive
accuracy \(\exp(-O(b))\) cannot infer positivity of that
rare event. Increasing the accuracy to the requisite
exponential-in-\(n\) scale is not licensed by the
half-scale time bound. A multiplicative approximation
or a new way to avoid conditioning on a rare event
would be needed.

## 5. Priority 3 and the remaining problem

The anchor formulation reduces every rank step to one
dense arithmetic predicate, removes inverse-product
verification, and permits polynomial advice. An
arithmetic-specific uniform hitter now needs only to
produce a candidate from the set in (2), not a family
covering adaptive subsets. But neither the density
argument nor the reviewed general PRGs proves that
any prescribed short list intersects this set.
The one-pass fixed-target test and read-many exact
checker isolate distinct possibilities for further work.
A verifier obeying a proved small-space randomness
model, or an arithmetic argument selecting an anchor
directly, remains necessary. The recent derandomization
results have not yet been applied to obtain uniform
deterministic half-scale factoring.

## 6. Finite exact checks

The standard-library script
[common_translation.py](../verification/research/common_translation.py)
was executed on the finite fixtures below. Exhaustive
support tables are used only for the small rank fixtures,
and are not proposed as an asymptotic algorithm. The
separate arithmetic-progression scanner is independently
compared with an exhaustive table. The matrix test
enumerates all 1296 choices of the common and target
vectors for \(m=3,L=2\). Exact Bareiss determinants,
signed modular relations, annihilation of every band
prime, and the proper gcd are checked in the rank tests.

Tested source: Git blob
1a8e9ee4fa5ba25f394d2f7537f1acb79c26262d,
SHA-256
6d2cd63a026727f927e62931ceff1198a10c84b4098051bac19f4f45e006de4a.

Observed output:

    AP scanner: 24 unit residues, 20 represented
    matrix check: 1296 nonsingular matrices at T=L+1; singular at T=L: [[2, 0, 0], [0, 0, 2], [0, 0, 2]]
    N 899 B 23 L 12 band 4 support 408 good anchors 10 T 13 anchor 44 determinant bits 16 factor 31
    N 47053 B 200 L 6 band 21 support 46152 good anchors 37335 T 7 anchor 1 determinant bits 60 factor 211
    N 23707 B 150 L 8 band 14 support 23400 good anchors 23400 T 9 anchor 1 determinant bits 46 factor 151

The first rank fixture is deliberately one with only ten good
anchors, none equal to one. These are finite illustrative
tests using small parameters, not evidence of a uniform
short hitting set. The new low-workspace circuit verifier
is a theoretical construction; its actual uniform circuit
evaluator and resource bounds have not been instrumented or
Lean-verified.

**The uniform deterministic \(L_N[1/2,O(1)]\) bound is still
open; we have not started the one-third program.**
