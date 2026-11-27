# Correlated ideal reduction and modular-image transport

27 November 2026. **Status:** new unconditional finite algebraic transition and exact residual-rank criterion. It applies to verified correlated incidence blocks; no uniform supply theorem or sub-one-third factoring bound is asserted. The constructive shared-subfield source of such blocks is developed in [the companion note](shared_base_norm_transport.md).

This continues [terminal ideal reduction](terminal_ideal_reduction_and_support.md), [exact valuation descent and the probe-free certificate](exact_descent_unit_certificate.md), and the [adaptive residual-span program](adaptive_rank_or_residual.md). The key point is to account for the algebraic ideal and the newly introduced modular image as one coupled coordinate, not as two independently evolving residual directions.

## 1. Exact input interface

Let \(N\) be odd, with perfect powers and primes already handled. All modular computations described below are public. Use finitely many explicit odd-degree fields \(K_a\), with evaluable localized orders and homomorphisms \(\psi_a\) to \(\mathbb Z/N\). All field elements in the row identities are invertible in their respective localizations. Rational factors are likewise units modulo N. The algorithm checks gcds and every modular identity; a proper gcd terminates successfully.

For each field fix a terminal set \(S_a\) of prime ideals in its full ring of integers. It need not be explicitly factored; a known cardinality bound suffices for the certificate. Similarly fix a set \(S_0\) of terminal rational prime labels. In the following exact finite interface, active ideal labels are supplied nonzero integral invertible ideals of the explicit orders, with their extensions to the full ring having disjoint nonempty prime supports outside \(S_a\). The active rational labels are distinct rational primes outside \(S_0\). The most immediate case is ordinary good prime-ideal labels from verified norm factor lists. More general disjoint invertible blocks may be handled by the same calculation. We do not assume one can factor a large defining discriminant or find a maximal order.

Combine the active rational and field labels into a free integer coordinate group \(P=\mathbb Z^m\). A public row is a compact identity
\[
 s_i=r_i\prod_a\psi_a(\gamma_{ai})\pmod N.
 \tag{1}
\]
Its active incidence vector \(v_i\in P\) records the signed rational exponents and the signed active ideal exponents of every field product. All remaining rational/ideal valuations are terminal. The factor lists or the exact ideal identities supporting these statements are part of the input. When \(s_i=h_i^2\) for independent sealed private roots, the construction of the row and its acceptance may use only the public square \(s_i\) and independent public data.

We also admit **unsealed anchors**: compact verified identities of the same form with left side 1, with active vectors \(c_j\). Write \(V=(v_i)\) and \(C=(c_j)\) as matrices of columns. An anchor may use any of the public field/rational elements and terminal labels; it is not an assumption of a new multiplicative relation among secret roots. For example, KeyBreak's internal rational/algebraic correction is the exact public identity
\[
 1=(Q/G(P))\,\psi_a(a-b\theta_a)\pmod N
\]
with its signed rational and ideal incidence. Such an identity is an admissible anchor if its full active and terminal valuation data are supplied. See the pinned source E.6, [source audit](keybreak_source_audit.md), and [U40](keybreak_u40_proof.md), §6. All previously uncharged large rational cofactors must be included among the active labels.

## 2. Coupled local reduction

For each active ideal label \(\mathfrak p_j\), choose a *single* nonzero integral reduction element \(\alpha_j\) with
\[
 (\alpha_j)=\mathfrak p_j\mathfrak b_j,\qquad
 t_j=\psi_{a(j)}(\alpha_j)\in(\mathbb Z/N)^\times .
 \tag{2}
\]
Here \(\mathfrak b_j\) is integral and invertible. For totally real explicit orders the [exact trace-Gram LLL reduction](terminal_ideal_reduction_and_support.md), §1, gives
\[
 \operatorname{Norm}\mathfrak b_j
 \le 2^{d(d-1)/4}d^{-d/2}\sqrt{|\operatorname{disc} A|}.
 \tag{3}
\]
We use the same \(\alpha_j\) every time the label occurs, with the signed multiplicity of that occurrence. The norm bound is not necessary for the rank argument; it provides an independent height control on the local move. The modular-unit guard is checked, and a failure may terminate or reject the block. The equality of ideals in (2) is verified in the explicit order. The extension to the maximal order preserves the equality.

