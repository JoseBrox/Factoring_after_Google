# Uniform positive smooth-relation coverage by prime-character moments

**Status (26 November 2026): proved uniform relation existence and a
uniform randomized half-scale algorithm, using the already verified
Dirichlet/zeta seven-eighths zero-free theorem. No additional smoothness
or covariance conjecture is invoked. Uniform deterministic half-scale
factorization remains open.** The proof is written mathematics, not a
new end-to-end Lean certification.

This is a different route from the quadratic rank-one search. It removes
the number-field relation-existence hypothesis, rather than proving
coverage for the previous particular field family. The residual
problem is the deterministic selection of one product from a dense
set of successful prime words.

## 1. Why rational positive relations suffice

For every odd composite \(N\), the earlier quadratic field has
\(c=C+4\equiv0\bmod N\) and \(b=Ca-4\), where \(a=(\ell-1)/2\).
For integer marks \(r+t\theta\), the exact norm identity is
\[
 A=r^2-brt+ct^2
 =D+(C+4)t(t-ar),\qquad
 D=r(r+2(\ell+1)t).
\]
Thus \(A\equiv D\bmod N\). If the numerator and denominator
are units modulo \(N\), every exact prime factorization of
\(A/D\) gives an ordinary integer exponent relation modulo \(N\).
Such rational relations can be pooled across field parameters;
they need not give a unit in one field. In fact we will not need
a field or any quadratic norms at all.

Let \(\mathcal P\) be a finite set of primes not dividing \(N\).
A positive relation means a vector \(v\in\mathbb Z_{\ge0}^{\mathcal P}\)
such that
\[
 \prod_{p\in\mathcal P}p^{v_p}=1\bmod N.
\]
If we have \(m=|\mathcal P|\) independent positive relation rows,
their square matrix \(V\) has nonzero integer determinant. The
adjugate identity implies that
\[
 E=|\det V|,\qquad p^E=1\bmod N\quad(p\in\mathcal P).
 \tag{1}
\]
This argument needs no discrete logarithms, class group, algebraic
unit lattice, or factorization of the determinant.

The new theorem supplies a positive relation supported on any
prescribed subset \(S\subseteq\mathcal P\) of at least half the primes,
with any specified \(p_0\in S\) occurring at least twice. This allows
a rank-increasing construction using the signs of a rational
annihilator of the current relation rows.

## 2. Uniform prime-character estimate

Write \(n=\operatorname{len}_2 N\), and, using exact integer rounding,
take
\[
 b=\lceil\sqrt{n\lceil\log_2(n+2)\rceil}\rceil,\qquad B=2^b,
 \qquad \mathcal P=\{p\text{ prime}: B/2<p\le B\}.
\]
All assertions below concern sufficiently large \(n\), so \(B<N\).
First sieve to \(B\) and test these small primes against \(N\);
if a proper gcd occurs, return it. Henceforth every prime in
\(\mathcal P\) is a unit. Set \(G=(\mathbb Z/N\mathbb Z)^\times\)
and \(m=|\mathcal P|\). The ordinary PNT gives
\(m\ge B/(4\log B)\) eventually.

The [verified seven-eighths zero-free result and written
smoothed-character estimates](quasi_rh_witnesses.md) imply,
uniformly for every nonprincipal character of \(G\),
\[
 \left|\frac1m\sum_{p\in\mathcal P}\chi(p)\right|
          \le \epsilon,\qquad \epsilon=B^{-1/100}.
 \tag{2}
\]
For clarity, the required sharp-interval estimate is the
\(t=0\) case of the contour proof in
[the deterministic progression note, Section 1](qrh_deterministic_progressions.md).
Its proof applies to modulus \(N\) directly: the only conductor
dependence in the uniform log-derivative estimate is
\(\log(q(|t|+4))\), and here \(\log q=\log N=O(n)\).
Smooth a subinterval of \([B/2,B]\) on relative scale
\(B^{-1/64}\) and move the Mellin contour to \(15/16\).
The weighted prime-power sum has bound
\(O(B^{61/64}\log(2N))\), and the two endpoint errors are
\(O(B^{63/64}\log B)\). Higher prime powers contribute
\(O(\sqrt B\log^2 B)\). Partial summation removes \(\log p\)
and division by \(m\asymp B/\log B\) gives (2), since
every fixed polynomial in \(n,\log B\) is \(B^{o(1)}\).
All constants and thresholds are uniform in the nonprincipal
character, including imprimitive characters.
This is a consequence of the fixed strip already proved in
our pinned QRH integration, not an additional conjectural
prime-in-progressions estimate.

