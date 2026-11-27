# Selection bias, restart repair, and growing-depth descent accounting

**Status (27 November 2026):** proved abstract accounting lemmas and a conditional restart repair, with no new factoring exponent asserted. These lemmas specify what a relation-supply analysis must prove. They do not establish the required arithmetic incidence estimates for a growing descent.

## Source and distinction from the source audit

Kasper Nielsen's precursor manuscript, *Theorem U-MF: a Las Vegas factoring algorithm in expected time L_N[2/5]*, [pinned source, §§7 and 9](https://github.com/kasper0406/factoring-connection/blob/351e8eeee142b2b13790cf67c3e8e2e35aaf1f0d/notes/mfU_theorem.md), contains a correct size-biased field-selection calculation in Proposition select and a single-contraction recurrence lemma F_alpha. We generalize those particular accounting arguments below. The Shanghai manuscript *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds* (2026), [primary URL](https://crypto.sjtu.edu.cn/factoring.pdf), could not be retrieved for inspection; see the [source-intake checkpoint](2026-11-27_source_intake_and_closure.md). These are independent extensions of the accessible precursor, **not** corrections to a specific unread Shanghai proof.

The key point is that the law of a selected request is not the uniform distribution over eligible primes or other labels. We can nevertheless sometimes cancel a readiness denominator by matching the selection law to the continuation law.

## 1. Exact incidence transfer after field retention

Consider a finite or countable set of environments \(A\), drawn with law \(\mu\). In factoring applications \(A\) includes the field data, any retained local primes and all public parameters needed to define subsequent sampling. One independent trial chooses \(A\), runs its proposal, and returns a verified factor with probability \(f_A\), a certified row with probability \(s_A\), or neither. The outcomes are disjoint. Set
\[
p=\int(f_A+s_A)\,d\mu(A)>0.
\]
A first-capture procedure repeats fresh independent trials until a factor or row is returned. The *unconditional* probability of retaining a row in an environment belonging to a set \(E\) is
\[
\Pr(\mathrm{row}, A_*\in E)=\frac1p\int_E s_A\,d\mu(A).
\tag{1}
\]
The probability of the factor exit is \(\int f_A\,d\mu/p\). Both follow by summing the geometric series for the failed trials. This is the size-bias identity used in Proposition select of the cited predecessor.

For a row proposal at \(A\), let \(Z_A\) be the nonnegative integer number of its child requests in a bad set \(D_A\); \(D_A\) may depend arbitrarily on \(A\). Define the **raw accepted incidence**
\[
I_A=\mathbb E[1_{\mathrm{row}} Z_A\mid A].
\tag{2}
\]
Conditional on acceptance at \(A\) with \(s_A>0\), the mean number is \(I_A/s_A\). Thus, conditional on the initial retention and without changing \(A\), suppose the next accepted row has the same conditional incidence bound \(I_A/s_A\). Averaging over (1) gives
\[
\mathbb E[1_{\mathrm{retained\ row}} Z_{\mathrm{next}}]
\le \frac1p\int_{\{s_A>0\}} I_A\,d\mu(A).
\tag{3}
\]
For up to \(M_A\) subsequent accepted rows the same estimate holds with \(M_A I_A\) on the right, provided the incidence bound holds for each next row *conditionally on the entire past*. Stop early on verified factors; missing rows contribute zero. No independence of the requests within a row is required. An identical proof works with nonnegative request weights instead of counts.

In particular, the probability of any bad request is at most the integrated count in (3), or its \(M_A\)-row version, by the elementary union bound. The numerator is the *raw accepted incidence* with respect to the same sampling law that determined \(s_A\). The cancellation does not follow merely from the density of bad labels in a uniformly sampled universe.

### Failure modes

1. Let \(A\) be uniform on \(1,\ldots,m\), let \(D_A=\{A\}\), and always request label \(A\). Every bad set has uniform density \(1/m\), and the marginal request label is uniform. Yet every request is bad. A joint conditional law, not its marginals, is needed.
2. Take two environments of equal mass. Their initial retention probabilities are \(1\) and \(1/10\); their subsequent row probabilities are \(1/1000\) and \(1/10\), respectively. The first environment is overwhelmingly favored by retention but is far less ready for continuation. There is no cancellation of the second denominator. This illustrates why a changed descent rule must either prove matching readiness or account for the mismatch.

For deeper descents the same argument may be used conditionally on a parent history, but only if the law defining the raw incidence matches the retention at that parent. Applying (3) repeatedly without this check is not justified.

## 2. Generalized first-capture cost ledger and a restart repair

Let \(C=\mathbb E[\text{cost of one initial trial}]\), including failures. Fresh independent trials have expected first-capture cost \(C/p\): whether trial \(i\) is reached is independent of its own cost, even if that cost correlates with its outcome.

Suppose that at retained environment \(A\) the continuation has the following certified bounds:

