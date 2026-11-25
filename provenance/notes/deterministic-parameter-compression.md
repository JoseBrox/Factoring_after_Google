# Deterministic factoring: parameter compression towards the 2/3 power

**Historical initial checkpoint.** The analytic transfer and its algebraic/splitting dependencies are now supplied in [the analytic proof](deterministic-analytic-audit.md), [the exact extraction and complexity assembly](deterministic-algebraic-completion.md), [the splitting core](deterministic-splitting-core-audit.md), and [the enumeration/Burgess proof](enumeration-burgess-audit.md). Together these give an ordinary mathematical proof of the 2/3+epsilon bound. The original open-obligation discussion below is retained for provenance; it is superseded by those proofs. This is not machine certification.

2026-11-25. **Status: parameter-transfer checkpoint, not yet an independently proved improvement to general deterministic factoring.** The concrete exponent schedule below passes the scale constraints identified in Sections 7–11 of the pinned source. The required uniform reproof of its analytic and peeling lemmas is still open. Correctness of the verified-exponent output is separate from the runtime claim.

Source: [deterministic_factoring_l34/paper.pdf](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf), hash-verified extraction [run 45666731595](https://github.com/JoseBrox/factoring-algorithms/actions/runs/45666731595), pp. 31–57. The source constructs an order multiple in time exp(3 (ln N)^(3/4)) and then splits using it. Its two-field archimedean unit lattice (Lemmas 7.3–7.5) is particularly relevant to our class-group, Pell/regulator, sparse-relation, finite-algebra and spectral ideas.

## 1. Concrete replacement schedule

Let L=ln N, L2=ln L, κ=ln 2. Use the source's computable rational-power integer rounding e(N;a,b) to implement all exponents below. Fix rational 0<δ<=1/100. For convenience the notation exp(κ L^x) below allows bounded rounding of the power of 2.

| Variable | Source power of L | Proposed power |
|---|---:|---:|
| d=z0 (not exponentiated) | .30 | a=1/3 |
| -ln w | .31 | t=1/3+δ |
| ln K1 | .35 | k=1/3+2δ |
| ln B | .36 | b=1/3+3δ |
| ln A | .44 | c=1/3+6δ |
| ln U | .75 | h=2/3+8δ |
| ln m | .70 | m0=1-a=2/3 |
| ln Xsc | .75 | h |
| smoothness parameter u=ln Xsc/ln B | .39 | r=h-b=1/3+5δ |
| -ln ν0 / ln L | .355 | v=1/3+5δ/2 |
| ln zBr | .37 | j=1/3+4δ |
| Brun truncation order (not exponentiated) | .06 | s=δ |
| auxiliary Euler-decay power | .38 | η=1/3+4δ |

In particular a<t<k<v<b<η<r<c, m0<h, a+c<h, c<m0, j+s<c, m0<2b, m0-v<b, m0-b<k. The source's proof uses gaps between powers, rather than an invariant need for its particular decimal exponents. The displayed choice gives h<3/4, and h tends to 2/3 as δ tends to zero.

Retain the source's definitions of m, P0, cd, Xsc, the root-centered sampling intervals, discrete Gaussian means and widths, Δclose=A K1^(-1/2), and all finite exact output verification. Replace:
- Qmax=exp(3 L^(2/3)), T*=2 K1^(3.5), DSK,1=exp(cLP ln B/(800 L2)), ν1=400 L2/ln B, ν0=L^(-v).
- EBr=exp(-δ L^s L2/2), Erel=exp(-3δ L^s L2/4), with τdiag=Erel^(1/4), δpeel=Erel^(1/8). Scale all remaining numerical constants in the peeling exponent (e.g. .07, .148, .015) by (3δ/4)/.15. In particular µ*=Erel^(7/15).
- In the final output size cap replace 2^(e(N;13,20)) by the rounded 2^(L^(1-b+δ)). All sufficiently large instances should pass because the exponent bit-length is exp(O(L^(1-b) L2)).
- The analytic conductor definitions are for existence proofs only; the algorithm need not enumerate them.

## 2. Scale checks against the source

The following are asymptotic calculations, not a substitute for proving the modified uniform versions of the cited statements.

**Base-m construction and root stability (Lemma 8.1, Lemma 8.2(1),(3), pp.37–41).** We have ln m=(1+o(1))L^m0; ln P0=(1+o(1))L^a; ln U=(κ+o(1))L^h. Since a+c<h and m0<h, the minimal power of 3 used in cd satisfies ln cd=(κ+o(1))L^h, and ln Xsc=(κ+o(1))L^h. In particular cd dominates 4P0 B, A d=o(m), and d A^(d-1)=o(ubar0). The proof of uniform polynomial approximation uses exactly these last inequalities. The true roots have displacement O(K1^(-.95)) on the normalized interval, and dividing by w gives O(K1^(-.90)), since t<k. Bounds on log |Pi*(a/A)| follow from ln(1/w)+O(d ln d)=O(L^t); the relative perturbation and window estimates on pp.40–41 transfer with strict slack. The source's guard on the sum of prime valuations holds since u=L^(r+o(1))=o(L). Also ln Xsc=o(L), so polynomial heights meet the TryPair guards.

**Pure Brun sieve (Lemma 8.2(2), pp.39–41).** The source's coprimality product stays bounded below by 1/4: all excluded primes exceed L^(1/3), and the number of distinct prime factors of k0 k0' is < L^(.76) for this schedule. The source bound using all primes up to L^.80 is then still valid, and improves since the lower cutoff is larger. For the new zBr=exp(L^j) and truncation order ceil(L^s), the inclusion-exclusion error from the tail is exp(-(2s+o(1)) L^s L2), while the number of terms is exp(O(L^s L2)). The largest modulus used in the elementary residue count is at most B^4 zBr^(2 ceil(L^s)), with log O(L^b+L^(j+s))=o(L^c). The short sampling intervals have length Aw=exp((κ+o(1))L^c), so all floor/counting errors are negligible compared to EBr. Weighted Lipschitz sums follow by the original partition argument.

**Gevrey-Mellin smoothing and the greedy Rankin upper bound (Lemmas 8.3–8.4 and 9.1, pp.41–44).** These statements are parameter-general, subject to their explicit input inequalities. The proposed schedule satisfies ln(Y/S) asymptotic to a constant multiple of L^k in the clean windows, and S/(qB) is enormous because ln S is of order L^h and ln q=O(L^m0). The saddle parameter satisfies uY=L^(r+o(1)), so it belongs to [C0,B^.1]. Their polynomial/logarithmic prefactors are immaterial to subsequent strict exponent comparisons.

**Prime-sum and saddle analysis (Lemma 9.2, pp.44–47).** The Landau–Page small conductor proof needs ln T*=O(L^k)=o(ln B/L2), and (1−αY)=O(L2/L^b)=o(ν0). The uniform saddle equation gives λY=(r+o(1))L2, ϕ''(αY) of order uY(ln B)^2, and all cumulant estimates depend only on uY tending to infinity. Replacing ln |Pi*| by O(L^t) in the differentiation argument preserves its O(u^-1) relative estimate because t<b. The low-frequency Euler-product repulsion is of order uY/λY^2, hence exceeds L^η, with η<r. High-frequency prime sums use the same Perron bound, H=L^10, with ν1 or ν0 and the original constants. Since η>k, losses exp(O(L^k)) from the Mellin window remain negligible. **Obligation:** independently establish the stated uniform Edgeworth remainder O(u^-2) and its differentiation bounds; one cannot infer a derivative estimate by differentiating an unspecified O-term.

**Zero-density counts and clean progression asymptotics (Proposition 9.3, pp.47–48).** The same density theorem gives ln |Emed|=O(L^(b-v)), ln |Ehi|=O(L^(m0-v)), since log conductor bounds are O(L^b) and O(L^m0). The number of medium prime divisors removed is at most a polynomial in L times |Emed|. The essential two-prefix decomposition of n in the proof requires q² B²<e^(-.31)Y even for q=Qmax; this holds because m0<h. Its character Cauchy–Schwarz cost is exp(O(L^(m0-b) L2)), and its B² factor and Mellin loss cost exp(O(L^b+L^k)). All are dominated by exp(-c uY) because m0-b<b<r. Consequently the proof's claimed error exp(-c4 L^η) has the same scale slack. This is the most important constraint not to drop when redesigning the schedule.

**Gaussian one- and two-point estimates (Lemmas 9.4–9.5, pp.48–51).** Lemma 9.4 is parameter-general. U≫B^4; the relevant q and shifted values meet the coprimality and positivity conditions under the original exclusions. Its rough-moment loss is exp(O(L^(m0-b) L2)), from (1−α) log(µ/(UA)), not exp(O(L^h)). Since m0-b<k<b, the exclusions for short pairs, repeated prime factors, and discarded roots still give a saving in the original argument. The window and stability bounds use t<k and the clean-pair separation Δclose. Saddle density satisfies log((Z1 Z2)^(-1))=O(L^r L2), as seen from αY=1−O(L2/L^b). Hence diagonal variance terms, including all B^O(1) and rough-moment factors, vanish as exp(-Ω(L^c)), since c>r,b,k.

**Exceptional conductor geometry in the centered Gram proof (Proposition 10.1, pp.52–54).** For medium conductors, the shortest-prefix argument saves a fixed power of DSK,1, whose logarithm has order L^b/L2. The number of such conductors contributes exp(O(L^(b-v))); divisor weights contribute exp(O(L^(b/2))) by the source's bound on sum_{h|d0} h^-1/2; rough-moment losses contribute exp(O(L^(m0-b) L2)). All are negligible compared with the saving. For high conductors the proof saves B^O(-1) by the >B^10 prefix and its splitting into |a-m|, |a'-m|, |a'-a|; the corresponding number and divisor-weight costs are exp(O(L^(m0-v))) and exp(O(L^(m0/2))), both negligible because m0-v<b and m0/2<b. This comparison explains why the high-conductor exclusion cannot simply be suppressed. The remaining short-pair and repeated-prime losses are exp(-Ω(L^k)) and exp(-Ω(L^b)), respectively. The EBr^2 term from the centered cancellation is o(Erel) since δ>3δ/4. The original proof only uses polynomial losses in L in the rescaled peeling inequalities; they are absorbed by exp(-Ω(L^s L2)). **Obligation:** verify the actual weighted conditional sums, including the equal-prime blocks and the exceptional prime exclusion, not merely their power comparisons.

**Spectral projection (Proposition 10.1, pp.54–55).** The deterministic norm identity of the log-weight vector on a clean smooth relation removes the two product constraints. For a unit input vector w_in and projected vector w', the source's case split gives, up to absolute constants,
||w'||² >= const min(1,d/max_i ||wi||²,d/(ln Xsc)^2).
Here ||wi||² is of order u(ln B)^2, with power r+2b=h+b<2h. Thus ||w'||² >= L^(a-2h-o(1)). The normalized expected Gram on the complement of the two log-weight vectors has lower bound of order 1/(du), by the saddle covariance rank-one correction and the root-centered archimedean means. In fact each diagonal of the archimedean mean-difference matrix has size of order L^t, whereas its off-diagonal Frobenius norm is O(d L2)=o(L^t). The same Cauchy–Schwarz argument yields sum π0(a) g_y(a)^2 ≳ d^-1(y0²+||yarch||²). Combining the two bounds yields smallest eigenvalue at least L^(-2h-r-o(1)), with 2h+r=5/3+21δ<3. All Gram, peeling and actual-root replacement errors are superpolynomially smaller. This verifies the polynomial gap comparison, conditional on the source's uniform covariance estimates.

**Extraction (Lemmas 7.3–7.5) and saturation (Lemma 11.1).** These are parameter-general and do not require the particular schedule. The local valuation offset of nonmonic fields, cancellation by the extra top row of ones, and the unit-lattice denominator argument retain their exact identities. TryPair is deterministic and verifies ℓ^Eℓ=1 mod N; its complexity is polynomial in A,B,d,Drow,Pbit, with Pbit=64d³ Drow ceil(L). The subgroup-index argument needs at least B/(6 ln B) certified generator primes; it then gives an exponent multiple for all p−1, with bit length exp(O(L^(1-b) L2)). Trial division up to the same Kidx and its saturation product have this time scale. The source's gcd checks for a−m remain necessary.

## 3. Conditional resulting complexity

If the listed transfer obligations are discharged, Steps 0–3 of Aexp require
exp((4κ+o(1)) L^h) + exp(O(L^(1-b) L2))
bit operations: at most B times 16 ceil(L)^80 U^4 A² calls to a poly(A,B,d,Drow,Pbit) extractor. The certified order multiple is short enough that either the original order splitter or our sparse Gram splitter has smaller time power. Therefore, for every fixed ε>0, taking sufficiently small fixed rational δ with 8δ<ε gives exp(O((ln N)^(2/3+ε))) deterministic worst-case factoring. This conclusion is conditional on the generalized source lemmas and is **not yet a new proved unconditional factoring theorem**. There is no conflict with the source's stated exponent; we are proposing a different parameter schedule, not disputing its weaker bound.

For instance δ=1/120 (within the specified range) gives h=11/15=0.73333...; δ=1/480 gives h=41/60=0.68333.... There is no claim that these schedules are practical for cryptographic sizes. The asymptotic thresholds can be immense.

## 4. A sharp obstruction to a tempting further compression

It is not necessary for U to dominate m just to construct the polynomials. One might try d=L^a for tiny a>0, b≈1/2, A slightly larger than B, U slightly larger than A^d. That would have an apparent time power near 1/2 while ln Xsc is dominated by ln m≈L^(1-a).

But the proof of Proposition 9.3(2) explicitly factors each supported smooth integer into **two** shortest prime prefixes >q and a remaining tail. If q is of size m (let alone Qmax), Xsc≈mU with ln U=o(ln m) does not exceed q². The decomposition is impossible for those large moduli. Replacing the double-prefix Cauchy–Schwarz estimate by a one-prefix bound with a square-root-of-q loss is also insufficient: exp(Ω(L^(1-a))) exceeds exp(O(u)). Thus the near-1/2 schedule does not transfer the existing proof.

Within the schedule class having U dominate both m and A^d, with c>b>k>t>a, the two constraints h≥1−a and h≥a+c>2a force h≥2/3. This is a barrier for this *specific parameter mechanism*, not a lower bound on deterministic factoring, or even on all two-field exponent construction. Escaping it requires a different large-modulus smoothness equidistribution argument, less expensive polynomial-height control, or a non-enumerative certified search. Our short arithmetic circuits, auxiliary orders, tensor/SAT and composite-character methods remain relevant precisely at those interfaces.

## 5. Next proof obligations

1. Reprove the generalized Lemma 9.2(2)–(3) and Proposition 9.3 with all moduli/windows quantified; audit imported prime-sum and zero-density hypotheses.
2. Reprove Lemma 9.5 and Proposition 10.1 with symbolic slack, not numerical decimal substitutions alone. Verify exceptional conductors, the conditioning at prescribed roots, the centered cancellation, and the stopping-time invariant.
3. Audit Lemmas 7.3–7.5 and every output-size guard and exceptional small-N fallback, using the unchanged exact certificates. Only then promote the conditional exp(O(L^(2/3+ε))) statement.
4. Seek an improved large-modulus mean-square estimate or a different certified exponent constructor that bypasses the double-prefix barrier. Do not count a smaller smoothness parameter without the corresponding proof of equidistribution.

The original sparse Gram checkpoint improves a different stage. Combining them is legitimate only after both sets of imported lemmas and new transfers are verified.