## 3. A uniform Fourier estimate for every half-subset

Let \(S\subseteq\mathcal P\) have \(s=|S|\ge m/2\).
Let \(\mu\) be uniform on \(\mathcal P\), \(\nu\) uniform on
\(S\), \(\rho=s/m\), and write
\[
 \lambda_\chi=\mathbb E_{p\sim\nu}\chi(p).
\]
The subset \(S\) is arbitrary; in particular it may depend
on \(N\), on earlier relations, and on the full prime list.
We require no independence between its definition and any
character.

### 3.1 Non-real characters have a constant spectral gap

Call a character real if \(\chi^2=1\), including the principal
character. For a non-real character, rotate by a unit complex
scalar to make \(\lambda_\chi\) nonnegative real. Put
\(X=\Re(e^{-i\vartheta}\chi(p))\) on \(\mathcal P\). Equation
(2), applied both to \(\chi\) and \(\chi^2\), gives
\[
 |\mathbb E_\mu X|\le\epsilon,\qquad
 \mathbb E_\mu X^2\le(1+\epsilon)/2.
\]
Since
\(\rho\mathbb E_\nu X=\rho\mathbb E_\mu X+
 \mathbb E_\mu[(1_S-\rho)X]\), Cauchy–Schwarz yields
\[
 |\lambda_\chi|\le
 \epsilon+\sqrt{\frac{1-\rho}{\rho}\frac{1+\epsilon}{2}}
 \le 3/4
 \tag{3}
\]
eventually, uniformly. Real characters may have mean arbitrarily
close to \(1\) or \(-1\); we do not assume a gap for them.

### 3.2 Few Fourier coefficients can be large

For distinct characters \(\chi,\psi\), (2) bounds the
inner product of their restrictions to \(\mathcal P\)
by \(\epsilon\) in absolute value. If \(M\) characters have
\(|\lambda_\chi|\ge x>0\), choose complex coefficients of
absolute value one aligning their inner products with \(1_S\).
Cauchy–Schwarz and the preceding almost-orthogonality give
\[
 \rho^2 M^2 x^2
 \le \rho\bigl(M+\epsilon M(M-1)\bigr).
\]
Consequently, if \(x^2\ge4\epsilon\), then
\[
 M\le4/x^2.                                               \tag{4}
\]
This is the needed counting bound for the large spectrum;
in particular it has no factor of \(|G|\).

### 3.3 Exact small-product moment

Choose \(k=\lfloor(n-2)/b\rfloor\), so \(B^k<N\) and
\(k\to\infty\). Orthogonality of the characters of \(G\)
gives
\[
 \sum_\chi|\lambda_\chi|^{2k}
 = |G|\,\Pr\left[\prod_{i=1}^k p_i
                     \equiv \prod_{i=1}^k q_i\bmod N\right],
\]
for two independent uniform \(S\)-words of length \(k\).
Both products are positive integers less than \(N\), so
the congruence is actual equality. Unique factorization says
that for each first word at most \(k!\) permutations of it
can be the second word. Therefore
\[
 \sum_\chi|\lambda_\chi|^{2k}
       \le N\,k!/s^k\le B^4.                              \tag{5}
\]
Here the final explicit envelope holds for all sufficiently
large \(n\): \(s\ge B/(8\log B)\),
\(n-bk\le b+2\), and
\[
 \log_2(Nk!/s^k)
 \le b+2+k\log_2 k+k\log_2(8\log B)
 \le b+2+k(\log_2 n+O(1))\le4b .
\]
The last inequality uses \(b^2\ge n\log_2(n+2)\).
No distinctness of primes in a word is required.

### 3.4 The non-real part of the walk is negligible

