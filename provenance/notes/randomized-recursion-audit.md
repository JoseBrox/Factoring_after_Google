# Enlarging the root-prime cap in the randomized factoring recurrence

25 November 2026. Source: the pinned Google Research `integer_factorization/paper.pdf`, Git blob `19f36b2f189ed41ec8e112b92aa9b88a96c6bd1e`, read from the hash-verified page-separated extraction in `audit/sources/randomized-paper.txt`. The relevant statements are Definition 2.7 and Lemma 2.8 (pp. 11–14), Lemmas 3.5–3.6 (pp. 18–28), Lemmas 4.2–4.6 (pp. 29–40), and Definition 6.1 with its proof (pp. 44–49).

## Status and precise conclusion

**The exact parameter, path-modulus and recurrence calculations below are proved.** They give a substantially stronger *conditional* randomized target than the earlier coefficient 102. The transfer is supported by the changed-parameter derivations below, including a second adversarial pass through the fixed-root smoothing argument. The original source has not been independently certified here, and finite arithmetic checks cannot certify its analytic estimates.

**Correction found in the adversarial pass:** increasing `tau` to `19/16` while retaining `g=3` is invalid. The root rational first moment uses arithmetic progressions of modulus `a~sqrt(q_0)`, outside its available progression range for those parameters. The repaired candidate below also changes `g` to `43/8`. Its sharper root-density calculation is essential; merely increasing `g` and reusing the old displayed density bound would not justify the transfer. Section 3 gives the failed inequality and the repair explicitly.

The concrete modified schedule has root-prime coefficient `tau=19/16`, rather than `1/3`, and base-pair coefficient `g=43/8`, rather than `3`. It yields the candidate expected-time bound

\[
L_N[1/3,91.4]
\]

with the earlier sparse implementation's conditional workspace bound `L_N[1/3,19]`. The limiting leading constant for its top recurrence is

\[
\frac{358/19}{1-2^{-1/3}}=91.3337532877\ldots.
\]

This decreases the *second* L-parameter. It does not establish a first L-parameter below `1/3`.

The main idea is to accept products of **fewer, larger eligible primes** at the root. This improves the probability of the blind rational-smoothing event. A sharper bound on the moduli formed along a descent path shows that the enlarged prime cap still fits the available progression estimates. Larger prime factors do make descendant factoring calls larger, but the resulting recurrence remains strictly below the top cost.

## 1. Modified algorithm

Write

\[
L=\log N,\quad \ell=\log L,\quad U=(L/\ell)^{1/3},
\quad \Lambda=U\ell,\quad \Xi=L/U.
\]

Retain the source constants `delta=1/2`, `mu=8`, `beta=18`, `eta_0=2`, and descent ratio `rho=3/4`. Set `g=43/8`. In particular, the degree is `d=(1/2+o(1))U`, the factor base is `B=exp((18+o(1))Lambda)`, the base-pair scale is `G=exp((43/8+o(1))Xi)`, and the coefficient scale is `M=exp((8+o(1))Xi)`.

Together with the stated change to g, change the following parameters, using the source's dyadic integer rounding and retaining all actual algebraic and modular output checks:

\[
\tau=\frac{19}{16},\qquad
r_0=\left\lceil\frac{U}{2\tau}\right\rceil
=\left\lceil\frac8{19}U\right\rceil,
\qquad Q_0=\max\{q\in\mathbb N:4q^{2r_0}\le N\}.
\]

Thus `log Q_0=(tau+o(1))Xi` and still `N/8 <= Q_0^(2r_0) <= N/4` for sufficiently large N. Use the same geometric ladder `Y_j`, tuned smoothness grid, special-q boxes, exact weighting, and descent code, but change the pair-separation parameter to

\[
M_{\rm pair}=\left\lceil e^{(19/100)\Lambda}\right\rceil.
\]

This is an analytic parameter used to classify pairs in the proof; it is not an extra sampling loop. Replace the blind root-trial cap by

\[
M_{\rm cap}=\left\lceil8R_{\rm tot}
\exp\big((16/19+\epsilon_N)\widehat\Lambda\big)\right\rceil,
\qquad \epsilon_N=(\log\log N)^{-1/2},
\]

