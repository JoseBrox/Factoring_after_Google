# Prime-word derandomization: recent results and exact applicability

**Status (26 November 2026).** Literature audit and new conditional
reduction/obstruction lemmas for the uniform half-scale search.
The [positive smooth-relation theorem](positive_smooth_relation_coverage.md)
already proves uniform relation existence and randomized half-scale
construction from the verified Dirichlet zero-free strip. This note
does not prove uniform deterministic half-scale factorization.
The one-third program remains deferred.

Use n=ceil(log_2 N), b=ceil(sqrt(n log_2(n+2))) up to the exact
integer rounding in the previous note, B=2^b, k=floor((n-2)/b),
L=k+J with the fixed J of that note, and
P={p prime: B/2<p<=B}. Given S subset P with |S|>=|P|/2
and p0 in S, the remaining task is to find a length-L word
from S such that the inverse residue of p0^2 times its product
has a length-L S-product representative <=B^L. The exact
AP scanner takes exp(O(b)) bit time, and the proven uniform
success probability for a random first word is 1-o(1).

## 1. The recent literature and why it matters

* OpenAI, [Exact derandomization of logarithmic space:
  L = RL = BPL](https://github.com/openai/math/tree/main/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026),
  23 September 2026. The introduction states the fixed-machine
  acceptance-probability approximation theorem, and the conclusion
  and compiler sections give polynomial running time on padded
  inputs with inverse-polynomial accuracy. The model uses fresh
  independent coins (or a one-way random tape with a cached current
  bit), not arbitrary rereading of a random string. The formalized
  class equality has independent checking evidence including
  comparison of actual definition bodies:
  [verification record](https://mathcommunity.github.io/oai-math-revised/papers/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/);
  [scope](https://github.com/openai/math/blob/main/lean/docs/103.md).
  The explicit compiler's numerical bounds are not a separate
  Comparator target. We use the written probability-approximation
  theorem below, and identify the additional verifier requirement.

* Chen, Doron, Ebtehaj, Tell,
  [Targeted Samplers](https://eccc.weizmann.ac.il/report/2026/345/),
  TR26-345, released 26 November 2026. Directly relevant to
  input-specific dense search. The published abstract states
  conditional constructions under hardness assumptions, including
  quantified derandomization at exponentially small error.
  It does not supply an unconditional polynomial-time hitter
  for our padded verifier. The available abstract was checked;
  the full paper could not be retrieved in the present audit.

* Cheng and Wu, [Weighted pseudorandom generators for read-once
  branching programs via weighted pseudorandom reductions](https://eccc.weizmann.ac.il/report/2025/027/),
  revision 5 (20 October 2026). The unbounded-width result with
  especially short seeds is for permutation ROBPs with a single
  accepting vertex. Our dense inverse-smoothness predicate has
  many accepting final residues, while the exact identity of
  two independent prime products is a single-residue event of
  exponentially small probability in n. Additive-error estimates
  for individual entries cannot simply be summed at the desired
  precision. See Section 3 for a direct obstruction. The more
  general regular-ROBP space bounds still depend on log(width).

* Cheng and Wu, [SC Derandomization for Regular ROBPs and Models
  Beyond BPL](https://arxiv.org/abs/2609.23603), 20 September 2026.
  This is the most useful extension to examine if one-pass
  space compression fails. It handles logarithmic-space machines
  with a two-way random tape visiting each cell at most a fixed
  constant number of times, and logarithmic-space auxiliary
  pushdown machines with a polynomial-size stack and a randomness-
  independent push/pop/idle schedule, with simultaneous polynomial
  time and polylogarithmic space. Ordinary random-access evaluation
  of the arithmetic verifier does not establish either restriction.
  A single auxiliary stack is not a random-access work tape.
  On a padded input, polynomial simulation time is enough for us;
  the deterministic simulation's polylogarithmic space need not
  itself be O(b).

* Krak, [Optimal Hitting Set Generators via a Potential-Descent
  Framework](https://eccc.weizmann.ac.il/report/2026/178/),
  September 2026, and [Beyond Width-3](https://eccc.weizmann.ac.il/report/2026/225/),
  October 2026. These give strong unconditional HSGs for
  read-once CNFs, parity extensions and small-width branching
  programs. We have no reduction of our verifier to those classes.
  Likewise Lee and Viola's [group product generators](https://eccc.weizmann.ac.il/report/2025/071/)
  (July 2026 revision) have group-dependent parameters: results
  for a fixed group or character tests cannot be substituted
  for an arbitrary terminal predicate in a growing group.

The scoped results above are significant; none automatically
gives a uniform deterministic half-scale hitting set for the
current prime-word predicate. The standard hardness-versus-
randomness constructions would give a conditional solution if
they supplied polynomial-time hitting sets for circuits of
the padded verifier's size. That is not our unconditional goal.

## 2. A precise route from the logarithmic-space breakthrough

**Proposition (sufficient verifier).** Suppose there is a uniform
randomized machine which, on the encoded input (N,S,p0,prefix),
uses O(b) counted workspace, runs in exp(O(b)) worst-case time,
and estimates/tests the inverse-smoothness acceptance event
for the uniform completion of the prefix using fresh random
bits. More precisely, it must have the acceptance probability
of the exact predicate under the completion distribution,
or approximate that probability uniformly to o(1/n).
Then the cited logarithmic-space probability-approximation
theorem gives a uniform deterministic L_N[1/2,O(1)]
factorer, with no further relation existence hypothesis.

Proof. Use a fixed-length binary encoding of the prime words:
at each position take h=ceil(log_2 |S|)+ceil(3 log_2(n+2))
bits and reduce the integer index modulo |S|. The distribution
of the index is within |S|/2^h of uniform in total variation.
The joint error in L positions is O(L/(n+2)^3)=o(1).
Every binary string yields a valid word; no exponentially
small acceptance penalty from discarding invalid index blocks.
The total number of bits R=hL is O(n), and the exact predicate
has density 1-o(1) on these strings.

Pad each input including the prescribed prefix to length
M=2^{C b}, with a sufficiently large fixed C. The explicit
S list (even using B bits for membership) fits after increasing
C. Virtual padding can be supplied by scanning a fixed-length
zero extension or computed on request; the padding length
is itself within the budget. The assumed machine is polynomial
time and logarithmic space in M. Apply the fixed-machine
deterministic probability estimator at error 1/M, uniformly
to prefixes of any length. Its time is M^{O(1)}, since the
source machine and resource exponents are fixed. Include
the assumed verifier approximation error if present, and
denote the combined error by delta=o(1/n).

For the empty prefix the true acceptance probability is
1-o(1). At each next bit, estimate the conditional probabilities
of the two child prefixes and retain the child with greater
estimate. The parent probability is the mean of the two
true child probabilities. Hence each greedy step loses at
most 2 delta in true acceptance probability. After R steps
the cumulative loss is o(1); the resulting fully specified
word is accepted by the exact predicate (probability 0 or 1).
Check it with the AP scanner. The R estimations still
take exp(O(b)) time. Applying this uniform procedure to the
existing sign-subset rank driver proves the proposition.

The same reduction would apply to the Cheng–Wu SC result
if the verifier satisfied one of its precise randomized
machine models, with inverse-polynomial accuracy in the
padded input length. Merely asserting that multiplication,
division and smoothness testing can be carried out in
logarithmic space on a read-only input containing the whole
random word does not supply the required model.

### The streaming obstruction to the obvious verifier

Fix N and S in the above range. Among k-symbol prefixes
with distinct primes, in increasing order, there are
binom(|S|,k) distinct integer products. All are <N, so they
are distinct residues modulo N. Appending the same suffix
to each preserves their distinctness since every appended
prime is a unit.

Any deterministic one-pass computation producing the exact
final residue of the word must distinguish all these prefixes
in its state after the k-th symbol. Its state needs at least
\[
 \log_2\binom{|S|}{k}\ge
 k\log_2(|S|/k)=n-O(b)
\]
bits. Here |S|>=B/(8 log B) and
k log_2 n=O(b). Fixed finite control, polynomial-in-padded-
length head positions, and clocks supply only O(b) extra
bits. Thus a one-pass exact residue-computation strategy
cannot have O(b) work bits. Read-many access to a random
word could avoid storing the residue by recomputation,
but the basic L=BPL theorem does not allow that access.
This is a lower bound for the exact-product subroutine,
not for every possible decision procedure for the final
smoothness predicate. In particular it leaves open
compressed probabilistic decision/fingerprinting schemes
that never compute the exact full product.

## 3. Why generic permutation-walk PRGs do not close the gap

There is a simple black-box restriction for this particular
arithmetic walk, independent of general branching-program
lower bounds. Take S=P, with the full prime band.
The proven Fourier moment bound gives
\[
 \sum_{\chi\ne1}|\lambda_\chi|^{2L}
 \le B^4 B^{-2J/100}=o(1).
\]
Thus the full-band product distribution pi is o(1) in
total variation from uniform on G=(Z/NZ)^*. For any proposed
list of K<=exp(O(b)) prime words, let A be their final
residue set. Then
\[
 \pi(A)\le K/|G|+o(1)=o(1).
\]
For example the elementary bound phi(N)>=N/(n+1)
follows by ordering its distinct prime divisors and using
p_j>=j+1 in the Euler product. The complement G\A is a
dense accepting set for precisely the same modular
multiplication walk, but the proposed list misses it.

Consequently no short list of outputs can hit **all**
arbitrary dense terminal predicates on this walk.
This does not rule out a list hitting our special
inverse-smoothness set. It explains why a generic
unbounded-width multi-accept HSG, without exploiting
the terminal predicate, is not a viable target.
This is consistent with the general width lower bound
in [Limitations of the INW generator](https://pmc.ncbi.nlm.nih.gov/articles/PMC11634949/),
Proposition C.2.

The single-accept alternative considers two independently
sampled words and the target congruence of their product.
Its probability is exponentially small, so an additive
error on the order of B^{-C} for a fixed C does not certify
positivity. The explicit one-accept WPRG bounds still have
a log(1/error) term, which is of order n at the requisite
precision. Replacing the whole distribution by one with
small support and demanding L2 closeness is also impossible:
Parseval gives sum_chi |hat sigma(chi)|^2 >= |G|/K for a
probability distribution sigma supported on K residues.

## 4. The 1/3 scale requires an additional change

Use natural logarithms in this section: x=log N and b'=log B.
To keep AP scanning within exp(O(b')), a length-l product
representative must satisfy l b' <= x+O(b'). The number of
possible distinct products from the band is at most
\[
 \binom{m+l-1}{l}
 \le \left(\frac{e(m+l-1)}l\right)^l ,
 \qquad m=|P|\ll B/b'.
\]
At l~x/b' its log is at most
x+O(b')-l log(b'l)+O(l). If l is much smaller than x/b',
the simpler upper bound l b' already gives a large deficit.
Thus, at the one-third scale
b'=Theta(x^{1/3}(log x)^{2/3}), the support is at most
\[
 N\exp(-Omega(x^{2/3}(log x)^{1/3})).
\]
The unit group has size at least N/poly(x). Consequently
the current near-uniform residue mixing approach cannot
work at the one-third scale with the same bounded AP budget.
This is a support/entropy obstruction for the *present
mechanism*, not a general lower bound for factoring or
even for finding structured relations in that sparse support.
The two-sided inverse-symmetry of a sparse distribution
could conceivably be proved by other arguments.
Derandomizing the existing half-scale search alone therefore
does not automatically yield a one-third-scale result.

## 5. Deterministic Miller test: use the verified Dirichlet inputs

The user's observation is correct. Our own
[QRH witness proof](quasi_rh_witnesses.md) gives, for every
nonprincipal character mod q, a prime detecting it of size
O_epsilon((log(q+2))^{8+epsilon}). This implies the same
order of magnitude for generating bases of the unit group:
otherwise a nontrivial character of the quotient by the
subgroup generated by the small primes would vanish as a
detector (be identically one on those generators).

For an odd composite N, put N-1=2^s d with d odd.
If the Fermat-liar subgroup {a in G:a^(N-1)=1} is proper,
some generating base lies outside it, hence is also a
strong Miller witness. If it is all of G, N cannot have
a repeated prime divisor p (the unit group at p^2 has an
element of order p, and p does not divide N-1). For
distinct p,q|N, when the two valuations v_2(p-1),v_2(q-1)
are equal, the product of their quadratic characters is
nonprincipal; a small detecting prime has opposite Euler
signs. When the valuations differ, a small nonresidue at
the prime with larger valuation suffices. In either case,
a unit base has different local two-primary orders.
As these orders divide N-1, its odd-part power and
square chain cannot pass the global strong Miller test:
not all local values begin at one, and their times to
reach one differ. Nonunit tested bases are already
compositeness witnesses. Prime powers also fall in the
first case. Primes always pass the test at unit bases.
This gives the deterministic polynomial-time Miller
bound from the fixed strip, with no new conjecture.
The numerical constant for our QRH derivation would
need to be extracted for a literal explicit cutoff.

More directly, the stronger independently machine-checked
Dirichlet GRH is available, see
[MIT verification report](https://math.mit.edu/~drew/shortgrh/).
Bach's classical [explicit bound](https://doi.org/10.1090/S0025-5718-1990-1023756-8)
gives a Miller witness at most 2(log N)^2 under the
required Dirichlet hypothesis. We may use the integer
cutoff 2n^2 (clipped at N-1) with n the binary length,
handling N=2 and even N separately. This avoids estimating
a transcendental constant and is polynomial-time.
Use a verified source dependency for GRH before claiming
the complete Miller endpoint formally certified in our
project. AKS remains an independent exact fallback.

This simplifies primality checks, including the recursion
and any future generation of prime candidates. It does not
construct the unknown order multiple used in the split
and does not by itself derandomize the prime-word choice.
The current prime band can already be sieved deterministically
within the half-scale budget.

## 6. Research priority

The most promising concrete next goal is to realize the
prefix-conditioned smooth-inverse predicate in the reduced
randomness-access or auxiliary-stack model of Section 2,
or to exploit arithmetic features of its terminal predicate
so as to avoid evaluating the whole residue in one pass.
A general low-space claim about read-only arithmetic is
not sufficient. Targeted samplers are relevant but remain
conditional at the published level reviewed here.
Neither this audit nor the proved conditional reduction
changes the established uniform worst-case factoring
bound. No new Lean milestone is counted.
