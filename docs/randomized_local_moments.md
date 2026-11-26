# Enlarged local conditional moment transfer

**Status:** written transfer proof for the algebraic-node and root-algebraic
moment assertions of source Lemma 4.4, conditional on QRH and on the
explicit classical two-dimensional lattice and homogeneous linear-form
lemmas described below. The rational-root smoothing assertion (source
Lemma 4.3), complete setup sampler, and full Lean certification remain
separate. In particular this is not yet an unconditional proof of C1.

Use the exact parameter ranges and notation of the randomized manuscript,
and [the fibre-coupling proof](randomized_fibre_coupling.md). The
[weighted AP proof](qrh_weighted_progressions.md) and
[rough/bad-child proof](weighted_rough_bad_child.md) give the uniform
estimates and tuned-scale comparisons; under QRH the actual source
exceptional conductor set is empty. We use the pinned source's elementary
Proposition 2.3(1) (Lagrange–Gauss reduced-basis inequalities) and
Proposition 2.4 (comparison of the discrete homogeneous linear form
with its continuous unimodal density). The latter has no fixed
factoring parameter: its hypotheses are primitivity of \((a,b)\),
\(n\ge1\), and \(W_0\ge4n\max(|a|,|b|)\). Its proof is the
finite convolution and progression-Riemann-sum argument on pp. 51–52
of the pinned PDF; these lemmas still need kernel verification here.

## 1. Geometry with no exceptional conductors

Let \(E=E_q\), \(A_0\) be the primitive points in the non-skewed
special-q box, and \(A_{\rm alg}\) the points passing the source's
gcd, wedge and capped-powerful-part guards.
Lagrange–Gauss gives a half-open tile of the special-q lattice
of diameter \(O(Ee^{-1.49\Lambda})\), since
\(\lambda_1\ge\sqrt q/S_{\rm skew}\) and
\(\lambda_2\le(2/\sqrt3)q/\lambda_1\). The tile-area comparison
and Möbius inversion of source Lemma 3.6(2) therefore give
\[
 |A_0|=(6/\pi^2+o(1))E^2/(32q),\qquad
 E^2/q=e^{(4+o(1))\Lambda}.
\]
These estimates use only \(E<q\), the non-skewness bound, and
\(E/(\sqrt q\,S_{\rm skew})=e^{(1.5+o(1))\Lambda}\),
all valid in the enlarged range. For the primitive count, sum the
area approximation over \(e\le e^{.5\Lambda}\) with the Möbius
weight; the tail is bounded by the reduced-basis coordinate count
\(O(E^2/(qe^2)+E/(e\lambda_1))\) summed over larger e. This
gives the same \(O(e^{-.5\Lambda})\) relative error as in the source.

For any \(m\) coprime to q and a primitive linear congruence
\(u a-v b=0\bmod m\), the joint sublattice has index qm.
In a reduced basis, primitive points with second coordinate zero
contribute at most one; the rest contribute at most
\(20E^2/(qm)\), by the two coordinate bounds
\(|z_i|\le2E/\|w_i\|\). When \(m>E^2/q\), two distinct
primitive points would have determinant divisible by qm but
absolute determinant less than \(E^2\), impossible.
Thus the count is at most \(20E^2/(qm)+1\), or at most one
when \(m>E^2/q\). This is precisely source inequality (3.2).

The source's remaining guard estimates now use no conductor
pruning:
* A prime divisor of N is bigger than B, hence bigger than
  \(E^2/q\); the gcd-to-N guard removes only \(O(L)\) points.
* Failure of an ancestor wedge confines the point to a strip of
  width \(O(E/M_{\rm wed})\), unless the slope of the ancestor
  is outside the possible box range, in which case it cannot fail.
  Tiling bounds the total relative count over \(O(\ell)\)
  ancestors by \(O(\ell/M_{\rm wed})+O(\ell e^{-1.49\Lambda})
  =O(e^{-44\ell^2})\).