- At most \(M_A\) accepted rows are needed per round.
- At each row-search attempt, conditional on the entire current history, the mean cost is at most \(c_A\), and the probability of a row or immediate verified factor is at least \(r_A>0\).
- The expected certification cost after collecting a round is at most \(d_A\), and each completed round yields a verified factor with conditional probability at least \(\eta_A>0\), given its entry history.

The factor outcome always terminates. From the conditional geometric tail bound, the expected cost of collecting one accepted row or exiting is at most \(c_A/r_A\). At most \(M_A\) such collections and one certification are needed per round. Summing over reached rounds in the same manner, the conditional expected continuation cost is at most
\[
R_A=\frac{M_Ac_A/r_A+d_A}{\eta_A}.
\tag{4}
\]
These estimates allow history-dependent attempt costs and distributions. For the conditional tail argument, the success bound is required at the start of each attempt or round, not only on average over histories.

The complete expected cost is bounded by
\[
\frac{C+\int s_A R_A\,d\mu(A)}{p}.
\tag{5}
\]
This extends Proposition select's uniform-cost, matching-readiness case. If \(r_A\ge\kappa s_A\) and \(\eta_A\ge\eta_0>0\), then
\[
\int s_A R_A\,d\mu(A)
\le \eta_0^{-1}\left(\kappa^{-1}\int_{\{s_A>0\}} M_Ac_A\,d\mu(A)
 +\int s_A d_A\,d\mu(A)\right).
\tag{6}
\]
One can therefore use an integrable environmental cost envelope rather than a worst-field bound. If \(r_A/s_A\) varies, its reciprocal appears inside the integral. There is no general bound merely in terms of the mean of \(r_A/s_A\).

### A repair when readiness holds only on sufficiently much selected mass

Suppose the bounds in (4) are proved only on a set of good environments \(G_0\), which need not be efficiently recognizable. Outside \(G_0\), the continuation may have unbounded expected cost or fail to terminate. Suppose
\[
\frac{\int f_A\,d\mu+\int_{G_0}s_A\,d\mu}{p}\ge\gamma>0,
\qquad
W=\frac1p\int_{G_0}s_A R_A\,d\mu<\infty .
\tag{7}
\]
Take a known deterministic integer operation cap \(Q\ge\max(1,2W/\gamma)\) (a proved upper bound for \(W\) suffices). After each first-capture, return a verified factor immediately if one was found. Otherwise run the continuation for at most \(Q\) bit operations. If it has not returned a verified factor, discard the environment and start afresh. The cap is on the actual computation, not only successful calls.

By Markov's inequality applied to the subprobability law of good retained rows, the probability of timing out on such a row is at most \(W/Q\). Thus the cycle success probability is at least \(\gamma/2\), and its expected cost is at most \(C/p+Q\). The total expected cost is at most
\[
\frac{2}{\gamma}\left(\frac C p+Q\right).
\tag{8}
\]
Fresh cycles, or the same bounds uniformly conditional on the past, suffice. Verification of every output and almost-sure termination make this a Las Vegas repair. It does not require recognizing good environments. If \(\gamma^{-1}=L_N[\alpha,o(1)]\) and the other quantities have the desired leading exponent, this repair preserves that leading exponent. If \(\gamma\) itself has a significant subexponential penalty, it must be charged explicitly.

A crucial qualification: (7) requires **selected** good mass, not raw good-environment probability. For instance, good environments may occupy 99 percent of \(\mu\) but have much smaller \(s_A\) than the rest. Also a computable cap or explicit bound is needed; mere finiteness of an unknown expectation does not specify this capped algorithm.

## 3. Adaptive branching without a fixed descent depth

Let a subproblem state \(x\) have a positive potential \(V(x)\ge1\). A node performs local work of nonnegative cost, then creates a finite collection of child subproblems. Each child is counted with multiplicity, including repeated requests, unless actual caching eliminates the request. Let \(\mathcal H\) denote the full history at node entry, including the state \(x\).

Assume the uniform conditional inequalities
\[
\mathbb E[C_x\mid\mathcal H]\le aV(x),\qquad
\mathbb E\left[\sum_{y\ {\rm child}}V(y)\mid\mathcal H\right]\le\rho V(x),
\quad 0\le\rho<1 .
\tag{9}
\]
Here \(C_x\) is all local work excluding recursively charged child work. The inequalities must apply to an actually implemented exploration (or an explicitly defined tree-valued oracle algorithm whose implementation and transcript invariance have been proved). In a sequential implementation the children may be discovered during adaptive processing: then the second bound refers to their eventual total conditional on node entry, including all unsuccessful generation work in the first bound. It must not omit requests made after earlier child outcomes.

