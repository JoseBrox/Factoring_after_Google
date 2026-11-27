# Collision bounds for determinant-scale rational and number-field affine cores

27 November 2026. **Status:** proved unconditional counting obstructions for specific representation budgets in the [affine-core collision theorem](affine_core_collision_supply.md). They apply even to an adaptively selected *coarse* tag with a common bounded-rank difference space of actual ideal valuations. They are not lower bounds on factoring, arbitrary modular square certificates, or unbounded-degree/height constructions.

The purpose is to test the actual new positive-mass collision objective, rather than infer usefulness from cancellation of one shared cofactor.

## 1. Fixed field tuple and bounded actual elements

Fix odd N. Fix a finite tuple of number fields \(K_j\), of degrees \(d_j\) with total degree \(D=\sum d_j\), and specified evaluable localized orders. Include the rational field when there are rational correction factors. Use only unit-evaluable nonzero elements, and combine all occurrences in one field into the actual resulting field element. A representation of a residue u is a tuple \(\gamma=(\gamma_j)\) with the verified product of its modular evaluations equal to u.

For its reduced principal fractional ideals in the full rings of integers write
\[
 (\gamma_j)=\mathfrak a_j/\mathfrak b_j,\qquad
 (\mathfrak a_j,\mathfrak b_j)=1 .
\]
Assume the following bounds on the **actual resulting tuples** of a proposed core:
\[
 \prod_j N\mathfrak a_j N\mathfrak b_j\le X,\qquad
 \sum_{j,\sigma}|\log|\sigma(\gamma_j)||\le A .
 \tag{1}
\]
Embeddings count both complex conjugates. These bounds are not upper bounds on the bit length of a compact expression alone; a short expression with enormous powers may fail (1).

Let \({\cal P}\) be any fixed finite set of prime-ideal labels in the tuple, initially allowed to include rational primes and primes of arbitrary sizes. The outside tag of \(\gamma\) is its complete signed valuation vector at the primes outside \({\cal P}\). A tag t specifies two coprime outside ideal parts in each field. Let \(R_t\) be the product of their norms (numerator times denominator, so \(R_t\ge1\)). Its value is determined by the tag.

