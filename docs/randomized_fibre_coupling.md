# Enlarged polynomial fibre coupling and readiness transfer

**Status:** written proof of the enlarged version of the fibre-tail,
mod-N conditioning and translation estimates in source Lemma 4.2(3)–(4),
and of the backward readiness implication from the stated local-moment
contract. Not a Lean certification of those analytic/probabilistic
statements. The remaining local conditional moments and rational-root
smoothing are not assumed proved here.

Use the randomized manuscript's scales \(L,\ell,U,\Lambda,\Xi\), degree
\(d=(1/2+o(1))U\), \(G=e^{(43/8+o(1))\Xi}\),
\(W=e^{(8+o(1))\Xi}\), and \(\Lambda_0=\lceil32\widehat\Lambda\rceil
=(32+o(1))\Lambda\).
Let \(\alpha=\Lambda_0/W\) and write
\[
 w(c)=e^{-\alpha\|c\|_1},\qquad
 Z(S)=\sum_{c\in S}w(c),\qquad
 \mathcal B=[-W,W]^{d+1}\cap\mathbb Z^{d+1}.
\]
Assume the base pair is primitive and coprime to \(3N\). Let
\(R\le\lceil J/2\rceil+3\le .65\ell+3\), and let
\(v_s=(a_s,b_s)\) be the prescribed primitive pairwise non-collinear
evaluation vectors, with \(a_s\ge3b_s\ge3\),
\[
 \prod_s(2a_s)\le e^{(34/25)\Xi},\qquad
 \gcd(a_sg_1-b_sg_0,N)=1.
\]
In particular the sign of this last determinant is immaterial.

## 1. Integer parameterization of every evaluation fibre

A homogeneous integral form of degree d that vanishes at the R
evaluation vectors is divisible in \(\mathbb Z[X,Y]\) by
\[
 P_V(X,Y)=\prod_s(b_sX-a_sY).
\]
For one factor, vanishing gives divisibility over \(\mathbb Q[X,Y]\);
primitivity gives integral divisibility by Gauss's lemma. Distinct
linear factors are nonassociate, so their product divides the form.
Conversely every multiple vanishes at the specified vectors. Thus
if \(c_*\) is any integral coefficient vector in a nonempty fibre,
all its vectors are uniquely \(c_*+T u\), where
\(u\in\mathbb Z^n,\ n=d+1-R\), and T multiplies the homogeneous
degree \(n-1\) form with coefficients u by \(P_V\).
The factor 3 in the source's affine coefficient map does not affect
the kernel for exact equalities.

Write \(A=\prod_s(4a_s/3)\), \(D=\prod_s(3/(2a_s))\).
The coefficient triangle inequality gives
\(\|Tu\|_\infty\le A\|u\|_\infty\).
For the inverse bound, division by one factor gives the recursion
\(Q_j=(b_s Q_{j-1}-C_j)/a_s,\ Q_{-1}=0\); hence
\(\|Q\|_\infty\le\|C\|_\infty/(a_s-b_s)
 \le(3/(2a_s))\|C\|_\infty\).
Iterating gives \(\|u\|_\infty\le D\|Tu\|_\infty\).
Notice \(AD=2^R\), independently of the magnitude of the evaluation
points. Empty products handle R=0.

If there is also a specified mod-q root condition, with
\(B<q\le Q_0\), \(q\nmid3N\), choose \(c_*\) satisfying it.
Either \(P_V(r_q,1)=0\bmod q\), in which case there is no further
constraint on u, or this condition is a single linear congruence
on u with coefficient one at \(u_0\).
Set \(q_1=1\) or \(q_1=q\) accordingly, and let \(L_q\) be the
lattice of u satisfying that congruence. The homogeneous fibre
\(F\) in the box is now exactly
\[
 F=\{c_*+Tu:u\in L_q,\ \|c_*+Tu\|_\infty\le W\}.
\]