* For the powerful-part guard, the first product exceeding
  \(K_0\) is a powerful integer between \(K_0\) and \(K_0H_0\).
  Such integers have the form \(u^2v^3\) with v squarefree.
  Their number up to X is at most \(\zeta(3/2)\sqrt X\), and
  their reciprocal tail beyond K0 is \(O(K_0^{-1/2})\).
  Applying the sublattice bound therefore removes at most
  \(O(\ell)(E^2/(q\sqrt{K_0})+\sqrt{K_0H_0})\) points,
  or relative \(O(e^{-78\ell^2})\).
* For the remaining gcd guard, for each of the forbidden integers
  \(Y\) (ancestor product or ancestor determinant product), the
  number of its distinct prime factors is \(O(L\ell^2)\).
  Remove points where a prime \(p>K_0,\ p\ne q\) dividing Y
  divides the current determinant, or where a power \(p^e>H_0\)
  of a prime \(p\le K_0\) divides it. The sublattice bound makes
  this relative \(O(e^{-150\ell^2})\).
  The powerful part of the remaining gcd is at most K0. For the
  squarefree part put \(S(a)=\sum_{p\mid Y,\ p\le K_0}
    (\log p){\bf1}_{p\mid\Delta_t(a)}\).
  Expand its m-th moment at \(m=\lceil200\ell\rceil\).
  Group the tuples of primes by their set of k distinct primes:
  the count is at most \(k^m\) for that set, and the corresponding
  congruence has modulus the product of those k primes, at most
  \(K_0^m=e^{O(\ell^3)}=o(E^2/q)\). The sublattice bound gives
  a constant times the reciprocal of that product as its
  relative probability. With
  \(A=\sum_{p\mid Y,p\le K_0}(\log p)/p=O(\ell)\)
  (split at \(L^4\), use PNT below and \(\omega(Y)=O(L\ell^2)\)
  above), the moment is at most \(C(m\log K_0)^m e^{A/\log K_0}\).
  Markov at threshold \(L^{1/4}/2\) yields
  \(O(e^{-39\ell^2})\); multiplying by the powerful part K0
  preserves the required \(E_{\rm gcd}=e^{L^{1/4}+o(1)}\) cap.

These are the same effective estimates as the source's proof
through the definition of \(A_{0,\rm clean}\), with a larger
polynomial bound on \(\omega(Y)\) harmless. Since
\(S_{\rm bad}=\varnothing\), take \(A_{\rm clean}=A_{\rm alg}\):
there is no additional pruning. Thus
\[
 |A_{\rm clean}|\ge(1-e^{-34\ell^2})|A_0|.
 \tag{1}
\]
For a fixed point a2, the points a1 with
\(0<|\det(a_1,a_2)|<E^2/M_{\rm pair}\) lie in a strip of
width \(O(E/M_{\rm pair})\). The same tile argument gives at
most an \(e^{-.18\Lambda}\) fraction of clean points, since
\(M_{\rm pair}=e^{(.19+o(1))\Lambda}\). Every clean point has
a distinct well-separated partner for sufficiently large N.
All other distinct pairs have determinant at least q.

## 2. Conditional shift, interval size, and gcd guards

Fix the exact valid history and use the source's notation:
\(P_{\rm anc}=\prod_{t<r}(b_t^*X-a_t^*Y)\), \(n=d-r-1\).
For two distinct clean points \(a_1,a_2\) shift the polynomial by
\[
 3P_{\rm anc}(X,Y)(b_2X-a_2Y)
     \sum_{s=0}^{n} w_s X^s(-Y)^{n-s},\qquad
 w_s\in[-W_0,W_0]\cap\mathbb Z.
\]
This fixes every ancestor evaluation and the value at a2.
It preserves the mod-q slice of the active field because
\(a_2\equiv b_2r_q\bmod q\). Set
\(K_{\rm sh}=\prod_{t<r}(2a_t^*)\,2E\) and
\(W_0=\lfloor e^{-32\ell^2}W/((d+1)\Lambda_0K_{\rm sh})\rfloor\).
The coefficient displacement has Lipschitz exponent at most
\(e^{-32\ell^2}\). The proved fibre tail and translation
bounds apply. In particular \(W_0\ge e^{(8-19/14-o(1))\Xi}\),
whereas \(a_1\le E\le e^{(19/32+o(1))\Xi}\); this verifies
\(W_0\gg4na_1\) and makes the error in Proposition 2.4
exponentially small on the Xi scale.