or a sufficiently accurate dyadic version. Keep the sparse parity representation and verified sparse kernel algorithm from `sparse-randomized-factorer.md`. The old `ParamsValid` guards that express concrete finite operations remain; any insufficient asymptotic guard used to invoke a changed estimate must be replaced by the explicit inequalities proved below. Finite exceptions can use the same deterministic fallback as the source.

### Root acceptance probability

Proposition 2.3(2) is parameter-general. On the source's good setup event, its proof gives

\[
\Pr(\text{eligible rational ratio})
\ge \frac18(4r_0\log Q_0)^{-2r_0}-N^{-1/2+o(1)}.
\]

Since `2r_0=(16/19+o(1))U` and `4r_0 log Q_0=(2+o(1))L`, the logarithm of the first term is

\[
-\left(\frac{16}{19}+o(1)\right)\Lambda.
\]

The proposed cap therefore suffices to collect `R_tot=exp((18+o(1))Lambda)` relations with constant probability, provided the widened good-prime/readiness assertion is established. Its leading logarithmic cost is

\[
\log M_{\rm cap}=\left(18+\frac{16}{19}+o(1)\right)\Lambda
=\left(\frac{358}{19}+o(1)\right)\Lambda.
\]

The old cap coefficient was 21. The saving here is a real exponential-in-Lambda reduction in the number of expensive top recursive calls. It is not an improvement obtained from probability amplification alone.

## 2. Exact path-modulus bounds

This is the central new quantitative calculation. Let `t=rho^2=9/16`. Along any valid path, the ancestors occur at levels separated by at least two buckets. If the current depth is `r`, their prime scales and the current scale satisfy

\[
\log p_j\le(\tau t^j+o(1))\Xi\quad(0\le j<r),
\qquad \log q\le(\tau t^r+o(1))\Xi.
\]

The errors are uniform for `r=O(log log N)`. Since `E_q=sqrt(q) exp((2+o(1))Lambda)`, the sum of all lower-order special-box contributions is `O(Lambda log log N)=o(Xi)`.

For the two-point shift in Lemma 4.4, put `Delta_j=|b_j^* a_1-a_j^* b_1|`. Its moduli are

\[
m_1=3\prod_{j<r}\Delta_j\,
\frac{|b_2a_1-a_2b_1|}{q},\qquad m_2=qm_1.
\]

The final quotient is at most `E_q^2/q=exp(O(Lambda))`. Also `Delta_j <= 2E_{p_j}E_q`. Consequently

\[
\frac{\log m_1}{\Xi}
\le \frac\tau2\left(\sum_{j<r}t^j+r t^r\right)+o(1),
\]

and the corresponding bound for `m_2` adds `tau t^r`.

Define `F_r=(sum_{j<r}t^j+r t^r)/2` and `G_r=F_r+t^r`. Their successive differences are exactly

\[
F_{r+1}-F_r=t^r\frac{25-7r}{32},\qquad
G_{r+1}-G_r=t^r\frac{11-7r}{32}.
\]

Thus `F_r` has its maximum at `r=4`, and `G_r` at `r=2`:

\[
\max_rF_r=\frac{40261}{32768},\qquad
\max_rG_r=\frac{181}{128}.
\]

With `tau=19/16`, this proves

\[
\log m_1\le(1.459044+o(1))\Xi,
\qquad
\log m_2\le\left(\frac{3439}{2048}+o(1)\right)\Xi.
\]

### Available progression range

The source defines `Q_AP=floor(y^(u_0/2-1/16))`, with the tuned relation

`4u_0(log y-kappa_0)=log X+O(1)`.

At an algebraic node `X` is either `M a^d/q` or `M a^d`, and `a` lies in a fixed positive fraction of the special-q box. Since `q>=B`, one obtains uniformly

\[
\log Q_{\rm AP}\ge
\left(\frac{\mu+\delta\eta_0+\delta\beta/2}{8}+o(1)\right)\Xi
=\left(\frac{27}{16}+o(1)\right)\Xi.
\]

For completeness, write `log X >= (mu+delta eta_0+o(1))Xi+(d/2-1)log q`. The tuned equation gives `log Q_AP >= log X/8-log y/16+O(1)`, and `log y<=log q`. The coefficient of `log q` is eventually positive; its minimum occurs at `q=B`. The `O(1)` degree-rounding errors then contribute only `O(Lambda)=o(Xi)`.

The conductor comparison has a strict **exact** gap:

