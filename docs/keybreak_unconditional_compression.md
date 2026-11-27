# Compressing KeyBreak's unconditional descent: a 40-constant target

**Later proof checkpoint:** [U100](keybreak_u100_proof.md) and [U40](keybreak_u40_proof.md) provide the written changed-range ordinary and semismooth proofs and the linear exceptional-mass transfer. The conditional formulation below is retained as the historical development. The new written proof uses the pinned source's finite lemmas and classical unconditional analytic inputs; no independent record certification or full Lean proof is claimed.

**Status, 27 November 2026:** a written extension of the unconditional source proof, with a precise conditional \(L_N[1/3,40]\) transfer. The new small-value large-sieve lemma, deterministic-profile truncation lemma, polynomial-pool lemma and exact cost margins are proved below. The extension of the source's full local-density/covariance calculation is given explicitly as a transfer argument, not yet independently certified line by line or in Lean. In particular do **not** promote 40 into an unconditional record pending that audit. No GRH or new conjectural smoothness assertion is used in the proposed U schedule. The first L-parameter remains 1/3.

Source throughout: The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 Nov. 2026, [PDF](https://crypto.sjtu.edu.cn/factoring.pdf), 144 pp., SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9. Equation and lemma numbers refer to that version; see [source audit](keybreak_source_audit.md). Its unconditional constant is \(10^{13}\), not 1013. This note uses its unconditional box law and common-determinant proof, its GRH section's *finite* (nonanalytic) incidence-truncation and broad-band shape ideas, and the project's earlier [descent accounting](multilevel_descent_accounting.md). It does not import the conditional GRH progression estimate into U.

## 1. A stronger large-conductor bound

Write \(S_x(\theta)=\sum_{n\le x,\,P^+(n)\le y} a_n e(n\theta)\), where the single coefficient sequence satisfies \(|a_n|\le1\), and \(\rho=\Psi(x,y)/x\). Assume \(y\in[(\log x)^{21},x^{1/100}]\), \(\rho=x^{-o(1)}\), and the saddle \(\beta(x,y)=1-o(1)\), uniformly in the parameters considered. These are precisely the elementary smoothness ranges below.

Let \(\Theta\) be any finite \(1/x\)-separated set in \(\mathbb R/\mathbb Z\). For \(p=12/5\), Harper, *Minor arcs, mean values, and restriction theory for exponential sums over smooth numbers*, Compos. Math. 152 (2016), Proposition 2, (4.1), [DOI](https://doi.org/10.1112/S0010437X15007782), [accepted manuscript, p.23](https://wrap.warwick.ac.uk/id/eprint/107457/), gives by layer cake
\[
\sum_{\theta:\ |S_x(\theta)|/\Psi>x^{-1/1000}}
       |S_x(\theta)/\Psi|^p\ll (\log x)^4
\]
eventually: use \(\epsilon=1/100\), \(1-\beta\le1/100\); the distribution exponent is at most 2.21, strictly less than 2.4. This is the same large-value input used in source C.11.

**New handling of small values.** There is no need to bound the number of fractions by \(x^{1/1000}\). The classical additive large sieve gives
\[
\sum_{\theta\in\Theta}|S_x(\theta)|^2
  \ll (x+x)\sum_{n\le x}|a_n|^2 1_{P^+(n)\le y}
  \ll x\Psi(x,y).
\]
Consequently the small values have total normalized p-energy at most
\[
 x^{-(p-2)/1000}\frac{O(x)}{\Psi(x,y)}
     =x^{-1/2500+o(1)}=o(1).
\]
Together the two bounds prove the same normalized p-energy estimate as C.11 for *all* separated sets, without its much stronger small-value guard.

For reduced fractions of denominators \(R<r\le2R\), it suffices that \(4R^2\le x\), or simply \(4K_{\max}^2\le x\) for the full conductor ceiling. There are \(O(R^2)\) fractions. Primitive Gauss sums and orthogonality give
\[
\sum_{R<r\le2R}\frac1{\varphi(r)}
 \sum_{\chi\bmod r}^{*}\left|\frac{S_x(\chi)}{\Psi(x,y)}\right|^2
 \ll R^{-1}(R^2)^{1-2/p}(\log x)^{8/p}
 \ll R^{-2/3}(\log x)^4.
\]
Here \(S_x(\chi)\) denotes the same weighted smooth prefix sum twisted by \(\chi\). The stars restrict to primitive characters. The proof uses the *same* coefficients for every frequency; we have not taken maxima inside Harper's theorem.

The random-sign dyadic-block argument in C.11 then applies unchanged to the supremum of prefixes in a deterministic endpoint range, costing a further \((\log x_+)^3\). Thus (C.52) holds with the separation guard \(4K_{\max}^2\le x_-\), rather than \(8R^2\le x^{1/1000}\). This improvement is unconditional. The small-value estimate is a standard large-sieve argument, not a novelty claim about large-sieve theory.

For the rational side in an **internal** region \(V=Y^6\), take the local predetermined lower endpoint \(x_-=M/(64Y^7)\) (not \(M/(64Y_0^7)\)); \(x_+=2MV\) and \(K_{\max}=4Y^{12}\). The product of content and induction divisors is at most the modulus, at most \(4Y^{12}\); the original numerator endpoints are of order \(MV\). Even after an endpoint halving the stated local \(x_-\) is conservative. The separation condition therefore follows from \(31\log Y<(1-o(1))\log M\). There is no such C.11 estimate needed in the top box, where the proof uses the upper pair moment rather than concentration.

## 2. Extend the unconditional residual estimate to semismooth bands

This is the principal transfer to audit. Retain the source's raw box law (B.4)–(B.6), one- and two-value comparison laws B.3–B.4, and common rational environment event B.1, with the modified fixed parameters of §5 below. At an internal parent box take any child query \(q,t\) with \(B<q\le y=Y_{i+1}\) and use the same rationally eligible point set as for an ordinary root query. It is important that this is the larger **parent** box, not the child's later smaller box.

Let \(J=(P,2P]\cap\mathbb P\), with \(y\le P\), \(2P\le Y\), and delete fixed primes dividing N as in the source. Fix positive deterministic weights of bounded within-band ratio, normalize their maximum to one, and put
\[
f_J(n)=\sum_{\ell\in J}w_\ell 1_{\{0<|n|\in\ell S_y\}} .
\]
The support sets are disjoint, so \(0\le f_J\le1\). This is B.38, not a product of two independent prime counts. Use the same fixed one-value proxy as C.2, with \(f_J\) replacing the ordinary smooth indicator in its conditional expectation on the odd grid cell and capped prime pattern. No polynomial-dependent weight or companion point is allowed in the definition.

The following transfer uses the original explicit estimates (B.26)–(B.29), the small-conductor estimate C.10, the finite pattern counting and residual inequalities C.4–C.9, and the geometry and shared-determinant normalization C.6. For an independent check, the changed terms are itemized here.

### 2.1 One-point proxy and higher moments

Let \(x\) be a positive reflected grid location, \(S=\gcd(n,Q_o)\) and \(T_s(\gamma)\) the product of capped local density factors of C.15. Since \(\ell>y>z\), division of a semismooth value by \(\ell\) preserves the entire recorded pattern and oddness. On the divided interval \(I/\ell\) the denominator for that pattern is \(1/\ell\) times the original pattern denominator, up to the relative finite counting errors of C.14. Thus the exact conditional-density numerator is the positive sum of the ordinary numerators on the divided intervals, and the retained proxy is
\[
 D_I(s)=
 \sum_{\ell\in J}\frac{w_\ell}{\ell}
    c_o(x/\ell,y)T_s(1-\beta(x/\ell,y))(1+O(\eta_{\mathrm{loc},\ell})).
 \tag{1}
\]
Use the actual divided widths \(L/\ell\) and all their smaller endpoints in C.14, C.19, C.20. No error is multiplied by \(|J|\): all terms are positive and the maximum relative error bounds the sum. All the divisions cost at most an additional factor \(Y\) in the endpoint budgets.

For a point with reference height \(X_P\) use the reference
\[
 c_{P,J}=\sum_{\ell\in J}\frac{w_\ell}{\ell}c_o(X_P/\ell,y)
       \asymp \rho(X_P/P,y)/\log P .
\]
All summands have \(u\asymp d\), \(0\le1-\beta\le C/d\), and \((1-\beta)\log Y=O(\log D)\). The pointwise score bound in C.5 is uniform in the saddle shift, also for outcome-dependent choices. In C.29–C.31 use that bound simultaneously at every divided endpoint \(x/\ell\), followed by positive averaging with the fixed weights \(w_\ell c_o(X_P/\ell,y)/\ell\). The shift \(\log(X_P/|n|)\) is the same for all parent summands. Hence no new independence is needed for the higher moment. Exact cancellation on complete retained pattern cells still holds by definition; the smooth count used on an endpoint cell becomes the positive semismooth count, bounded by \(D^C c_{P,J}\) times its length using the divided direct interval bounds. The discarded patterns and near-zero and total-variation errors use \(c_{\min,J}\ge e^{-C\Lambda}\) exactly as before. In particular the factor \(1/\log P\) is not a new exponential density loss.

With \(A=(j+10)^3\), \(m=1000A\), the C.31 bound is \(D^{-1/3+o(1)}\), and centering as in C.34 yields, for the actual point mean \(a_{P,J}\),
\[
 \|D_P^U-a_{P,J}\|_m\le D^{-1/4}a_{P,J}.
 \tag{2}
\]
The source's C.7 proof at its original parameters has the weaker \(D^{-5/24+o(1)}\) exponent because A was a power of D. The new exponent calculation for (2) is in §5.

### 2.2 Full-content fourth moment

The principal residual calculation C.8–C.9 requires the normalized fourth moment of the exact full-gcd conditional expectation of \(f_J\), not of \(f_J\) itself. Fix \(K=2^a K_o\), \(T=\gcd(n,K_o)\), and let \(n\) be odd and uniform in a retained cell. Its ideal content law is \(\pi_K\) of C.13.

For a parent \(\ell\nmid K_o\), the divided interval \(I/\ell\) has the same full content, since multiplication by \(\ell\) is a unit modulo \(K\). C.16 and C.6 therefore bound the fourth norm of its conditional density by \(C w_\ell c_o(x/\ell,y)/\ell\). Minkowski sums these contributions.

For \(\ell\mid K_o\), that term is zero unless \(v_\ell(n)=1\). Under the ideal capped law the support event has probability at most \(1/\ell\); this remains true when the cap at \(\ell\) is one (the cap event then also includes larger valuations). Remove the prime \(\ell\) from the content modulus and apply the ordinary formula to \(n/\ell\) on the divided interval. If the cap exceeds one the divided value is required to be a unit at \(\ell\); if the cap is one no such denominator restriction is necessary. Since \(\ell>y\), the smooth numerator already avoids \(\ell\); the difference costs at most \((1-1/\ell)^{-1}\). Other prime coordinates have the same independent geometric law. This term's fourth norm divided by \(c_{P,J}\) is \(O(\log P\,\ell^{-1/4})\): the possible gain from forcing the parent is absorbed by the number of parents in the complete band, whose densities and weights have bounded ratios. Sum over the at most \(\log K/\log P\) such primes to get \(O(\log K\,B^{-1/4})=o(1)\). This proves the bounded fourth moment; relative finite content counts are applied before the normalized norm, as in C.9. The semismooth reference density varies by at most \(D^C\) in retained cells, just as the ordinary reference.

The truncation, conditional independence of nested capped prime coordinates, TV conditional-stability inequality and exceptional-cap probability in C.8–C.9 now apply to \(f_J\) unchanged. In particular the principal residual bound (C.48) is still \(D^{-4A+O(1)}\), after the same density normalizations. This is the unconditional box-law counterpart of the source's GRH semismooth fourth-moment argument on pp.113–114.

### 2.3 Nonprincipal sums: same conductor majorant

Enlarge the deterministic lower endpoint of the algebraic envelope in C.51 downward by two further powers of Y to include division by a parent and an endpoint halving. Let \(u_y(r,\chi)\) and \(b(r)\) refer to the smooth character prefix envelope on this enlarged deterministic range. It still has \(\log x\asymp d\log Y\) up to fixed constants and includes all endpoints; C.10 and the stronger C.11 of §1 apply there.

For any positive content/induction divisor \(h\) and primitive nonprincipal \(\chi\) of conductor \(r\), consider the interval sum of \(f_J(hn)\chi(n)\), retaining oddness where required. If h is y-smooth, its terms are exactly the sum over \(\ell\in J\) of smooth sums on the interval divided further by \(\ell\), times \(\chi(\ell)\); terms with \(\ell\mid r\) are zero. If h is not y-smooth, either h contains precisely one eligible parent to exponent one and its other factors are y-smooth, in which case there is one ordinary smooth sum on the interval already divided by h, or the test is identically zero. This also covers a parent contained in an induction divisor.

By (B.29), using \(\beta_*\) the minimum saddle over the chosen enlarged range, the absolute value of these primitive sums is bounded by
\[
 C\,\Psi(x,y)h^{-\beta_*}
       u_y(r,\chi)\left(1+\sum_{\ell\in J}w_\ell\ell^{-\beta_*}\right)
 \le D^C\Psi(x,y)h^{-\beta_*}u_y(r,\chi).
 \tag{3}
\]
Indeed \(\sum_{\ell\in J}\ell^{-\beta_*}\le C Y^{1-\beta_*}=D^{O(1)}\), since the ratio \(\log Y/\log y\) is bounded. The odd-prefix identity applies term by term, with all parents odd. The semismooth reference is at least a constant times \(\rho(x,y)/\log P\), so switching to it costs another polynomial in D, not an inverse smooth density. This is the key point: applying Harper directly to a sequence supported on all Y-smooth integers, with normalization by the much smaller semismooth population, would not prove the desired error.

The Möbius induction identity (C.56) is an identity for any bounded test, including \(f_J\). Use (3) and its squared version in the weighted Cauchy–Schwarz argument of (C.57). Its factor \(r/k\), the summation over odd induction factors, and the weights \(f^{1-2\beta_*}\) are unchanged; only a factor \(D^C\) is inserted. Thus \(b(r)\) in C.12 can be replaced by \(D^C b(r)\). The rational side is **unchanged**: its parent label in C.63 is now the query child q, still a prime greater than B, with \(q\nmid he\). The algebraic modulus is \(2\Delta/q\), including powers of q and two. The same positive common-determinant convolution C.12 consequently bounds the normalized nonprincipal f-f term by
\[
 D^C\eta^{-2}\exp(-cD^{1/4}).
 \tag{4}
\]
Here the constant c can be reduced from C.64; its precise value is irrelevant. Terms with proxies still use (C.49)–(C.50), since the proxy is fixed, bounded by one and constant on each retained grid/content cell. The rational population factor cancels pointwise before averaging (C.63), using the actual semismooth mean. No independent sampling of the parent band prime is assumed in this calculation.

### 2.4 Remaining terms and the exact interface

For thin determinants, B.10 already supplies the upper pair bound for semismooth tests. Use the C.5 bound on the number of these pairs, and the single-proxy bound from (1), exactly as C.68. For the diagonal, \(f_J^2\le f_J\); (2) gives the needed \(O(a_{P,J})\) residual second moment. Boundary rectangles use the positive majorant \(ff+fD+Df+DD\), the full-content moment of §2.2 and the same lattice denominator (B.40). Near-zero strips, finite-law TV and partial-cell endpoint errors are bounded after division by the minimum semismooth density squared. The new worst endpoint after a parent division is still included in the enlarged range. With the guards in §5, all terms of the C.69 ledger retain their margins. In particular the source's hierarchy \(D^{1/4}\gg D^{1/6}\lambda^2\gg A(\log D)^2\) now has additional slack.

**Transfer conclusion (subject to independent completion of this analytic audit):** for every deterministic complete parent band with bounded weight ratio, every complete query child band in \((B,y]\), and the specified common rational-environment law, the actual weighted count \(Z_J\) and its true conditional mean \(\tau_J(g,q,t)\) satisfy
\[
 \Pr_{\rm base}(|Z_J-\tau_J|>\tau_J/2)\le D^{-3A},
 \qquad
 E[(Z_J/\tau_J)^2\mid g,R_{q,t}]\le D^C .
 \tag{5}
\]
The mean is pointwise comparable to the source B.51 formula and has a positive exponential-in-\(\Lambda\) lower bound after normalizing weights. The corresponding ordinary count tail uses C.3 with the same modified guards. The second-moment inequality already follows from the appropriately scaled B.10. The probability in the first inequality is only a complete-band baseline average over the environment, query prime, root and field. **Do not** claim a pointwise conditional tail for every root, or replace a selected child by a uniformly sampled one.

In (5) the analytic work is the transfer of the source's C.4–C.9 and C.63–C.69 estimates, not an already existing theorem of the source for this changed distribution. The steps above give the changes, but a second independent referee should check each finite local divisor/endpoint normalization. The final cost theorem below is explicitly conditional on this transfer and the other source inputs in the new ranges.

## 3. Linear unconditional propagation

The following finite implication is proved independently of the remaining analytic obligations. Assume the root flatness B.7, uniform pointwise whole-box mean comparisons B.6/B.11, ordinary baseline tail and (5). Use deterministic profiles
\[
 B_1(q)=q^{\gamma_0-1},\qquad
 B_{i+1}(q)=B_i(q)+\sum_{J_e\subset(y_i,Y_i]}
                  q^{\gamma_{i,e}-1}\sum_{\ell\in J_e}B_i(\ell)
\]
as in (B.68)/(G.40), with \(\gamma_{i,e}=1-\beta(2X_i/2^e,y_i)\), and \(0\le\gamma_{i,e}\log y_i=O(\log D)\). Every profile and individual summand has within-band ratio at most two. Put \(W_i=\sum_{B<q\le Y_i}B_i(q)\) over the fixed allowed prime domain, and use the unnormalized finite event measure
\[
 \mathcal B_i(E)=W_i^{-1}\mathbf E_{g,F}
       \sum_{\ell,s} B_i(\ell)1_{R_{\ell,s}}1_E.
\]
Its mass is bounded above and below by constants, by B.7. The estimate \(W_{i+1}/W_i\le D^C\) and \(W_1\le D^C\) follows as in (G.41) from the harmonic sum \( \sum_{q\le y}q^{\gamma-1}\le y^\gamma(1+\log y)\). This measure is not asserted to be the adaptive visitation law.

Define good states as in 4.2: at an active state, at least \(\tau/4\) candidates have no bad child, and \(Z\le2\tau\); pass-through has the same status as the next-level copy. Terminal states are good. Put \(\delta_i=\mathcal B_i(\mathrm{Bad}_i)\), \(\delta_j=0\). The exact deletion bound (4.2), the ordinary count tail, and \(\tau_l(g)\asymp\bar\tau_i(\ell)\) on G give, after multiplication by the deterministic profile, the surrogate incidence
\[
 H_i^{\rm det}(g,F,q,t)=
   \sum_{\text{active }l=(\ell,s)}
       \frac{B_i(\ell)}{\bar\tau_i(\ell)}X_{l,(q,t)}
\]
where \(\bar\tau_i(\ell)=T_i\rho(2X_i/\ell,y_i)/\ell\). All weights in a parent band are deterministic and have bounded ratio. Reorder under the single child-root condition as in B.55/G.48. The result is at most the corresponding complete semismooth count \(S_e\) with weights \(\ell B_i(\ell)/(T_i\rho(2X_i/\ell,y_i))\). Omitting the finite parent mask \(\ell\nmid b(P)\) is legitimate for this upper bound. Its conditional mean is comparable to
\[
 P_e(q)=q^{\gamma_{i,e}-1}\sum_{\ell\in J_e}B_i(\ell).
\]
There is no lower bound required for the masked count.

For each e, split its contribution at \(S_e\le C P_e(q)\), choosing C larger than twice the uniform mean comparison constant. On the complement, (5) bounds the tail under every complete query band. Changing to the measure weighted by \(P_e(q)1_{R_{q,t}}\) costs a fixed factor because the profile ratio and root flatness are bounded. The pointwise second moment from (5), Cauchy–Schwarz and the tail bound give
\[
 \mathbf E\sum_{q,t}S_e\,1_{\{S_e>C P_e(q)\}}
     \le D^{-3A/2+C}\sum_qP_e(q).
\]
On the bounded part with an arbitrary correlated child-bad indicator, use \(C P_e(q)1_{R_{q,t}}\). Sum all e, add pass-through, and normalize by \(W_i\). Together with the ordinary tail this yields
\[
 \delta_i\le D^C\delta_{i+1}+D^{-3A/2+C}.
 \tag{6}
\]
There is no repeated Cauchy–Schwarz power on \(\delta_{i+1}\). This proof requires only the baseline tail and second moment of each complete semismooth count, not a joint law across the parent bands, or a conditional variance estimate at a realized bad child.

For \(j=O(\log D)\) and \(A=(j+10)^3\), (6) gives \(\delta_1\le D^{-A}\) eventually. At the top, Proposition B.13 supplies a second moment against \(B_1(q)\); only one Cauchy–Schwarz loss is needed, giving normalized expected discarded mass at most \(D^{C}\sqrt{\delta_1}=D^{-A/2+C}\). This conclusion applies bandwise to the broad-band private shapes below, using the same \(B_1\) and the same internal bad sets in all bands. Thus the huge q-star and growing-power A were needed by the repeated square-root recursion, not by the algebraic descent identities.

## 4. Eliminate the exponential field pool and reduce shape cost

### 4.1 Polynomial-moment top pool

At an individual top parent there is no coefficient-root condition. The unconditioned version of B.4 uses the same translation/window proof before conditioning, with q=1 and K=2∆. The odd-lattice, normalization, progression and upper pair bounds B.8–B.10 then apply to ordinary smoothness in that box. The rational points are primitive and have \(G(P)=\pm p n_P\) a unit modulo N, so the hypotheses of B.3–B.4 hold. This gives
\[
 E[(Z_p/\tau_p)^2\mid g]\le D^C
\]
using B.12/B.13's same-level mean lower bound (with the new parameters), including the diagonal term. This uses no ordinary *concentration* at the top. In particular C.11's rational range need not hold there.

The following replacement of Proposition 4.2 is elementary. If the normalized count \(X=Z_p/\tau_p\) has mean one and second moment at most U, the empirical mean of J independent fields at fixed g has variance at most U/J. If setup rejection without a factor has probability at most ρ, its expected normalized loss is at most \(\sqrt{U\rho}\) by Cauchy–Schwarz, not \(U\rho\). The same Markov/Chebyshev argument of D.2 then gives at least three quarters of top labels with
\[
  \sum_a D_{p,a}\ge J\tau_p/2,\qquad
  \sum_a Z_{p,a}\le5J\tau_p/4
\]
in the accepted pool, except with probability
\[
 \epsilon_G+128U/J+32(\theta_N+\sqrt{U\rho}).
 \tag{7}
\]
All loss expectations use the original law; a verified factor is absorbing. Thus one may take \(U=D^C\), \(J=2^{m_b^2}\) with \(m_b=\operatorname{bitlength}(n)\). This pool is superpolynomial in n but \(L_N[1/3,o(1)]\); it dominates any fixed unknown polynomial loss, and does not require the algorithm to know C. The source's exponential pool \(2^{(U_*+20)dm_b}\) is unnecessary for this upper-pair argument. A polynomial pool also suffices if a suitable explicit polynomial bound is supplied.

### 4.2 Multi-band shapes in U

Import only the elementary shape count H.5 (pp.134–135), not its GRH supply theorem. Let \(k_0=\kappa d\) and \(e_0=\lfloor(n-5)/(2k_0)\rfloor-1\). Use its integer definitions (H.18)–(H.19) of \(m_k,k,L_x,S_b,D_0,J_b,D_c,P_{\rm sh}\), with this \(k_0\); require all its finite shape guards. The private bands are \((2^{e_0-h-1},2^{e_0-h}]\), \(0\le h\le J_b\), above \(Y_{\min}=2^{\lceil127e_0/128\rceil}\). Top parents in U are now these bands, not the source single band above \(Y_0\). They all exceed \(Y_1\).

The proof of B.1's individual and aggregate top rational counts applies to each such band: replace its parent scale \(Y_0\) in (B.12)–(B.16) by the band's lower endpoint P, keeping the top point box \(V_0=Y_0^6\). The top multiplicity parameter uses \(\log(x_0 V_0)/\log P=O(\kappa)\), and every P is \(Y_0^{127/128+o(1)}\) or larger. All the other estimates are uniform by the guard checks in §5. Union over polynomially many bands for the common rational event. B.13's profile \(q^{\gamma_0-1}\) and upper second moment hold bandwise: the same cancellation \(\rho_J\asymp |J_{\rm band}|\rho_P/P\) in B.59 removes the band population. The top algebraic box and \(y_0=Y_1\) are unchanged, so \(\gamma_0\) is the same for every band. Hence §3's top bad-mass bound and (7) hold simultaneously for one pool, with probability \(1-o(1)\) after the polynomial union. No different independently chosen good field is substituted at internal levels. Each actual top request chooses a fresh uniform slot from this one pool and samples its corresponding point; its completed tree then uses that field.

H.5's counting argument now applies to the pooled sets of good top primes. In its notation \(k=k_0+\lceil k_0/m_k\rceil\sim\kappa d\), so
\[
 \log P_{\rm sh}=(2\kappa/3+o(1))\Lambda
\]
rather than the source's original single-band \(2\kappa\). The only input to H.5 is the simultaneous per-band good density, not how it was proved. The shape cap is \(32(C+1)P_{\rm sh}\), and at most \(4k_0\) top requests are launched per accepted shape. The same stopped-process proof as 4.3/D.3 gives an epoch success probability bounded below by an absolute positive constant, after the source's independent probe/sampler error allowances and sealed-root extraction.

## 5. Concrete new parameter schedule and guard ledger

Use natural logarithms for the asymptotic quantities, \(D=\log N/\log\log N\), \(\lambda=\log\log N\), \(\Lambda=D^{1/3}\lambda\). Let \(d\) be the original least odd integer with \(d^3m_b\ge n\), \(t=dm_b\), \(\Lambda_b=(\log 2)t\sim\Lambda\). Set
\[
 \kappa=9,\quad b_0=201/100,\quad q_*=2,\quad U_*=12,\qquad
 e_B=\lceil 201t/100\rceil,\quad
 e_{i+1}=\max(e_B,\lceil(e_i+2t)/2\rceil),
\]
with \(e_0,k_0\) as §4.2, \(Y_i=2^{e_i}\), \(V_i=Y_i^6\), \(B=2^{e_B}\). Keep (B.4) exactly, including the independent w and the original uniform cube, with \(E=2^{d^2m_b}\). The unclamped fixed point is \(2t\), strictly below \(e_B\) by \(t/100\). All active transitions eventually strictly decrease and \(j=\log D/(3\log2)+O(1)\). Set \(A=(j+10)^3,m=1000A\). Use the same grid, cap, Bonferroni and tail constructions C.2, C.9, C.35.

Here are the changes in the source's analytic hypotheses, not just a numerical optimization of a fixed-parameter theorem.

* **Top geometry and rational supply:** \(\log Y_0/\log M\to1/18\), \(\log Y_1/\log M\to1/36\), \(\log V_0/\log M\to1/3\), \(V_0^2/M=M^{-1/3+o(1)}\). Thus all B.1 scale/upper moment conditions hold with room: \(KY B^3\log B/V\le K\log B/Y^2=o(1)\), \(K=\lceil e^{D^{1/6}\lambda^2}\rceil=B^{o(1)}\), and numerator endpoints remain in the Hildebrand direct interval range. Here K denotes the cell count, not the determinant modulus. B.8 rational-error terms are bounded by poly(n) \(K^4\rho^{-1}(Y^{-8}+Y^4/M)\). The latter at the top is \(M^{-7/9+o(1)}\), and at all internal levels is smaller. Top B.14–B.16 with each private band P have margins \(P^2/V_0^2\le Y_0^{-10}\), \(P/M\le M^{-17/18+o(1)}\), \(Y_1^4/V_0^2,Y_1^4/M=o(1)\) exponentially on \(\log M\) scale, and \(1/P+Y_1/V_0+Y_1P/V_0^2\) is likewise negligible. The polynomial union of all level/band/cell failure bounds is \(o(1)\). The stronger own-root density bounds use the same g event.
* **Window law:** (B.4) gives \(\log(HM)=(11+6/\kappa+o(1))d\Lambda_b=(35/3+o(1))d\Lambda_b<12d\Lambda_b\). It implies \(\log(2X_i)<12d\Lambda_b+6d\log Y_i\) eventually, including rounding and the polynomial/d factors in B.4. The B.3/B.4 total-variation errors remain \(O(qE^{-4})\) (use \(Y_0\le E^{1/(2\kappa)}\)). All window relative geometric errors are exponentially small on at least the \(d\Lambda_b\) scale. Increasing fixed constants \(C_X,C_U,C_{\rm cut}\) does not change any program cost. All polynomial heights and derivative/content/leading-coefficient initialization guards \(8MH<N,\ 2H+1<N\) hold eventually. The derivative rejection bound is \(O(1/H)\).
* **Density and own-level means:** for every value and every required root/parent division, the cutoff recurrence gives \(\log(2X_i)/\log y_i\le12d\). There is also a fixed positive lower multiple of d, since \(\log X_i\asymp d\log Y_i\) and the cutoff ratio is bounded; dividing by O(1) primes of size at most \(Y_i\) costs \(O(\log Y_i)\). Thus \(-\log\rho(x,y_i)\le(4+o(1))\Lambda_b\) by the sharp Dickman estimate used in source G.13, which is **unconditional** in the large-y range here. For the rational side the worst log-size is \((1+3/\kappa+o(1))d\Lambda_b=(4/3+o(1))d\Lambda_b\), including top cofactor division or aggregation. The worst loss coefficient is at most \((4/3)/(3b_0)=400/1809\). The rough denominator sieve and complete-parent-band logarithmic factors cost \(o(\Lambda_b)\). Hence
\[
 4+\frac{400}{1809}<\frac{423}{100},\qquad
 p_{\rm den}=2^{-\lceil423t/100\rceil}
 \tag{8}
\]
is an eventual uniform lower bound on \(\tau/|\Omega|\), for actual means before rejection. All ordinary means and the normalized semismooth means are exponentially large: even \(11b_0-423/100>17\) in \(\Lambda_b\) units using \(V_i^2/q\ge Y_i^{11}\) and the additional complete-band factor \(1/\log Y_i\). This replaces the original unnecessary \(e^{1000\Lambda_b}\) bound in B.12 by \(e^{17\Lambda_b}\). It absorbs the diagonal terms. B.35, B.51–B.55 and B.59 still have fixed comparison constants from (B.27)–(B.30); \(\gamma\log Y=O(\log D)\) suffices for all B.9/B.10 pair bounds.
* **Character endpoints:** for internal \(Y\le Y_1\), the new rational guard is \(31/36<1\). For the algebraic side enlarge C.51's lower endpoint exponent \(6d-14\) to \(6d-16\); \(\log x_-/\log x_+\to1\) uniformly as the subtracted terms are \(O(\log Y +d+C_X\log y)\). Both log heights are \(\asymp d\log Y\); no longer use the specific inequality \(\log(HM)\le d\log Y\) from C.11, which would be false with the smaller \(b_0\). Instead \(\log(HM)=O(d\log Y)\), which suffices for \(x_-\ge x_+^{1/3}\), \(\log y\ge\sqrt{\log x_+}\) (ratio of squares at least a constant times \(\lambda\)), \(u\asymp d\gg(\log\log x_+)^5\), and \(y\in[(\log x_+)^{21},x_-^{1/100}]\). On the rational side the same last range holds for B. These are the C.10 and revised C.11 hypotheses, retaining the exceptional character. In C.12 the algebraic and rational saddles tend to one, and \((1-\beta_r)\log\log(3T_0)=o(1)\). Both the nonprincipal and rational-principal companion sums have their former margins, with polynomial factors allowed by (4).
* **High moments and finite counts:** \(\log z=8A\log D=D^{o(1)}\), \(m=1000A=D^{o(1)}\), \(\gamma=O(1/d)\). Hence \(m\gamma\log(2z)=D^{-1/3+o(1)}\). In C.19 use \(\log(S_0E_{\rm cut})/\log y=D^{o(1)}\) both for \(S_0=U\) and \(S_0=K\); the term squared over \(\log x\log y\) is \(D^{-1/3+o(1)}\). The Mertens \(\log^4(2z)\) factor is \(D^{o(1)}\); the truncated-divisor tail in C.20 is negligible after the chosen fixed \(C_{\rm cut}\) and the mesh factor \(x/L\). The smallest divided width has log \(\gg d\log Y\), because the extra parent and root divisions cost \(O(\log Y)\) and \(\log\eta^{-1}=O(D^{1/6}\lambda^2+A\log D)=o(\log y)\). C.35's \(\log B_\nu=O((\log Y/\lambda)A^5(\log D)^5)=o(d\log Y)\) and \(-\log E_\nu\gg m C_\rho\Lambda+\log K\) follow as before. The relative pattern-count and TV errors survive density normalization and m-th roots. The latter is also immediate for the TV \(O(qE^{-4})\): its log is \(-\Omega(d\Lambda)\), and \(m=d^{o(1)}\). C.38's two moment errors therefore improve to \(D^{-1/3+o(1)}\); the fixed tails have sufficient margin by choosing constants after the uniform density lower bound. The proxy score and thin/boundary remainder hierarchy is strict. These comparisons cover the further one-parent division in §2. An actual re-verification of each local-count lemma is still required for a polished unconditional theorem.
* **Private shapes and finite guards:** (H.18) has \(k\sim9d,\ k\le2k_0\), \(J_b\sim2e_0/m_k\), \(\lceil127e_0/128\rceil>e_1\). Thus \(J_b+1\le e_0/128\) and \(2m_k(J_b+1)\ge e_0\) eventually; \(S_b\ge0\), and the center \(D_c\) differs from \(S_b+k\) by at most k by its floor definition. The least parent prime has log \(\asymp d\Lambda_b\), whereas \(\omega(N)\log2\le(\log N/\log B)\log2=o(\log Y_{\min})\) and the shape loss is only \(O(\Lambda_b)\). This verifies the noncoprime-pair error in H.5. Use its \(P_{\rm sh}\), exact checks, and shape-factor cutoff \(K=2k_0\) in U.

These strict asymptotic margins are uniform through all \(O(\log D)\) levels. They are proof guards, not empirical extrapolations from small N.

## 6. Exact cost transfer

Only this section's theorem is claimed as a conditional complexity result. Assume the source B/C/E analytic/algebraic inputs with the above transfers, in particular (5) and the ordinary count and source mean estimates in the specified ranges. Use exact recursive auxiliary factorization as in U (no RH-dependent recognizer). Modify the source's integer value-size guard (F.2): require \(|F(P)|\le \lceil N^{167/500}\rceil\), as well as strictly smaller inputs, checked by integer powers. Indeed its actual uniform height satisfies
\[
 \log|F(P)|/\log N\le 3/\kappa+o(1)=1/3+o(1)<167/500 .
\]
One may check the integer sufficient inequality \(500(12d^2m_b+6de_0)\le167(n-1)\) before beginning any epoch. The actual shape guard remains \(\lceil\sqrt{2N}\rceil\). Use the source's trial-division backup and input induction; no recursive call is subject to a hidden ancestor time budget.

All quantities in the following table are leading upper coefficients of \(\Lambda\) in the logarithm; fixed polynomial factors, \(J=2^{m_b^2}\), tree depths and branch caps of logarithmic size have coefficient zero.

| Quantity | Coefficient |
|---|---:|
| Column bound C and retained occurrence count A (F.3),(F.6) | \(201/100\) |
| Shape cap and all Search states | \(201/100+2\kappa/3=801/100\) |
| Raw trials per Search | \(423/100\) |
| All raw trials / value factorizations | \(1224/100\) |
| Probe bit length \(S^*\) | \(2/3\) |
| Probe sampler / bounded direct call ledger \(64 Q_\chi^2P\) | \(28\) |
| Direct reconstruction bound (F.8) | \(12(201/100)=24.12\) |

Indeed \(J\) and all degree, t-star and T-star factors have subleading logs. The broad-band private shape count supplies the exponent \(2\kappa/3=6\). The old direct-work bound (F.9) can be used *term by term*, without its very coarse final envelope (F.10). The exponents of its other terms are \(3b_0,\ 3b_0,\ 12.24+\max(b_0,2/3),\ 12.24+2b_0\); each is below 28. The original memory-copy charges on each smaller-input call are retained, not treated as constant random access. Use 29 as a slack upper coefficient of direct work.

For a full recursive expected-time coefficient \(C_*=40\), the two heterogeneous contraction inequalities of Section 6 are
\[
 801/100+2^{-1/3}C_*<C_*,
 \qquad
 1224/100+(167/500)^{1/3}C_*<C_* .
\]
Both hold by exact positive rational cubes:
\[
 (3199/4000)^3>1/2,\qquad (347/500)^3>167/500 .
\]
These strict margins, and \(29<40\), suffice for the same induction of source Theorem 6.1 (or our [size-stratified recurrence lemma](multilevel_descent_accounting.md)). Conditional on the arithmetic interface, the epoch success probability is bounded below uniformly in the past; the private-root argument is unmodified. Outer factor-tree size is polynomial in n. All finite invalid parameters fall back to the persistent trial-divisor rule, so termination and verified output correctness on every tape do not depend on the analytic estimates.

**Conditional theorem (explicit):** the modified U-program above has the verified-output and every-tape termination properties of U. If the transferred ordinary/semismooth tail (5), mean and geometry estimates at §5's parameters and the source's certificate/computation bounds hold, its expected bit complexity is at most \(L_N[1/3,40]\). This is a fixed-input, uniform leading-constant implication, not a claimed practical speedup. It improves both the source's \(10^{13}\) and our earlier conditional 91.4 at the level of the proposed proof ledger; it is not yet a certified replacement for those results. Unlike KeyBreak G's 2.97, the proposed proof does not use GRH.

## 7. Priority for further verification

The arithmetic gap is now concentrated in the explicit §2 transfer, especially the finite conditional-pattern and common-determinant residual normalization for weighted semismooth counts. The §1 large-sieve extension and §3 finite propagation eliminate two major parameter restrictions, so this is a concrete and potentially tractable proof target. The remaining analytic obligations must be verified before replacing the repository's main claimed randomized bound. The [intermediate U100 checkpoint](keybreak_unconditional_fallback.md) avoids the additional semismooth concentration requirement by tightening the source's original growing moments and is the preferred first unconditional-route verification target. More extensive reoptimization of \(\kappa,b_0,q_*\) is secondary to completing that check. The above schedule was chosen for simple exact guards; it is not asserted optimal.

A future route below exponent 1/3 cannot come merely from replacing the numerical constants: in this particular degree/height/smoothness architecture, the usual \(d\), base and norm scale balance remains. The deterministic half-scale uniform selector is still a separate objective.

## 8. Finite verification receipt

The standalone [exact check script](../verification/research/verify_keybreak_compression.py) was executed locally with Python 3.13.5, then checked against its committed blob `85231107645e41ed4b383cc564e543f9b95293f6` (SHA-256 `9f6d2e9f3475ac252961c6f12f0190272d1ffe1261b821c54cddcf882fd03128`). It verifies the rational leading constants, both recursive cube margins, the explicit dyadic schedule/shape/height guards at 18 symbolic bit lengths, and 72,000 semismooth content identities. The depth range is 333–833. It does not certify the analytic estimates or the runtime of an implemented factorer. The full repository suite, PDFs and Lean targets were not rebuilt here.