Writing \(X_s=M a_1^d/q\) or \(M a_1^d\) as appropriate, the
evaluation on the shifted form is
\(z_0\pm m_s S_n(w)\), where
\(z_0=X_s(1+O(K_\xi^{-1}))\), and \(m_1,m_2\) are exactly
the moduli in the manuscript's equation (pathmoduli).
The shift distribution is an \(o(e^{-c\Lambda})\)-accurate
mixture of uniform progressions of half-length R, with
nonnegative weights \((2R+1)(\widetilde q_n(R)-
\widetilde q_n(R+1))\). This follows from Proposition 2.4,
with total mixture mass \(1+o(e^{-c\Lambda})\).
The density is bounded above by \(1/(2W_0a_1^n)\).
Use \(R_{\min}=\lfloor e^{-32\ell^2}W_0a_1^n\rfloor\).

For \(R\ge R_{\min}\), put \(H=2m_sR\). By the ancestor
wedge guards, \(|\Delta_t|\ge a_t^*E/M_{\rm wed}\); the
well-separated determinant is at least \(E^2/M_{\rm pair}\).
Together with the bound on W0 these give
\[
 e^{-.195\Lambda}\le H/X_s\le e^{-60\ell^2}
 \tag{2}
\]
for a well-separated pair. In detail the lower bound loses at
most the factor \(M_{\rm pair}=e^{(.19+o(1))\Lambda}\), the
\(O(\ell)\) ancestor factors \(M_{\rm wed}\), powers of two
and polynomial factors, \(W/M=e^{-30\ell^2+O(1)}\), and the
two \(e^{-32\ell^2}\) factors. All losses other than
\(M_{\rm pair}\) have log \(O(\ell^3)=o(\Lambda)\).
For the upper bound use
\(|\Delta_t|\le2E a_t^*\), \(|\det(a_1,a_2)|\le E^2\),
\(a_1\asymp E\), and the geometric sum
\(\sum_{s=0}^n a_1^s b_1^{n-s}\le(3/2)a_1^n\).
Equivalently cancel the polynomial evaluation factors directly
against \(K_{\rm sh}\); \(W/M\) and \(e^{-32\ell^2}\) give
the strict upper margin. For the close pair the determinant
lower bound q instead gives \(H/X_s\ge e^{-4.05\Lambda}\).

For either field, if q divides both the centered evaluation
and its progression modulus, the weight is zero throughout
that progression because \(q>y\). Otherwise q is absent from
their gcd; 3 is absent by the mod-3 irreducibility guard.
A prime power dividing an ancestor determinant and the current
form value also divides the corresponding ancestor form value:
use primitivity and homogeneous evaluation, choosing the
coordinate invertible modulo that prime. The ancestor gcd
guard then bounds this prime-to-q part by \(E_{\rm gcd}\)
per ancestor. The remaining determinant quotient is at most
\(E^2/q\). Thus every nonzero-weight case satisfies
\(g_{\rm AP}\le (E^2/q)E_{\rm gcd}^{\,r}
 \le e^{4.02\Lambda}<\min(B,y^{.3})\).
The exact tuned-scale center error is \(O(K_\xi^{-1})\),
so short-scale density continuity applies to z0.

