# U40: semismooth concentration and linear transfer

27 November 2026. **Written mathematical proof checkpoint.** This note completes the additional weighted semismooth concentration argument for [U40](keybreak_unconditional_compression.md), using the finite local-density, character-energy and common-determinant proof in [U100](keybreak_u100_proof.md). It establishes the changed-range arithmetic transfer and closes the cost recurrence at 40 as a written unconditional-route proof. Classical published analytic results and the pinned source's elementary lattice, algebraic certification, and bit-operation lemmas are imported as mathematical results. The proof has not been independently refereed or formally verified. In particular the 40 bound is not asserted as a certified record or as a practical factoring implementation. The older conditional notes remain as historical checkpoints.

The pinned source is The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 Nov. 2026, 144 pp., [PDF](https://crypto.sjtu.edu.cn/factoring.pdf), SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9. We use its unconditional box law and common-determinant structure (Appendices B–C), its elementary broad-band private-shape count (H.5), and the idea of deterministic-profile truncation from G.6. No GRH-dependent assertion of Appendix G or H is used. All ordinary-case references below refer to the U100 proof unless explicitly prefixed by a source section number.

## 1. Parameter-uniform ordinary proof at the U40 schedule

Use the notation of U100 §1 but choose
\[
 b=201/100,\quad \kappa=9,\quad Q_*=2,\quad e_B=\lceil201t/100\rceil,
 \quad e_0=\lfloor(n-5)/(2\kappa d)\rfloor-1,\qquad
 e_{i+1}=\max(e_B,\lceil(e_i+2t)/2\rceil).
\]
The coefficient distribution is the same B.4/B.6 law, and \(V_i=Y_i^6\). The moment parameter is now \(A=(j+10)^3,\ m=1000A\), with \(j=\log D/(3\log2)+O(1)\). Use exactly the small-prime cutoffs, grid and revised Bonferroni order of U100 §3 with this A. We check the changed constants before using any of the ordinary estimates.

* \(e_B>2t\), and the limiting fixed point of the unclamped recurrence is \(2t\); hence it reaches eB in the stated number of levels. The top ratios \(\log Y_0/\log M\to1/18,\ \log Y_1/\log M\to1/36,\ \log V_0/\log M\to1/3\) give \(V_0^2/M\to0\) on the \(\log M\) scale. The broad bands are above the next cutoff. The relative rough-sieve error \(K_{\rm cell}YB^3\log B/V=o(1)\) holds at all levels. The common rational environment error \(D^CK_{\rm cell}^4\rho^{-1}(Y^{-8}+Y^4/M)\) is uniformly \(o(1)\), even after the level and band unions, since the rational density loss is at most \((4/3)/(3b)+o(1)\) in \(\Lambda_b\) units. The top individual and aggregate errors, including the primitivity mask, have fixed margins on the \(\log M\) scale, using \(P\ge Y_0^{127/128+o(1)}\) in each top band and \(Y_1\le Y_0\). Thus the U100 §2.1 proof gives the same common event G, whole counts, cell upper bounds and thin-pair count, in every parent box and for every \(B<q\le Y_i\), not only the active roots.
* \(\log(HM)=(35/3+o(1))d\Lambda_b<12d\Lambda_b\); the root and content TV errors are \(O(qE^{-4})\) as before. Thus the finite evaluation-window and upper pair proofs of U100 §2.2–2.3 apply to every root in the parent box and to the unconditioned top case. The changed mean ledger is \(-\log\rho_{\rm alg}/\Lambda_b\le\min(4,(12+6\xi)/3b)+o(1)\), \(\xi=\log Y/\Lambda_b\ge b+o(1)\). The cutoff gives \(u\le12d\), so the simpler uniform cap 4 suffices even at the bottom. The rational loss cap is \(400/1809+o(1)\); the total loss is strictly below \(423/100\). All normalized ordinary and complete-band semismooth means are exponentially large, since \(11b-423/100>17\). The mean comparisons and upper second moments follow at these changed parameters. The density threshold used by Search is \(p_{\rm den}=2^{-\lceil423t/100\rceil}\).
* For internal boxes \(Y\le Y_1\), the improved large-sieve separation guard of U100 §5.2 is \(31/36<1\). On the algebraic side \(\log x\asymp d\log Y\) and \(\log y\asymp\log Y\), so every source range in U100 §§1, 5 holds uniformly. The algebraic lower envelope may be enlarged downward by \(Y^2\), using exponent \(6d-16\) in place of \(6d-14\). It then includes all further parent divisions as well as root, content, induction and parity divisions. This does not change any limiting log-height comparisons. In particular \((\log y)^2/\log x_+\gg\lambda\), \(u\asymp d\), and \((1-\beta)\log Y=O(\log D)\).
* The small-prime cutoffs have \(\log z=8A\log D=D^{o(1)}\), \(\log U,\log E_c=o(d\log Y)\), and \(m=D^{o(1)}\). Thus U100 (6) improves to \(D^{-1/3+o(1)}\), and its one-point centered moment bound improves to \(D^{-1/4}\). All discarded and finite-count errors remain exponentially negligible after density normalization, and \(D^{1/4}\gg D^{1/6}\lambda^2\gg A(\log D)^2\) is strict. With the new m the proxy Markov error is at most \(D^{-10A}\). Consequently the ordinary C.3 tail (U100 (15)) is valid at these parameters.

This checks the parameter-sensitive uses of the U100 proof, without replacing an active-root assertion by a child-root assertion: the finite rational and value laws, determinant count and envelopes used in that proof require only \(q>B\) and \(q\le Y\). They do not require \(q>y\). This distinction is essential for the incoming-count application.

## 2. Weighted semismooth concentration: exact statement

In a fixed parent box i, let \(J=(P,2P]\cap\mathbb P\), with \(y\le P,\ 2P\le Y\), deleting primes dividing N. Let \(w_\ell>0\) for \(\ell\in J\) be deterministic weights with fixed bounded maximum/minimum ratio, and normalize their maximum to one. Define
\[
 f_J(u)=\sum_{\ell\in J} w_\ell 1_{\{0<|u|\in \ell S_y\}}.
\]
The supports are disjoint, since each supported value has exactly one prime above y and its valuation is one. Thus \(0\le f_J\le1\), also for signed u. Let \(J_q\) be any complete dyadic band in \((B,y]\) of queried child primes, with fixed primes of N deleted, and let the baseline choose \(g\sim\bar\mu\) on the common event G, \(q\) uniformly in \(J_q\), an admissible root s uniformly, then the **raw** form F conditional on \(R_{q,s}\). All points are rationally eligible primitive points in the *parent* box at \(a\equiv sb'\pmod q\). Set
\[
 Z_J=\sum_{P'} R_{P'} f_J(F(P')/q),\qquad \tau_J=E[Z_J\mid g,R_{q,s}] .
\]
Here \(P'\) denotes a lattice point, distinct from the numerical band endpoint P. Any deterministic mixture of the query bands is also allowed.

**Theorem.** Uniformly in the fixed weights (with a common ratio bound), every permitted level and the complete query band,
\[
 \Pr_{\rm base}(|Z_J-\tau_J|>\tau_J/2)\le D^{-3A}.
 \tag{S1}
\]
Moreover, pointwise in \(g\in G,q,s\), under the single root condition,
\[
 E[(Z_J/\tau_J)^2\mid g,R_{q,s}]\le D^C,\qquad
 \tau_J\asymp \frac{T_i}{q}\sum_{\ell\in J}\frac{w_\ell}{\ell}
               \rho(2X_i/(q\ell),y).
 \tag{S2}
\]
These estimates are for the unmasked complete semismooth count. They imply the required upper comparison for the actual incoming count, not a concentration theorem for an arbitrarily conditioned or masked count. The mean and upper moment (S2) were proved in U100 §2.3 and checked at the new parameters in §1. We now prove (S1). The argument below treats all changed terms explicitly, rather than assuming a common-determinant bound for a new support.

## 3. Local conditional densities for a semismooth test

Write \(c_\ell(x)=c_o(x/\ell,y)\), where \(c_o(x,y)=2(1-2^{-\beta(x,y)})\rho(x,y)\). On a retained reflected grid cell \(I=(x,x+L]\), put
\[
 c_J(x)=\sum_{\ell\in J}\frac{w_\ell}{\ell}c_\ell(x).
\]
For a point with reference height \(X_{P'}\) put \(c_{P',J}=c_J(X_{P'})\). Within the complete band the individual densities \(c_\ell(x)\) have fixed ratio, by the saddle ratio theorem at a shift of at most \(\log 2\). The PNT and the fixed bounded weight ratio give
\[
 c_J(x)\asymp \rho(x/P,y)/\log P .
 \tag{S3}
\]
In particular \(c_{P',J}\ge e^{-C\Lambda}\) uniformly, and \(c_J(x)\le D^C c_{P',J}\) on retained cells by the same saddle shift as the ordinary case. These two normalizations are used throughout; no factor comparable to the number of parent primes is hidden in the errors.

### 3.1 Small-prime patterns and the centered proxy

Use \(S=\gcd(u,Q_o)\) and the actual uniform odd-cell law P. For each point define \(D_{P',J}^U(u)=E_P[f_J\mid S]\) on its complete cell, zero on \(S>U\) or the rounded near-zero strip. It is a single fixed function of u, defined before the point is paired with any other point. For every \(\ell\in J\), \(\ell>y>z\) and \(\ell\) is odd. The substitution \(u=\ell v\) therefore preserves the small-prime pattern and oddness. The exact numerator for the \(\ell\)-term at \(S=s\) is the corresponding ordinary smooth numerator on \(I/\ell\); the odd-pattern denominator on \(I/\ell\), relative to that on I, is
\[
 \ell^{-1}(1+O(\epsilon_{\rm ar}(I)+\epsilon_{\rm ar}(I/\ell))).
\]
This follows from the actual finite count (U100 (1)), not from treating a full period of \(Q_o\) as contained in the interval. The divided width is \(L/\ell\) and the retained forced divisor s is unchanged. All relative errors in U100 (1)–(4) hold for this divided interval, since an extra \(\log Y\) in the endpoint budgets is \(o(d\log Y)\), and its relative width is the same. Apply the ordinary conditional-density product at \(x/\ell\) and sum the nonnegative terms to obtain
\[
 D_{I,J}(s)=
 \sum_{\ell\in J}\frac{w_\ell}{\ell}c_\ell(x)
   \prod_{3\le p\le z}t_{p,K_p}(v_p(s);1-\beta(x/\ell,y))
   (1+O(\epsilon_{\rm loc,\ell})) .
 \tag{S4}
\]
There is no uniform error multiplied by \(|J|\): it is the maximum relative error within the positive sum. This remains true for rare retained patterns because their denominator errors were relative. Zero patterns can be given value zero, as before.

Under the single-point ideal comparison window, the archimedean random shift \(\log(X_{P'}/|u|)\) is identical for every parent summand. All saddles at the divided locations satisfy \(\gamma\le C/d\), and the uniform score bound in U100 §3 holds pointwise even when that saddle depends on the pattern and location. Apply the proof of U100 §4 to each summand in (S4), normalized by the deterministic reference weights \(w_\ell c_\ell(X_{P'})/\ell\), then use Minkowski. The finite density error is \(D^{-1/3+o(1)}\); the relative score and archimedean errors are no larger. Discarded values have zero proxy and hence normalized deviation -1. A total-variation transfer of the bounded proxy costs at most \(2c_{\min,J}^{-1}(CqE^{-4})^{1/m}\), which is negligible. Centering at the actual point mean uses the exact cancellation on complete cell patterns. For a partial endpoint cell the absolute residual is bounded by twice its full semismooth weighted count; divide by each \(\ell\) in the short interval theorem and sum positively to bound this by \(D^C c_{P',J}\) times its length. Large-pattern and near-zero tails are controlled using the same fixed density lower bound. Thus
\[
 \|D_{P',J}^U-a_{P',J}\|_m/a_{P',J}\le D^{-1/4},
 \qquad a_{P',J}=E[f_J(F(P')/q)\mid g,R_{q,s}].
 \tag{S5}
\]
This proves the high moment at the true one-point mean. It does not depend on joint independence of several value evaluations or on a selected parent prime.

### 3.2 Full-content fourth moment: the additional parent-in-modulus cases

Let \(K=2^vK_o\) be even, \(T=\gcd(u,K_o)\), and \(\pi_K\) the ideal full-content law \(2\phi(K/\delta)/K\) on \(\delta\mid K_o\). We need to prove
\[
 E_{\pi_K}\left(\frac{E_P[f_J\mid T]}{c_J(x)}\right)^4\ll1 .
 \tag{S6}
\]
This cannot be inferred merely from bounded fourth moments of the ordinary smooth test or from Jensen applied to the indicator itself. A prime above y dividing K can force the unique semismooth parent and create an exceptional conditional density of order \(c_\ell(x)\) rather than \(c_\ell(x)/\ell\). Treat these primes exactly.

First, if \(\ell\nmid K_o\), the substitution \(u=\ell v\) preserves the full content T. Let \(D_\ell(\delta)=E_P[1_{\{0<|u|\in\ell S_y\}}\mid T=\delta]\). Its exact numerator is the ordinary numerator on \(I/\ell\). The full-content denominator on that interval divided by the original denominator is \(\ell^{-1}(1+O(K\ell/L))\) from the actual relative class counts. Therefore
\[
 \|D_\ell\|_{4,\pi_K}\ll c_\ell(x)/\ell
 \qquad(\ell\nmid K_o)
\]
by U100 (5) at the divided endpoint. The factor \(K\ell/L\) is exponentially small. Sum these terms by Minkowski with weights \(w_\ell\).

Now suppose \(\ell\mid K_o\) and \(e=v_\ell(K_o)\). For \(e=1\), the \(\ell\)-term is supported only on the capped event \(v_\ell(T)=1\), whose ideal probability is \(1/\ell\). On this event the original denominator, under \(u=\ell v\), is exactly the odd-cell denominator on \(I/\ell\) with the other-prime content constraints. No constraint at \(\ell\) remains on v. Its ordinary smooth numerator automatically avoids \(\ell>y\). If \(e>1\), the term is supported only on \(v_\ell(T)=1\), now the exact-valuation event of probability \((1-1/\ell)/\ell\). After division its denominator additionally requires \(v_\ell(v)=0\); this inserts the single bounded factor \((1-1/\ell)^{-1}\) into the density since the ordinary smooth numerator already avoids \(\ell\). All other prime constraints are unchanged because \(\ell\) is a unit at them. In both cases the remaining capped valuation variables under the ideal law are independent of this support event. Apply the ordinary full-content product formula and fourth-moment estimate on \(I/\ell\) with the \(\ell\)-coordinate removed (or fixed at zero). Uniform relative finite counting errors at these moduli are \(o(1)\), also for a rare remaining content. We obtain
\[
 \|D_\ell\|_{4,\pi_K}\ll c_\ell(x)\ell^{-1/4}
 \qquad(\ell\mid K_o).
 \tag{S7}
\]
No assumption is made that the \(e=1\) cap event has exact valuation one: it includes higher valuations in the denominator, and the smooth numerator removes them. No division by a zero-probability content is used.

The number of such exceptional parents is at most \(\log K/\log P\). Since the reference densities and weights have fixed within-band ratios, (S3) bounds the sum of their contributions divided by \(c_J(x)\) by
\[
 O(\log P)\sum_{\ell\in J,\ell\mid K_o}\ell^{-1/4}
 \ll (\log K)P^{-1/4}=o(1)
\]
uniformly, as \(K\le4Y^{12}\) and \(P\ge y\ge B\). The nonexceptional contributions sum to at most \(C c_J(x)\). This proves (S6). The argument is valid for arbitrary positive fixed weights of bounded ratio, including those from deterministic profiles. In particular it closes the additional case not addressed by the ordinary source C.6.

### 3.3 Principal residual and the boundary products

Use the same joint ideal law of S,T and shared caps \(V_*=\gcd(u,\gcd(Q_o,K_o))\) as U100 §4. Conditional independence given \(V_*\) is independent of the test. The rare-valuation bound \(\epsilon_0\) in U100 (8) and the distinguished-value probability are also independent of the test. With \(f=f_J\), (S6) supplies the bounded fourth moment needed there. Attach the actual conditional distribution of \(f_J1_{S\le U}\) to the ideal retained joint patterns; these are finite nonnegative bounded random variables. The relative retained pattern comparisons transfer the conditional fourth moment *before* using TV. All subsequent projection/TV inequalities from U100 §4 hold for any real \(0\le f\le1\), not just an indicator. Hence the principal residual inequality (9) holds with \(c_J(x)\) in place of \(c_I\) and \(f_J-D_{I,J}^U\) as residual. Its leading normalized size is \(D^{-4A+O(1)}\). In the boundary rectangle calculation, (S6) bounds the full-content moments for f, and (S4) plus the score and actual finite relative pattern comparisons bound the fixed moment of the proxy. Conditional Jensen then bounds the full-content proxy moment. This verifies all positive principal products of f and D on the covering rectangles with density factors retained. Thus the boundary area loss is multiplied by \(D^C c_{P_1,J}c_{P_2,J}\), not divided by their exponentially small product.

## 4. Primitive and imprimitive character estimates for semismooth support

Here the crucial difference from the ordinary test is in the original f-f nonprincipal term. We do not apply the smooth large-value theorem to the larger Y-smooth support and then divide by a y-semismooth density. That would lose an exponential factor.

Fix a positive content/induction divisor h and primitive nonprincipal \(\chi\bmod r\). Consider, after reflection if necessary, the sum on a positive interval \(I/h\) with upper endpoint of order \(x/h\), of \(f_J(hv)\chi(v)\), including the odd restriction when applicable. Write \(\beta_*\) for the minimum smooth saddle over the enlarged deterministic algebraic envelope in §1, and \(u_y(r,\chi)\) for the primitive ordinary endpoint supremum defined in source C.51 on this envelope.

There are exactly three possibilities.

1. If \(h\) is y-smooth, the sum is the sum over \(\ell\in J\) of ordinary smooth sums on \(I/(h\ell)\), multiplied by \(w_\ell\chi(\ell)\). This follows from \(\ell\nmid h\) and smoothness of the remaining factors. If \(\ell\mid r\), that term is zero because \(\chi(\ell)=0\).
2. If \(h\) contains exactly one prime above y to exponent one and that prime is an allowed \(\ell\in J\), all other factors of h must be y-smooth. There is then one ordinary smooth sum on \(I/h\), multiplied by \(w_\ell\); no further parent division occurs.
3. Otherwise the test is identically zero on this content.

This dichotomy remains valid after any induction divisor is multiplied into h; negative signs contribute a character factor of modulus one. In case 1 odd prefixes are expressed as the difference of the corresponding ordinary prefixes at the half endpoint, since the parent is odd. In case 2 the same identity applies directly. Every needed endpoint, including \(x/(h\ell)\) and its half, belongs to the enlarged envelope, since h divides the actual modulus before induction has been completed and the total content–induction factor is at most the modulus. The global dilation inequality gives the common upper bound
\[
 \left|\sum_{v\in I/h}^{\rm odd} f_J(hv)\chi(v)\right|
 \ll \Psi(x,y)h^{-\beta_*}u_y(r,\chi)
             \left(1+\sum_{\ell\in J}w_\ell\ell^{-\beta_*}\right).
 \tag{S8}
\]
The sum in parentheses is \(D^C\), since \(\ell\le Y\) and \((1-\beta_*)\log Y=O(\log D)\). This uses a bound for the algebraic saddle, not the rational one. Furthermore \(c_J(x)\gg\rho(x,y)/\log P\) by (S3) and the uniform smooth ratio estimate for the allowed endpoint shift (or directly by monotonicity of the Dickman function with the relative global error). Thus \(\Psi(x,y)\ll D^C x c_J(x)\), and (S8) becomes
\[
 \left|\sum_{v\in I/h}^{\rm odd} f_J(hv)\chi(v)\right|
 \ll D^C x c_J(x)h^{-\beta_*}u_y(r,\chi).
 \tag{S9}
\]
Only a polynomial factor in D is lost, uniformly in the chosen band. The source small-conductor estimate (including exceptional real characters) and the strengthened large-conductor estimate therefore remain the ordinary smooth-character estimates, with no new analytic input.

For a character modulo k induced from a primitive nonprincipal character of conductor r, the exact odd induction identity is
\[
 U_h(k,\chi)=\sum_{e\mid\operatorname{rad}(k_{\rm odd}),(e,r)=1}
             \mu(e)\chi^*(e) U_{he}^{\rm odd}(r,\chi^*).
\]
This identity is valid for the real-valued test \(f_J\); it is just inclusion-exclusion of nonunit primes not dividing the conductor. In particular it retains the case where the unique parent lies in e. Applying (S9) to each he, using the weighted Cauchy–Schwarz argument of U100 (11), gives the new energy majorant
\[
 B^{J}_h(k)
 \ll D^C L_K\sum_{er\mid k,\ e\ {\rm odd}}
       (r/k)e^{1-2\beta_*} b(r),
 \tag{S10}
\]
where the denominator of the energy is \(x c_J(x)h^{-\beta_*}\). Thus this is exactly the former energy with \(b(r)\) replaced by \(D^C b(r)\). The \(\phi(r)/\phi(k)\) induction loss and the factor \(r/k\) have not been omitted. The rational energy is untouched. Its ordinary B-smooth numerator still forbids a query prime \(q>B\) in its content or induction factor, even though q may be smaller than y. The algebraic modulus stays \(2|\det(P_1,P_2)|/q\) with all powers retained.

The rectangular character identity grouped by full content is exact for every bounded test and for two distinct intervals. Use (S10) in U100 (13) with the references \(c_{P_1,J},c_{P_2,J}\). Since the actual semismooth means satisfy (S2), the pointwise cancellation of the two algebraic reference factors against \(\tau_J^2\) is the same as in U100 (14). The rational environment count is unaltered and independent of the new weights. Consequently the entire common-determinant summation (U100 §5.3) applies, including its rational-principal companion and the exceptional conductors divisible by q. By U100 (10), its result is
\[
 D^C\eta^{-2}e^{-cD^{1/4}}
 \tag{S11}
\]
after baseline averaging and normalization. The weights \(w_\ell\) appear only in the positive reference sum and the polynomial loss in (S8), not in a second independent determinant or a resampling of the parent. The nonprincipal terms involving the proxy use U100 §5.4 verbatim: the semismooth proxy is bounded by one and constant on each retained grid/pattern cell, which are the only properties used there. This closes the nonprincipal residual estimate for the new support.

## 5. Finish (S1)

Put \(\widetilde Z_J=\sum R_{P'}D_{P',J}^U(F(P')/q)\). Minkowski and (S5) imply
\[
 \|\widetilde Z_J-\tau_J\|_m/\tau_J\le D^{-1/4}.
\]
The proof of U100 §6 now applies with the following explicit substitutions.

* On the diagonal \(f_J^2\le f_J\), and (S5) bounds the residual square by \(O(a_{P',J})\). The normalized diagonal cost is \(O(1/\tau_J)\), exponentially small by (S2) and §1.
* All near-zero, large-pattern and finite-window TV errors are divided only by the two minimum algebraic densities. Those densities satisfy the same \(e^{-C\Lambda}\) lower bound. The fixed tail constants and finite cutoff budgets can be chosen uniformly once.
* Thin pairs use the complete-band upper pair bound of U100 §2.3, which was proved for this exact semismooth test, including the exceptional parent dividing the pair modulus. The normalized proxy supremum from (S4) is at most \(e^{CA(\log D)^2}\), since each forced divisor is at most U and all divided saddles satisfy \(\gamma\le C/d\). The normalized thin error is \(D^Ce^{CA(\log D)^2}/\Theta\).
* On nonthin pairs the same mesh and actual lattice denominator give the same total interior/cover weights and the relative boundary mass \(O(D^{-10A}+e^{-c d\Lambda})\). The principal residual and boundary positive principal products are supplied by §3.3. All nonprincipal products are supplied by §4, including the separate proxy character errors. The boundary count is not treated as a bare absolute probability.
* The pointwise mean normalization and determinant-pair count are those of U100 §5.3, with q a queried child root in the larger parent region. This is the only average over q and s; no actual adaptive visitation law has been replaced by it.

The normalized residual second moment is therefore at most \(D^{-4A+O(1)}\), since all terms except the principal rare-valuation term have strictly smaller orders by §1. Markov at order \(m=1000A\) for the proxy deviation \(\tau_J/4\), and Chebyshev for the residual deviation \(\tau_J/4\), give (S1). This proves the semismooth theorem at every complete query band and for any deterministic mixture, without a new smoothness conjecture. The proof does not give a pointwise concentration result for all environments and roots.

## 6. Linear exceptional-mass transfer for the actual descent

We now prove the exact deterministic-profile propagation implication of (S1)–(S2), closing the changed transfer in the earlier U40 note.

Use the actual pointwise means \(\tau_i(g,\ell,s)\) of the ordinary parent test; the deterministic comparison mean is
\[
 \bar\tau_i(\ell)=T_i\rho(2X_i/\ell,y_i)/\ell,\quad
 T_i=V_i^2\rho_{r,i}/\log B,\quad y_i=Y_{i+1}.
\]
By §1 and U100 §2 these means have fixed comparison ratio on G. For a complete active band \(J_e=(2^e,2^{e+1}]\) inside \((y_i,Y_i]\), define \(\gamma_{i,e}=1-\beta(2X_i/2^e,y_i)\). The deterministic profiles are
\[
 B_1(q)=q^{\gamma_0-1},\qquad
 B_{i+1}(q)=B_i(q)+\sum_e P_e(q),\qquad
 P_e(q)=q^{\gamma_{i,e}-1}\sum_{\ell\in J_e}B_i(\ell).
\]
As in B.13, \(\gamma_0=1-\beta(2X_0,Y_1)\) is the same for every broad top band because the algebraic top box and next cutoff are common. Domains exclude fixed primes dividing N. All cutoffs are powers of two, so each active interval is a union of complete bands. Each profile is a positive sum of powers with exponents in \([-1,0]\) and consequently varies by at most two within any complete band, as does each summand \(P_e\). Also
\[
 W_i:=\sum_{B<q\le Y_i} B_i(q),\qquad W_1\le D^C,\quad
 W_{i+1}/W_i\le D^C .
\]
Indeed, for each \(\gamma=\gamma_{i,e}\), \(y_i^\gamma=D^{O(1)}\) by the saddle bound, so \(\sum_{q\le y_i}q^{\gamma-1}\le y_i^\gamma(1+\log y_i)\le D^C\). Pass-through contributes at most \(W_i\). When the next label domain is empty its mass is zero and is omitted.

For a raw field and environment, define bad states recursively just as in source 4.2, using the *actual* \(\tau_i\) and the number of ordinary candidates all of whose actual required children are good. Terminal states are good and pass-through has its copy's status. Let
\[
 \delta_i=\frac1{W_i}E_{g,F}\sum_{\ell,s}B_i(\ell)1_{R_{\ell,s}}1_{\mathrm{bad}_i(\ell,s)} .
\]
The measure has bounded total mass because \((q-1)\Pr(R_{q,s}\mid g)\asymp1\) uniformly. Its definition does not presume it to be the visitation distribution. For any deterministic positive profile of bounded within-band ratio, a baseline tail estimate valid at every complete band bounds its normalized profile-weighted event by a fixed multiple of the same tail: choose the band with mass proportional to the sum of its profile, and use root probability \(\asymp1/q\). This observation also applies to the \(P_e\) profiles separately.

For an active parent that is bad outside the ordinary two-sided concentration failure, at least \(\tau_i/4\) of its candidates were deleted by a bad child. This is the source's pointwise candidate-deletion inequality. Multiply it by \(B_i(\ell)1_R\), then sum and integrate. The ordinary tail costs \(O(D^{-3A})W_i\). Replace the actual denominator \(\tau_i(g,\ell,s)\) in the incidence term by its fixed comparison \(\bar\tau_i(\ell)\), losing only an absolute factor. For a particular child \((q,t')\) and active parent band \(J_e\), the resulting formal incidence sum is bounded pointwise, on the single child-root event, by
\[
 S_e(g,F,q,t')=\sum_{P'}R_{P'}\sum_{\ell\in J_e}
  \frac{\ell B_i(\ell)}{T_i\rho(2X_i/\ell,y_i)}
       1_{\{0<|F(P')/q|\in\ell S_{y_i}\}} .
 \tag{S12}
\]
Off its child-root event put it equal to zero. This reordering is exact before dropping the finite-parent mask \(\ell\nmid b(P')\): every formal incidence determines one parent prime and its unique finite root, and the incidence may also count an even valuation or terminal child. Its weight is positive, so dropping the mask is legitimate for an upper bound. The weights in (S12) are fixed before the environment and field, with fixed bounded within-band ratio by the profile and smooth-density ratios. Thus (S1)–(S2) apply after normalization by their maximum, and scaling back. The mean is comparable to \(P_e(q)\), by the calculation B.51–B.53 (division by \(q\le y_i\) changes the density by a factor comparable to \(q^{\gamma_{i,e}}\)). Uniformly in \(g,q,t'\),
\[
 E[S_e^2\mid g,R_{q,t'}]\le D^C P_e(q)^2 .
\]
Select a fixed \(C_1\) exceeding twice the uniform upper mean comparison constant. The event \(S_e>C_1P_e(q)\) has probability at most \(D^{-3A}\) under every complete query-band baseline, by (S1); on its complement, its contribution times any child-bad indicator is bounded by \(C_1P_e(q)1_R1_{\rm bad}\). On the exceptional event, change measure to the profile \(P_e(q)\) and use Cauchy–Schwarz on the *normalized* second moment:
\[
 E_{g,F}\sum_{q,t'} S_e1_{\{S_e>C_1P_e(q)\}}
 \ll D^{-3A/2+C}\sum_qP_e(q).
 \tag{S13}
\]
All summands here vanish off the root event. This argument makes no assertion about the conditional law of a child given that it is bad. It uses one tail for the full semismooth count, not independent incidences.

Sum (S13) over parent bands and add the deterministic pass-through term \(B_i(q)\). The bounded parts sum pointwise to at most a fixed multiple of \(B_{i+1}(q)\) times the child-bad indicator; the exceptional tails sum to \(D^{-3A/2+C}W_{i+1}\). Normalizing the deletion inequality by \(W_i\) and using its ratio bound gives
\[
 \delta_i\le D^C\delta_{i+1}+D^{-3A/2+C},\qquad\delta_j=0.
 \tag{S14}
\]
Unlike the original square-root recurrence, (S14) is linear in the child-bad mass. It follows that \(\delta_1\le D^{-A}\) eventually, since j=O(log D), \(A=(j+10)^3\), and iteration multiplies the error by at most \(jD^{Cj}\). No multiplication by the number of parent labels has occurred. The same bad sets and deterministic profiles apply for every top band.

At the top use the actual normalized mean weights for each broad parent band, as in B.13. Its incoming mean compares to \(B_1(q)\), and its upper second moment is \(D^C\), by the checked top estimates. One Cauchy–Schwarz loss against \(\delta_1\) gives top expected normalized discarded mass \(D^{-A/2+C}\). There is no further repeated square-root loss. The polynomial union over the top bands remains valid. The polynomial-moment pool argument in U100 §7 then supplies one actual pool of \(J=2^{m_b^2}\) fields for which at least three quarters of every band's parents have the required usable and total count inequalities, with probability \(1-o(1)\). Rejected slots are charged, and all internal descendants remain in the field chosen by their top atom. This completes the unconditional relation-supply theorem for U40.

## 7. Expected time closure

The exact program and certificate machinery of U100 §§7–8 are reused, with the schedule of §1. All finite parameters are explicit. Use the same broad-band shape definitions H.18–H.19 and guards with \(k_0=9d\); the inverse shape probability exponent is \(2\kappa/3=6\). The proof of the shape count uses only the simultaneous per-band good-density conclusion just established. The exact stopped Search caps, root checks, shape normalization, field initialization, factor-base tests, row construction, matrix columns, bounded probe arithmetic, public square reconstruction, and private-root invariance all apply. The actual field and value heights obey the guard \(500(12d^2m_b+6de_0)\le167(n-1)\) eventually because \(3/\kappa=1/3<167/500\). All smaller-input factor calls are exact and run to completion. The analytic tail estimates are not tested by the algorithm, and no work is assigned to computing their means or profiles.

In \(\Lambda\) units the leading cost ledger is:
\[
 \begin{array}{c|c}
 \text{columns, retained occurrences, reconstruction precision}&2.01\\
 \text{shape attempts and all Search states}&8.01\\
 \text{raw trials per Search}&4.23\\
 \text{all raw trials and raw-value factorization calls}&12.24\\
 \text{probe bit length}&2/3 .
 \end{array}
\]
Each figure is a logarithmic upper coefficient plus o(1). The first is dominated by the base primes, since \(J=2^{m_b^2}\) has subleading logarithm. The state multiplier has subleading logarithm \(O((\log D)^2)\). The direct probe cost in source F.7 has coefficient 28; the direct reconstruction bound F.8 has coefficient \(12(2.01)=24.12\), because the pool, degree factors and \(2^{4d}\) are subleading. The other F.9 terms have ceilings \(3b,\ 3b,\ 12.24+\max(b,2/3),\ 12.24+2b\), all below 28. Thus direct work per epoch has coefficient at most 29 with slack. These bounds retain the actual failed-path and state-copy charges; they are not a random-access simplification.

The expected-cost proof uses only conditional uniform epoch success, now supplied by §6 and the original sealed-root certificate, and the exact smaller-input induction. The coordinate calls have count coefficient 8.01 and log-size ratio at most \(1/2+o(1)\); the value calls have coefficient 12.24 and ratio at most \(167/500+o(1)\). For \(C_*=40\), the required strict inequalities
\[
 8.01+2^{-1/3}C_*<C_*,\qquad
 12.24+(167/500)^{1/3}C_*<C_*
\]
are certified by the positive rational cubes
\[
 (3199/4000)^3>1/2,\qquad (347/500)^3>167/500.
\]
Together with \(29<40\), these close the source Section 6 induction. For each actual smaller input and all entry histories, use fresh recursive coins; the expected cost of an epoch is bounded by the direct work plus the two deterministic call-count ceilings times the corresponding induction bounds. Each fresh epoch has a constant success lower bound independent of its past; summing reached epochs is a geometric bound, without assuming independence between cost and success. The persistent trial-divisor backup and checked strict shrinking ensure termination on every tape, and the outer verified factorization tree has at most \(2\lfloor\log_2N\rfloor-1\) nodes. Therefore the written proof gives
\[
 \boxed{\mathbb E T(N)\le L_N[1/3,40]}
\]
in the limsup leading-constant convention, uniformly over fixed inputs. This is the complete changed-parameter transfer using the source's finite arithmetic/certification lemmas and the unconditional classical analytic inputs in U100 §1. No imported GRH result, external factoring algorithm with a hypothetical bound, or conjectural semismooth covariance assertion is needed in this derivation.

## 8. Proof status and review

The genuinely additional mathematical steps over U100 are the full-content fourth-moment estimate (S6)–(S7), the semismooth primitive/induced energy bounds (S8)–(S10), the application to the same determinant (S11), and the deterministic linear exceptional-mass recurrence (S12)–(S14). The proof gives these steps with all changed endpoint and density factors, rather than assuming that a theorem for ordinary smoothness also holds for semismooth support. The finite source results remain imports and this is not an independent machine-checked proof of the entire factorization algorithm. The source's analytic and finite-arithmetic arguments and the new proof should receive external review before a public unconditional-record claim. No claim is made below first L-parameter 1/3 or for uniform deterministic half-scale factoring. No new workspace constant is asserted.

The proof ledger is accompanied by standalone exact finite tests of the content decomposition and projection identities; such tests cannot prove the asymptotic estimates. The earlier conditional U40 note is historical and is superseded for the written arithmetic transfer by this proof and the U100 proof.

Exact regression receipt: [verification/research/README.md](../verification/research/README.md#keybreak-ordinary-and-semismooth-proof-checks). The new script passed 156 weighted-content comparisons (including 78 capped-parent and 24 exact-parent cases), 36 conditional projection identities, 170,723 common-determinant inequalities, and 90 weighted imprimitive induction identities. The earlier compression checker was rerun successfully. These finite checks are not asymptotic proofs; no Lean, PDF or whole-repository build was performed.