For a rational label \(p_j\), put \(t_j=p_j\bmod N\), with no corresponding residual ideal. Write
\[
 \beta_{ai}=\gamma_{ai}\prod_{j:a(j)=a}\alpha_j^{-v_{ji}} .
\]
Then every row becomes
\[
 s_i=t^{v_i}\,r_{i,0}\prod_a\psi_a(\beta_{ai}),
 \qquad t^u:=\prod_j t_j^{u_j},
 \tag{4}
\]
where \(r_{i,0}\) has only terminal rational support. At every nonterminal prime ideal, the signed ideal valuations of \(\beta_{ai}\) are **exactly**
\[
 -\sum_{j:a(j)=a}v_{ji}\,v_{\mathfrak q}(\mathfrak b_j).
 \tag{5}
\]
The same calculation applies to an anchor column \(c_j\). Thus the nonterminal residual ideal block is \(-Bv_i\), for one fixed linear map B, with one column for each reduction label. There is no independence hypothesis and no need to factor any \(\mathfrak b_j\) to establish (5).

This already gives the exact graph identity
\[
 \operatorname{rank}_{\mathbb Q}
 \begin{pmatrix} V\\-BV\end{pmatrix}
 =\operatorname{rank}_{\mathbb Q}V .
 \tag{6}
\]
The reduced ideal factors and their modular-image labels must not be charged as two independent ranks. Equation (6) does not by itself save rank relative to V: a novel modular image can be completely unconstrained. The next step uses actual unsealed correlations.

## 3. Odd-pivot elimination of correlated labels

Select a submatrix of anchors \(C_*\) with \(h\) columns and a set of \(h\) active coordinates on which its square pivot matrix has odd determinant. Put \(D=|\det(\text{pivot})|\), an odd positive integer. The integer adjugate formula gives for every input column
\[
 Dv_i=w_i+C_*\lambda_i,\qquad
 \lambda_i\in\mathbb Z^h,
\]
where the pivot coordinates of \(w_i\) are zero. Apply (4) to the anchors. Since their left sides are 1, substituting their identities eliminates \(t^{C_*\lambda_i}\) in the row for \(s_i^D\). Equivalently raise the row to D and multiply by the inverse of the anchor products with signed exponents \(\lambda_i\). All arithmetic is on compact exponent vectors. After this substitution the nonterminal residual ideal valuations are exactly \(-Bw_i\), not \(-BDv_i\) plus an unrelated anchor residual.

Define \(W=\operatorname{span}_{\mathbb Q}\{v_i\}\), \(U=\operatorname{span}_{\mathbb Q} C_*\). Since the projection has kernel U, the coupled rank after the transition is
\[
 \boxed{
 \operatorname{rank}_{\mathbb Q}\binom{(w_i)}{-B(w_i)}
 =\dim W-\dim(W\cap U).
 }\tag{7}
\]
This is a strict, quantified residual-rank saving whenever the supplied anchor span intersects the actual incidence span nontrivially. In particular it is not enough that the ambient label universe shrinks; the intersection in (7) must be measured on the actual rows.

If the initial roots \(h_i\) were sealed, raising all rows to the same odd D does not lose their independent private sign fibres. The later extraction can use \(h_i^D\). The exponent transformation and all acceptance decisions remain public. Even pivot determinants cannot be used in this simple way: raising every square to an even power destroys the private sign randomness.

## 4. General parity-aware elimination, including even Smith factors