Take \(U_{\rm in}=\lfloor W/(16(d+1)A)\rfloor\),
\(U_{\rm out}=\lfloor 2WD\rfloor\). Uniformly,
\[
 U_{\rm in}\ge e^{(8-1.36-o(1))\Xi}\gg q_1,\qquad
 U_{\rm out}/U_{\rm in}\le (32+o(1))(d+1)2^R .
\]
For u in a cube of radius H, count the choices of u0 after fixing
the other n-1 coordinates: the count lies between
\((2H+1)^n/q_1\) times \(1\pm q_1/(2H+1)\).
The same count holds for affine cosets of \(L_q\).
For any anchor in the box the fibre lies in the outer u cube.
For an anchor of norm at most \(W/2\) in l1, the inner u cube
is in the box and its l1 displacement is at most \(W/16\).

The logarithm of the ratio of these upper and lower counts is
at most
\[
 n\log((34+o(1))(d+1)2^R)
 \le \bigl(\tfrac12(\tfrac13+.65\log2)+o(1)\bigr)\Lambda
 <.40\Lambda
\]
eventually. Here \(\log(d+1)=(1/3+o(1))\ell\),
\(n\le d+1\). The strict margin is valid uniformly for the enlarged
parameters, including R=0. We may use the looser bound
\(e^{.45\Lambda}\) in all subsequent estimates.

## 2. Fibre tail

If \(F\) meets the core \(\|c_*\|_1\le W/4\), the inner cube
above consists of points of l1 norm at most \(5W/16\).
Thus \(Z(F)\) is at least the inner count times
\(e^{-5\Lambda_0/16}\). Every point outside the middle
box \(\|c\|_1\le W/2\) has weight at most \(e^{-\Lambda_0/2}\).
Taking their ratio gives
\[
 Z(F\setminus\mathcal B_{\rm mid})/Z(F)
 \le e^{.45\Lambda-3\Lambda_0/16}
 \le e^{-5.5\Lambda}
\]
eventually. The required \(e^{-5\Lambda}\) is weaker.

## 3. Short tiles for conditioning modulo N

For this step assume F meets the middle box and use such an anchor.
The mod-N constraint on the polynomial changes, after the factorization
in Section 1, to one affine congruence on u:
\[
 \sum_{j=0}^{n-1}u_j m_N^j\equiv r\pmod N,\qquad
 m_N=g_0g_1^{-1}\pmod N .
\]
Indeed \(P_V(g_0,g_1)\) and \(3g_1^{n-1}\) are invertible modulo N.
Since \(q_1\) is coprime to N, varying \(u_0\) solves both
congruences, and the solution in \(L_q\) is a coset of the lattice
\(\Gamma=L_q\cap\Lambda_n\), of index \(N\) in \(L_q\).

For clarity the dual-lattice estimate from source Proposition 2.2
has a short direct proof. An element \(y\in\Lambda_n^*\) has
\(Ny_j\in\mathbb Z\) and
\(Ny_j\equiv k m_N^j\bmod N\) for some integer k, by testing the
standard basis \(N e_0,\ e_j-(m_N^j\bmod N)e_0\).
If \(\|y\|_\infty<1/(4G)\), the integer
\(N(g_1y_{j+1}-g_0y_j)\) is divisible by N and has absolute
value less than N (as \(g_i\le2G\)); it is zero.
Thus the integer vector \(Ny\) is a multiple of
\((g_1^{n-1},g_0g_1^{n-2},\ldots,g_0^{n-1})\), by coprimality.
A nonzero such vector has first coordinate at least \(g_1^{n-1}\)
in absolute value. Since
\[
 (n-1)\log g_1=(43/16+o(1))L>L-\log 2
\]
eventually, this contradicts \(|Ny_0|<N/(4G)\).
Hence all nonzero dual vectors have sup norm at least \(1/(4G)\).
Since \(q_1\Lambda_n\subset\Gamma\), the same bound is
\(1/(4q_1G)\) for \(\Gamma^*\).

For a (3/4)-LLL-reduced basis \(b_1,\dots,b_n\) of \(\Gamma\)
with orthogonalized vectors \(b_j^*\), the nonzero dual vector
\(b_n^*/\|b_n^*\|_2^2\) has norm \(1/\|b_n^*\|_2\).
The dual estimate gives \(\|b_n^*\|_2\le4q_1G\).
The Lovasz and size-reduction inequalities imply
\(\|b_j^*\|_2^2\le2^{n-j}\|b_n^*\|_2^2\)
and \(\|b_j\|_2^2\le\|b_j^*\|_2^2+
 \frac14\sum_{i<j}\|b_i^*\|_2^2\le2^{n+1}\|b_n^*\|_2^2\).
