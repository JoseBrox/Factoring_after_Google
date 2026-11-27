# An intermediate unconditional-route constant 100 without new semismooth concentration

**Later proof checkpoint:** [U100 written proof](keybreak_u100_proof.md) supplies the changed-range argument, including the ordinary covariance and exact recurrence. The conditional statement below is retained as historical development. The new proof uses the pinned source's finite lemmas and unconditional published analytic inputs; independent review and formal verification remain open.

**Status, 27 November 2026:** a conditional changed-parameter transfer and a smaller analytic verification target than [compressed U at 40](keybreak_unconditional_compression.md). It retains KeyBreak's *original* ordinary-count concentration theorem and square-root exceptional-mass recursion. In particular it does not depend on the new weighted semismooth **concentration** estimate proposed in §2 of the 40 note, or on GRH. The changed-range ordinary-count and incoming upper-moment estimates and the source's certificate/computation bounds still require full independent verification. This is not a new unconditional record.

Source: The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 Nov. 2026, 144 pp., [PDF](https://crypto.sjtu.edu.cn/factoring.pdf), SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9; see [pinned-source audit](keybreak_source_audit.md). All source lemma numbers refer to that version.

## 1. What changes and what does not

Retain the source U uniform-box law (B.4)–(B.6), actual conditional-mean incidence weights (B.47), deterministic-profile comparison B.17, and the finite deletion transfer (4.4). Retain the improved additive-large-sieve handling of tiny character sums from §1 of the 40 note, as well as that note's elementary top-pool second-moment bound and broad-band root-shape argument from source H.5. We only need the source's *upper pair moment* for semismooth counts (B.10), not a new semismooth covariance theorem. The same source C.3 ordinary-count proof is used with the guards below.

Let \(D=\log N/\log\log N\), \(\lambda=\log\log N\), \(\Lambda=D^{1/3}\lambda\), \(n=\operatorname{bitlength}N,\ m_b=\operatorname{bitlength}n\). Let \(d\) be the original least odd integer at least 3 with \(d^3m_b\ge n\), \(t=dm_b,\ \Lambda_b=t\log 2\sim\Lambda\).

Use
\[
 b_0=1,\quad \kappa=24,\quad q_*=161/10,\quad U_*=6q_*=483/5,\quad
 k_0=24d,\quad e_B=t,\quad e_0=\lfloor(n-5)/(2k_0)\rfloor-1,
\]
\[
 e_{i+1}=\max(e_B,\lceil 10(e_i+2t)/161\rceil),
 \qquad Y_i=2^{e_i},\quad V_i=Y_i^6 .
\]
Keep the original E, W, H and coefficient distribution of (B.4). For the broad top shapes use (H.18)–(H.19) and the top bands therein with this k0, private parent primes in \((Y_{\min},Y_0]\). Use the subleading pool \(J=2^{m_b^2}\) as in §4 of the 40 note.

The unclamped fixed point is \(2t/(q_*-1)<t\); thus the finite cutoffs strictly decrease above \(e_B\) eventually, and
\[
 j=\frac{\log D}{3\log q_*}+O(1).
\]
No need to make the level count as small as in the original \(q_*=2^{32}\) proof.

## 2. Optimize only the original growing moments

The source uses \(A=4^{j+10}\), but (4.4) only needs \(A/2^j\) to dominate the logarithmic loss of the profile weights. Instead choose the proof parameters
\[
 A=2^{j+10}m_b^3,\quad m=100000A,\quad
 \alpha=\frac{\log 2}{3\log(161/10)},\quad A=D^{\alpha+o(1)} .
\]
In particular \(4\alpha<1/3\) and \(2\alpha<1/3\). This choice avoids any new semismooth concentration theorem. The changes to the estimates C.4–C.9 are solely in the following error ledger; the one-value proxy and the ordinary test remain exactly as in the source.

Keep \(z_{\rm sieve}=R=D^{8A}\), the mesh, the same finite local pattern truncations, and log cutoffs
\[
 \log U=C_U\log(2z_{\rm sieve})(\Lambda+A\log D),\quad
 \log E_{\rm cut}=C_{\rm cut}\log(2z_{\rm sieve})(\Lambda+A\log D)
\]
from C.9 and C.35. Fixed large constants are chosen after the uniform minimum-density bound. At each level use the Bonferroni order
\[
 \nu=\left\lceil(A d+\log Y/\lambda)(\log D)^2\right\rceil
\]
instead of the larger order in C.35.

We check the two critical places.

1. With \(E_\nu=(\sum_{p\le z}p^{-1})^\nu/\nu!\) and \(B_\nu=(1+z)^{\nu+1}\) as in C.4, the elementary Mertens and factorial bounds give \(-\log E_\nu\gg \nu\log D\). The definition of nu implies \(-\log E_\nu\gg m C_\rho\Lambda+\log K\), with the quotient tending to infinity for every fixed \(C_\rho\) and with \(K\le4Y^{12}\). Indeed \(\log\nu\gg\log D\) and \(\log\sum_{p\le z}p^{-1}=O(\log\log D)\), while \(\nu/(A d+\log Y/\lambda)\) has an extra unbounded logarithmic factor. Also
\[
 \log B_\nu=O\big((A^2d+A\log Y/\lambda)(\log D)^3\big)
           =o(d\log Y)
\]
uniformly since \(\log Y\ge\Lambda_b\asymp d\lambda\) and \(A^2/d\to0\) even after logarithmic factors. Thus (C.14), (C.49)–(C.50), and the finite-pattern counts survive division by the smooth-density factors and the m-th roots. The original C.39 uses a larger exponent only because its chosen nu was larger.

2. In (C.20) use the explicit \(\log^2(2z)\) factor of the source's lemma, **not** its optional weaker \(\log^4(2z)\) estimate. The condition \(\gamma\log z\le1/8\) holds because \(\gamma=O(1/d)\). The large primes of the determinant modulus cost a bounded factor because \(\omega(K)z^{-\beta+1/\log z}=o(1)\). For \(S_0=U\) or K, C.19 has \(\log(S_0 E_{\rm cut})/\log y=D^{\alpha+o(1)}\); its saddle-variation term is \(D^{-1/3+2\alpha+o(1)}\) and its remaining terms are no larger. Hence the local-density relative error is
\[
 \eta_{\rm FO}=D^{-1/3+4\alpha+o(1)} .
\]
The Rankin tail is exponentially small relative to the retained mesh as in the original C.20 proof. The C.22 score term \(m\gamma\log(2z)\) is \(D^{-1/3+2\alpha+o(1)}\). The log-archimedean saddle shifts have the same or better margin.

For clarity, \(\gamma_*:=1/3-4\alpha=\log(q_*/16)/(3\log q_*)>1/1449\); use \(\log(161/160)>1/161\) and \(\log(161/10)<3\). Thus the normalized ordinary proxy m-th norm is eventually at most \(D^{-1/3000}\), which suffices for Markov's inequality at any fixed positive threshold with \(m=100000A\). The loss from the m-th root of the uniform-box TV error is negligible since its logarithm is \(-\Omega(d\Lambda)/m\). The principal residual scale C.48 stays \(D^{-4A+O(1)}\). In C.69 the thin-pair/mesh/nonprincipal hierarchy remains strict:
\[
 D^{1/4}\gg D^{1/6}\lambda^2\gg A(\log D)^2 .
\]
The full-content fourth moment C.6 and finite ordinary two-point upper moment B.10 are not high-order estimates and retain their original hypotheses. Consequently the same ordinary residual calculation, if transferred with these explicit margins, yields its original baseline tail \(D^{-3A}\) (we may weaken it to \(D^{-2A}\)). This is the ordinary source theorem C.3 at changed parameters, not a new weighted semismooth residual computation.

## 3. Original exceptional-mass transfer now suffices

B.17 uses only pointwise conditional means, the upper pair moment and positive profiles with within-band ratio bounded by a fixed constant. Its comparison factors are \(L_i\le D^{Ci}\), the normalized incidence second moments are bounded by \(D^C L_i^4\), and the weight normalization ratios are bounded by a polynomial in D. These are precisely the conclusions of the original B.17. The source's bound (4.4) therefore applies with \(T=D^{O(j)}\) and \(\epsilon\le D^{-2A}\), after absorbing the polynomial comparison losses. In particular
\[
 \log\delta_1 \le O(j\log D)-\Omega(A\,2^{-j}\log D)
              \le -\Omega(m_b^3\log D).
\]
All polynomial losses and the extra top Cauchy–Schwarz step are harmless, even after the polynomial union over broad top bands. The field-pool second-moment proof from the 40 note applies unchanged; it does not need top concentration. We need B.13 for each top private band with the actual same environment and weight law, not independent samples for each visited child. The normalized top count bound uses the q=1 unconditioned version of B.4 followed by B.10. The cutoff and incidence calculation in this fallback differs from the 40 route precisely in avoiding the latter's additional semismooth concentration transfer.

## 4. Range and numerical guard ledger

Here all coefficient/endpoint parameters are fixed or explicitly computable. At the top \(\log Y_0/\log M\to1/48\), \(\log V_0/\log M\to1/8\), \(\log Y_1/\log M\to1/(48q_*)\). Thus \(V_0^2/M\to0\) exponentially on log M scale, all B.1 top/band and internal mean-square bounds have positive margins, and the uniform sieve conditions \(K\le B^{1/4}\), \(KY B^3\log B/V=o(1)\) hold for the source mesh \(K=\lceil e^{D^{1/6}\lambda^2}\rceil\). The broad bands are above the next cutoff. The improved character-energy separation guard from the 40 note is \(31/(48q_*)<1\). The original larger separation guard is not silently assumed. All conductor intervals are predetermined and use the local \(x_{-,r}=M/(64Y^7)\).

The coefficient windows have \(\log(HM)=(11+6/\kappa+o(1))d\Lambda_b<12d\Lambda_b\); the root and content divisions and fixed near-zero paddings change each log endpoint by at most \(O(\log Y+d)\). The same C.10 and strengthened C.11 hypotheses hold, because \(\log x_F\asymp d\log Y\), \(\log y/\log Y\) has a positive fixed lower bound, and \(u\asymp d\). All finite geometry/TV errors retain their strict log-height margins. The two remaining high-moment and truncated-divisor comparisons are proved in §2. We use only the ordinary test in C.3; B.9–B.10 continue to treat complete-band semismooth upper moments.

The cutoff guarantees \(\log(2X_i)/\log Y_{i+1}\le U_*d\). In the large-y range the sharp unconditional Dickman comparison gives \(-\log \rho_{\rm alg}\le(32.2+o(1))\Lambda_b\). The worst rational size \(MV_0\) is at most \(\exp((1+3/\kappa+o(1))d\Lambda_b)\), giving cost \((3/8+o(1))\Lambda_b\), also for its cofactor or aggregate band (the extra logarithmic density factor is subleading). Use the new cutoff
\[
 p_{\rm den}=2^{-\lceil(3259/100)t\rceil},\qquad 32.2+3/8<32.59.
\]
Use the **level-specific** density for the source's required large-mean lower bound: for \(\xi=\log Y/\Lambda_b\ge1\),
\[
 \log\mu_{\rm norm}/\Lambda_b
 \ \ge\ 11\xi-(12+6\xi)/3-3/8-o(1)
 \ \ge\ 37/8-o(1)>4.
\]
This covers both ordinary and normalized semismooth upper-moment counts, since a complete band costs only a polynomial factor in D after dividing by its maximum weight. This replaces the original B.12's unnecessarily large numerical lower bound by \(e^{4\Lambda_b}\). Do not use the single global worst density at the bottom, which would give a false mean margin.

The source's exact sampler, field and private-root checks, broad-band root-shape guards, and stopping caps are retained. The value-size sufficient guard before starting an epoch becomes
\[
 500(12d^2m_b+6de_0)\le63(n-1).
\]
It eventually holds because the leading raw value ratio is \(3/\kappa=1/8<63/500\). Numerical subcalls on algebraic values are on strictly smaller inputs at most \(\lceil N^{63/500}\rceil\), checked exactly. Coordinate subcalls keep the original \(\lceil\sqrt{2N}\rceil\) bound. All invalid finite parameter choices use the source's persistent trial-division backup.

## 5. Recurrence

The broad-band shape probability, from the elementary source H.5 transfer in the 40 note, has inverse leading exponent \(2\kappa/3=16\); the shape cap and total number of Search states therefore have coefficient \(s=17\). All raw trials/value calls have coefficient \(v=17+32.59=49.59\). Retained columns, occurrence count and precision have coefficient 1. The source F.9 deterministic direct-work terms have ceilings
\[
 3,\quad3,\quad v+\max(1,2/3),\quad v+2,\quad28,\quad12,
\]
all less than 53. Field pool, growing depth, degree factors and original finite error budgets contribute \(o(\Lambda)\). Coordinate and value recursive branches must be charged separately.

For target C=100, the exact contraction checks are
\[
 (1-17/100)^3>1/2,\qquad
 (1-(4959/100)/100)^3>63/500.
\]
Thus both \(17+2^{-1/3}C<C\) and \(49.59+(63/500)^{1/3}C<C\) are strict. The same input induction and fixed positive epoch-success argument in source Section 6 give the conditional expected-time transfer
\[
 L_N[1/3,100].
\]

**Boundary of the result:** this proof target has the ordinary source covariance, upper semismooth pair moment, and source certificate machinery as remaining changed-range obligations. It no longer needs the new semismooth concentration or linear-incidence transfer of the 40 target. The sharper finite arithmetic and moment bounds are explicit, not a substitution into a fixed-parameter theorem. As this is an independent changed-range audit still in progress, it is not an unconditional theorem, and the numerical comparison with Cogentic 105 does not establish a record. The 100 target is a useful intermediate verification milestone even though 40 is more ambitious.

## 6. Exact finite check receipt

Run [`verification/research/verify_keybreak_fallback.py`](../verification/research/verify_keybreak_fallback.py) with the compression checker alongside it. Locally executed with Python 3.13.5. Tested Git blob `ce9361b129c86f87226d2c82e73e2ea46fd1af65` matches the committed file; SHA-256 `b497b0d76597f7bc46e31e98682e5484ab84a0714e927e2f3740fb00abc1cc19`. All exact rational leading-constant margins and 18 symbolic finite schedules passed (depth range 81–206). The logarithmic inequalities in §2 have written elementary proofs; the script checks their subsequent rational margins, not their asymptotic analytic consequences.