\[
\frac{27}{16}-\frac{3439}{2048}=\frac{17}{2048}>0.
\]

Therefore the larger root primes do not force these two-point moduli beyond the source's progression range. The old proof's displayed envelopes `.51` and `.85` were much coarser than the underlying geometric path calculation.

## 3. Other changed envelopes

The following is a transfer audit of the places in the source where its original `tau=1/3` was actually used. These checks are not a replacement for independently certifying the original analytic estimates.

### Fixed-root progression range: the omitted guard and its repair

In the first-moment proof of Lemma 4.3 (source p. 33), fixing `(a,b)` and `g_0` sends the allowed values of `g_1` to the progression

\[
z_{a,b}=z_{\min}+a s.
\]

Its modulus is **a**, not the much smaller pair determinant divided by q. At a root prime in `(Q_0/2,Q_0]`,

\[
\log a=(\tau/2+o(1))\Xi,
\quad
\log z_{a,b}=(g-\tau/2+o(1))\Xi,
\quad
\log Q_{\rm AP}=((g-\tau/2)/8+o(1))\Xi.
\]

Consequently this application needs `g>9tau/2`, with strictness absorbing rounding and lower-order terms. The initial schedule `tau=19/16,g=3` fails: its conductor gap is `-75/256`. With `g=43/8`, the gap is exactly

\[
\frac{g-\tau/2}{8}-\frac\tau2=\frac1{256}>0.
\]

This is an actual correction of a missing hypothesis, not an optional improvement of constants.

### Admissible smoothness parameters and the sharper root density

The root rational value has logarithm

\[
\log((ag_1-bg_0)/q_0)
=\left(g-\frac\tau2+o(1)\right)\Xi
=\left(\frac{153}{32}+o(1)\right)\Xi.
\]

Hence its tuned parameter obeys

\[
\frac{4u_0}{U}=\frac{g-\tau/2}{18}+o(1)
=\frac{17}{64}+o(1).
\]

The source requires `u_0>=U/30`, equivalent asymptotically to `4u_0/U>=2/15`. The exact margin is

\[
\frac{17}{64}-\frac2{15}=\frac{127}{960}>0.
\]

Replace the printed upper root-rational bound `.16U` by `.27U`; the universal admissibility bound `.96U` still holds. Crucially, the root smoothness-density cost is smaller than `.27` because here `u_0 log y=(153/128+o(1))Xi`, so `log(u_0 log y)=(2/3+o(1))ell`. The source's explicit lower bound `nu >= (1/2)(5u_0 log y)^(-4u_0)` therefore gives

\[
\nu_{\rm rat}\ge
\exp\left(-\left(\frac{17}{96}+o(1)\right)\Lambda\right),
\qquad \frac{17}{96}=0.17708333\ldots.
\]

Since `E_q^2/q=exp((4+o(1))Lambda)`, the first-moment calculation gives

\[
\mu_{\rm rat}\ge
\exp\left(\left(4-\frac{17}{96}+o(1)\right)\Lambda\right)
\ge L_N[1/3,3.82],
\]

because `4-17/96-3.82=7/2400>0`. Thus the source's rationally good threshold `|R_q|>=L[3.80]` survives unchanged, although its intermediate displayed density bound `L[-.17]` must be replaced by the sharper asymptotic statement above (or by `L[-.18]` with the exact mean margin recorded).

The root algebraic ratio remains `(4/9+o(1))U` because both the norm height and `log Y_2` scale with tau. The all-node upper bound `<.96U` is unchanged: it follows from `(mu+delta eta_0)/beta + delta/(2rho^2)=17/18<.96`.

### Root rounding thresholds, boundary fibres, and slope bins

For fixed q, all root rational scales lie in `[E_q G/(4q),2E_q G/q]`, an interval of logarithmic length `log 8`. For sufficiently large N, the ceiling defining `u_0` has at most one jump there. On each region with constant `u_0`, the grid index before flooring has derivative in `log X` of magnitude `10u_cap/(4u_0)=(2560/17+o(1))`. The total number of rounding thresholds is at most `(2560/17+o(1))log 8+O(1)<320`, in particular below the source's bound 1000. Within one G-block, `u_0` takes at most two values and the grid index at most two for each, so the at-most-four tuned parameter pairs used in its second moment remain valid.

Keep the original root boundary-fibre cutoff `T_min=ceil(L[-.19] L_G/E_q)`. Its normalized second-moment contribution has coefficient at most

