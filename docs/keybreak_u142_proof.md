# U14.2: a reduced-degree, thinner-box and two-quota optimization

27 November 2026. **Tightened conclusion:** the same schedule gives 14.1 by the exact stricter auxiliary-size guard in §8. The 14.2 ledger is retained for auditability.

**Status:** written changed-range proof and cost transfer from the U40 arithmetic mechanism, with the additional changes proved below. The constant 14.2 is not an independently reviewed or formally certified record. The original source's finite arithmetic/certification lemmas and the unconditional analytic imports in [U100](keybreak_u100_proof.md) and [U40](keybreak_u40_proof.md) are reused. The [critical U40 audit](keybreak_u40_critical_audit.md) records the source checks. This note changes the parameters, the coefficient windows, the sieve level, the search quotas and the exact reconstruction algorithm; none is silently substituted into a fixed-parameter theorem. No GRH or conjectural smoothness assertion is used in the written argument.

Source: The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 Nov. 2026, 144 pp., [PDF](https://crypto.sjtu.edu.cn/factoring.pdf), SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9. Source lemma numbers below refer to that version.

## 1. Parameters

Put \(D=\log N/\log\log N,\ \lambda=\log\log N,\ \Lambda=D^{1/3}\lambda\), \(n=\operatorname{bitlength}N,\ m_b=\operatorname{bitlength}n\). Fix the exact rational constants
\[
 c=233/1000,\quad \kappa=9,\quad b=151/100,\quad v=301/100,\quad
 a=44,\quad h_*=265,\quad s_0=401/200 .
\]
Choose d to be the least odd integer at least 3 satisfying \(d^3m_b\ge c^3 n\), so \(d\sim cD^{1/3}\). Write \(t=dm_b,\ \Lambda_d=t\log2\sim c\Lambda\); b is a constant in \(\Lambda\) units, not \(\Lambda_d\) units. Set
\[
 k_0=\kappa d,\quad e_B=\lceil (b/c)t\rceil,\quad e_0=\lfloor(n-5)/(2k_0)\rfloor-1,
 \qquad e_{i+1}=\max(e_B,\lceil(h_*t+\lceil v e_i\rceil)/a\rceil),
\]
\[
 Y_i=2^{e_i},\quad V_i=2^{\lceil v e_i\rceil},\quad B=2^{e_B},\qquad M=\lfloor N^{1/d}\rfloor .
\]
The condition \(h_*<(a-v)b/c\) ensures the unclamped fixed point is strictly below \(e_B\) by a positive constant times t. Hence the cutoffs strictly decrease above \(e_B\) for sufficiently large N and \(j=\log D/(3\log(a/v))+O(1)\). Retain the source's elementary shape guards H.18–H.19 and use the same broad private bands. Take \(J=2^{m_b^2}\) independent field slots as in U40, \(A=(j+10)^3,\ m=1000A\) in its concentration proof.

The limiting top ratios are
\[
 R_0=\log Y_0/\log M\to1/(2\kappa),\quad
 R_1=\log Y_1/\log M\to v/(2\kappa a),\quad
 \log V_0/\log M\to v/(2\kappa).
\]
Here and below equations involving these ratios mean their limiting values when used as exact rational guards.

## 2. Smaller uniform coefficient windows, with conditional error accounted for

Retain the homogeneous interpolant \(\widehat F(r,Q)=N\), parity correction \(F_0\bmod2\), and distribution \(F=F_0+2(w\widehat F+GR_{\mathbf c})\) from source B.6. Instead of the very large margins \(E^4,E^8\) in B.4, use
\[
 R=2^{t\lceil\sqrt d\rceil},\quad
 W=M^2V_0^2 Y_1^2 R,\qquad
 H=2^{d+20}d^{10} W Y_1^2 R,\qquad h_0=2H+1.
\]
Use the original uniform integer windows \(w\in(W,2W]\), \(\mathbf c\in[-H,H]^d\). These are explicit finite integers, and are not the analysis cutoffs z,R of U100 §3 (rename that earlier R to the valuation-cap cutoff in this note). All finite evaluation-lattice, cyclic-quotient and reanchoring arguments in B.3–B.4 are independent of the old sizes of W and H. Before root conditioning the TV error is bounded by
\[
 C\left(\frac{d(1+V^2)+Wd^32^d+1}{h_0}
               +\frac{M^2 V^2}{W}\right)
 \le \frac{C'}{Y_1^2R}.
\]
The one-point comparison has smaller terms and obeys the same bound. Root conditioning costs at most \(4q\) since its unit-slope equation has probability \(1/q+O(h_0^{-1})\). Thus the actual conditional error is \(O(q/(Y_1^2R))\) for every \(q\le Y_1\) (and q=1 at the top). **This is why the extra \(Y_1^2\) is retained:** the single-point mean of a specified semismooth parent \(\ell\) may have size \(1/\ell\) times the smooth density. All such \(\ell\) in an internal parent box satisfy \(\ell\le Y_1\), so the ratio of the TV error to the individual mean is \(O(1/(R\rho_{\min}))=o(1)\), even with the two factors q and \(\ell\). At the top the parent prime divides the rational value, not the tested polynomial value; an algebraic child query is still at most \(Y_1\). The error divided by any fixed power of the smooth density is \(e^{-\Omega(\sqrt d\,\Lambda_d)}\); its m-th root divided by the density is negligible because \(m=O((\log D)^3)=o(\sqrt d)\). Thus all the high-moment and pair-law transfers of U100 and U40 survive.

The new field height coefficient is
\[
 \frac{\log(HM)}{d\Lambda_d}
 =\frac{3+v/\kappa+2v/(\kappa a)}{c^3}+o(1)
 <h_*.
 \tag{1}
\]
The \(2v/(\kappa a)\) term is from the two squared \(Y_1\) factors in W and H; it has not been dropped. The R margins have log \(o(d\Lambda_d)\). Also \(\log M=O(d\Lambda_d)\), so the setup guards \(8MH<N,\ 2H+1<N\) hold eventually. The derivative rejection bound is \(O(H^{-1})\) as in source A.2. With the deterministic height checks \(16dMH\le 2^{h_*dt}\) and \(|F(P)|\le 2^{h_*dt+d\lceil v e_i\rceil}\), the source's deterministic reference scale \(X_i=16(d+2)h_0 M V_i^d\) has \(\log_2(2X_i)\le h_*dt+d\lceil v e_i\rceil\) eventually by the strict margin in (1). Implement this slightly stronger scale inequality explicitly if needed, before using an epoch. All these guards are eventually valid; finite exceptions fall back to the persistent trial-divisor procedure.

## 3. Rational supply with a thinner denominator box

Replace only the fixed linear-sieve parameter 3 in source B.17 by \(s_0=401/200>2\). The Rosser–Iwaniec lower sieve function \(2e^{\gamma_E}\log(s_0-1)/s_0\) is a positive fixed constant. This is the classical linear sieve, e.g. Montgomery–Vaughan, *Multiplicative Number Theory II*, Thm.21.9 and (21.66) ([publisher](https://doi.org/10.1017/9781009445030.007)), or the standard Rosser weights supported at level \((B+1)^{s_0}\). For a denominator interval of length \(L\asymp V/K_{\rm cell}\) in a unit class modulo \(\ell>B\), the sieve main term is \(\asymp L/(\ell\log B)\). Each divisor progression has error \(O(1)\); the total remainder is \(O(B^{s_0})\). The requisite relative bound is
\[
 K_{\rm cell}YB^{s_0}\log B/V=o(1)
\]
uniformly, since \(v>1+s_0\), \(Y\ge B\), and \(K_{\rm cell}=\exp(o(\log B))\). There is no prime-in-short-progression assumption. The fixed lower sieve constant can be very small; it affects only the eventual threshold and multiplicative constants.

The multiplicative large-sieve calculation B.19–B.20 now uses \(V=2^{\lceil ve_i\rceil}\) with \(V_0^2/M=o(1)\) since \(v/\kappa<1\). Its proof uses the same smooth–rough unique-product multiplicity and uniform environment r,Q. For the common internal event the failure bound is
\[
 D^C K_{\rm cell}^4 \rho^{-1}(Y^4/V^2+Y^4/M).
\]
The worst rational density loss (using the safe larger endpoint \(MV_0\) everywhere) is
\[
 r_*=\frac{1+v/(2\kappa)}{3bc},
\]
in \(\Lambda\) units by the sharp Dickman estimate. Thus the first ratio has strict bottom margin \((2v-4)b-r_*>0\); the second is exponentially smaller on the \(\log M\) scale even at the largest internal Y (and \(4R_0<1\)). The whole and cell estimates, including the thin determinant strip bound, follow with their unchanged \(V^2/\ell\) geometry. The top individual and aggregate arguments of U100 §2.1 use the actual top broad bands P with \(Y_0^{127/128+o(1)}\le P\le Y_0\), and \(V_0=Y_0^{v+o(1)}\). Their ratios \(P^2/V_0^2,P/M,Y_1^4/V_0^2,Y_1^4/M\) and primitive-mask ratios \(P^{-1},Y_1/V_0,Y_1P/V_0^2\) have fixed negative exponents in \(\log M\). This verifies the common G event simultaneously over levels and broad bands, including the auxiliary child-root whole and cell counts. Rounding V by powers of two affects only fixed factors. Source A.3's geometric sampler works because \(V/Y\to\infty\).

## 4. Density, geometry and moment-transfer guards

The reference scale bound in §2 and the integer recurrence imply \(\log(2X_i)/\log Y_{i+1}\le ad\). For all allowed root/parent/cofactor divisions the log-height is between fixed positive multiples of \(d\log Y_i\) and the smoothness argument \(u\) is between fixed positive multiples of d. Indeed \(h_*\) and \(a/v\) are fixed, the largest root/parent/modulus divisions change the log-height by \(O(\log Y_i)\), and the smallest box has \(\log Y_i\gg \Lambda_d\). The sharp Dickman losses in \(\Lambda\) units are at most \(p_*=ac/3\) for the algebraic side and \(r_*\) above for the rational side. Use
\[
 p_A=2^{-\lceil ((171/50)/c)t\rceil},\qquad
 p_{\rm den}=2^{-\lceil ((453/100)/c)t\rceil}
 \tag{2}
\]
because \(p_*<171/50\) and \(p_*+r_*<453/100\). These are lower bounds on the **one-point ordinary algebraic mean** at each eligible rational point, and on the **whole relation mean / geometric domain size**, respectively. The same-level ordinary and normalized semismooth means are exponentially large, since
\[
 (2v-1)b-453/100>3 .
\]
A complete semismooth band after dividing its weights by their maximum loses only an additional polynomial factor, by its population and uniform single-parent estimate. The one-point comparison (B.5) on every uniform interval is unchanged; the TV relative error for an individual parent was checked in §2. The ratio theorem gives the fixed dyadic cofactor comparability and \(q^{\gamma_e}\) mean profile just as in U40.

Here are the remaining changed-range checks for the ordinary and semismooth proofs; the finite formulae and their derivations are those in U100 §§2–6 and U40 §§2–5.

- The pair determinant modulus is now at most \(16Y^{2v}\), with \(\vartheta\ll V^2\). The projection widths, chord and area estimates from B.4/B.8 remain the same in terms of V. In particular \(K/L_2\ll2^d V^{2-d}/(HM)\) after the determinant cancels. All relative lattice counting and central strip errors are still negligible. The padding lengths for B.9's semismooth pair upper bound have logs \(\gg d\log Y\), since the extra factors \(Y,K,\vartheta,y^{C_X},d\) subtract only \(O(\log Y+\log d)\) from the log-height. Thus the required progression lengths \(\lambda_1/(4Y),\lambda_2/(2YK)\ge2y\) hold. The algebraic saddle satisfies \((1-\beta_F)\log Y=O(\log D)\), so the progression factors raised to \(1-\beta_F\) are polynomial in D. The normalized diagonal cost is small by the large mean bound above.
- Use rational endpoint range \(x_{-,r}=M/(128Y^{v+1})\), \(x_{+,r}=2MV\) for every internal parent box, and conductor ceiling \(16Y^{2v}\). This includes all combined content/induction divisions, since they divide the determinant modulus \(O(V^2)\). The improved separated-fraction guard is
\[
 (5v+1)R_1<1.
\]
For the algebraic envelope it is enough to take a deterministic lower endpoint \(h_0 M\,2^{-C d} V^d\,y^{-C_X}/(C(d+2)Y^{2v+3})\) with an absolute sufficiently large C. All pair-modulus, root, parent and odd-prefix divisions are included: their combined size is at most \(O(Y^{2v+2})\). The log-height remains comparable to \(d\log Y\) and the lower/upper log-endpoint ratio tends uniformly to one. In particular \((\log y)^2/\log x_+\gg\lambda\), \(u\asymp d\), and \(y\in[(\log x_+)^{21},x_-^{1/100}]\); on the rational side the analogous bounds hold with B. These are precisely the range checks used for the classical small- and large-conductor theorems, including the possible exceptional real character. The semismooth primitive-sum loss remains \(D^C\) because it uses the algebraic saddle. Both saddles exceed any fixed \(\beta_0<1\) eventually, so the common-determinant convolution, including the rational principal companion, is unchanged.
- Set the proof cutoffs \(z=D^{8A},Q_o,\eta,U,E_c,\nu\) as in U100 §3 (with the present A). Because \(A,m=D^{o(1)}\), \(\log(S_0E_c)=o(d\log Y)\), \(z<y\), and the finite relative local error and score bound are \(D^{-1/3+o(1)}\). In detail, \(\log B_\nu=o(d\log Y)\) and \(-\log E_\nu\gg m C\Lambda+\log K\) for every fixed C; the smallest retained cell still has \(\log L\gg d\log Y\) including the extra parent division; \(\log\eta^{-1}=o(\log y)\). Therefore every finite Bonferroni, conditional projection and relative endpoint error in U100 §§3–4 is valid. The local density supremum of the proxy is \(e^{O(A(\log D)^2)}\) times the reference density. The residue fourth-moment proof of U40 (S6)–(S7) still absorbs the exceptional parent-in-modulus contribution by \((\log K)P^{-1/4}=o(1)\), and the proof of (S8)–(S10) still costs only a polynomial factor in D. None of these comparisons requires the old exponent v=6 or c=1.
- The near-zero/large-pattern error constants can be chosen once after the new fixed minimum-density lower bound. The pair TV contribution now uses §2's \(R^{-1}\) margin in place of \(E^{-4}\); its density-normalized size is smaller than \(e^{-C\Lambda}\) for every fixed C. The same lattice-boundary normalization and thin-pair count apply. With d a fixed positive multiple of \(D^{1/3}\), the hierarchy \(D^{1/4}\gg D^{1/6}\lambda^2\gg A(\log D)^2\) remains strict. In particular the ordinary and weighted complete semismooth baseline tails are \(D^{-3A}\) with the same normalized upper second moments \(D^C\).

This verifies all parameter-dependent steps of the U40 concentration proof at the new degree, box and coefficient scales. The underlying finite determinant calculation is not replaced with a new heuristic independence assumption. Apply the deterministic profile and linear bad-child recursion (S12)–(S14) of U40, whose proof uses only the baseline tail and pointwise upper moment just checked. Its conclusion \(\delta_1\le D^{-A}\) follows with \(j=O(\log D)\); the top second-moment deletion and subleading field pool work as before. The H.5 broad-band shape probability has inverse exponent \(2\kappa c/3\) in \(\Lambda\) units, because \(k\sim\kappa d\). All top bands remain above \(Y_1\), and \(\omega(N)\log2=o(\log Y_{\min})\) from B-roughness, so its elementary coprime-pair argument applies.

## 5. Separate exact algebraic quotas and cubic reconstruction

Use the unconditional search-quota proof in the [critical audit §4](keybreak_u40_critical_audit.md). On every good internal request \(D_{\mathrm{usable}}\ge\tau/4\ge p_A|R_{\mathrm{rational}}|/4\); on every covered top request use \(D_{\mathrm{usable}}\ge J\tau/2\) and at most \(J|R_{\mathrm{rational}}|\) rational opportunities. Therefore the source H.4 stopped-stream argument applies to the pooled field law and exact recursive factorization instead of its RH recognition algorithm. Implement H.15 with the exponents in (2), and \(K=2k_0\). The new local algebraic quota is \(r_A=4096p_A^{-1}L_s\), with the original \(q_s=128 L_s\) and \(r_s=4096p_{\rm den}^{-1}(q_s+L_s)\), where \(L_s=\operatorname{bitlength}(64K(n+1))\). On any state, including bad ones, increment its algebraic counter on rational acceptance before the factoring call; overflow fails only that search. Every call is exact, with no inherited timeout. The verified-candidate cap, child-failure union, geometric opportunity bound and raw proposal cap give the source failure target \(\epsilon_s=1/(16K(n+1))\). The number of all search states is bounded deterministically by the broad-shape attempt cap times \((q_s(n+1)+1)^{O(j)}\). Consequently all algebraic calls are charged against the smaller \(r_A\), not the raw \(r_s\). This changes the proof of the time recurrence but not the ideal exact-predicate success law.

Keep the conservative exact probe sampler and direct caps of source F.7, including deterministic AKS (no probabilistic false-prime pass is required). Degree \(d\sim cD^{1/3}\) means \(\log S^*/\Lambda=2c/3+o(1)\), so \(64Q_\chi^2P\) has leading coefficient \(28c\). The source E.3 odd-degree separation and all field-wise parity columns apply to the same subleading field pool. Use the unconditional characteristic-zero square-root argument of source H.7, verified in the critical audit §3, **for every field**. It factors the degree-2d norm polynomial of a separating shifted element using LLL Thm.3.6 at cubic dependence on expanded coefficient bit length. Products can be expanded sequentially at cost polynomial in n,d times retained occurrence count times squared maximum expanded height; field roots and exact verification have cubic height cost. The source trace-dual construction and signed norm corrections are unchanged. This replaces F.8's overly coarse twelfth-power charge by coefficient \(3b\), since both retained count and expanded height have leading coefficient b and the number of fields is subleading. Character evaluations on retained atoms cost polynomial in n,d times their count and \((S^*)^3\), giving coefficient \(b+2c\). If a direct implementation chooses instead to evaluate/store characters on failed raw attempts, its cost can still be bounded by \(s+453/100+2c\) (below the claimed direct envelope), but the retained-only version is simpler.

All frame copy costs are still charged conservatively using F.9's \(P_{\rm raw}C^2\) bound, and the per-proposal lookup/roughness/smooth rational tests cost \(J(B+S^*+1)\operatorname{poly}(n)\) or less. Even on failed paths a field table scan and local storage use charged bit operations. No reliance on a unit-cost random access to a subexponential-sized array is needed. The actual worklist and complete factorization outputs are as in U100.

## 6. Exact constant and recurrence closure

Write
\[
 s=b+2\kappa c/3=727/250,\quad
 v_A=s+171/50=791/125,\quad
 v_{\rm raw}=s+453/100=3719/500 .
\]
The leading coefficient of columns, retained occurrences and maximum expanded coefficient bit length is b. The shape attempt and all search state counts have exponent s. The raw proposal count has exponent \(v_{\rm raw}\); the **algebraic factorization** call count has exponent \(v_A\) by §5. The coordinate factorization count has exponent s. Direct work upper coefficients (including the conservative memory-copy charge even at every raw proposal) are bounded by
\[
 3b,\quad v_{\rm raw}+\max(b,2c/3),\quad v_{\rm raw}+2b,
 \quad28c,\quad b+2c,\quad3b .
\]
Their maximum is \(5229/500=10.458<11\). A fixed polynomial factor includes exact parameter tests, finite loop caps and environment/prime samplers. The pool \(J=2^{m_b^2}\), degree factors and search tree multiplicity contribute \(o(\Lambda)\).

Check raw-value auxiliary size by the sufficient exact integer inequality
\[
 125(h_*dt+d\lceil ve_0\rceil)\le21(n-1).
\]
It holds eventually by \(v/(2\kappa)=301/1800<21/125\), because \(h_*dt=o(n)\). Reject any invalid finite parameter state and use the original persistent backup; verify every actual value input is at most \(\lceil N^{21/125}\rceil\) and strictly smaller than N. Coordinate subcalls have size at most \(\lceil\sqrt{2N}\rceil\). The source's uniform success proof applies after the new exact-predicate caps and concentration; fresh recursively called coins are independent of all earlier public and sealed-private data. No deterministic runtime cap on those recursive calls is assumed.

For \(C_*=71/5=14.2\) the two strict recursive margins are
\[
 (1-s/C_*)^3>1/2,\qquad
 (1-v_A/C_*)^3>21/125.
\]
They are positive rational inequalities (checked by the standalone exact ledger). In particular
\[
 s+2^{-1/3}C_*<C_*,\qquad
 v_A+(21/125)^{1/3}C_*<C_*.
\]
Together with the direct ceiling 11, the same strong input induction and geometric epoch-success bound as U100 §8 prove the written expected bit complexity
\[
 \boxed{L_N[1/3,14.2]} .
\]
The exact certified output and every-tape termination follow from the verified integer split/worklist and persistent trial-division backup. The argument still uses the source's finite direct-operation implementations, the analytic imports and the U100/U40 proof dependencies; it has not been independently reviewed or formalized. No smaller workspace bound or practical speedup is claimed. This is a fixed-input upper-bound argument, not an average over randomly chosen N.

## 7. Numerical optimization and limitations

The schedule was found by optimizing the displayed recurrence coefficients with c, \(\kappa,b,v\) varying, using floating-point search only for candidate generation. The proof uses the explicit rational constants above and exact checked margins, not an optimizer's assertion of a minimum. The tight terms are now the coordinate and raw-value recursion, rather than the huge field pool or probe cost. The smaller windows have been chosen conservatively to preserve relative individual-parent error estimates; further exact conditioning could reduce them slightly. A much stronger gain requires a new initialization or rational/algebraic descent mechanism. In particular changing fixed constants cannot make the first L-parameter less than 1/3. See the separate scale-breaking investigation.


## 8. Tighten the same schedule to 14.1

No arithmetic estimate or relation-supply hypothesis changes. Replace the raw-value size guard in §6 by
\[
 18000(h_*dt+d\lceil ve_0\rceil)\le3011(n-1),
 \qquad\theta'=3011/18000>301/1800 .
\]
This holds eventually by the same strict asymptotic height comparison. Require each actual raw-value factorization input to be at most \(\lceil N^{\theta'}\rceil\) and strictly smaller than N. The full direct ledger and the coefficients s and \(v_A\) are unchanged. For \(C'=141/10\), the two exact positive cube margins are
\[
 (1-s/C')^3-\tfrac12=9659059/87600656250>0,\quad
 (1-v_A/C')^3-\theta'=135796037/700805250000>0.
\]
Thus the same recursive proof yields **\(L_N[1/3,14.1]\)**. This is the preferred leading constant from this schedule, with the same written-proof and independent-review qualifications. It is not asserted optimal over other designs.

The standalone checker [verification/research/verify_keybreak_u142.py](../verification/research/verify_keybreak_u142.py) verifies both ledgers and the stronger integer size, window, cutoff, sieve, conductor and shape inequalities on 18 symbolic bit lengths. The local execution passed; the committed Git blob matches the tested file (25feb8ef6a81e29d013af7d89bed459863800e46, SHA-256 a0d5a22950ceaa19c01c74d5bfbd1cfe04bada768ea757245bf6b62ab0128c28). These tests do not independently prove the analytic estimates. See also the new [scale-breaking investigation](beyond_one_third_research.md) and [probe-free unit certificate](exact_descent_unit_certificate.md).