Take \(J=2000\) (any sufficiently large fixed constant
suffices), \(L=k+J\), and \(\eta=2\sqrt\epsilon\).
Eventually \(\eta^2\le B^{-1/200}\). For coefficients
smaller than \(\eta\), (5) implies
\[
 \sum_{|\lambda_\chi|<\eta}|\lambda_\chi|^{2L}
 \le B^4\eta^{2J}\le B^{-6}.                             \tag{6}
\]
For non-real characters whose coefficients are at least
\(\eta\), use (3) and the counting bound (4). Integrating
the tail count of these absolute values,
\[
 \sum_{\substack{\chi\ {\rm nonreal}\\|\lambda_\chi|\ge\eta}}
             |\lambda_\chi|^{2L}
 \le 4\eta^{2L-2}+
     \frac{8L}{2L-2}(3/4)^{2L-2}.
\]
Together,
\[
 \Delta:=\sum_{\chi\ {\rm nonreal}}|\lambda_\chi|^{2L}
                 =o(1),                                \tag{7}
\]
uniformly in every \(N,S\) under consideration. For the
full prime band, (2) in place of (3)-(4) would make all
nonprincipal Fourier contributions small; the sign-subset
construction specifically needs the stronger uniformity
over arbitrary halves established here.

## 4. Positive relations in every half-subset