\[
-0.19+\frac{17}{96}+o(1)
=-\frac{31}{2400}+o(1)<-0.01.
\]

The same saving applies to the boundary term in the slope-bin calculation. For interior fibres and determinant `D>=E_q^2 q^{-1} exp(-35ell^2)`, the original interval lower bound `H/X>=L[-.195]` is unchanged: the G and E factors cancel. For smaller D the rough estimate still uses `u'=2`, since `6D(z/H)<=9z/T_min<=L[4.21]<<(y/2)^3`. No extension of the source's `L[-.20]` AP interval range is needed. The original root slope-bin condition `sum N_alpha N_beta<=L[-.18]|R_q|^2` and the later root algebraic mean lower bound `L[3.30]` consequently keep their numerical margins.

The tuned-grid cardinality changes from the printed bound `12L log L` to a harmless `40L log L`; all exceptional-set unions still have only polynomially many members. Bounds such as `(8u_0 log y)^u_0 <= L_N[1/3,.25]` remain valid because `u_0<=.24U` and `log y<=O(Xi)`. In the density proof, replace the dispensable strict bound `5u_0 log y<L` by `5u_0 log y<=C L`; its extra logarithm is `O(u_0)=o(Lambda)` and does not affect `.97`.

### Coefficient widths and conditional mod-N sampling

The ancestor product with two current evaluation vectors has exponent at most

\[
\frac12\sum_{j<r}t^j+t^r
=\frac87-\frac{t^r}{7}<\frac87.
\]

Thus its logarithm is at most `(8tau/7+o(1))Xi=(19/14+o(1))Xi`. Use this envelope in place of `.80` in the conditional polynomial-fibre lemma. Including the optional mod-q condition and the base scale G, the lattice-tile displacement has logarithmic coefficient at most

\[
g+\tau+8\tau/7=\frac{887}{112}<8.
\]

The coefficient box still dominates it with gap `9/112`. Although this is a smaller fixed gap than before, `(9/112)Xi/Lambda` tends to infinity, so it still makes the tile errors negligible compared with every required `exp(-c Lambda)` error. The ratio between the inner and outer coefficient boxes is unchanged because the ancestor product cancels.

The global sampler also remains in range: `log W_cut=(7+o(1))Xi`, hence `log(W_cut/G)=(13/8+o(1))Xi`. Its lattice-volume error is still smaller than `L_N[2/3,-.98]`, sufficient for the printed total-variation target `L_N[2/3,-.5]`. Furthermore `(d-J-4)log G=(43/16+o(1))log N>log N`. The source's leading-coefficient/derivative shift has `log U_0=(21/8+o(1))Xi`, still much larger than log B. The displayed envelopes `3.01`, `4.20`, `4.9`, and `7.40` must be replaced by these inequalities or their slackened numerical forms; their literal old values are not asserted.

For the algebraic local moment, the shift width has leading coefficient at least `8-8tau/7=93/14>6.64`, while its current evaluation coordinate has coefficient at most `tau/2=19/32`. Thus its scalar convolution error is exponentially small on the Xi scale. The extra q-preserving shift has width coefficient at least `8-tau-8tau/7=611/112>5.45`, exceeding the largest q coefficient `19/16`. These are the concrete checks needed when replacing the source's printed shift-width constants.

### Close pairs and rough progression bounds

Increasing `M_pair` from `L[.15]` to `L[.19]` improves the close-pair counting bound in Lemma 3.6(4)(b) to `L[-.18]`, with slack for constants. AP-admissible pairs still have relative interval length at least `L[-.195]`, inside Lemma 3.5's range `L[-.2]`.

For the rough estimate at the remaining close pairs, take

\[
u'=\left\lceil\frac{1.47\Xi}{\log(y/2)}\right\rceil+4.
\]

The `1.47` coefficient is strictly larger than `tau max F_r`. The extra prime factors cover the standalone q and the `B` factor needed for `6m_s(z/H)`. Because `log y>=(17.82+o(1))Lambda`,

\[
u'<.083U.
\]