We can avoid discarding nonprimitive anchor directions. Let \(k\) be the number of sealed rows and \(h=\operatorname{rank}_{\mathbb Q} C\). Put
\[
 r=\operatorname{rank}_{\mathbb Q}[\,V\ C\,]-h,\qquad
 e=h-\operatorname{rank}_{\mathbb F_2}(C\bmod 2).
 \tag{8}
\]
The rational space of sealed coefficients for which the active incidence can be canceled by anchor coefficients is
\[
 W_0=\{x\in\mathbb Q^k:Vx\in\operatorname{im}_{\mathbb Q}C\},
 \qquad \dim W_0=k-r.
\]
It is important that \(r\) is a quotient rank, not the rank of the full augmented matrix. The integral joint active kernel is
\[
 L=\{(x,y)\in\mathbb Z^{k+\ell}:Vx+Cy=0\}.
\]
It is saturated in \(\mathbb Z^{k+\ell}\). Its projection \(P_x\) onto the sealed integer coefficients is the kernel on \(W_0\cap\mathbb Z^k\) of the homomorphism
\[
 x\longmapsto Vx\quad\text{in}\quad
 G=\big(\operatorname{im}_{\mathbb Q}C\cap\mathbb Z^m\big)/
                         \operatorname{im}_{\mathbb Z} C .
\]
By Smith normal form, G is finite with h nonzero invariant factors, of which exactly e are even. The image H of this homomorphism is a subgroup of G. Its 2-primary part requires at most e generators, since this is true of every subgroup of the 2-primary part of a finite abelian group. Consequently
\[
 \dim_{\mathbb F_2}(P_x\bmod2)\ge k-r-e.
 \tag{9}
\]
Indeed \(W_0\cap\mathbb Z^k\) is saturated, has rank \(k-r\), and its quotient by \(P_x\) is H. Reducing the exact sequence modulo 2 gives the bound on the image (not an assertion that the integral projection is saturated).

This loss is computable more precisely by actual Smith/Hermite elimination. For example \(V=(1), C=(2)\) has quotient rank zero but requires even sealed coefficients: ignoring e would produce a false factor-success assertion. The simple odd-pivot argument of §3 is an alternative that avoids this obstruction by construction.

On L, every temporary image label introduced in (4) cancels *as an actual multiplicative element*. The entire nonterminal residual ideal block in (5) cancels at the same time. It follows that the combined field products now have support only in the **original terminal sets** \(S_a\); there is no need to enlarge those sets to the union of the \(\mathfrak b_j\) supports. Even factoring the individual reduced norms is unnecessary for this cancellation. This statement remains true if some temporary residual primes coincide with an old active label. It is the exact joint incidence \(Vx+Cy=0\) that enforces cancellation.

Let
\[
 T_{\rm fin}=|S_0|+\sum_a |S_a|,\qquad
 T_{\rm log}=\sum_a (r_1(K_a)+r_2(K_a)-1).
\]
Known upper bounds may replace these cardinalities. On the active kernel impose zero terminal rational/ideal valuations and then zero unit-log vectors. The first is a rational linear constraint of codimension at most \(T_{\rm fin}\). The second is a rational constraint of codimension at most \(T_{\rm log}\), by the discrete product unit lattice and the exact reconstruction in [the probe-free certificate](exact_descent_unit_certificate.md). It is only after the finite valuations vanish that we use unit-log rational reconstruction. Refined valuation matrices for these compact products can be computed on explicit integral atoms via Ge's ideal-refinement theorem; no expanded enormous powers are required. The same applies to the rational gcd-free basis. Let \(L'\subset L\) be the resulting saturated sublattice.