Let \(\pi\) be the distribution on \(G\) of the product
\(Y\) of \(L\) independent uniform primes from \(S\).
Fix any \(p_0\in S\), and let \(\pi'\) be the distribution
of \(Z=(p_0^2Y)^{-1}\) in \(G\).
For every character, their Fourier coefficients are
\[
 \widehat\pi(\chi)=\lambda_\chi^L,\qquad
 \widehat{\pi'}(\chi)=\chi(p_0)^{-2}
                     \overline{\lambda_\chi^L}.
\]
For every real character the two coefficients agree
exactly. This is the reason for insisting on \(p_0^2\),
rather than just \(p_0\). For non-real characters their
difference has absolute value at most \(2|\lambda_\chi|^L\).
Parseval followed by Cauchy–Schwarz therefore gives
\[
 d_{\rm TV}(\pi,\pi')
 \le \frac12\left(\sum_\chi
       |\widehat\pi(\chi)-\widehat{\pi'}(\chi)|^2\right)^{1/2}
 \le\sqrt\Delta=o(1).                                   \tag{8}
\]
There is no assumption that either distribution is close
to uniform on all of \(G\); the real-character obstruction
is allowed and cancels in this comparison.

Since \(\pi\) is supported on residues of products of \(L\)
primes in \(S\), (8) proves
\[
 \Pr_Y\left[(p_0^2Y)^{-1}\text{ has an }S\text{-product
 representative of length }L\right]\ge1-\sqrt\Delta .
 \tag{9}
\]
Every such representative is a positive integer at most
\[
 B^L=B^{k+J}<N B^J.
\]
In particular there exists a positive relation
\(p_0^2 Y X=1\bmod N\), with every factor in \(S\), and
with exactly \(2L+2\) prime occurrences. Its integer
product is at most \(N^2 B^{2J+2}\).

**Theorem 1 (uniform positive-relation coverage).**
For every sufficiently large surviving composite \(N\),
every half-subset \(S\) of the dyadic prime band and every
\(p_0\in S\), such a relation exists. Furthermore a
randomly chosen first-half word succeeds with probability
\(1-o(1)\), uniformly. This result uses the already proved
fixed zero-free strip and elementary Fourier and counting
arguments. It contains no unproved assertion about smooth
polynomial values or the distribution of their valuation
matrices.

## 5. Uniform randomized construction in half-scale time

The high-probability search in (9) can be implemented
without computing any characters or testing any analytic
hypotheses.

* Given \(S,p_0\), sample \(L\) independent uniform primes
  from the explicit list \(S\), using exact capped rejection
  sampling of integer indices (or ordinary rejection with
  expected constant attempts per draw). Compute
  \(r=(p_0^2Y)^{-1}\bmod N\) by integer gcd and modular
  multiplication.
* Enumerate \(r+jN\), \(j\ge0\), through \(B^L\).
  There are at most \(B^J+1\) candidates.
  Trial-divide each by all primes in \(S\); accept one
  precisely if its remaining cofactor is 1 and the number
  of prime occurrences is \(L\). Every operation has a
  verified exact integer specification. Return the
  positive exponent row from \(p_0^2 Y X\), after checking
  the modular congruence.
* If no candidate is accepted, independently resample
  the first-half word. For all sufficiently large inputs
  the success probability is at least \(1/2\), even after
  adaptive choices of \(S,p_0\), by the uniform proof.

Each trial uses a number of bit operations polynomial in
\(B,n\), with absolute constants (the fixed exponent \(J\)
is very conservative). The sampled product has polynomial
bit length, and a successful relation has row entries
between 0 and \(2L+2\). For arbitrarily small inputs one
can dovetail trial division of \(N\) to ensure correctness
and termination without having to compute the analytic
threshold.

### Rank driver

Maintain the exact rational row span of the already found
positive relations. If it is deficient, compute any nonzero
rational annihilator \(w\). One of the sets of nonnegative
or nonpositive coordinates has size at least \(m/2\) and
contains a strict nonzero coordinate: if one sign is absent,
use the other sign including zeros; otherwise choose the
larger of the two sign sets. Use this as \(S\) and a strict
coordinate as \(p_0\). The returned row is nonnegative,
supported entirely on \(S\), and strictly positive at
\(p_0\). Thus its scalar product with \(w\) is nonzero,
so the rank strictly increases. There are at most \(m\)
successful trials/iterations. Exact rational elimination
with integer minor bounds has cost polynomial in \(m,n\).

This also proves that the **complete set** of bounded positive
relations in Theorem 1 has full rational rank, without
an algorithmic or probabilistic qualification: a putative
annihilator is contradicted by choosing its sign subset.

Upon reaching full rank, compute \(E=|\det V|\) as in (1).
Hadamard bounds its bit length by
\(O(m\log(m(2L+2)))\), which is polynomial in \(B,n\).
Every prime of the band is annihilated by \(E\).

### Splitting and complete factorization

The band generates the group \(G\): if it generated a
proper subgroup, a nonprincipal character of the finite
abelian quotient, lifted to \(G\), would be identically
one on the band, contradicting (2). Thus \(E\) annihilates
\(G\). In particular it is divisible by \(p-1\) for every
prime divisor \(p\) of \(N\) (the CRT projection of \(G\)
onto \((\mathbb Z/p\mathbb Z)^\times\) is surjective).

Even inputs and prime powers can be handled by deterministic
elementary arithmetic and polynomial-time primality testing.
Otherwise choose two distinct hidden odd prime factors
\(p,q\), for the proof only. If their two-adic valuations
of \(p-1,q-1\) agree, the nonprincipal product of their
Legendre characters, pulled back to \(G\), has value \(-1\)
at some band prime, by (2). At that base the local orders
have different two-parts. If their two-adic valuations
differ, the nonprincipal Legendre character of the prime
with larger valuation likewise has a nonresidue in the
band, producing different two-parts. The algorithm simply
scans all band primes. Starting with the odd part of \(E\)
and successively squaring, the first level where one local
power becomes 1 and the other does not gives a proper gcd.
Thus this last step is deterministic and has bit cost
polynomial in \(B,n\).

Apply the splitting algorithm recursively to composite
children, testing primes and prime powers as usual.
At most \(O(n)\) nodes are needed, and the uniform expected
cost bound at each node applies conditional on its input.
This gives a uniform Las Vegas complete factorization
algorithm with expected bit cost
\[
 \exp(O(\sqrt{\log N\log\log N}))=L_N[1/2,O(1)] .
\]
This is not a claim of a new best randomized exponent:
the point is the simple, fully specified relation-generation
route, with no additional unproved smoothness assumption,
which can now be targeted for derandomization.

## 6. A nonuniform deterministic half-scale consequence

For fixed bit length \(n\), the prime band, \(L\), and all
word encodings are independent of \(N\). Choose a uniformly
random word from the full band \(\mathcal P\). For any
given surviving \(N,S,p_0\) with \(|S|\ge m/2\), the chance
that every entry is in \(S\) is at least \(2^{-L}\);
conditional on that event, the word is uniform on \(S^L\).
Thus the chance of a successful first-half word is at least
\(2^{-L-1}\) for sufficiently large \(n\).

There are at most \(2^n 2^m m\) triples \((N,S,p_0)\).
A union bound over an independently sampled list of
\[
 T=\left\lceil 2^{L+1}
        (n+m+\lceil\log_2(m+1)\rceil+2)\right\rceil
\]
full-band words shows that some such list simultaneously
contains a good word for every one of these triples.
Indeed the probability of missing any fixed triple is
at most \(\exp(-T2^{-L-1})\), so the total failure
probability is less than one. Because \(L=O(n/b)\),
\(m\le B\), the list length and total advice bit length
are \(\exp(O(b))\).

Given these advice words, enumerate them at every rank
step, skip those not wholly in \(S\), and run the exact
inverse-representative scan. The rank argument now
becomes deterministic with bit cost polynomial in \(B,n\)
and advice length. For full recursive factorization,
advice for all lengths at most \(n\) can be included;
the extra factor \(n\) preserves the half-scale bound.
This proves **nonuniform** deterministic half-scale
factorization, not uniform deterministic factorization.
No procedure for finding this advice in the required
budget has been proved.

## 7. The precise remaining uniform deterministic problem

The field-free version of the outstanding problem is now:

Given \(N\), an arbitrary \(S\) of at least half the
dyadic primes, and \(p_0\in S\), find a length-\(L\) word
of primes in \(S\) whose product \(Y\) has the property
that \((p_0^2Y)^{-1}\) has an \(S\)-smooth integer
representative at most \(N B^J\) (with exactly \(L\)
prime occurrences). The deterministic checking/search
of the second half already costs only half-scale time,
and (9) proves that a fraction \(1-o(1)\) of all first
halves work, uniformly.

The gap is **not a missing smooth-number density
conjecture in this new formulation**. It is an efficient
uniform deterministic dense-search/hitting-set problem.
Enumerating all independent first-half words uses
\(L\log_2|S|=\Theta(n)\) bits, not \(O(b)\).
Likewise, the positive relation itself can be as large
as \(N^2 B^{2J+2}\); enumerating all integers congruent
to 1 through that limit is exponential, not half-scale.
Equation (9) does not assert that a particular fixed
word, a cyclic block of consecutive primes, or a
low-seed family must contain a good word.

A tempting space-bounded PRG shortcut is not justified:
Nisan–Zuckerman's linear-in-space randomness reduction
applies to read-once random coins with bounded working
space. Streaming the product residue needs \(n\) bits
of state in the ordinary implementation. Computing
bits of the product with a smaller workspace by
rereading an entire random word does not satisfy that
read-once hypothesis. No \(O(b)\)-space read-once
implementation or appropriate random-access PRG has
been established. See Nisan and Zuckerman, [Randomness
is Linear in Space](https://doi.org/10.1006/jcss.1996.0004),
and the distinction between read-once and multiple-access
randomness in [On read once vs. multiple access to
randomness in logspace](https://www.sciencedirect.com/science/article/pii/030439759390258U).

It is also possible to pool the original quadratic norm
congruences across parameters, but for a bounded rectangle
of primitive rational ratios \((a+kN)/a\), a common prime
divisor of two distinct numerators must divide \(ak'-a'k\).
Consequently larger primes can again be private. Merely
using gcd-free factor refinement on that rectangle does
not prove coverage or solve the dense-search problem.

## 8. Finite exact verification

The [standard-library verification script](../verification/research/positive_smooth_relations.py)
checks the exact AP scanner and the sign-subset rank driver.
In the finite full-rank fixtures it uses exhaustive product
support tables to speed up the tiny test cases; these
tables are **not** the asymptotic algorithm and have no
claimed half-scale cost. The actual AP scanner is checked
separately, independently of the table.

Exact tested source: Git blob `effb09f6dfa5dc53a9653a73eb3ea468ec32aaa6`,
SHA-256 `c938705bf601f5435e175fac78d5f4948a126e286997881153a46819052870e3`.

Observed output:

    AP scanner: 285 represented residues and 50 absent residues checked
    N 47053 B 200 L 6 rank 21 trials 46 determinant bits 35 factor 211
    N 23707 B 150 L 8 rank 14 trials 25 determinant bits 29 factor 151

Every accepted row is checked by exact modular multiplication
and the strict annihilator scalar product. The determinant
is independently verified by exact Bareiss elimination,
and all band prime orders are checked against the resulting
exponent before the gcd scan. The input factorization is
not used to generate the relations.

The small parameters are examples, not the deliberately
large uniform asymptotic constants. In particular, an
earlier small trial with \(N=47053,B=200,L=4\) failed to
complete rank; the uniform theorem requires the stated
asymptotic choice \(L=k+J\).

**No uniform deterministic general half-scale result has
yet been proved.** The next task is an explicit uniform
hitting-set or deterministic selection algorithm for
Section 7. The original quadratic transverse-unit coverage
remains unproved and is not silently counted as solved.
The one-third program remains deferred.