At algebraic nodes `2u_0>=(.125+o(1))U`, so `u'<=2u_0` holds. This uses the algebraic-node lower bound rather than the weaker universal `u_0>=U/30`. Each rough weight loss is at most `L[.084]`; the two-field moment loss is therefore at most `L[.17]`. Combining it with the close-pair frequency `L[-.18]` leaves a strict saving. The bad-child loss is still at most `L[.084-.93]`, stronger than the source's required `L[-.80]`. Diagonal and exceptional-conductor pairs are unchanged.

These calculations supply the numerical replacements used in the source's concentration proof: all error terms still have a negative fixed coefficient on the Lambda scale, which dominates every requested `exp(-c(log log N)^2)` error. This is needed in addition to the AP conductor and fixed-root checks; merely increasing Q_0 without revisiting them would not justify the result.

### Descendant inputs

Every algebraic integer sent to the recursive factorer satisfies

\[
\log|f(a,b)|\le(\delta\tau/2+o(1))L
=\left(\frac{19}{64}+o(1)\right)L.
\]

Rational cofactors have logarithm at most `(153/32+o(1))Xi`, and determinant factors have logarithm `O(Xi)`. Therefore all descendant recursive inputs are at most `N^(19/64+o(1))`. This replaces the source's convenient `N^(1/10)` bound; the exact code's checks against `sqrt(N)/2` still hold. The product of two algebraic cofactors has exponent at most `19/32+o(1)<1`, retaining the `log_2 N` child-count bound. Tree depth and tree size remain `O(log log N)` and `exp(O((log log N)^2))`. The source's path-telescoping proof uses the same estimates and the same cancellation of smoothness weights. Neither the root trial budget based on the `L[2.75]` mean threshold nor the algebraic trial budget based on `L[2.00]` changes.

### Remaining imported ingredients

The coefficient degree and height, factor-base size, square-obstruction dimension, character-sampling bit size, and exact algebraic square-root extraction are unchanged at leading L scale. Enlarging Q_0 by a fixed coefficient has no effect on their logarithmic-size bounds. Their original algebraic and analytic correctness still has to be accepted or independently checked. In particular, the transfer above does **not** independently prove the source's Siegel-free progression asymptotic, weighted second moments, global readiness or Stark–Chebotarev square certification.

The distinction is precise: the source's lemmas, taken only as black-box statements with their original fixed constants, do **not** imply the modified algorithm's bound. The calculations here recheck the changed inequalities in their proofs, including the additional root guard that initially failed. They give an explicit route to widened versions of those lemmas without asking for a stronger AP modulus formula or a shorter AP interval range. They are not a standalone independent certification of every analytic and conditioning step in the widened lemmas. Accordingly, the complexity claim below remains conditional on the source argument with these derived replacements, together with its algebraic certification and the earlier sparse solver. Passing the arithmetic verifier alone never discharges those dependencies.

## 4. Time recurrence and exact numerical certification

Let `A=358/19`. With an induction majorant of coefficient C, the top ratio-factoring calls cost

\[
L_N[1/3,A+2^{-1/3}C+o(1)].
\]

Descent trials cost at most

\[
L_N[1/3,A+2.05+(19/64)^{1/3}C+o(1)].
\]

Setup, sparse linear algebra and square-root extraction remain below coefficient 38. Thus it suffices that

\[
C>\max\left\{38,
\frac{358/19}{1-2^{-1/3}},
\frac{358/19+2.05}{1-(19/64)^{1/3}}\right\}.
\]

The last threshold is about `62.758`; the top ratio calls dominate. For the rational choice `C=457/5=91.4`, the two recurrence coefficients are approximately `91.38633334` and `81.86508294`, both strictly smaller than C.

The companion script `verify_recursion_budget.py` verifies the crucial strict comparisons using rational arithmetic. In particular, it certifies the first recurrence comparison by

`2(C-A)^3 > C^3`,

and the descendant comparison by

`64(C-A-41/20)^3 > 19 C^3`.

It also verifies the exact path difference identities, their maxima, both conductor gaps, the failed `g=3` root guard, the repaired fibre-width margin, the root density/mean/boundary margins, and rational-root admissibility. These are arithmetic certificates only. They do not certify any analytic estimate or the original paper.

## 5. Two tempting alternatives that do not supply a saving

### Asymmetric rational reconstruction

For uniform `w` in the square subgroup Q_N, the number of possible unit ratios `x/y mod N` with `1<=x<=X` and `1<=y<=Y` is at most `XY`. Therefore

\[
\Pr(\text{a representation exists in the box})\le XY/|Q_N|.
\]

