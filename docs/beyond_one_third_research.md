# Beyond 1/3: explicit barriers and a different certificate architecture

27 November 2026. **Status:** proved necessary conditions for specified descent architectures, a proved lattice-transform identity, and a new probe-free exact certificate (separate theorem). No first L-parameter below 1/3 is established. The purpose is to make the new mathematical target precise rather than optimize an architecture whose dominant exponents cannot improve.

This follows the [U40 audit](keybreak_u40_critical_audit.md), [U14.2](keybreak_u142_proof.md), and the [rational-fibre support bound](short_ratio_scale_barrier.md). The catalogue-family screening again points to N15 (norms/traces with nonconstant descent data), N23 (descent), N42/O28 (smoothness-free relations), N47/O29 (recursive reductions/large cofactors), O25 (lattice), O27 (resultants and ramification), and O52 (NFS). The separate [sealed polynomial certificate](sealed_polynomial_certificate.md) also uses N11–N12/O34. This is a review at family/interface level, not a new exhaustive audit of the historical 1,514 entries.

Throughout put \(L=\log N\). For a proposed exponent \(0<\alpha<1/3\), write \(T=\exp(L^{\alpha+o(1)})\) for the time/attempt budget. Factors polynomial in L and fixed powers of log L do not affect comparisons of these powers. We distinguish a barrier for a specific uniform random-certificate route from a general algorithm lower bound.

## 1. The private-shape plus rational-cofactor obstruction

Consider balanced semiprimes \(N=p_1p_2\), \(p_i=N^{1/2+o(1)}\). Restrict to the source KeyBreak-style route with the following hypotheses (these include U40 and U14.2):

* A single rational environment has height \(M=N^{1/d+o(1/d)}\), where \(d=L^{\delta+o(1)}\), \(0<\delta<1\). The top cutoff has \(\log Y_0\asymp\log M\), with \(Y_0\le M^{1-\varepsilon}\) for fixed \(\varepsilon>0\). Its top box \(V_0\) satisfies \(Y_0^{1+\varepsilon}\le V_0<M/4\). Broad top bands remain between fixed powers of \(Y_0\). The base has \(\log B=L^{\alpha+o(1)}\).
* Each accepted row starts from a fresh uniform private unit square and a primitive public ratio \(u/v\bmod N\), with \(1\le |u|,|v|\le C\sqrt N\) and both coordinates \(Y_0\)-smooth. This includes the unique shortest-vector shape of source H.5, but we need no prescribed number of factors, squarefreeness, dyadic band count, or distribution of the shortest vector.
* Each nonempty top prime request \(q\) is handled by uniform raw point proposals in the source top box and its special-prime lattice, with rational numerator \(G(P)=\pm q n_s\), \(n_s\) B-smooth, and the same rough denominator condition as in source B.12. Rational environments are fresh from the source law when redrawn. In this hypothesis the individual upper count B.12/B.14 is applicable in the stated changed scales (checked below). Choosing different accepted fields within an environment does not change the rational point supply.
* We count successes through this certificate path, not through an unrelated gcd exit, and charge each actual private or top trial. A fixed positive probability of success under a time cap \(O(T)\) is required. If the route instead gives an expected bound and constant probability of this type of success, Markov truncation gives such a cap with a constant multiplier.

**Claim.** For these hypotheses, the probability of a nontrivial completed public row through this route within T tends to zero when \(\alpha<1/3\).

