# Multiway norm-parity collisions: a distinct-input obstruction

27 November 2026. **Status:** proved unconditional counting theorem for a specified bounded-actual-norm representation architecture, extending [projected norm parity collisions](projected_norm_parity_barrier.md) from matched pairs to all subsets of a quarter-scale pool. It is not a lower bound on factoring, arbitrary modular square certificates, or high-height normalized norm lattices. In particular it isolates repeated representations of the *same* target as a real escape from the distinct-input obstruction, not a sufficient construction. See [normalized norm lattices](normalized_norm_lattice_supply.md), §5, for the exact pooled-target criterion and finite experiment.

## 1. Setup and distribution guards

Put \(L=\log N\), \(\Lambda=L^{1/4}(\log L)^{3/4}\). Fix a finite menu of J tuples of number fields, each of total degree at most D, with specified modular evaluation maps. For a representation of a unit \(v\in(\mathbb Z/N)^\times\) take the **actual resulting** tuple of nonzero elements \(\gamma_a\), with v determined by the tuple and the specified maps. Rational correction elements may be included as degree-one fields. The following hypotheses refer to the unexpanded actual elements, not merely the length of their compact encoding:
\[
 \prod_a N\mathfrak a_a N\mathfrak b_a\le X,\qquad
 \sum_{a,\sigma}|\log|\sigma(\gamma_a)||\le A,\qquad
 (\gamma_a)=\mathfrak a_a/\mathfrak b_a
\]
in reduced integral ideal pairs of the full rings of integers. This is exactly the height budget of the earlier projected parity theorem. A fixed separable rational algebra can also be decomposed into its field components for the counting argument if the public value is a single-valued function of their actual tuple; no evaluation on the maximal order is required. Any additional freely chosen square multiplier not encoded in these data must be counted separately.

For an actual tuple define its rational norm parity vector
\[
 \nu_p(\gamma)=\sum_a v_p(|\operatorname{Norm}\gamma_a|)\bmod2 .
\]
Let \(\mathcal P\) be a fixed set of terminal rational prime labels, chosen before the raw samples under consideration, with \(|\mathcal P|\le \exp(O(\Lambda))\). Include any primes of N whose coordinates are to be discarded; knowing their factors is unnecessary for this proof-only set. Ignoring the sign coordinate only increases the counted events.

Consider K raw unit queries, \(K\le\exp(O(\Lambda))\). For every fixed subset of m distinct query positions assume their ordered public inputs have joint point probabilities bounded by
\[
 G^m/\varphi(N)^m,\qquad \log G=O(L/\Lambda).
 \tag{1}
\]
The representation for each position may be chosen adaptively from the whole transcript, subject to the fixed menu and height budget. The theorem counts **existence** of suitable representations, so it does not require independence of their selection coins.

Examples of (1) include independent uniform ordinary units (G=1), independent uniform squares (\(G=|U/U^2|\) for \(U=(\mathbb Z/N)^\times\)), and independent ordered uniform same-square-coset pairs as in the [affine collision sampler](affine_core_collision_supply.md). A whole such pair has density at most \(|U/U^2|\) relative to two independent uniforms; either coordinate alone is uniform. For odd B-rough N with \(\log B\gg\Lambda\), the bound \(\log|U/U^2|=\omega(N)\log2=O(L/\Lambda)\) holds. It also holds for balanced semiprimes. Fresh square masking of an adaptively selected public square gives a uniform masked square conditionally on the prior public history. Fresh ordinary pairs generated from those masked squares have the same pair law conditionally on the past. Thus a fixed cap of those raw pair attempts satisfies (1), even with stopping and adaptive target selection, by filling out unperformed trials with independent hypothetical draws. This does not cover arbitrary repetitions of a known target, nor reuse of the *same* public mask in multiple positions.

## 2. Counting arbitrary multiway parity cancellation

Fix m distinct inputs. We bound the event that there exist permitted representations for all m positions whose sum of rational norm parities outside \(\mathcal P\) is zero.

Take \(1/2<\sigma<1\). Multiplying the negative \(\sigma\)-th-power norm weights by \(X^{m\sigma}\) upper bounds the count of m-tuples of their ideal pairs. At rational prime p, the numerator and denominator exponents over all m field tuples give at most \(j=2Dm\) independent nonnegative exponent coordinates, with residue degrees at least one. At \(p\notin\mathcal P\) their sum weighted by those residue degrees must be even. Therefore the local contribution is bounded coefficientwise by
\[
 E_j(x)=\sum_{k\ge0,\ k\ {\rm even}}\binom{j+k-1}{k}x^k
       =\tfrac12\big((1-x)^{-j}+(1+x)^{-j}\big),
 \qquad x=p^{-\sigma}.
\]
Indeed each local series \((1-x^f)^{-1}\), f a positive residue degree, is coefficientwise dominated by \((1-x)^{-1}\); retain only even coefficients after multiplying. At p in the terminal set use the unrestricted \((1-x)^{-j}\). This drops principality, coprimality within reduced ideal pairs, and unit guards for an upper bound. It covers even residue degrees and arbitrary ramification.