After small factors are removed, `|Q_N|=N^(1-o(1))`. A success probability `exp(-O(Lambda))` therefore requires `XY>=N^(1-o(1))`. At least one of X,Y must be `N^(1/2-o(1))`. Merely skewing the box does not shrink both recursive arguments below sqrt(N). This is a statement about this sampling interface, not a lower bound for factoring.

### Blindness is not preserved by choosing known smooth ratios

Generating x and y from already known prime factors is easy. For the source proof, however, one must also possess a root z of `x/y mod N` whose hidden CRT signs retain the required conditional distribution. Producing that root efficiently is an additional algorithmic problem. Choosing products first does not reproduce the source's uniformly sampled square and its hidden-root guarantee. The reverse construction cannot be treated as a free replacement for the top factor calls.

### Batch gcds among root candidates almost never reuse an eligible prime

This particular reuse proposal has a rigorous obstruction under the actual root-sampling law. Suppose N has no prime factor at most B, and take `T=exp(O(Lambda))` independent blind trials, each retaining at most the two positive coordinates bounded by `sqrt(N)/2`. For any fixed prime `q` in `(Q_0/2,Q_0]`, there are at most `O(N/q)` possible coordinate pairs in that box with q dividing either coordinate. Uniformity of the exposed square in Q_N therefore gives

\[
\Pr(q\text{ divides a retained coordinate in a fixed trial})
\le O\!\left(\frac{N}{q|Q_N|}\right).
\]

Different trials are independent before any filtering. A union bound over trial pairs and eligible primes, using `sum_{q>Q_0/2} q^(-2)=O(1/Q_0)` even when summing over all integers, gives

\[
\Pr(\text{an eligible prime occurs in two trials})
\le O\!\left(\frac{T^2}{Q_0}\left(\frac{N}{|Q_N|}\right)^2\right).
\]

For odd N, `|Q_N|=phi(N)/2^omega(N)`. The roughness assumption implies `omega(N)<=L/log B`, while `N/phi(N)=1+o(1)` because every prime divisor exceeds B. Hence

\[
\log(N/|Q_N|)=O(L/\log B)=o(\Xi).
\]

The displayed collision probability is therefore

\[
\exp\big(-(\tau+o(1))\Xi\big)=o(1).
\]

Accepting only successful relations cannot create a collision absent from the entire capped sample. Thus pairwise gcds, or a product-tree batch-gcd implementation of the same operation, almost never reveal a shared **eligible root prime** within this subexponential batch. This does not rule out batching descent cofactors, changing the sampler, or deliberately arranging shared factors. It specifically rules out the proposed replacement of expensive independent root factorizations by accidental reuse of their eligible primes under the existing blind sampler.

## 6. Why this parameter mechanism does not yield k<1/3

There is a useful *scoped balance obstruction*, not a complexity lower bound. Suppose one keeps the source's polynomial-value and explicit-factor-base architecture, lets degree have log-N power a, factor-base logarithm have power b, and charges reciprocal weighted smoothness density as in Lemma 3.5. The following three costs remain:

1. An explicit factor base of size `exp(L^(b+o(1)))`.
2. At the bottom special-q scale, the algebraic norm contributes smoothness parameter at least order d, giving cost power a in this analysis.
3. The coefficient construction requires `d log G` at least order L and coefficient height at least G. Thus `log M>=L^(1-a+o(1))`; smoothing it over B costs power at least `1-a-b` in the same density analysis.

The resulting certified time power is bounded below by

\[
\max\{b,a,1-a-b\}\ge1/3.
\]

Equality occurs at a=b=1/3. Changing a fixed constant such as tau cannot evade this balance. A successful sub-1/3 construction must remove one of the charged steps: avoid an explicit factor base, obtain relations without the same smoothness density, or build a useful polynomial/auxiliary representation with a different height mechanism. This observation says nothing against those other constructions and does not dismiss a route merely for being factoring-equivalent.

## 7. Practical next audit target

The enlarged-cap schedule is more promising than unproved ECM substitution: it asks for the same types of estimates in the source and exposes exact numerical margins. The remaining highest-value check is a complete independent proof audit of Lemmas 3.5, 4.4 and 4.6, with the widened cap and revised pair threshold in place. A standalone fully checked implementation would also need to replace every hard-coded proof envelope, not just set tau in a single line.
