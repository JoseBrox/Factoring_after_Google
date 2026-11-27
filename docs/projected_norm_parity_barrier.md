# Rational norm parity collision bound and restrictions on paired marks

27 November 2026. **Status:** new unconditional counting bounds extending the earlier [true-valuation affine collision obstruction](affine_tag_height_barrier.md) to *rational norm squareclasses*. These results test the square-aware projected-core route, including cancellation of even prime exponents and cancellation of distinct prime ideals over the same rational prime. They are not lower bounds on factoring or on arbitrary algorithms for modular square roots. The [paired norm construction](paired_norm_affine_lift.md) supplies a positive exact transport mechanism outside some of these hypotheses, but its remaining arithmetic core is open.

## 1. Setup: actual height, not syntactic expression length

Fix odd composite N and put \(L=\log N\). An ordinary unit representation is a tuple of actual nonzero elements \(\gamma_j\) in fixed number fields \(K_j\), with specified localized-order evaluations whose product is the public unit u. Include rational factors as a degree-one field. Let \(D=\sum_j [K_j:\mathbb Q]\), and require unit-evaluable elements only. Write their reduced principal fractional ideals as
\[
 (\gamma_j)=\mathfrak a_j/\mathfrak b_j,\qquad
 (\mathfrak a_j,\mathfrak b_j)=1 .
\]
Assume the following bounds on the **actual resulting tuples** of the core:
\[
 \prod_j N\mathfrak a_j N\mathfrak b_j\le X,\qquad
 \sum_{j,\sigma}|\log|\sigma(\gamma_j)||\le A .
 \tag{1}
\]
Embeddings count both members of conjugate complex pairs. Compact exponent descriptions are allowed, but do not imply (1).

Define the projected rational norm parity vector, in a fixed direct sum over rational primes, by
\[
 \nu_p(\gamma)=\sum_j v_p(|\operatorname{Norm}_{K_j/\mathbb Q}(\gamma_j)|)\bmod2 .
\]
It is the prime-valuation parity of the product of rational norms. Any signed rational correction in the representation can be included as a degree-one component. The sign axis can be charged separately; dropping the sign restriction for an upper bound is harmless. Here we retain **only** the rational norm projection, not the individual prime-ideal valuations. Even completely different distributions of prime ideals over a rational p can have the same projected parity. We are deliberately allowing that cancellation.

For each ordered pair of core representations counted as compatible, suppose their projected parity difference lies in a fixed binary span of dimension at most r. For example, in the [binary square-aware generator presentation](square_resultant_norm_transport.md), this hypothesis follows from a common low-dimensional difference space when the rational norm parity block is retained as a separate projection. It also follows if rational squares have been discarded from that block. It need not follow from a quotient that identifies arbitrary unmatched cofactor residues with norm factors; such identifications may erase the rational norm coordinates. We do not assume it follows merely from the small dimension of the quotient of actual units by modular squares.

As in the [affine-core collision theorem](affine_core_collision_supply.md), draw u uniformly in \(U=(\mathbb Z/N)^\times\), s uniformly in \(S=U^2\), independently, and take \(v=us\). Each representation sampler receives only its own public input and independent public coins (the upper bound below allows even correlations between the coins). Write \(g_0=[U:S]\). The probability of a particular ordered pair of units in the same square coset is \(g_0/\varphi(N)^2\), and pairs from different cosets have probability zero. Denote the probability of a compatible core pair by \(\Gamma\).

## 2. Parity support of the compatible differences

For a single actual tuple satisfying (1), every rational prime in the support of \(\nu\) contributes at least \(\log 2\) to its total absolute weighted ideal valuations. For a difference of two tuples, the number of rational-prime coordinates is at most \(2\log X/\log2\). Choose a binary basis for the common span **from the actual compatible differences**. Its union of supports is a finite rational-prime set \({\cal P}\), with
\[
 |{\cal P}|\le 2r\log X/\log2 .
 \tag{2}
\]
Every compatible pair has equal projected rational norm parities outside \({\cal P}\). If some other terminal rational-prime coordinates were omitted from the rank bound but are known to lie in a fixed set of size \(t_0\), adjoin that set and use \(t_0+2r\log X/\log2\) instead. This basis choice is only for the proof, and does not require the algorithm to know the primes.