If a saturated sublattice has codimension t in a free lattice, its inclusion modulo 2 is injective and its image has codimension t. Therefore restricting the sealed projection from L to \(L'\) decreases its mod-2 image dimension by at most \(T_{\rm fin}+T_{\rm log}\). Impose one more binary equation for the combined torsion sign. Odd-degree fields have only the roots of unity \(\pm1\), and the signs of compact products are computed at chosen real embeddings, as in the earlier certificate. We obtain the sufficient condition
\[
 \boxed{k-r-e>T_{\rm fin}+T_{\rm log}+1.}\tag{10}
\]
Under (10), there is an exactly computable vector \((x,y)\) with at least one odd sealed coefficient \(x_i\), whose combined public rational and field product is 1. Hence \(\prod_i s_i^{x_i}=1\bmod N\). Verify this congruence and the odd coefficient before first private exposure.

For independent uniform sealed private roots, conditional on their public squares and on the whole public transcript, \(X=\prod_i h_i^{x_i}\) is uniform in the unit roots of 1, because some \(x_i\) is odd. The gcd of \(X-1\) and N is proper with probability \(1-2^{1-\omega(N)}\ge1/2\) when N has at least two distinct prime divisors. No independence of the *active incidences* is needed.

All integer kernel, intersection, Smith and Hermite computations are polynomial bit time in the actual compact row/anchor input. For polynomial bit bounds on Smith/Hermite multipliers use Kannan–Bachem, *Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix*, SIAM J. Comput. 8 (1979), 499–507, [DOI](https://doi.org/10.1137/0208040). The exact remaining finite and logarithmic rank computations are the imported Ge and unit-lattice reconstruction of the earlier certificate. One can avoid even the pessimistic bound (10) in an actual computation: compute a saturated basis of \(L'\), reduce its sealed-coordinate projection modulo two, and impose the sign equation directly. These steps decide whether this particular certificate has an odd sealed coefficient.

## 5. Adaptive batch progress with new labels

Let \(E=\operatorname{im}_{\mathbb Q}C\) be the old anchor space in the old active vector space \(P_{\mathbb Q}\). Quotient out E, so the current target space is \(U=(W+E)/E\), of dimension r. A new anchor batch may contain previously unseen labels. Split its projected column matrix into old and new coordinates, \(A_o,A_n\), in \((P_{\mathbb Q}/E)\oplus P_{\rm new}\). A linear combination of the new anchors eliminates all genuinely new directions exactly when its coefficients lie in \(\ker A_n\). The extra anchor space available in the old quotient is
\[
 H_o=A_o(\ker A_n).
\]
This proves the exact progress equation
\[
 \boxed{r_{\rm after}=r_{\rm before}
                  -\dim(U\cap H_o).}\tag{11}
\]
Here the same old target rows are being compared before and after the batch. If new sealed rows are added, their new target directions must be counted separately. The formula is a rational-rank assertion; §4 accounts for the associated integer/2-primary obstruction.

In particular, when the old projections lie in U, strict progress occurs whenever
\[
 \operatorname{rank}\binom{A_o}{A_n}>\operatorname{rank} A_n.
\]
This tests a whole correlated batch even when **none** of its individual residuals lies in the old support. It is not necessary to recognize individual smooth cofactors. It gives a precise adaptive objective for two-sided descent: generate a batch with a nontrivial old-target component after taking the kernel of the new-label block, and control the even Smith obstruction. This can be tested using exact incidence data and factor-free refinement.

A useful invariant for screening a proposed construction is that adding a known anchor to a target row cannot improve (11): it does not change that row's class modulo the anchor span. In particular, expanding an already-known internal modular identity into many more syntactic requests, and then canceling them, is not new progress. There must be a strict saving on the *preexisting* target quotient, or a separately proved reduction in its future relation supply cost. This is why merely stripping all previously used internal descent identities does not solve factoring.

## 6. Consequences and precise boundary

The new mechanism simultaneously controls modular image introduction and ideal reduction: (5) couples their residuals, (7) proves strict rank savings on correlated blocks, (9)–(10) preserve the odd-coefficient readout even with even anchor invariant factors, and (11) gives exact adaptive progress accounting. Unlike a norm-only reduction, no unknown modular port is silently removed.

The [shared-subfield construction](shared_base_norm_transport.md) supplies a particular family of genuine joint transitions without requiring the base ideal to be principal or the separate reduction images to coincide. It gives exact rank savings for full-extension packets and a norm-projected version for partial packets. Their usefulness for a complete algorithm depends on the incidence of such correlated requests among the accepted rows.

The U40 common-determinant covariance estimates and upper moments were for a different ordinary/semismooth descent law. They do not prove an anchor intersection of the necessary size in this new two-sided scheme. In particular the existence of enough new anchors at quarter-scale cost is not established by linear algebra, LLL or Smith saturation. No replacement first L-parameter or improvement of the previous U14.1 written bound follows. The next priority is a generation theorem for the genuinely new old-target component in (11), with the terminal support and parity budget in (10), rather than a bound on the norm of each image separately.


## 7. Exact binary quotient and a parity-progress target

The rational rank in (11) is useful but need not track the actual odd-coefficient gain: an even Smith factor can obstruct an otherwise nonzero rational dependency. There is a simpler exact invariant for the adaptive driver.

For fixed sealed columns V and current unsealed anchors C, use the integer sublattices
\[
 A_0=V\mathbb Z^k,\qquad E=C\mathbb Z^\ell,\qquad
 Q_2=(A_0+E)/(2A_0+E).
\]
The latter is an elementary abelian 2-group: every element is represented by a sealed combination and twice that combination belongs to the denominator. The map
\[
 \mathbb F_2^k\longrightarrow Q_2,\qquad b\longmapsto Vb
\]
is surjective. A binary vector b is the parity of some integral joint active-kernel vector exactly when
\[
 Vb\in 2A_0+E . \tag{12}
\]
Indeed an integer lift has the form \(b+2z\); asking that its active vector be canceled by integer anchor coefficients is exactly (12). This gives the exact active parity capacity
\[
 \boxed{\mathcal B=\dim_{\mathbb F_2}\ker(\mathbb F_2^k\to Q_2)
              =k-\dim_{\mathbb F_2}Q_2.}\tag{13}
\]
It equals the mod-two rank of the sealed-coordinate projection of a saturated integer basis of \(\ker_{\mathbb Z}[V\ C]\). In particular \(\mathcal B\ge k-r-e\) by (9), but it can be strictly larger. It can be computed without enumerating binary vectors: form the two indicated integer column lattices by Hermite normal form, use the coordinate inclusion matrix and Smith normal form, or compute the joint kernel directly. All matrix multipliers have polynomial bit bounds as in §4.

For an incoming anchor batch, split its active columns into the old and genuinely new coordinates \(A_o,A_n\), now **over the integers**, without taking a rational quotient first. Form
\[
 H=A_o(\ker_{\mathbb Z} A_n)\subseteq P.
\]
Use a saturated integer basis of the kernel, not arbitrary cleared rational basis columns. The exact new projection lattice of feasible sealed coefficients is \(\{x:Vx\in E+H\}\). Hence the new quotient in (13) is
\((A_0+E+H)/(2A_0+E+H)\). There is a surjection from the old quotient to this quotient whose kernel is precisely the image of
\[
 H\cap(A_0+E)\quad\text{modulo }2A_0+E.
\]
To see this, intersect the new denominator with the old numerator and use \(2A_0+E\subseteq A_0+E\). Therefore the necessary and sufficient condition for strict **parity** progress is
\[
 \boxed{H\cap(A_0+E)\not\subseteq 2A_0+E.}\tag{14}
\]
Both membership and intersection are exact integer-lattice calculations. This handles new residual labels that disappear only in a batch combination, and handles a rational-rank plateau during which an even invariant factor is repaired. In particular an anchor whose old projection belongs to \(2A_0+E\) cannot by itself contribute a new odd direction. Conversely a batch that does not change the rational quotient rank can still be useful if it changes its integral parity obstruction. The capacity is monotone when adding anchors (including extension by new labels with zeros in old columns), because every earlier feasible lift remains feasible.

For a concrete adaptive prescription, choose an old binary vector b not in the kernel of (12). An unsealed batch whose integer-canceled old projection contains \(Vb\) modulo \(2A_0+E\) makes that missing parity available. This is a more precise target than forcing one individually smooth cofactor, or even forcing a rational residual-span dependency. The shared-base packet reductions supply candidate correlated blocks for this purpose; their actual projected images must still be checked in (14).

**Conditional quarter-scale reduction.** Write \(\Lambda=L^{1/4}(\log L)^{3/4}\), \(L=\log N\). Suppose a public initialization produces \(k=\exp(O(\Lambda))\) independently sealed rows, with compatible shared fields and a fixed terminal/logarithmic rank bound \(T\le k-2\), in \(\exp(O(\Lambda))\) expected bit work. Suppose further that, at every reached public state with \(\mathcal B\le T+1\), one can generate a capped verified anchor batch in \(\exp(O(\Lambda))\) bit work that either factors N or satisfies (14), with conditional probability at least \(\exp(-O(\Lambda))\), uniformly in the history. New labels may be introduced; each successful batch has at most its charged bit size, and the bound T on remaining terminal and logarithmic rank must be maintained. All tests are public, including failures and rejection. Then retaining only strict-progress batches gives the desired certificate in \(\exp(O(\Lambda))\) expected work: at most k strict gains are needed, each conditional waiting time is geometric with the stated lower bound, and the total successful data and all polynomial exact operations still cost \(\exp(O(\Lambda))\). Once \(\mathcal B>T+1\), the saturated terminal/log kernel and one sign constraint leave an odd sealed coefficient, by the proof of §4 with \(\mathcal B\) in place of its lower bound. The private-root split succeeds with probability at least one half. Fresh epochs and the usual verified factor tree preserve the scale; a capped epoch plus persistent trial-divisor backup gives every-tape termination if desired.

This is an exact conditional reduction, **not** a proof of either of its relation-generation hypotheses. It isolates the outstanding arithmetic statement as a uniform probability of (14) for a prescribed actual missing parity, with a common rank budget, rather than a uniform smoothness assertion for every isolated request. A theorem about unconditioned average rank gains that fails on adaptively selected histories would not suffice.


## 8. Exact finite verification

Run [verify_joint_ideal_transport.py](../verification/research/verify_joint_ideal_transport.py) and [verify_parity_quotient.py](../verification/research/verify_parity_quotient.py) with Python 3.13.5 and SymPy 1.14.0. The first executed 250 joint Smith/parity blocks, 184 odd-pivot eliminations, 94 instances of the sufficient parity bound after additional constraints, and 85 strict novelty-batch rank gains, as well as the actual ideal reductions reported in [shared-base transport](shared_base_norm_transport.md), §7. The second executed 200 integer anchor batches, 8,976 exhaustive binary membership comparisons, 68 strict parity gains (including 18 at unchanged rational quotient rank), and an explicit even-factor repair. The tested script blobs match their committed versions: respectively `581804e86f20a64e842d335f029781ff0eefadd4` (SHA-256 `094c64c4af84b2b015725f7580079d3a8e32109f9db05c5fa7f5febf85c9c414`) and `b0471f221ee85915843742bc31a2597f2f531765` (SHA-256 `ac3715e5c4de54c91971c1fe394096e2d8f6f8eb65ca1ed7bd96261f84e8edad`). The binary membership comparisons use independent HNF lattice membership versus saturated Smith kernels; the new-label calculation compares full augmented systems against integer cancellation before projection. These tests are finite regression checks, not a supply theorem. No full repository, PDF or Lean build was performed.


## 9. Subsequent uniform-supply reduction

The [known-square anchor theorem](uniform_masked_anchor_supply.md) permits anchors whose evaluations have explicitly known square roots, rather than only 1. Its lattice coverage and uniform masking theorem gives strict gains in (14) from a positive-mass bounded-novelty representation core, so a separate adaptive per-history gain estimate is no longer necessary under that core hypothesis. The [affine-core collision reduction](affine_core_collision_supply.md) needs only common low-rank **differences** of ordinary-unit representations with matched tags in the same square coset; their absolute offsets may have high rank. Its exact mass is the mean squared conditional tag mass. This is a new conditional uniform-supply theorem, not an unconditional quarter-scale arithmetic supply result.

The [square-resultant presentation](square_resultant_norm_transport.md) gives a binary analogue of (14) using actual public generators and known square corrections. Unlike bare ideal valuation parity, it does not require integer saturation or a relative unit-log budget for terms whose cofactor discrepancy cancels. The [conic refresh theorem](conic_masked_incidence_supply.md) extends uniform masking to correlated public companions. The [new collision barrier](affine_tag_height_barrier.md) proves that a determinant-scale bounded-actual-height fixed field tuple cannot realize the unprojected low-rank affine-core hypothesis at quarter scale with total degree below \(L^{3/4-\varepsilon}\). Thus the remaining promising interface is the explicit square-aware projection or a genuinely larger height/field-family budget. No smaller general factoring exponent is established.