We may therefore bound the displacement in a half-open
fundamental parallelepiped by
\[
 \rho:=A\,n\,2^{(n+3)/2}q_1G
 \ge \sup_{z\in P_\Gamma}\|Tz\|_\infty .
\]
This uses only the LLL basis inequalities and the existence of an
LLL-reduced basis; executable LLL bit costs are a separate task.
Crucially the enlarged parameters give
\[
 \log\rho\le(43/8+34/25+19/16+o(1))\Xi
           =(7.9225+o(1))\Xi,\qquad
 \rho/W\le e^{-(.0775+o(1))\Xi}.
 \tag{*}
\]
The q-factor is essential. Omitting it would overstate the margin.

The half-open tiles centered at the affine mod-N solutions
partition real u-space. Each contains exactly N points of \(L_q\):
the unique representative of each of the N quotient cosets is
obtained by reducing the real coordinates in the lattice basis
into \([-1/2,1/2)^n\).
If a tile center in coefficient space satisfies
\(\|c\|_\infty\le7W/8\), every tile point lies in the box by (*).
For each such tile the ratio of any point's weight to the center's
weight is between \(e^{-\alpha(d+1)\rho}\) and
\(e^{\alpha(d+1)\rho}\), hence \(1+O(e^{-c\Xi})\)
for some absolute \(c>0\).

Every remaining tile meeting the box has center and all its points
with sup norm greater than \(3W/4\), since the center is at distance
at most \(\rho\) from its points. Also their sup norms are at most
\(W+2\rho\). Relative to the middle anchor, their displacement is
at most \(3W/2+2\rho<2W\), so their u-coordinates belong to
the same outer cube in Section 1. In particular the number of
these tiles times N is at most the outer lattice count, because
each tile's full set of N points belongs to that cube, even if not
to F. All their weights, including the centers' weights, are
at most \(e^{-3\Lambda_0/4}\).
The inner cube bound at a middle anchor gives
\(Z(F)\ge \text{inner count}\cdot e^{-9\Lambda_0/16}\).
Therefore the entire error from the remaining tiles, both in
\(Z(F)\) and in \(N Z(F\cap L_N)\), is bounded relatively by
\[
 O(e^{.45\Lambda-(3/4-9/16)\Lambda_0})
 \le e^{-5.4\Lambda}
\]
eventually. Combining the interior and boundary estimates proves
uniformly for every fibre meeting the middle box
\[
 \left|N Z(F\cap L_N)/Z(F)-1\right|\le e^{-5\Lambda}.
 \tag{1}
\]
No enumeration of exponentially many tiles is needed for this
probabilistic comparison.

## 4. Expectation transfer and translations

For a slice U meeting the core and a function \(\Psi\in[0,1]\)
of the additional listed evaluations, partition U into fibres
on which \(\Psi\) is constant. Put \(\epsilon=e^{-5\Lambda}\).
The bad fibres not meeting the middle box have original mass at most
\(\epsilon Z(U)\) by Section 2. By (1) for U and the good fibres,
their restricted mass is at most
\([(1+\epsilon)-(1-\epsilon)^2]Z(U)/N
 \le3\epsilon Z(U)/N\).
On each good fibre the restricted mass differs from the original
mass divided by N by at most \(\epsilon\) relatively.
Normalize by \(Z(U\cap L_N)\). To see the exact claimed constants,
use the stronger tail and relative errors \(e^{-5.4\Lambda}\)
from Sections 2–3 rather than \(\epsilon\).
If \(\eta=e^{-5.4\Lambda}\), subtraction and division bound
the difference in expectation by
\((2\eta\,\mathbb E_0\Psi+4\eta)/(1-\eta)\);
this is at most \(2\epsilon\,\mathbb E_0\Psi+5\epsilon\)
eventually. This is the desired fibre-conditioning estimate.