The point is that even the low rank of a coarse tag's projected differences imposes a support restriction, despite arbitrary cancellations over p in the underlying ideal vectors.

## 3. Exact parity-constrained Euler product

We first count possible pairs of ideal tuples; this is an **upper bound**, dropping principality, coprimality within reduced ideal pairs, the modular unit guard and the sign restriction. Take \(1/2<\sigma<1\). The weight of an ideal tuple is the negative \(\sigma\)-th power of its norm product in (1). For a pair of tuples with both norm products ≤X, multiplying this weight by \(X^{2\sigma}\) gives a number at least one.

For a rational prime p, write \(x=p^{-\sigma}\). In the pair of tuples, each prime ideal over p contributes two arbitrary nonnegative exponents from the numerator and denominator ideals of each tuple. There are at most \(4D\) such exponents in total, each contributing \(x^{f e}\) for its residue degree \(f\ge1\). At p outside \({\cal P}\), equality of the two projected norm parities is exactly the constraint that the sum of *all* these weighted exponents is even. The signs in the original valuation difference do not matter modulo two.

Define
\[
 E_j(x)=\sum_{\ell\ {\rm even}}\binom{j+\ell-1}{\ell}x^\ell
       =\frac{(1-x)^{-j}+(1+x)^{-j}}2 .
\]
The local parity-restricted Euler sum is bounded coefficientwise by \(E_{4D}(x)\). Indeed each series \((1-x^f)^{-1}\) is coefficientwise dominated by \((1-x)^{-1}\); multiply the nonnegative series and retain just the even coefficients. This covers even residue degrees (which impose no additional individual parity constraint) and arbitrary ramification. At primes in \({\cal P}\) use the unrestricted \((1-x)^{-4D}\). Thus the number of compatible ideal-tuple pairs is at most
\[
 X^{2\sigma} Z_{\cal P}(\sigma)^{4D}
             \prod_{p\notin{\cal P}}E_{4D}(p^{-\sigma}),
 \qquad Z_{\cal P}(\sigma)=\prod_{p\in{\cal P}}(1-p^{-\sigma})^{-1}.
 \tag{3}
\]
This is a different Euler product from the earlier exact outside-ideal tag bound: even-total norm exponents are allowed, not just identical prime-ideal exponents. In particular it would be incorrect to simply reuse \(\zeta(2\sigma)^{2D}\) for this new constraint.

### Uniform bound on the new Euler product

Assume \(\sigma\ge3/4\) and \((1-\sigma)\log(2D)\le1\). Put \(j=4D\). We claim
\[
 \log\prod_p E_j(p^{-\sigma})=O(D\log(2D)).
 \tag{4}
\]
To prove it set \(Y=(2j)^{1/\sigma}\); then \(Y=O(j)\), since \((1-\sigma)\log(2j)=O(1)\). For \(p\le Y\), use \(E_j(x)\le(1-x)^{-j}\), and \(-\log(1-x)=O(x)\) uniformly since \(x\le2^{-3/4}\). Summing even over all integers up to Y costs \(O(j\log(2j))\), since \(p^{1-\sigma}\le Y^{1-\sigma}=O(1)\). For \(p>Y\), \(jx<1/2\). Taylor's theorem on \([-x,x]\) for \(f(t)=(1-t)^{-j}\) gives
\[
 0\le E_j(x)-1
      \le \tfrac12 j(j+1)x^2(1-x)^{-j-2}
      \ll j^2x^2.
\]
Thus the remaining log sum is
\[
 O(j^2\sum_{n>Y}n^{-2\sigma})
       =O(j^2 Y^{1-2\sigma})=O(j^{1/\sigma})=O(j).
\]
This proves (4). It also explains why treating large p parity cancellation as cost-free still leaves a small-prime smoothness penalty.

## 4. Counting actual generator tuples