The manuscript's verified rational exponent comparisons give
\(\log m_2/\Xi\le3439/2048+o(1)\) whereas
\(\log Q_{\rm AP}/\Xi\ge27/16+o(1)\).
With (2), the uniform weighted asymptotic therefore applies on
every long well-separated progression. For close pairs apply
the rough bound with
\(u'=\lceil1.47\Xi/\log(y/2)\rceil+4<2u\):
the m1 bound is \(\tau\max F_r<1.47\), the extra four
factors cover q and \(e^{4.05\Lambda}\) since
\(\log q/\log y<16/9+o(1)\) and \(\log y\ge17.82\Lambda+o(\Lambda)\).
The resulting rough loss is at most \(e^{.084\Lambda}\)
per field.

The short radii \(R<R_{\min}\) do not require an AP theorem
at arbitrary short length. Their contribution is at most
\(\widetilde q_n(0)\sum_{|t|\le R_{\min}}\widetilde w(z_0+m_st)\).
Apply the corresponding long-radius bound at \(R_{\min}\);
since \(\widetilde q_n(0)(2R_{\min}+1)=O(e^{-32\ell^2})\),
the resulting contribution has the same relative suppression
times the density (and the rough loss in the close case).
This avoids the invalid use of a bare probability of short
radii when the density itself is exponentially small.

## 3. First and second conditional moments

Let \(U_a,V_a\) be the weights in the active and opposite
fields, under the independent unconditioned-mod-N slice
distributions. Applying the long-radius weighted AP bound,
the short-radius estimate and the translation comparison
to the shift above gives
\[
 \mathbb E[U_{a_1}U_{a_2}]
 \le (1+O(e^{-27\ell^2}))\nu_1(a_1)\mathbb E U_{a_2}
       +O(e^{-5\Lambda})
\]
for well-separated pairs, and the same inequality with
\(e^{.084\Lambda}\nu_1(a_1)\) in the close case.
The same argument with the other weight omitted bounds the
individual first moments. Repeat for \(V\).
For matching first-moment lower bounds, the only possible
obstruction is q-divisibility of the centered value.
At most one ancestor is collinear modulo q, because the
valid history excludes q from \(R_{\rm anc}\).
The sublattice of index \(q^2\) shows at most one primitive
current point has q² dividing an ancestor determinant.
Outside that possible exceptional point, the source's shifts
\(3q^{1-s}P_{\rm anc}w_0Y^{d-r}\) in the active field,
with \(s=v_q(P_{\rm anc}(a_1))\in\{0,1\}\), and
\(3P_{\rm anc}w_0Y^{d-r}\) in the opposite field when
\(q\nmid P_{\rm anc}(a_1)\), vary the corresponding divided
evaluation by a unit modulo q. Their width
\(W/(16(d+1)\Lambda_0q^{1-s}\prod 2a_t^*)\) has Xi
coefficient at least \(8-\tau-19/14>5\), hence exceeds q.
The translation comparison bounds the unwanted divisibility
probability by \(O(e^{-5\Lambda})\).
When the opposite-field shift coefficient is zero modulo q,
the relevant ancestor opposite-field value is nonzero modulo q
by the valid-history assumption, giving nondivisibility directly.

Since each density is at least \(e^{-.97\Lambda}\),
the additive translation errors are negligible relative to the
individual or pairwise main terms. In the two-field case the
product slice distribution is independent, and the estimates
multiply. Equation (1) and tuned comparability within
\(L^{10}\) give
\[
 \mu=\sum_{a\in A_0}\nu_1(a)\nu_2(a)\ge e^{2.04\Lambda},
 \qquad
 \mathbb E Z_{\rm clean}=(1+O(e^{-27\ell^2}))\mu .
\]
Here the strict mean margin uses the manuscript's sharper actual-node
bound \(4u/U\le17/18+o(1)\) (in its admissibility calculation),
not the abstract admissibility ceiling \(.96\). Together with
\(\log(5u\log y)\le\ell+O(1)\) this gives the density lower bound
\(e^{-(17/18+o(1))\Lambda}\) per field. The primitive-box
constant is absorbed by the strict margin \(4-17/9>2.04\).
For the variance, well-separated pairs contribute at most
\(1+O(e^{-27\ell^2})\) times the product of their means.
The diagonal and the at-most-one exceptional point
contribute \(O(\mu)\), using \(0\le X_a\le1\).
The close-pair fraction \(e^{-.18\Lambda}\), two-field loss
\(e^{.168\Lambda}\), and polynomial density comparability
give \(O(e^{-.01\Lambda})\mu^2\).
There are no conductor-excluded pairs. Hence
\(\operatorname{Var} Z_{\rm clean}=O(e^{-27\ell^2})\mu^2\),
which by Chebyshev gives the desired
\(\Pr(Z_{\rm clean}<\mu/2)\le e^{-25\ell^2}\) eventually,
and the first-moment upper bound with \(e^{-26\ell^2}\).

## 4. Bad children and the root-algebraic moment

Apply the proved rough bad-child estimate along a well-separated
partner shift, using the stronger prefix condition (satisfied
by the same u' above). The loss per field is at most
\(e^{.084\Lambda}\) and the rarity factor \(e^{-.93\Lambda}\).
Conditioning on the other field puts its primes in the
forbidden integer, which remains bounded by \(N^{J^2+2J}\)
from the exact history size bounds. This accounts also for
cross-field reuse. The geometric bad-prime argument needs only
\(\max(a,b)\ge\sqrt y\), not the stronger condition
\(\max(a,b)\ge y\); see the corrected proof in the rough
bad-child note. The weaker condition holds in every actual
special-q box even at the widened upper nodes.
Thus summing the local weighted bad-child expectations costs
\(O(e^{-.84\Lambda})\mu\), stronger than \(e^{-.4\Lambda}\mu\).
The short-radius portion is treated by the same cumulative
bound at \(R_{\min}\), now for the nonnegative bad-child weight.

At a rationally good root, use its given slope-bin set
\(\mathcal R_q\), with at least \(e^{3.80\Lambda}\) points and
adjacent-bin fraction at most \(e^{-.18\Lambda}\).
For the single-field mean shift no ancestor factors are needed;
for a pair use \(r=0\) in the argument above.
For nonadjacent bins the determinant is at least a fixed
constant times \(E^2/M_{\rm bins}\) and (2) holds.
For adjacent bins use the rough bound with u'=2: the
modulus is at most \(O(E^2)\), and
\((y/2)^3\ge e^{(3\cdot9/16+o(1))\log q}\gg
6m_s(z_0/H)\) since \(m_s\le3E^2\),
\(H/z_0\ge e^{-4.05\Lambda}\), and
\(\log q/\log y\le16/9+o(1)\) at the root.
The resulting loss is polynomial in L. The density at least
\(e^{-(.96+o(1))\Lambda}\) already gives the required
\(\mu_{\rm root}\ge e^{2.80\Lambda}\), without invoking the
source's stronger root-specific density estimate.
The same first/second-moment and bad-child argument yields
the asserted concentration and rarity, conditional on the
rationally good root set.

Finally the proved mod-N conditioning comparison applies to
each required function of one or two evaluations, because
the ancestor product plus both points has Xi coefficient
at most \(8\tau/7=19/14<34/25\).
Its additive \(O(e^{-5\Lambda})\) error is negligible even
relative to products of four densities (each at least
\(e^{-.97\Lambda}\)). For the bad-child functions, the
conditional forbidden integer on one side is determined by
the other field, so the same uniform comparison applies
after that conditioning. This transfers the preceding
moment estimates to the mod-N slice distributions.

## Remaining boundary

This proves the written local-moment transfer under the named
classical and analytic inputs and the precise valid-history
hypotheses. The implication from these moments to global
readiness is the weighted backward argument in the fibre note.
The rational-root first and second moment over the random base
pair (Lemma 4.3), sampler approximation and setup probability,
exact realization of the local history predicates in the
executable tree, algebraic square certification and full
kernel checking remain necessary. No claim is made that these
unproved algorithmic hypotheses are discharged simply by the
QRH theorem.

## Continuation

The subsequent [setup and global readiness assembly](randomized_setup_readiness.md) combines the [rational-root smoothing argument](randomized_rational_root_smoothing.md), the local moment and fibre results, and the sampler analysis under their stated QRH and classical inputs. It is a written conditional C1 argument, not a completed Lean certificate or proof of C2–C5.