Under these hypotheses the expected total work is at most
\[
aV(x_0)/(1-\rho).
\tag{10}
\]
Indeed, for each non-root node take the conditional expectation in (9) and sum over nodes at a given depth, using nonnegative summation. The expected total potential at depth \(j\) is at most \(\rho^j V(x_0)\), so summing the work bound over all generations yields (10). Equivalently, one may use a queue of pending subproblems and telescope a one-step potential drift for an exploration with children announced at processing time. The generation proof does not require sibling independence or a deterministic upper bound on depth. The bound also implies the expected total number of created nodes is finite since \(V\ge1\). If local work terminates almost surely and leaves are validly solved, the complete recursion terminates almost surely. Correctness still requires the actual algebraic descent identities and verified outputs.

This lemma handles growing depth without multiplying a worst-case loss once per possible level. It also identifies the obligation if the descent ratios approach one: total child potential must contract, not merely individual problem sizes.

### Heterogeneous subcall sizes: exact leading-constant transfer

Let \(t=\ln N\), \(F_\alpha(t)=t^\alpha(\ln t)^{1-\alpha}\), \(0<\alpha<1\), and consider a verified recursive algorithm with finite small-input costs. Suppose its own expected work is at most \(\exp((\beta_0+o(1))F_\alpha(t))\), and all recursive calls fall into finitely many classes \(j\), with uniform expected counts at most \(\exp((\beta_j+o(1))F_\alpha(t))\) and input logarithms at most \((\theta_j+o(1))t\) for fixed \(0<\theta_j<1\). Counts include every actual call, unsuccessful rounds and oracle calls, not only a successful certificate. Calls may be adaptive; the recursive cost bound must hold conditional on the actual chosen input and history, for instance by fresh independent subcall coins and an exact-output oracle substitution proof. Assume strict shrinking for sufficiently large inputs, and finite termination of the local work and base cases.

Then worst-case expected cost is at most \(L_N[\alpha,c]\), in the limsup leading-constant sense, with
\[
c=\max\left(\beta_0,\max_j\frac{\beta_j}{1-\theta_j^\alpha}\right).
\tag{11}
\]
For any fixed \(\varepsilon>0\), use \(V(N)=K\exp((c+\varepsilon)F_\alpha(\ln N))\), extended monotonically at small inputs and chosen at least 1. The \(j\)-th expected contribution of child potentials divided by \(V(N)\) is at most
\[
\exp\left(\left[\beta_j-(c+\varepsilon)(1-\theta_j^\alpha)+o(1)\right]F_\alpha(t)\right)=o(1).
\]
The own-work ratio also tends to zero. For all sufficiently large inputs their sum is at most one (even one half); choose \(K\) to handle the finite base cases, and use strong induction on input size. This proves the bound with \(c+\varepsilon\), and then the limsup statement. A fixed polynomial prefactor is absorbed into the \(o(1)\). This is an extension of precursor lemma F_alpha to adaptive, size-stratified recurrences: it avoids combining the largest expected call count with the slowest shrinkage when those occur in different classes.

### Near-unit shrinkage and a growing ladder

Formula (11) cannot simply be applied with a growing number of classes and ratios tending to one. For a parent of log-size \(t\) and child of log-size \(t-d\), where \(0<d=o(t)\), elementary differentiation gives
\[
F_\alpha(t)-F_\alpha(t-d)
=(\alpha+o(1))\,dF_\alpha(t)/t.
\tag{12}
\]
The error is uniform in \(d/t=o(1)\) and follows from the mean value theorem and \(F_\alpha'(t)=F_\alpha(t)(\alpha+(1-\alpha)/\ln t)/t\).

For \(V=\exp(cF_\alpha(t))\), the precise expected weighted child count to bound is
\[
\mathbb E\left[\sum_y
   \exp(-c[F_\alpha(t)-F_\alpha(\ln y)])\mid\mathcal H\right].
\tag{13}
\]
A bound by a uniform \(\rho<1\) suffices in (9), regardless of the depth. For \(d=o(t/F_\alpha(t))\), the weight of such a child tends to one, so merely showing strict shrinkage by that amount cannot justify a constant contraction with branching at least one in expectation. This is a limitation of the one-step potential argument, not a lower bound on descent or a refutation of a growing-ladder analysis; multi-step amortization, caching, or a different potential may repair it.

## 4. Research integration

This is a concrete way to audit and potentially repair proofs with selected-field and selected-request readiness issues:

1. Identify the actual retention law and raw accepted child incidences. Use (3) only where the distributions match, with a conditional bound if the history changes the law.
2. Check weighted good mass, not unweighted density. When only a positive fraction of selected environments is ready, (7)–(8) replace unjustified all-environment expectations by a valid capped Las Vegas strategy.
3. Charge the exact conditional expected weighted branching (13); for fixed classes use (11), not a worst-count/worst-size envelope if those are disjoint.
4. Prove the algebraic certification, reconstruction, and fruitfulness separately. The cost lemmas do not supply these or the missing arithmetic estimates.

A one-third or better theorem would still need arithmetic control strong enough for these bounds on its actual incidence law. No such transfer from the Shanghai paper is made here. The next step after obtaining the exact PDF is to map each of its descent levels and retry events to (1)–(13) and check all uniformity and constant claims.