Use the log-unit separation and packing argument from [the previous support theorem](terminal_ideal_reduction_and_support.md). For completeness the published input is Voutier, *An effective lower bound for the height of algebraic numbers*, Acta Arithmetica 74 (1996), 81–95, Corollary 2, p.84, [arXiv:1211.3110](https://arxiv.org/pdf/1211.3110), page 4 of the author's PDF; checked again against the actual page image. It gives \(\log M(\epsilon)>2/(\log(3d_\epsilon))^3\) for a nontorsion algebraic unit of degree \(d_\epsilon\ge2\). The log vector of a non-torsion unit in one of the fields has Euclidean norm at least \(2/(\sqrt D(\log(3D))^3)\): its positive log-coordinate sum over the actual field's embeddings is at least its logarithmic Mahler measure, and Cauchy–Schwarz bounds this sum by \(\sqrt D\) times the norm. The same separation holds for the product unit lattice (a nonzero vector has a nonzero component).

For any fixed principal ideal tuple, choose one height-restricted generator tuple if there is one. All other such generators differ by tuples of units with log-vector norms at most \(2A\). Packing in the log-unit span of dimension at most D, and bounding torsion by \(\prod_j2d_j^2\le e^{3D}\), gives at most
\[
 C(D,A)=e^{3D}\left(1+2A\sqrt D(\log(3D))^3\right)^D
\]
generator tuples for each ideal tuple. This is a count, not a unit enumeration algorithm. In degree one the statement holds directly. Each actual representation tuple yields one public residue since the evaluation maps are fixed. Multiply (3) by \(C(D,A)^2\) and divide by the number \(\varphi(N)^2/g_0\) of possible ordered same-square-coset residue pairs. Under the assumptions of §1 we obtain
\[
 \boxed{
 \Gamma\le\min\left(1,
 \frac{g_0 C(D,A)^2 X^{2\sigma} Z_{\cal P}(\sigma)^{4D}
           \exp(O(D\log(2D)))}{\varphi(N)^2}\right)
 }\tag{5}
\]
whenever the guard of (4) holds. The proof does not assume a distribution of local splitting types, smooth ideals, the absolute norm parities, or the public tags.

There is a finite menu variant: if the sampler chooses among J predeclared field tuples and evaluation maps (each of total degree ≤D), sum over the ordered pairs of choices, giving a factor at most \(J^2\). At each p the two tuples together still have at most \(4D\) ideal-exponent coordinates, and the same two independent generator multiplicity bounds hold. The rational-prime parity support in (2) is common to the whole menu. The count includes all such choices even if the sampler selects the tuple after seeing the public input. An arbitrarily large family constructed from the input does not satisfy this menu assumption.

**Scope of explicit square corrections.** If the representation u is specified as the evaluation of the actual fixed tuple and the projected rational norm parity is used after a known-square resultant correction, the counting argument applies: the correction does not change the uniquely determined u of that tuple. But an independent arbitrary square multiplier depending on u, not counted among the actual representation data of (1), can give many u per tuple and is outside this argument. Similarly an arbitrary binary relation among actual modular generators may identify an unmatched cofactor value with a rational prime product; then the low-rank projection hypothesis must be checked, not assumed. Equation (5) is a bound for the stated norm-parity projection, not for all possible square-aware samplers.

## 5. Quarter-scale consequence and necessary norm inflation

Let \(\Lambda=L^{1/4}(\log L)^{3/4}\) and suppose for fixed \(\varepsilon>0\) that
\[
 D\le L^{3/4-\varepsilon},\quad
 \log X\le L+h,\quad 0\le h=o(L),\quad A\le L^{O(1)},\quad
 r+t_0,\ J\le\exp(O(\Lambda)).
 \tag{6}
\]
Assume also \(\log g_0=O(L/\Lambda)\), for instance for balanced semiprimes or after removal of all prime factors up to \(\exp(c\Lambda)\) for fixed c>0. The latter is a legitimate quarter-scale preprocessing guard. The elementary bound \(\varphi(N)\ge N/(\omega(N)+1)\) follows from ordering its distinct prime divisors \(p_i\ge i+1\).

By (2), a fixed \(B'=\exp(C_1\Lambda)\) for sufficiently large C_1 has at least \(|{\cal P}|\) rational primes below it (ordinary prime number theorem). Because the Euler factor decreases with p,
\(Z_{\cal P}(\sigma)\le Z_{B'}(\sigma)\).
Put \(b=\log B'\), \(u_0=L/b\),
\[
 \delta=\frac{\log(u_0/D)}{b},\qquad \sigma=1-\delta .
\]
Then \(\log(u_0/D)\gg_\varepsilon\log L,\ \delta=o(1)\), and \(\delta\log(2D)=o(1)\); the guard for (4) is satisfied eventually. Chebyshev and partial summation, as in the earlier rational Rankin bound, give
\[
 \log Z_{B'}(1-\delta)
 \ll \log(2b)+\frac{u_0/D}{\log(u_0/D)}.
\]
For an explicit justification, the prime-power terms of order≥2 contribute a bounded amount for \(\sigma\ge3/4\). For the first-power sum use the upper bound \(\pi(y)\ll y/\log y\) and split the integral \(\int_{\log2}^b e^{\delta v}\,dv/v\) at \(1/\delta\). Below the split it is \(O(\log(2b))\); above it substitute \(w=\delta v\) and bound the result by \(O(e^{\delta b}/(\delta b))\). The endpoint term is no larger. No smoothness distribution result is needed.

Taking logarithms in (5), using the menu factor if present, now gives
\[
 \boxed{
 \log\Gamma\le 2h-(2-o(1))u_0\log(u_0/D) .
 }\tag{7}
\]
Indeed \(2\sigma\log X-2L\le2h-2u_0\log(u_0/D)\). All other logarithmic terms are
\[
 O\left(\Lambda+\log g_0+\log L+D\log(2D(1+A)b)
                              +u_0/\log(u_0/D)\right)
       =o(u_0\log(u_0/D)).
\]
In particular for \(h=O(\Lambda)\), the collision mass is at most
\(\exp(-L^{3/4+o(1)})\), far smaller than the \(\exp(-O(\Lambda))\) required by the [affine-core theorem](affine_core_collision_supply.md). More generally positive collision mass at that scale within this architecture requires actual additional norm height
\[
 h\ge (1-o(1))u_0\log(u_0/D)
          =\Omega_\varepsilon(L^{3/4}(\log L)^{1/4}) .
 \tag{8}
\]
This is a *necessary height inflation* in the specified representation family. The new parity cancellation, though exact, does not remove that requirement. It extends the earlier obstruction for exact ideal-valuations to the remaining natural norm-squareclass projection under the same degree/height guards. It is not a sufficient condition for supply when the height is inflated. The paired norm sampler in the companion note uses much larger actual norm envelopes and does not claim the determinant-scale hypothesis (6).

## 6. A separate obstruction to matching whole cofactor values of small marks

The [mark-local construction](paired_norm_affine_lift.md), §1, permits pairing at particular marks instead of forcing the entire modular cofactor to be a square. Matching just the two **scalar** cofactor resultant values is weaker than equality of full polynomial remainders. There is nevertheless a useful elementary bound for this particular strategy with small marks.

Take a balanced squarefree semiprime \(N=p_1p_2\). Let t be a public residue sampled with point probabilities at most \(C_0/N\); this includes uniform t. It also includes the public companion z of the unit-guarded [conic law](conic_masked_incidence_supply.md) with fixed unit parameters: there are at most four possible hidden h for any fixed z by the two finite-field quadratic root bounds, and the full conic has \(\asymp N\) points, with only \(O(p_1+p_2)\) excluded by the unit guard. Thus its marginal law has the stated bound with fixed \(C_0\). No independence between t and the chosen marks or polynomials is required.

Let \({\cal M}\) be any fixed finite menu of nonzero integer polynomials of degree at most m and coefficient sup norm at most H_P. Consider arbitrary monic f_i (chosen after viewing t), each with modular root t and monic quotient \(g_i\). For a mark \(P_i\in{\cal M}\), suppose its norm \(n_i=\operatorname{Res}(f_i,P_i)\) is a nonzero integer of absolute value at most H_n, and all values and norms are units modulo N. Then its complete cofactor value is \(b_i=\operatorname{Res}(g_i,P_i)\equiv n_i/P_i(t)\bmod N\).

If \(b_1=b_2\) modulo N, necessarily
\[
 n_1 P_2(t)-n_2 P_1(t)\equiv0\bmod N .
\]
Exclude the trivial integer-polynomial identity \(n_1P_2=n_2P_1\). If \(2H_nH_P<\min(p_1,p_2)\), the remaining polynomial is nonzero modulo both primes and has at most \(m^2\) roots modulo N. There are at most \(|{\cal M}|^2(2H_n+1)^2\) choices of the two marks and norm values. A union bound gives
\[
 \Pr(\text{a nontrivial whole-cofactor equality exists})
 \le \min\left(1,\frac{C_0m^2|{\cal M}|^2(2H_n+1)^2}{N}\right).
 \tag{10}
\]
The same proof covers equality up to sign. If instead \(b_1b_2=1\), use \(n_1n_2-P_1P_2\); the root bound is \((2m)^2\) and the coefficient guard becomes \(H_n^2+(m+1)H_P^2<\min(p_1,p_2)\). These statements also allow any fixed small menu of known rational scalars, by counting their choices and coefficient heights in the same way. They do not assert that modular equality up to an arbitrarily large, adaptively generated square correction is impossible.

For bounded-degree marks with \(\log H_P,\log H_n=O(L^{1/2}(\log L)^{1/2})\), the entire allowed mark menu has \(\exp(o(L))\) elements, so (10) is exponentially small. More generally the same holds if \((m+1)\log(2H_P+1)+\log(2H_n+1)+\log(2m)=o(L)\). Thus naively pairing whole scalar cofactor values of short low-degree marks is also insufficient for uniform square/conic targets, even if the field is allowed to be selected after viewing t. The guard intentionally excludes high-degree coefficient menus with entropy comparable to L, arbitrary factors of cofactors paired only partially, and compact products with enormous norm heights. Those remain outside this counting obstruction.

The integer-polynomial identity excluded in (10) just supplies a rational proportionality of the two marks and their norms, already present in their expressions; it is not evidence that new random target information was obtained by pairing. Neither (10) nor (5) prohibits the explicit paired construction with large marks in the companion note.

## 7. Exact checks and next interface

The [standalone regression script](../verification/research/verify_projected_norm_supply.py) independently enumerates the weighted local Euler coefficients for 160 random small residue-degree lists (1,760 coefficients), and checks 60 exact rational instances of the even-energy generating function and its Taylor majorant. It also checks the actual paired norm identities and rational squareclass ranks of the new constructive sampler. The asymptotic arguments (4)–(8) are written proofs, not extrapolations from those experiments. See [the full execution receipt](paired_norm_affine_lift.md#5-what-these-constructions-do-and-do-not-supply).

**Research decision.** The previous affine-core hypothesis cannot be attained just by projecting bounded actual norm tuples to rational squareclasses at the same determinant-scale height; a genuinely larger height/field-family budget or a different public generator mechanism is needed. The positive exact paired lift supplies such larger-height representations and even a fixed norm offset, but its finite batches show no significant rank compression. The next viable interface is to exploit additional structure of its remaining fixed-algebra norm values (for example via compact high-height norm equations or decomposition into genuinely smaller norm terms), not to assert that discarding even valuations makes arbitrary short representations dense. No quarter-scale bound is proved.


## 8. Multiway extension

The [multiway parity theorem](multiway_norm_parity_barrier.md) extends the even Euler product bound to any subset of an \(\exp(O(\Lambda_{1/4}))\)-sized distinct-input pool, uniformly in its subset size. Split the local parity energy at a larger quarter-scale prime bound, rather than incorrectly applying the fixed-two-tuple small-p estimate at an exponentially growing number of coordinates. Under the same bounded actual norm, degree and height assumptions and the stated input-density guard, all successful projected rows are independent modulo a fixed small terminal set with overwhelming probability. The extension separately accounts for repeated representations of one input: the probability count loses one input denominator per repetition. The [normalized norm lattice experiment](normalized_norm_lattice_supply.md) pursues that legitimate escape, outside the bounded undivided norm regime in general, but does not establish a positive-mass core.
