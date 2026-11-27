# Two smaller GRH constants for KeyBreak descent

**Status, 27 November 2026.** The first result is a cost-transfer improvement with the original analytic schedule and hypotheses. It is conditional on the correctness of the source's GRH arithmetic and certificate theorems; no new arithmetic conjecture is introduced. The second, slightly better schedule is a conditional changed-range transfer, with explicit margins for independent verification. Neither is an unconditional theorem or a claimed fully independently certified proof.

Source: The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 November 2026, 144 pp., [PDF](https://crypto.sjtu.edu.cn/factoring.pdf), SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9; see the [source audit](keybreak_source_audit.md). References below are to the pinned PDF. This work concerns the conditional G route, not the [proposed unconditional-route compression](keybreak_unconditional_compression.md).

Write \(D=\log N/\log\log N\), \(\lambda=\log\log N\), \(\Lambda=D^{1/3}\lambda\), \(n=\operatorname{bitlength}N\), \(m_b=\operatorname{bitlength}n\), \(t=dm_b\), \(\Lambda_d=(\log 2)t\).

## 1. Recognition slack and the same analytic schedule: 2.96

Proposition H.3 (pp.129–132) uses RH for zeta to show that, uniformly for an unresolved prime \(p\le y\) of a y-smooth input, one curve trial splits the cofactor with probability at least \(\exp(-(1+o(1))\sqrt{\log p\log\log p})\), after removing factors at most \(z_y=2^{k_y}\). All remaining p tend to infinity as y tends to infinity, so this lower bound is uniform. The source chooses \(R_{\rm curve}=2^{\lceil101k_y/100\rceil}L_c\) and concludes a cost constant of 2.01. No analytic step requires this particular slack.

For any fixed rational \(\eta>0\), use instead
\[
 R_{\rm curve}=2^{\lceil(1+\eta)k_y\rceil}L_c.
\]
Eventually each trial has splitting probability at least \(z_y^{-1-\eta/2}\), by the same uniform estimate and \(k_y\log2\sim\sqrt{\log y\log\log y}\). Hence each unresolved node fails with probability at most \(\exp(-z_y^{\eta/2}L_c)\le\exp(-64L_c)\). The original factor-tree union bound, correctness checks and every-tape caps are unchanged. The recognition cost is \(L_y[1/2,2+\eta]\operatorname{poly}(n)L_c\). This is only a transfer of the source's RH recognition theorem and its underlying uniform order-fibre estimate.

Keep G.1–G.2 exactly, including degree \(d\sim(3/4)D^{1/3}\), the original private bands, coefficient law, geometric boxes and cutoff schedule. Proposition G.13 (p.123) derives the actual leading algebraic and rational density losses in \(\Lambda\) units
\[
 s_A=43/40,\qquad s_R=5926/12255.
\]
Use the positive rational slack
\[
 a_A=\left\lceil \frac{10751/10000}{3/4}t\right\rceil,\qquad
 a_{\rm den}=\left\lceil \frac{15587/10000}{3/4}t\right\rceil .
\]
They bound the actual one-point and combined density losses, respectively, since \(10751/10000>s_A\), \(15587/10000>s_A+s_R\). The density margin for the G.6 mean remains positive and exceeds \(\Lambda_d/50\). All original geometric, arithmetic and moment ranges are unchanged. In H.15 and H.30 use the new density exponents; H.32 computes its confidence from the resulting ceilings, so the first-error coupling still holds. Every failed attempt and all public probes are charged.

Take \(\eta=1/10000\). By H.35, the search-count exponent is \(7/5\); the initial shape and algebraic-side cutoff exponents in the recognition scale are
\[
 z_0=\frac{40}{81},\qquad z_1=\frac{40}{81}\frac{51}{430}.
\]
Thus the full list of cost exponents from Table 2 becomes
\[
 \frac{19}{20},\quad
 \frac75+\frac{15587}{10000},\quad
 \frac75+(2+\eta)\sqrt{z_0},\quad
 \frac75+\frac{10751}{10000}+(2+\eta)\sqrt{z_1},
 \quad 2,\quad \frac{49}{20},\quad\frac{57}{20}.
\]
The two radical inequalities with target \(C=74/25=2.96\) are checked by squaring their strictly positive rational margins. All other inequalities are rational. Each exponent is strictly below C. As in H.8–H.9, the ideal success event has uniform positive probability before private-root exposure; all rejection budgets are unchanged; every tape has bounded epoch cost. Summing epochs and the outer verified factor tree gives the new bound
\[
 L_N[1/3,2.96].
\]
The only substantive algorithmic changes are the three finite caps above. In particular this first improvement does **not** substitute a different geometry into the source's fixed-parameter theorem. It is conditional on the exact source's analytic and certificate estimates, under Dirichlet GRH.

## 2. Changed-range schedule: 2.95 candidate

This section goes beyond the first transfer: the appendix G estimates must be applied at the changed scales below. We give their required guard ledger, using the same actual probability spaces, samplers, shape argument, Gaussian covariance, deterministic profile truncation and certificate machinery as in the source. It is not enough merely to assume that Theorem G.1 was stated for arbitrary schedules.

Use the fixed rational parameters
\[
 c=151/200,\quad \kappa=91/100,\quad b=19/20,\quad
 v=501/1000,\quad w=407/500,\quad z=v+w=263/200,
 \quad a=21/5,\quad h=723/200.
\]
The letter a here is the smoothness-argument cap multiplier, not a sampled coordinate. Choose d to be the least odd integer at least 3 satisfying \(d^3m_b\ge c^3 n\), so \(d\sim cD^{1/3}\). Set
\[
 k_0=\lceil\kappa d\rceil,\quad e_B=\lceil (b/c)t\rceil,\quad
 e_0=\lfloor(n-5)/(2k_0)\rfloor-1,
\]
\[
 e_{i+1}=\max(e_B,\lceil(v e_i+w e_B+h t)/a\rceil),
 \qquad V_i=2^{\lceil v e_i+w e_B\rceil},\quad
 T_H=\lfloor hdt\rfloor.
\]
Use all the other definitions G.2–G.5, with these data. Keep the explicit original Gaussian sampler, geometry (including rank sampler), private shape and certificate bounds. Use the generalized H.1 exponent inequality \(T_H+d(v e_0+w e_B)\le(n-1)/2\), with exact integer rounding up for its left side; all field/value sizes remain checked in the actual program.

Write \(H_*=(1+v/\kappa)/c^3\). Then
\[
 \log_2 M=(c^{-3}+o(1))dt,\quad
 \log_2(\sigma M)=(H_*+o(1))dt,\quad
 H_*<h<(a-z)b/c.
\]
The latter inequality puts the unclamped fixed point strictly below eB, so j=O(log D), and \(A=(j+10)^3,\ m=1000A\) still satisfy all subpower moment conditions. The first inequality supplies the reference/height guard G.57. The cutoff implies \(\log(2X_i)/\log Y_{i+1}\le ad\) uniformly, with its strict rounding slack in the height bound.

### 2.1 Geometric and rational-side guards

Use the following fixed limiting ratios relative to \(\log M\):
\[
 R_0=1/(2\kappa),\quad R_1=(v/a)R_0,\quad
 \log V_0/\log M\to vR_0,\quad
 \log V_1/\log M\to vR_1.
\]
They verify \(4V_0<M,\ 4Y_0<3M,\ 4Y_{\min}>3V_0,\ Y_{\min}>Y_1\) eventually because \(v/(2\kappa)<1/2\), \(1/(2\kappa)<1\), and \(127/128>\max(v,v/a)\). At the bottom \(z>1\) gives \(V_i>2B\); \(v>1/2\) gives \(V_i^2\ge Y_i\) even at the top. At a nonclamped step, the margin in \(\log_2(V_i/Y_{i+1})\) is at least \(((a-1)zb/c-h)t/a-O(1)>0\); at a clamped step it is at least \((z-1)e_B-O(1)>0\). Thus the original H.2 inequalities hold. The root-conditioning margin \(\log(\sigma/Y_1^3)\) has positive coefficient \((2v-3v/a)R_0\log M\) and dominates \(20A^2t\). The reference value bound \(T_H+d(v e_0+w e_B)<(n-1)/2\) eventually follows from its limiting ratio \(v/(2\kappa)<1/2\); other height and initialization conditions are unchanged, since all their non-box terms are polynomial in n or \(2^{O(d)}\).

For (G.12) and (G.17), choose the source's \(\epsilon=1/32\). Their limiting power margins in \(\log M\) are
\[
 (1/2-\epsilon)(1+vR_1)-(1+\epsilon)R_1>0,
\]
\[
 (1/2-\epsilon)(1+(v-1)R_0)-(1+\epsilon)R_1>0 .
\]
The internal margin is minimized at the highest internal level; the top aggregate smooth cofactor is at least a constant multiple of \(MV_0/Y_0\). All inverse smooth densities and the cell normalizations are \(\exp(O(\Lambda)+o(\Lambda))\), smaller than these \(\log M\) margins. The individual top-parent calculation still uses no AP estimate modulo that top prime.

The joint-root error (G.15) uses the level-specific rational density bound. Its exponent from \(\rho_i^{-1}\) is at most \((1/(3cb)+o(1))\Lambda+(v/(3bcD^{1/3})+o(D^{-1/3}))\log Y_i\); only the fact that the second coefficient tends to zero matters here. The factor \(Y_i/V_i^2\) has strictly negative fixed slope \(1-2v\) in \(\log Y_i\). Thus its bottom controls the bound. There the margin is at least \((2z-1)b-1/(3cb)>0\). The term \(Y_i/M\) is exponentially small at \(Y_1\). The individual and aggregate top mean-square errors (G.18 and G.15 for the top band sum) have ratios bounded by \(Y_0/V_0^2,\ 1/M,\ Y_1/V_0^2,\ Y_1/M\), all exponentially small on the \(\log M\) scale because \(2v>1\) and \(R_1<R_0\). The polynomial band union remains allowed.

### 2.2 Density and separate-period guards

The worst algebraic smoothness argument is \(ad\). The actual density losses, in \(\Lambda\) units, are bounded by
\[
 s_A=ac/3=1057/1000,\qquad
 s_R=\frac{1/c+vY'_1}{3b},\quad
 Y'_0=1/(2\kappa c),\quad Y'_1=(v/a)Y'_0 ,
\]
where \(Y'_0,Y'_1\) are limiting log-cutoffs in \(D^{2/3}\lambda\) units, not the cutoffs themselves. The worst internal rational height is \(MV_1\), and the top cofactor \(MV_0/p\) is smaller on this scale because all top p exceed \(Y_0^{127/128}\). Set
\[
 s_A^*=10571/10000,\quad s_{\rm den}^*=15371/10000,\qquad
 a_A=\lceil (s_A^*/c)t\rceil,\quad a_{\rm den}=\lceil(s_{\rm den}^*/c)t\rceil .
\]
Both slacks are strict. The new bottom mean satisfies
\[
 ((2z-1)b-s_{\rm den}^*)/c > 1/100 .
\]
Here the source's \(1/50\) mean exponent is no longer available from this ledger. Replace it in (G.6) and Proposition G.10 by \(1/100\). The proof of G.10 uses that fixed positive margin only to dominate the normalized diagonal term \(1/\mu\) and polynomial factors by an exponential decay, so this weakening is sufficient. Top individual and aggregate means have an even larger fixed \(\log M\) geometric margin. All dyadic cofactor/parent ratios and the ratio \(\log Y_i/\log Y_{i+1}\) remain bounded, uniformly in i.

For the Gaussian image and separate-period errors (G.23), (G.38), G.13 pp.123–125, one can retain the original exponents \(1/32\), mesh, tail and angular padding. The actual retained endpoint has log at least
\[
 (18/5)dt + d(v e_i+w e_B)-O(e_i+e_B+d)
\]
in base two, since \(18/5<H_*\); the separate modulus and its angularly enlarged version have log at most
\[
 (7/3)dt + 3(v e_i+w e_B)+O(1)
\]
since \(c^{-3}<7/3\). Consequently the worst normalized GRH error has strict bottom margin
\[
 (15/32)(18/5+zb/c)-(33/32)(7/3)=1099/19328>0
\]
on the \(dt\) scale. Fixed powers of Y, inverse density, the mesh and the truncation parameters are absorbed. This verifies the key error in (G.38) for one or two points, ordinary and semismooth, even after the angle, parent or root divisors. The endpoint term with the extra \(4k\) in (G.32) is smaller: it adds only \(O(e_i+e_B)\) to the period log, versus the endpoint of order \(dt+d(e_i+e_B)\). The moment parameter \(A=D^{o(1)}\), \(\log z_{\rm sieve}=8A\log D\), truncated divisor cutoffs, and single-point saddle shifts satisfy the same asymptotic comparisons as in the source's G.8/G.10; all errors with those parameters are unchanged in order. This paragraph concerns the *separate* periods, not their product, which would lose the required margin.

The previous section's proof of abstract linear bad-child propagation is unaffected by these fixed constants. H.5's bands and its exact shape guards are the same with the new k0. The coefficient of \(\log P_{\rm sh}\) becomes \(2\kappa c/3\) because the shape entropy depends on \(k\sim k_0\). All first-error and pre-extraction conditioning rules in H.8 remain essential.

### 2.3 Cost

Use the original H.3 recognition cap (constant 2.01), the new \(a_A,a_{\rm den}\), and unchanged H.15, H.30–H.32 and H.6–H.7, including their failed-path charges. The search coefficient is \(S=b+2\kappa c/3=42241/30000\), the probe bit-length coefficient is \(2c/3\), and column/retained-occurrence/precision coefficient is b. The leading cost ceilings are therefore
\[
 b,\quad S+s_{\rm den}^*,\quad
 S+(201/100)\sqrt{(2/3)Y'_0},\quad
 S+s_A^*+(201/100)\sqrt{(2/3)Y'_1},\quad
 8c/3,\quad b+2c,\quad 3b .
\]
Each is strictly less than \(59/20=2.95\). In particular the algebraic recognition term is approximately 2.948677, while the raw-search term is approximately 2.945133. These decimals are explanatory; the actual certificate squares positive rational margins against the rational radicands. The proof does not rely on floating-point optimization.

**Conditional changed-range conclusion:** if the source's arithmetic and certificate arguments are transferred with the guards above, the verified program has expected cost \(L_N[1/3,2.95]\) under Dirichlet GRH. The original termination and correctness checks apply unconditionally. The exact numerical schedule and margins are verified separately. Completing the independent analytic range check is required before claiming that this improves the source theorem, rather than its cost model. The same-geometry 2.96 transfer in §1 is preferable as the first rigorous continuation of the source.

No first-parameter improvement below 1/3 is established. Both improvements use fixed constants; they do not address the separate uniform deterministic half-scale search problem.

## 3. Exact finite check receipt

Run [`verification/research/verify_keybreak_grh.py`](../verification/research/verify_keybreak_grh.py) (standard library). Locally executed with Python 3.13.5; its tested Git blob `6cb2c6d8e2543662f6d29b2494f454c4920c1de8` matches the committed source. SHA-256 `596a5e465ea8da00c3679e1cf156bfedf4c48385dbca3ac28d9dc1160f1e6d31`. The two rational/radical ledgers passed, as did 18 symbolic finite bit-length schedules (depth range 111–274). The checks certify the listed numerical inequalities and sampled finite guards, not the analytic transfer, factoring implementation or a Lean theorem.