For translations, let U be an affine lattice slice in the box and
\(\delta\) an allowed shift in its translation lattice with
\(\|\delta\|_\infty\le\Delta\le W/8\).
Then \(w(c+\delta)/w(c)\) lies between
\(e^{-\alpha(d+1)\Delta}\) and \(e^{\alpha(d+1)\Delta}\).
The translation maps the sub-box of radius \(3W/4\)
injectively into U and its image contains the sub-box of radius
\(5W/8\). If the latter's complement has mass at most
\(\epsilon_{\rm tail}Z(U)\), discard that complement for the lower
bound and discard the preimage complement for the upper bound.
For every \(0\le\Phi\le1\) this gives
\[
 e^{-\epsilon_{\rm lip}}\mathbb E_U\Phi-\epsilon_{\rm tail}
 \le\mathbb E_U[\Phi(c+\delta)]
 \le e^{\epsilon_{\rm lip}}\mathbb E_U\Phi+\epsilon_{\rm tail},
 \quad\epsilon_{\rm lip}=(d+1)\alpha\Delta .
\]
Average over independent allowed shifts. This is the original
multiplicative translation bound, uniformly in the enlarged range.

## 5. What readiness follows from the local contracts

The source Lemma 4.6's backwards argument can be stated as a
general finite weighted-tree lemma, with no independence of
the visited nodes. For each fixed recorded history H, use the
conditional distribution of the polynomial pair given its exact
ancestor evaluations, not its distribution given that the
randomized sampler has selected that history. Let \(a\) range
over the permitted clean next choices, and let \(X_a\ge0\) be
their weights. Assume the precise conditional local estimates
from the manuscript: on local goodness the probability of
choosing \(a\) is bounded by \(2X_a/\mu_H\), the sum of the
conditional expectations of these bounds is at most 3,
and every chosen \(a\) has at most \(D_{\rm child}=\log_2 N\)
candidate children determined by the revealed evaluations.
For each possible \(a\), \(X_a\) is measurable with respect to
those revealed evaluations. Assume the unconditional-on-choice
conditional probability of local failure on each valid slice
meeting the core is at most \(p=e^{-24\ell^2}\). The more
detailed source local estimates imply this p after the timeout,
bad-child and exceptional-choice bounds, if they hold in the
enlarged range. The core-nonempty event is monotone along
history extension, so may be inserted into each conditional
expectation.

For a fixed depth r, the probability of failure at that depth
along some otherwise valid path is at most
\((3D_{\rm child})^r p\). Prove this by backward induction:
condition first on the exact evaluations at the next chosen a;
the bound for each descendant holds on the corresponding slice.
Pull the measurable weight \(2X_a/\mu_H\) outside the conditional
expectation, sum over at most \(D_{\rm child}\) children, then use
the conditional sum bound 3 at the preceding history.
This is the smoothness-cancelling step. Simply union-bounding
over adaptive histories without these weights would be invalid.

As \(r_{\max}\le.65\ell\), the sum of these bounds through
depth \(r_{\max}\) is at most \(e^{-23\ell^2}\) eventually.
Markov's inequality first over fresh tree coins at threshold
\(L^{-2}\), then over the fraction of bad root primes, gives the
same global-readiness implication as in the source: when the
rationally good root set is at least \(4/5\) of the root primes
and the exceptional setup/leading-coefficient events have
probability o(1), the good fraction is at least \(3/4\)
with probability \(1-o(1)\) over the polynomial pair.
All polynomial TV errors and rare gcd/derivative events must
still be charged. The actual cofactor size bounds are the
enlarged manuscript's bounds, not the smaller original
\(N^{1/10}\) exponent.

**Boundary:** Sections 1–4 establish the enlarged fibre-coupling
and translation estimates in writing, using the indicated
classical lattice facts. Section 5 establishes the logical
readiness implication, not the missing hypotheses of the local
moment theorem. The latter still requires the enlarged rational
root smoothing, polynomial-slice marginal AP estimates,
pair correlation bounds, all valid-history geometry, and
bad-child propagation for the actual sampler. The main weighted
AP and rough/bad-child estimates were established separately in
the two QRH/weighted notes. No full C1 theorem is claimed yet.