The previous [field-uniform generator multiplicity bound](projected_norm_parity_barrier.md), §4, bounds the number of actual generator tuples per ideal tuple by
\[
 C(D,A)=\exp(O(D\log(2D(1+A)))) .
\]
For clarity, that proof uses Voutier's published lower bound for non-torsion unit height (Corollary 2, Acta Arithmetica 74 (1996), p.84, [paper](https://arxiv.org/abs/1211.3110)), giving minimum nonzero unit-log vector length \(2/(\sqrt D(\log(3D))^3)\); the number of vectors of norm at most 2A is bounded by volume packing, and the product torsion count by \(\exp(O(D))\). We reuse the previous proved multiplicity lemma, not a regulator or a unit enumeration algorithm. It is uniform over the chosen fields and their degrees. Each actual representation tuple specifies one public unit, so there is no further factor for the number of possible public inputs per tuple.

A new issue for m growing exponentially in \(\Lambda\) is that the small-p estimate from the *two*-tuple theorem cannot simply be used with j=2Dm: the guard \((1-\sigma)\log j\le1\) may fail. Instead split at a sufficiently large
\(Y=\exp(C_Y\Lambda)\), with \(C_Y\) fixed, so that for all \(m\le K\) and \(\sigma\ge3/4\)
\[
 jp^{-\sigma}\le1/2\quad(p>Y),\qquad
 j^2Y^{1-2\sigma}\ll j .
\]
This is possible since \(\log j\le O(\Lambda)\); choose \(C_Y\) larger than twice the corresponding coefficient with a strict margin. For p>Y outside the terminal set Taylor's theorem on \([-x,x]\) gives
\[
 \log E_j(p^{-\sigma})\le E_j(p^{-\sigma})-1
                \ll j^2 p^{-2\sigma}.
\]
Summing even over all integers beyond Y gives \(O(j)\), uniformly in m. For the primes up to Y, and for all terminal primes, drop parity. There is a larger fixed \(B'=\exp(C_B\Lambda)\) such that the number of primes below \(B'\) exceeds \(\pi(Y)+|\mathcal P|\) (ordinary prime number theorem). Since the Euler factor decreases with p, the unrestricted product is bounded by
\[
 Z_{B'}(\sigma)^j,\qquad Z_{B'}(\sigma)=\prod_{p\le B'}(1-p^{-\sigma})^{-1}.
\]
This uses just the cardinality of the terminal set, not a bound on the sizes of its members. Consequently the total local product is at most \(Z_{B'}(\sigma)^{2Dm}\exp(O(Dm))\).

Multiply by \(X^{m\sigma}C(D,A)^m J^m\); the last term accounts for every ordered choice of menu entries. Applying (1) now bounds the desired event probability by
\[
 \boxed{
 \Gamma_m\le\min\left(1,
 \left[\frac{G J C(D,A) X^\sigma}{\varphi(N)}
            Z_{B'}(\sigma)^{2D}\exp(O(D))\right]^m\right).
 }\tag{2}
\]
The constants are uniform over all subsets of the stated size range. This is a true multiway Euler parity bound, not a pairwise-independence or a birthday approximation.

## 3. Asymptotic obstruction at quarter scale

Assume for some fixed \(\varepsilon>0\)
\[
 D\le L^{3/4-\varepsilon},\qquad
 \log X\le L+h,\quad 0\le h=o(L),\qquad
 A\le L^{O(1)},\qquad
 J,K,|\mathcal P|\le\exp(O(\Lambda)).
 \tag{3}
\]
Put \(b=\log B'\), \(u=L/b\),
\(\delta=\log(u/D)/b\), \(\sigma=1-\delta\). Then \(\delta>0\), \(\delta=o(1)\), \(\sigma\ge3/4\) eventually, and \(\log(u/D)\gg_\varepsilon\log L\). The elementary Chebyshev/partial-summation estimate from [projected norm parity](projected_norm_parity_barrier.md), §5, gives
\[
 \log Z_{B'}(1-\delta)\ll
       \log(2b)+(u/D)/\log(u/D).
\]
For completeness, prime powers of order at least two contribute a bounded amount for \(\sigma\ge3/4\). For the first-power sum use the Chebyshev upper prime-count bound and split \(\int_{\log2}^{b}e^{\delta v}\,dv/v\) at \(1/\delta\); the first piece is \(O(\log(2b))\), the second is \(O(e^{\delta b}/(\delta b))\) by substituting \(w=\delta v\). The endpoint term is no larger. No smoothness distribution theorem is needed.

Since \(\varphi(N)\ge N/(\omega(N)+1)\), taking the logarithm per selected position in (2) gives
\[
 \boxed{\log\Gamma_m\le
           m\,[h-(1-o(1))u\log(u/D)].} \tag{4}
\]
The errors are uniform in m: they are bounded per position by
\[
 O(\Lambda+\log G+\log L+D\log(2D(1+A)b)+u/\log(u/D)),
\]
which is \(o(u\log(u/D))\). Here \(\sigma\log X-L\le h-\delta L\).

In particular for \(h=O(\Lambda)\), there is a uniform \(Z\gg_\varepsilon L^{3/4}(\log L)^{1/4}\) such that \(\Gamma_m\le e^{-m Z}\) for **every** \(1\le m\le K\). Sum over subsets:
\[
 \Pr(\text{some nonempty distinct-input parity dependency exists})
 \le\sum_{m=1}^K {K\choose m}e^{-mZ}
 =(1+e^{-Z})^K-1\le 2K e^{-Z}
\]
eventually. This tends to zero much faster than the target inverse quarter-scale cost. It also holds if \(h\le(1-\varepsilon')u\log(u/D)\) for fixed \(\varepsilon'>0\), adjusting Z.

**Consequence.** In this representation architecture, with overwhelming probability **all successful projected parity vectors are independent modulo the fixed terminal set**, when at most one representation from each distinct raw input position may be used. It is not merely the failure of pairwise tag matching. Arbitrary multiway collisions or combining an entire subexponential-sized set of independent determinant-scale targets do not improve the conclusion. Adaptive choices of menu entries, ranks, tags or retained subsets cannot invalidate this existence count. The proof applies to same-coset pair samplers and fresh masked-query streams under the distribution guard (1).

This is not a statement that the observed number of finite prime labels equals their rank. The counting is directly on cancellation of all parities outside \(\mathcal P\), and permits arbitrarily many shared labels and even total exponents.

## 4. Repeated-target multiplicity and the remaining opening

If several representations of the *same* public input are allowed in a dependency, the above argument must not divide by \(\varphi(N)^m\) when only t<m distinct raw inputs occur. Their values provide only t independent input constraints. The same count for a fixed assignment of m representation positions to t distinct input positions instead gives
\[
 \log\Gamma_{m,t}
 \le (m-t)L + m[h-(1-o(1))u\log(u/D)]. \tag{5}
\]
To see this, each permitted tuple of m actual elements specifies at most one ordered tuple of t public input values (and may specify none if a repeated value is inconsistent). Use the same m-tuple ideal parity count, but point probability bound \(G^t/\varphi(N)^t\). Relative to (4) the missing m-t inputs cost at most \((m-t)\log\varphi(N)\le(m-t)L\), with any G factors still bounded by \(G^m\). All errors are uniform for a total cap of \(\exp(O(\Lambda))\) representation occurrences.

A union over assignments of positions and choices of a bounded pool of that size costs at most \(\exp(O(m\Lambda))\), so (5) still excludes nonnegligible success when
\[
 (m-t)L/m+h\le(1-\varepsilon')u\log(u/D)
\]
for fixed \(\varepsilon'>0\). In the determinant-scale case a nonnegligible collision thus needs at least order \(\delta=\log(u/D)/b\) repeated-position fraction, or must violate another height/distribution guard. This is a necessary-condition statement; a relation with many repetitions need not exist.

Repeated-target representations are an important escape because within-target differences are legitimate known-square anchors. The exact criterion in [normalized norm lattices](normalized_norm_lattice_supply.md), (11), separates those differences from useful sealed directions. The new finite experiment pools every guarded representation rather than retaining a single minimum norm, and finds useful directions only on the smallest fixture, not on the three larger tested moduli. Neither the multiway bound nor the experiment proves that repeated-target supply is asymptotically impossible. In particular the normalized norm lattices may have large **undivided** norm budgets and therefore fall outside (3).

Other genuine escapes include much larger actual norm/archimedean heights, total field degree or menu size, explicit square-aware projections that identify rational norms with other actual generator labels, and different correlated input laws that violate (1). When powers of N are stripped from a norm their rational prime support can be included in the terminal set, but the count still charges the original actual norm heights. The height inflation and repeated-target fraction must not be interpreted as computational lower bounds for arbitrary methods. The present theorem does not prove a sub-one-third complexity result.