**Proof, first case.** If \(\delta>\alpha\), the count of potential reduced ratios of the prescribed coordinate size is at most \(4\Psi(C\sqrt N,Y_0)^2\), whether or not they are distinct modulo N. Every unit square of the semiprime has exactly four private unit roots. Uniform private roots thus give success probability at most \(C'\Psi(C\sqrt N,Y_0)^2/N\) per attempt (up to \(1+o(1)\) since \(\phi(N)\sim N\)). Here \(\log Y_0=L^{1-\delta+o(1)}\), and the smoothness parameter is \(u=L^{\delta+o(1)}\). The Rankin argument of [short_ratio_scale_barrier.md](short_ratio_scale_barrier.md), applied to a single coordinate, gives
\[
 \log\big(\Psi(C\sqrt N,Y_0)/(C\sqrt N)\big)
 \le -(1-o(1))u\log u=-L^{\delta+o(1)}.
\]
One may also use the classical Dickman asymptotic in this range. The union over T private draws tends to zero, even if acceptance of a particular shape or its later use is adaptive.

**Proof, second case.** If \(\delta\le\alpha\), a top rational cofactor has size comparable to \(MV_0/q\), so its logarithmic size is \(\asymp\log M=L^{1-\delta+o(1)}\) uniformly over the allowed q. Its B-smooth density on the fixed-ratio numerator interval satisfies
\[
 \rho_q\le\exp(-L^{1-\delta-\alpha+o(1)}).
 \tag{4}
\]
Indeed \(u_q=L^{1-\delta-\alpha+o(1)}\), and the same Rankin estimate bounds the interval from above by the prefix. The corresponding lower bound needed in the environment-failure estimate is \(\rho_q\ge\exp(-O(u_q\log(2u_q)))\), from the direct fixed-ratio smooth interval theorem and the elementary Dickman lower bound. Its negative logarithm is \(o(\log M)\) because \(\log B=L^{\alpha+o(1)}\). The required smooth-number ranges hold: \(u_q\) is a power of L and \(u_q\le\exp(\sqrt{\log B})\) eventually. Since \(V_0\) is a fixed positive power of M, rough-denominator counts with fixed sieve level \(B^s,\ s>2\), have negligible relative error. The source individual top-prime proof B.14 (pp.40–41) counts smooth numerator times rough denominator with multiplicity one after division by q. Its primitive-Q large sieve argument gives, for a single q, relative upper-count failure probability at most
\[
 C\,\frac{\log M\log B}{\rho_q}
       (q/V_0^2+1/M).
\]
Its proof does not depend on the special choice \(V_0=Y_0^6\). Sum over all q≤Y_0 (or over all broad bands), using \(\rho_{\min}^{-1}=\exp(o(\log M))\). Both \(Y_0^2/V_0^2\) and \(Y_0/M\) have fixed negative exponents in \(\log M\) by hypothesis. Thus except with probability \(\exp(-\Omega(\log M))\) an environment supplies the simultaneous upper bound
\[
 |\mathcal A_q(g)|\ll V_0^2\rho_q/(q\log B)
\]
for every admissible top q. The geometric candidate set has size \(\gg V_0^2/q\) (uniform lattice point count since \(V_0/q\to\infty\)); hence even ignoring the algebraic predicate the conditional success probability of a raw rational top proposal is \(O(\rho_q/\log B)\). The simultaneous upper bound justifies this for adaptive q selection. Union over T fresh environments and T top proposals. Since \(1-\delta-\alpha\ge1-2\alpha>\alpha\), both sums tend to zero. A primitive nonzero ratio with both absolute coordinates 1 requires no top prime, but has probability \(O(1/N)\) under uniform private roots; these exceptional shapes cannot supply constant success either.

This completes the proof. The necessary inequalities can be summarized as
\[
 \delta\le\alpha,\qquad 1-\delta-\alpha\le\alpha,
\]
hence \(3\alpha\ge1\). No algebraic covariance issue is needed for this particular obstruction. It is not a lower bound on algorithms using nonuniformly chosen private roots, non-short rational initialization, alternative direct gcd exits, field selection conditioned on rare rational requests, or terminal support obtained without all rational cofactors B-smooth.

## 2. A more general height-ledger obstruction (including higher-degree atoms)

One might try to remove the preceding private-shape restriction by using higher-degree auxiliary polynomials, dynamically changing fields, or forcing many norm factors. The following algebraic inequality shows what must change in the *standard uniform envelope analysis* even if private initialization is solved separately.

Let a nonzero homogeneous integer field form F of degree d have coefficient height H≥1 and a nonzero value \(F(r,Q)\) divisible by N at a primitive rational vector \((r,Q)\), \(M=\max(2,|r|,|Q|)\). Then
\[
 L\le \log(d+1)+\log H+d\log M. \tag{5}
\]
Use auxiliary homogeneous atoms of degree \(1\le m\le d\), in a coefficient box of side cardinality W≥2, with each coefficient of absolute value at most W. The usual rational and algebraic resultant **envelopes** are at least \(W M^m\) and \(H^m W^d\), respectively (the familiar factors \(m+1,d+1\) from evaluation and Hadamard only enlarge these upper bounds). This is a statement about the chosen upper envelopes, **not** a lower bound on each actual atom's norm.

Suppose divisibilities \(A_R,A_A\) are imposed on the two norms, including at least one requested prime \(q\ge B\); suppose their independent combined index permits a full-volume argument of the form
\[
 \log B\le\log(A_RA_A)\le(m+1)\log W .
 \tag{6}
\]
For example, prescribed simple-root congruences modulo distinct prime powers have precisely this index by CRT. The right inequality is the usual population condition for at least constant expected occupancy of a full coefficient box. If the scheme instead uses rare environment-dependent exceptional short points or correlated congruences, (6) must be replaced by its actual occupancy and index calculation. Suppose \(\log(d+1)=L^{o(1)}\) (polynomial degree in L suffices), and both residual envelopes after division by \(A_R,A_A\) have logarithms at most \(L^{2\alpha+o(1)}\). The latter is the standard sufficient smoothness ledger for B-smooth trial density at least \(\exp(-L^{\alpha+o(1)})\).

Adding the two residual logs and using (6) gives
\[
 m(\log M+\log H)+(d-m)\log W\le L^{2\alpha+o(1)} .
 \tag{7}
\]
All terms on the left are nonnegative. If \(d<2m\), this gives \(\log H+d\log M\le 2L^{2\alpha+o(1)}\), contradicting (5). If \(d\ge2m\), it gives \(d\log W\le L^{2\alpha+o(1)}\); (6) yields \(d/(m+1)\le L^{\alpha+o(1)}\). Hence
\[
 d\log M\le (d/m)L^{2\alpha+o(1)}
            \le L^{3\alpha+o(1)},\qquad \log H\le L^{2\alpha+o(1)} .
\]
Again (5) contradicts \(\alpha<1/3\). This is an elementary necessary condition for the specified envelope-and-population ledger with arbitrary m,d, not a theorem asserting that no smaller-than-envelope norms exist. In particular switching to a larger auxiliary degree m does not by itself evade the tradeoff. Extra independent forced factors cannot repair it within the same full-volume model.

For linear atoms \(m=1\), even allowing two highly correlated forced divisibilities does not improve the ledger when \(d\ge3\), if each separate divisibility still has index equal to its divisor. In that case each of \(\log A_R,\log A_A\le2\log W\) and the target needs \(2\log W\ge\log B\). The algebraic residual log is at least \(\log H+(d-2)\log W\) and the rational one at least \(\log M-\log W\); the same argument gives \(\log H,\log M\le L^{2\alpha+o(1)},\,d\le L^{\alpha+o(1)}\). This fails for \(\alpha<1/3\). Thus a genuine escape involving high forced multiplicity must exploit, for instance, **a valuation power much larger than its congruence index** (ramification or an exact content construction), or depart from full-box occupancy.

## 3. Exact target-dependent lattice transformation

Here is a useful exact normalization for analyzing forced content, including ramification amplification.

Let \(A\in M_2(\mathbb Z)\) be nonsingular of determinant \(D\), so it parametrizes a special lattice of primitive or nonprimitive integer vectors. Put \(c_F=\operatorname{content}(F\circ A)\), \(F'=(F\circ A)/c_F\). Assume \(c_F\) is coprime to N; any proper gcd is an immediate factor. Let \(v=(r,Q)^T\) be primitive, \(u=\operatorname{adj}(A)v\), \(g=\gcd(u_1,u_2)>0\) and \(v'=u/g\). Since \(Au=Dv\), \(g\mid D\) and
\[
 F'(v')=\frac{(D/g)^dF(v)}{c_F}. \tag{8}
\]
It is a nonzero integer multiple of N (invert \(c_F\bmod N\)). The primitive linear form obtained by composing the rational linear form with A and removing its content vanishes at \(v'\); its height is exactly \(\max(|v'_1|,|v'_2|)\), because every primitive integer linear form vanishing on a primitive integer vector is its coordinate-rotated vector up to sign. This identity is valid also when the lattice lies in a repeated-root congruence and removes a very high common algebraic content.

Thus after forced factors that are literally polynomial contents have been removed, there is still an interpolation constraint (5) for the *transformed* primitive form and rational vector. Merely declaring a large forced factor without charging the transformed coefficient and rational heights is unsafe. The identity can be used to search for fields/lattices with small simultaneous transformed heights; it does not assert that every forced-divisor condition is polynomial content.

There is an interesting opening here: if **the lattice already imposes the parent request**, a new small coefficient box in lattice coordinates need not have volume at least q. The earlier implication \(d/(m+1)\le L^\alpha\) then disappears. For linear atoms in transformed coordinates with side W≥2, suppose both residual envelopes \(H' W^d\) and \(M'W\) have logarithms at most \(L^{2\alpha+o(1)}\). The interpolation constraint implies
\[
 d\ge L^{1-2\alpha-o(1)},\qquad
 d\le L^{2\alpha+o(1)}
\]
(the second since \(\log W\ge\log2\)). Hence this *weaker transformed-height ledger* only requires \(\alpha\ge1/4\). This is **not an algorithm with exponent 1/4**; it identifies a degree window that the old full-volume ledger excludes. In the range \(1/4<\alpha<1/3\), terminal fields can have degree higher than \(L^\alpha\), and the usual short private-shape initialization cannot use that same degree.

Two problems were previously immediate:
1. The original unconditional KeyBreak square-class probes have bit length \(\exp(\Omega(d\log d))\), impossible for this higher degree.
2. One must construct enough shared, low-height transformed atoms and handle rational parents and algebraic ideal parents without an uncharged switch of fields or uncontrolled repetition of large rational requests.

The first problem now has a proved solution: [exact valuation descent and a probe-free unit certificate](exact_descent_unit_certificate.md). It requires exact rather than parity cancellation, and a uniform support bound on the resulting S-unit rows. It is polynomial in the actual field/row binary data, so large polynomial degrees do not force the old probe exponent. The second remains open. In a random ordinary special lattice, its basis coefficients are often of order \(\sqrt q\), causing transformed norm heights of order \(q^{d/2}\) unless content or special cancellation removes them. We do not assert this heuristic for every lattice; the target is to construct a different, provably favorable distribution or an exact shared marked-field family.

## 4. Next relation-generation problem

The rank budget of the new certificate suggests the following more precise target for \(\alpha<1/3\):

* Initial public rows may use small-degree fields or a different sealed initialization. Exact large good valuations must be canceled, but rational cofactors may spawn rational requests rather than being B-smooth immediately.
* For terminal requests, construct target-dependent small atom lattices or exact norm-controlled marks in shared higher-degree fields. The transformed residual envelope and modular evaluation must be checked using (8), rather than counting a forced factor twice.
* The expected total size of the **remaining support set** in all fields and rational corrections must be \(L_N[\alpha,O(1)]\), and the number of shared fields and rows must allow the certificate's strict rank inequality. Giving every new row a new unrelated field generally increases rank along with the number of rows; it does not prove a dependence.
* A two-sided descent with rational-to-algebraic transitions and back-transitions must control total expected work of all spawned requests, including revisits or upward jumps. The heterogeneous potential in [multilevel descent accounting](multilevel_descent_accounting.md) is the correct starting point; strict shrinkage of each chosen algebraic child alone is insufficient if rational children return to a larger scale.

Existing explicit ramified-target and paired-unit constructions show how to force some exact norms and unit valuations without smoothness, but their unit-rank supply is not yet a shared sealed-row theorem. The new probe-free certificate makes it worthwhile to reconsider them at the higher-degree terminal scale instead of requiring a short Chebotarev probe. The separate sealed polynomial experiment replaces smoothness entirely but currently has no uniform witness-generation bound. These are concrete research directions, not a claim that the relation-supply theorem is already solved.

**Conclusion:** U14.1 is the current written one-third optimization, subject to review. The specified ordinary descent cannot be pushed below 1/3 merely by tuning degree/cutoff/box exponents. The exact S-unit certificate removes one fundamental obstacle to a changed architecture; the next ambitious target is a genuinely new relation-supply mechanism toward exponent 1/4 (or better), not another conditional substitution of parameters.