We require a uniform bound on the number of generators of fixed principal ideals satisfying the archimedean part of (1). The argument of [terminal support, §2](terminal_ideal_reduction_and_support.md) applies to the direct product. For clarity, the only non-elementary height input is Voutier, *An effective lower bound for the height of algebraic numbers*, Acta Arithmetica 74 (1996), 81–95, Corollary 2, p.84, [arXiv:1211.3110, p.4](https://arxiv.org/pdf/1211.3110). Its displayed bound \(\log M(u)>2/(\log(3d_u))^3\) for nontorsion algebraic units of degree \(d_u\ge2\) was rechecked in the PDF page image. Thus nonzero log-unit vectors in the tuple have Euclidean separation at least \(\epsilon=2/(\sqrt D(\log(3D))^3)\): use the sum of positive log coordinates in the actual field, which is at least \(\log M(u)\), and Cauchy–Schwarz. Degree-one units are torsion. In odd fields there are just two torsion choices; in general a field of degree d has at most \(2d^2\) roots of unity by the elementary totient bound.

Choose any one generator tuple in the height-restricted set for a fixed ideal tuple, if one exists. The others differ by a tuple of units with log-vector Euclidean norm at most \(2A\). Packing disjoint radius-\(\epsilon/2\) balls in the log-unit span of dimension at most D gives the uniform multiplicity bound
\[
 C(D,A)= e^{3D}(1+4A/\epsilon)^D .
 \tag{2}
\]
Indeed the torsion product is at most \(\prod_j2d_j^2\le e^{3D}\). This also covers zero unit rank. It is an upper bound on the number of actual elements per fixed ideal tuple, not a unit enumeration algorithm.

## 2. Bound on full outside-tag collision mass

For \(1/2<\sigma<1\) define the finite Euler product
\[
 Z_{\cal P}(\sigma)=\prod_{\mathfrak p\in{\cal P}}
                              (1-N\mathfrak p^{-\sigma})^{-1}.
\]
For a tag t, dropping coprimality of the inside ideal parts, Rankin's inequality bounds their number at remaining norm budget \(X/R_t\) by \((X/R_t)^\sigma Z_{\cal P}(\sigma)^2\). Multiplying by (2), the number of actual tuples with that tag satisfying (1) is at most
\[
 n_t\le C(D,A)(X/R_t)^\sigma Z_{\cal P}(\sigma)^2 .
\]
For \(R_t>X\) it is zero. Every actual tuple gives at most one residue, because its evaluation maps are fixed. The sampler may use arbitrary public random choices depending on u; this does not increase the count of distinct possible residues having a representation with the tag.

Let \(U=(\mathbb Z/N)^\times,\ S=U^2,\ g=[U:S]\). For the raw uniform-unit law, let \(p_t\) be its unconditional probability of returning a core representation with outside tag t. Then \(p_t\le n_t/\varphi(N)\). For uniform pairs in the same square coset as in the affine-core theorem, the outside-tag collision mass obeys
\[
 \Gamma_{\rm out}=\frac1g\sum_{\mathcal D\in U/S}\sum_t
                         p_{\mathcal D,t}^2
             \le g\sum_t p_t^2 .
\]
The inequality follows by expanding the square of a nonnegative sum; it does not assume tag independence across cosets. Now sum over all possible outside ideal parts, dropping their support and coprimality restrictions for the upper bound. The sum of \(R_t^{-2\sigma}\) is at most
\(\prod_j\zeta_{K_j}(2\sigma)^2\le\zeta(2\sigma)^{2D}\).
Here the last inequality follows from the Euler factors: at most \(d_j\) prime ideals over p, each of norm at least p. We obtain the exact upper bound
\[
 \boxed{
 \Gamma_{\rm out}\le
 \min\left(1,\frac{
       g C(D,A)^2 X^{2\sigma} Z_{\cal P}(\sigma)^4
                         \zeta(2\sigma)^{2D}}{\varphi(N)^2}\right).
 }\tag{3}
\]
This bound covers independent raw sampler coins, arbitrary tag-selected success events, and repeated prime powers of N. It is a support/collision statement for the raw sampler law, not for adversarially chosen residue queries.

For the rational-only case this is an immediate upper bound on collisions of primitive short ratios: \(D=1\), \(A\le\log X\), and the outside tag is the signed outside-base rational prime valuations. A ratio with \(x|y|\le X\) after reduction has the required actual norm product, regardless of the signs or of the shape of the lattice enumeration. One can take the rational multiplicity constant 2 instead of (2).

## 3. Extension to coarse tags with low-rank differences

There is a stronger implication that avoids requiring the proposed sampler to use full outside-prime tags explicitly.

Suppose its ordinary-unit core satisfies (1). Suppose that for every pair of core outputs in the *same square coset* and with the same public tag (or any allowed public compatibility relation), their difference of **true finite ideal valuation vectors** lies in one common rational subspace of rank at most r. No restriction is imposed on the rank of the individual affine offsets. The condition also holds if a full real valuation-and-log difference space has rank at most r, by projecting to the integer valuations. For a condition only on active valuations, separately assume a fixed set of at most t0 other terminal prime-ideal labels containing all their possible remaining finite valuations.

Choose a rational basis of the span of the actual active difference vectors **from those difference vectors themselves**. There are at most r. By (1), every such difference has weighted absolute valuation sum
\[
 \sum_{\mathfrak p}|\Delta v_{\mathfrak p}|\log N\mathfrak p
          \le 2\log X .
\]
Hence it has at most \(2\log X/\log2\) nonzero prime coordinates. The union of the supports of the chosen basis vectors, together with the terminal labels if needed, gives one fixed set \({\cal P}\) with
\[
 |{\cal P}|\le t_0+2r\log X/\log2 .
 \tag{4}
\]
Every same-coset compatible core pair has zero valuation difference outside \({\cal P}\), because it belongs to the rational span of that basis. Thus its outside tags relative to this (possibly unknown) set are equal. Consequently the actual affine collision mass of the proposed sampler satisfies (3) for some \({\cal P}\) obeying (4). It is not necessary to compute \({\cal P}\) for the upper bound. This argument also allows composite ideal labels if the stated rank bound is for the true valuation image of those labels.

The Euler product can be bounded uniformly just from its cardinality. If \(|{\cal P}|\le M\), and \(B'\) is such that \(\pi(B')\ge M\), then
\[
 Z_{\cal P}(\sigma)\le
 Z_{B'}(\sigma)^D,\qquad
 Z_{B'}(\sigma)=\prod_{p\le B'}(1-p^{-\sigma})^{-1}.
 \tag{5}
\]
Indeed replace each ideal norm by its underlying rational prime (increasing the corresponding factor); each p appears at most D times. The ordered multiset of at most M primes is dominated term by term, for this decreasing function of p, by taking the smallest M primes with up to D copies. The RHS includes all such copies below \(B'\). No assumption is made that \({\cal P}\) actually consists of small primes.

Equations (3)–(5) are an obstruction to **any** affine-core construction with bounded actual norm and archimedean heights and a common low-dimensional difference space of true ideal valuations. They do not apply to a rank after a norm projection that has discarded relative finite directions unless those discarded directions are also bounded. In particular the [known-square resultant presentation](square_resultant_norm_transport.md) can legitimately discard them when its explicit square correction exists; this is a genuinely different representation interface.

## 4. Quarter-scale asymptotic consequence

Put \(L=\log N,\ \Lambda=L^{1/4}(\log L)^{3/4}\). Suppose the tuple is fixed in advance of the raw unit sample, and the proposed core has the following bounds for some fixed \(\varepsilon>0\):
\[
 D\le L^{3/4-\varepsilon},\qquad
 X\le N\exp(O(\Lambda)),\qquad A\le L^{O(1)},\qquad
 r+t_0\le \exp(O(\Lambda)).
 \tag{6}
\]
Suppose also \(\log g=O(L/\Lambda)\); this holds for balanced semiprimes, and for all inputs with no prime factor \(\le\exp(c\Lambda)\) for fixed c>0. The latter is a legitimate preprocessing guard at the proposed scale, not a hypothesis on the distribution of N. Euler's formula gives \(\varphi(N)\ge N/(\omega(N)+1)\).

Choose \(B'=\exp(C_1\Lambda)\), for a sufficiently large fixed \(C_1>0\) so (4) and the ordinary PNT give \(\pi(B')\ge M\). This choice is for the proof, not for actually finding \({\cal P}\). Set
\[
 b=\log B',\quad u=L/b,\quad
 \delta=\frac{\log(u/D)}{b},\quad \sigma=1-\delta .
\]
Since \(u=L^{3/4+o(1)}\) and \(D\le L^{3/4-\varepsilon}\), eventually \(u/D>2\), \(\delta=o(1)\), and \(\sigma\ge3/4\). The elementary Euler-product bound from [the rational support barrier](short_ratio_scale_barrier.md), applied with \(\exp(\delta b)=u/D\), is
\[
 \log Z_{B'}(1-\delta)
 \ll \log(2b)+\frac{u/D}{\log(u/D)} .
\]
For completeness, expand the logarithm, bound the prime-power terms of order≥2 by a constant using \(\sigma\ge3/4\), then use Chebyshev's bound and partial summation for the first powers. The integral \(\int_{\log2}^{b}e^{\delta v}\,dv/v\) up to \(1/\delta\) is \(O(\log(2b))\); above that point put \(w=\delta v\) and use \(\int_1^{\log(u/D)}e^w\,dw/w\ll(u/D)/\log(u/D)\). This proves the claimed uniform estimate without a smoothness asymptotic.

Taking logarithms in (3) and using (5) yields
\[
 \log\Gamma\le
 -2u\log(u/D)+O\left(\Lambda+\log g+\log L+
      D\log(2D(1+A)b)+\frac{u}{\log(u/D)}\right).
\]
Here \(2\sigma\log X-2L\le-2\delta L+O(\Lambda)\), and \(\log\zeta(2\sigma)\) is bounded. All error terms are \(o(u\log(u/D))\) under (6), because \(\log(u/D)\gg_\varepsilon\log L\). Hence
\[
 \boxed{\Gamma\le\exp(-(2-o(1))u\log(u/D))
            =\exp(-L^{3/4+o(1)}) .}\tag{7}
\]
The equality on the right describes the scale of the displayed upper bound. This is much smaller than the \(\exp(-O(\Lambda))\) mass needed by the affine-core supply theorem. It rules out a fixed shared family with total degree about \(L^{1/2}\), determinant-scale aggregate norm and polynomial actual archimedean log height, if its successful correlations are claimed to have a common subexponential-rank difference space in the **unprojected** ideal valuations. The obstruction is stronger than the failure of matching complete large-prime tags.

There is a harmless menu extension. If every representation can choose from J possible fixed tuples with their specified maps, each satisfying (6), and their tag coordinate group is identified in advance, the same proof adds at most \(2\log J\) to the upper bound. For each tag the number of represented residues is at most the sum of the tuple counts, and Cauchy–Schwarz bounds the sum of their squared counts by J times the sum over tuples. Apply (3) to each tuple (with its induced \({\cal P}\)); the count includes all such possibilities, so selection can depend on u. This still gives (7) for \(J=\exp(O(\Lambda))\). A field constructed freely after viewing each u, with a much larger menu, need not satisfy this bound. Nor does counting a huge collection of shared fields with unbounded total degree fall under (6).

## 5. Implication for the research route

The [affine-core collision theorem](affine_core_collision_supply.md) gives exact uniform anchor generation from a low-rank difference core, but (7) prohibits trying to prove its hypotheses using only a determinant-scale collection of small actual field elements and ordinary true-valuation rank savings. This remains true for clever coarse tags as long as every accepted compatible difference lies in a fixed small rational span. It does **not** prohibit any of:

- square-aware norm projection with explicitly known square corrections, where the full ideal valuation space can be large while its actual public-generator binary presentation is small;
- compact products with aggregate actual norm height or archimedean log height beyond (6), provided their generation and use are charged;
- a large shared family with total degree near or above \(L^{3/4}\), or sufficiently many independent selectable field parts;
- structured public input laws not arising from uniform ordinary-unit queries;
- different relation-generation or factoring mechanisms.

These are real changes of hypotheses, not a counterexample to the finite norm, ramification or masking theorems. In particular the new conic law provides additional public information that the ordinary-unit collision bound does not count; a purported use of that information still needs its own positive-mass rank theorem. The most attractive remaining interface is [square-resultant norm transport](square_resultant_norm_transport.md) with many correlated residual factors and **actual** known-square corrections, possibly combined with [correlated conic sampling](conic_masked_incidence_supply.md). No quarter-scale arithmetic core or new factoring exponent is established.
