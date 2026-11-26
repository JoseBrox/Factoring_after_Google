# Enlarged rational-root smoothing

**Status:** written proof of the randomized manuscript's enlarged
version of source Lemma 4.3, conditional on QRH through the two-sided
weighted progression estimate, and on the stated classical reduced-basis
and primitive-lattice counting facts. The new argument also explains
the uniform rounding-boundary and short-fibre contributions. This
is not a completed Lean proof.

Use the scales \(L,\ell,U,\Lambda,\Xi\), and the modified constants
\(\tau=19/16,\ g=43/8,\ \beta=18\).
Use the [weighted AP](qrh_weighted_progressions.md) and
[rough AP/local-limit](weighted_rough_bad_child.md) results.
In particular the actual exceptional conductor set is empty under QRH.
All asymptotic estimates below are uniform in the prime
\(q\in(Q_0/2,Q_0]\) with \(q\nmid3N\), and in the base-pair blocks.

Write \(E=E_q\), \(M_G=\lceil e^{30\ell^2}\rceil\),
\(M_{\rm bins}=\lceil e^{.19\widehat\Lambda}\rceil\).
The special box is
\(\mathcal B=[3E/4,E]\times[E/8,E/4]\cap\mathbb Z^2\).
The important size relations are
\[
 \log E=(\tau/2+o(1))\Xi,\quad E^2/q=e^{(4+o(1))\Lambda},
 \quad \log G=(g+o(1))\Xi,\quad
 \log B=(18+o(1))\Lambda .
\]
In particular \(E<q\), and \(G/q\) is much larger than
any of the small dyadic-prime or rounding factors used below.

## 1. Base-pair rejection and reduction to blocks

Let \(G_0=([G,2G]\cap\mathbb Z)^2\) and
\(G_{\rm box}=\{(g_0,g_1)\in G_0:
 \gcd(g_0,g_1)=\gcd(g_0g_1,3N)=1\}\).
Möbius inversion, counting the coordinates not divisible by 3,
gives \(3G^2/\pi^2+O(G\log G)\) primitive pairs coprime to 3:
for \(3\nmid e\) the number of multiples of e in each interval
not divisible by 3 is \(2G/(3e)+O(1)\), and the Euler product
over \(p\ne3\) is \(9/(8\zeta(2))\).
For every \(p\mid N\), \(p>B\), at most
\(2(G+1)(G/p+1)\) pairs have p dividing a coordinate.
Their total over \(\omega(N)=O(L)\) is \(o(G^2)\).
Thus \(|G_{\rm box}|/|G_0|=3/\pi^2+o(1)>1/4\).

Partition \([G,2G]\cap\mathbb Z\) into \(M_G\) consecutive
blocks, each of size \(L_G\) or \(L_G+1\),
\(L_G=\lfloor(G+1)/M_G\rfloor\).
It suffices to show, for each product block \(I\) and each fixed q,
that the probability of an unsuccessful q, intersected with
\(G_{\rm box}\), is \(o(1)\) under the uniform law on I.
Here unsuccessful includes q dividing \(g_0g_1\), skewness,
too few qualifying rational points, or excessive slope-bin
clustering. The estimates below are uniform; summing over q
and then conditioning on \(G_{\rm box}\) costs at most 4 in the
expected bad fraction. Markov then shows that all but \(o(1)\)
of the base pairs have at least \(4/5\) of their allowed q's
rationally good (hence probability at least \(9/10\) eventually).
The primes excluded by \(q\mid3N\) are \(O(L)\), negligible
relative to the prime count in \((Q_0/2,Q_0]\).
The primes dividing \(g_0g_1\) also number \(O(L)\); these may
either be counted as unsuccessful or removed from the denominator.

For nonzero residues \(r\bmod q\), put
\(\mathcal L_r=\{(a,b):a\equiv rb\bmod q\}\).
A skewed r has a nonzero integer vector of Euclidean norm
less than \(\sqrt q/S_{\rm skew}\), and its second coordinate
is not zero modulo q (otherwise both coordinates vanish).
The number of these vectors, hence residues, is
\(O(q/S_{\rm skew}^2)\).
Since each coordinate of a uniform base pair in I has pointwise
residue probabilities \((1+O(q/L_G))/q\),
\(\Pr_I(q\mid g_0g_1\text{ or }g_0g_1^{-1}
 \text{ is skewed})=O(q^{-1}+S_{\rm skew}^{-2})=o(1)\).

## 2. Tuning and uniform weighted lattice counts

Let \((\bar g_0,\bar g_1)\) be the lower-left corner of I.
For \(a=(a_1,a_2)\in\mathcal B\) write, to avoid conflict with
the modulus,
\[
 z_a=(a_1g_1-a_2g_0)/q,\qquad
 \bar z_a=(a_1\bar g_1-a_2\bar g_0)/q.
\]
These real scales lie in \([EG/(4q),2EG/q]\), and
\(|z_a-\bar z_a|\le C\bar z_a/M_G\).
The root tuning has upper cap B. The exact tuning equations
and fine approximation errors imply
\[
 \log z_a=(153/32+o(1))\Xi,\quad
 4u/U=17/64+o(1),\quad \log y=(18+o(1))\Lambda.
\]
The error in the center equation
\(|4u(\log y-\kappa_0)-\log z_a|\) is at most
\(4u/(10u_{\rm cap})+o(1)<1/2\). This follows by substituting
the grid floor formula and using that \(y\) is exponentially
large, so its integer rounding is negligible. In particular
the same center condition with bound 2 holds when an actual
candidate pair is evaluated at \(\bar z_a\).

The density lower bound in the rough AP note now gives
\[
 \nu_{\min}\ge \exp(-(17/96+o(1))\Lambda),
 \tag{1}
\]
uniformly for every candidate tuned pair. Indeed \(4u/U\to17/64\)
and \(\log(5u\log y)=(2/3+o(1))\ell\).
Also all such densities across the root box are comparable
within \(L^C\) for an absolute fixed C (the tuned comparability
bound, applied at scales differing by a bounded factor, and
short-scale continuity). This includes a possible jump of u.

Let \((\bar y_a,\bar u_a)\) be the pair tuned at \(\bar z_a\),
and \(\nu_a=\nu(\bar z_a;\bar y_a,\bar u_a)\).
Across I, a given a has at most four possible pairs
\(\mathcal C_a\): there are at most two choices of u, and for
each at most two grid indices. To verify this without assuming
monotonicity of the fine approximation routine, compare with
the exact unrounded formulas. The slope of the ideal u input is
\(O(1/\Lambda)\) as a function of \(\log z\); for fixed u the
grid-index slope is \(10u_{\rm cap}/(4u)=2560/17+o(1)\).
Thus the entire root range of logarithmic length \(\log8\)
has fewer than 1000 ideal jump thresholds, and a block has
logarithmic width \(O(M_G^{-1})\).
The fine-approximation error bands, even after multiplication
by the grid coefficients, have width
\(e^{-(60\log2+o(1))\ell^2}=o(M_G^{-1})\).
All a outside the strips where \(\bar z_a\) is within relative
\(C/M_G\) of one of these thresholds have their tuned pair
constant throughout I. Denote these points by non-boundary points.
The strips have width \(O(E/M_G)\) and total area \(O(E^2/M_G)\).

For each non-skewed r, let \(A_r\) consist of the primitive
non-boundary points in \(\mathcal L_r\cap\mathcal B\).
Lagrange–Gauss reduction gives a half-open fundamental tile
of diameter \(O(Ee^{-(1.5+o(1))\Lambda})=:\rho\).
The following weighted count is uniform in all such r:
\[
 W_r:=\sum_{a\in A_r}\nu_a=(1+o(1))W_* ,
 \quad W_*\asymp (E^2/q)\,\overline\nu ,
 \tag{2}
\]
where \(\overline\nu\) is the average of the reference density
over the continuous box with the ideal non-boundary tuning
(define it arbitrarily on the deleted boundary curves).
In particular \(W_*\gg (E^2/q)\nu_{\min}\).
For a precise proof partition the box into \(M_G^2\)
equal small rectangles. On a cell disjoint from the threshold
strips the tuning is fixed and the density varies by a
relative \(O(e^{-28\ell^2})\), by the short-scale continuity
bound, since \(\log\bar z\) varies by \(O(M_G^{-1})\).
There are only \(O(M_G)\) cells intersecting the strips.
For each cell S of area \(|S|\), apply the reduced-lattice tile
area comparison to \(e^{-1}S\) for
\(e\le E_1=\lfloor e^{.5\Lambda}\rfloor\), with the Möbius weight.
These e are coprime to q. The number of lattice points in
\(e^{-1}S\) is \(|S|/(qe^2)\) plus
\(O((E\rho/(M_G e)+\rho^2)/q)\).
The sum of the errors over all cells and \(e\le E_1\),
relative to \(E^2/q\), is
\[
 O(M_G\rho E^{-1}(1+\log E_1)
       +M_G^2\rho^2 E^{-2} E_1)=e^{-(1.4+o(1))\Lambda}.
\]
The tail in Möbius inversion is bounded in absolute value
by the global sum of lattice counts in \(e^{-1}\mathcal B\)
for \(e>E_1\). As in the primitive-box proof, reduced-basis
coordinates bound this by
\(O(E^2/(q E_1)+E\log E/\lambda_1)\),
relative \(e^{-(.5+o(1))\Lambda}\).
The strip and cell-boundary counts are \(O(E^2/(qM_G))\)
by tile comparison. Multiplying all these errors by
\(\nu_{\max}/\nu_{\min}\le L^C\) still gives o(1), indeed
\(O(e^{-28\ell^2})\). This proves (2), with
\(W_*=(6/\pi^2q)\int_{\mathcal B_{\mathbb R}}\nu(a)\,da\).
It also proves the ordinary unweighted primitive count with
the expected \(6/\pi^2\) constant. No extra factor \(1/q\)
is inserted into the count of points summed over *all* residues.

For each \(a\in\bigcup_{r\ {\rm non-skew}} A_r\) define
\[
 Y_a=\mathbf1_{\{q\nmid g_0g_1,\ a_1g_1\equiv a_2g_0\bmod q\}}
        \widetilde w_{\bar y_a,\bar u_a}(z_a),\quad
 W_{\rm rat}=\sum_a Y_a .
\]
Set \(Y_a=0\) outside the congruence, so only integer z enters
the weight.

## 3. Uniform first moment, including gcd and endpoint guards

Fix a primitive a and \(g_0\) in the first coordinate block.
The congruence in \(g_1\) has one class modulo q, since
\(0<a_1<q\). Its length (number of integer points) is
\((1+O(q/L_G))L_G/q\). Along it \(z_a\) is an arithmetic
progression of step \(a_1\), with total width relative to
\(\bar z_a\) between constant multiples of \(M_G^{-1}\).
Use an odd-length subprogression by discarding at most
one endpoint. The resulting normalized error \(O(q/L_G)\)
inside the progression is exponentially small on the Xi scale.
It is negligible relative to every density in (1).
The midpoint is an integer z within \(O(M_G^{-1})\) relative
distance of \(\bar z_a\). The enlarged main weighted AP
estimate applies: the actual root modulus condition has
the strict gap
\[
 \frac{g-\tau/2}{8}-\frac{\tau}{2}=\frac1{256}>0,
\]
so \(a_1\le Q_{\rm AP}(y,u)\).
There is no exceptional conductor condition.
The interval width lies between \(e^{-.2\Lambda}\) and
\(e^{-29\ell^2}\) times its scale.

The remaining guard is
\(\gcd(z,a_1)=\gcd(g_0,a_1)\) since q is invertible modulo
\(a_1\) and \(\gcd(a_1,a_2)=1\).
If \(\gcd(g_0,a_1)\le B^{1/4}\), this is at most \(y^{.3}\).
The complementary probability, even on any subinterval of
the g0 block of length at least \(e^{-.20\Lambda}L_G\), is
\[
 \begin{split}
 \Pr(\gcd(g_0,a_1)>B^{1/4})
 &\le B^{-1/40}\sum_{d\mid a_1}
                 d^{1/10}(1/d+O(1/L_{\rm sub}))\\
 &\le e^{-(.45+o(1))\Lambda}.
 \end{split}
 \tag{3}
\]
To see the second inequality, the divisor reciprocal sum
is at most \(\prod_{p\mid a_1}(1-p^{-.9})^{-1}
=\exp(O(1+(\log a_1)^{.1}))=\exp(o(\Lambda))\):
order the distinct primes \(p_j\ge j+1\).
The endpoint sum \(\sum_{d\mid a_1}d^{.1}\le a_1^{1.1}\)
is negligible relative to \(L_{\rm sub}\) since
\(1.1\tau/2<g\).
On excluded g0's use only the bound 1 on the weight and
the congruence count \(O(L_G/q)\), so their additive error is
\(O(e^{-(.45+o(1))\Lambda}/q)=o(\nu_a/q)\).
The exclusion \(q\mid g_0g_1\) also costs only \(O(q^{-2})\);
if one coordinate vanishes modulo q and the congruence holds,
both do. This proves
\[
 \mathbb E_IY_a=(1+o(1))\nu_a/q.
 \tag{4}
\]
The relative errors here can be bounded by \(O(e^{-26\ell^2})\).
The same upper estimate applies without the indicator \(q\nmid
g_0g_1\), to each candidate \((y,u)\in\mathcal C_a\)
(with its own reference density), and to g0 subintervals as in
(3) when normalized by their length. In particular it applies
to the short-fibre boundary strips used below.

Since the number of non-skewed nonzero residues is \(q(1-o(1))\),
(2) and (4) give
\[
 \mu=\mathbb E_I W_{\rm rat}=(1+o(1))W_*
     \ge \exp((4-17/96+o(1))\Lambda)\ge e^{3.82\Lambda}.
 \tag{5}
\]

## 4. Second moment on the actual fibres

Distinct primitive positive points a,b can contribute to the
joint moment only if they have the same residue r.
Put
\(D=|\det(a,b)|/q\in[1,E^2/q]\).
Fix the exact integer value of \(z_b\) on a line in I.
Its integral points form a progression with direction
\((b_1,b_2)\), because b is primitive.
On a fibre of length \(T_b\), the other value \(z_a\) moves
in steps of magnitude D. Its gcd with D is automatically
at most \(D\le e^{(4+o(1))\Lambda}<y^{.3}\).
There is no conductor exclusion for this modulus.

Put \(T_{\min}=\lceil e^{-.19\Lambda}L_G/E\rceil\).
All fibres shorter than \(T_{\min}\) lie in the vertical
boundary strips of the first coordinate block of width
\(E(T_{\min}+2)\). Indeed the direction has
\(b_1\ge3b_2>0\) and the two coordinate blocks have lengths
differing by at most one. A line segment crossing only the
two horizontal sides has length in the t parameter at
least \((L_G-2)/b_2>T_{\min}+2\).
Otherwise it meets a vertical side; a short integral
segment has every first coordinate within \(b_1(T_{\min}+2)\)
of that side. The strips have relative width
\(O(e^{-.19\Lambda})\) and meet the length condition in (3)
(after rounding or enlarging by a bounded factor).
By (4) with the strip restriction the expectation of
\(Y_b\) on them is \(O(e^{-.19\Lambda}\nu_b/q)\).
Use \(Y_a\le1\) and the ordinary non-skewed lattice count
\(O(E^2/q)\) for the number of possible a for each b.
The resulting total relative to \(\mu^2\) is
\(O(e^{-.19\Lambda}/\nu_{\min})
=\exp((-.19+17/96+o(1))\Lambda)=o(1)\).
This is the small strict root margin; a loss estimated merely
as \(e^{-.19\Lambda}\) without division by the density
would not be sufficient reasoning.

On the long fibres \(T_b\ge T_{\min}\), take a centered odd
subprogression as before. Discarding an endpoint costs
\(O(1/T_b)\), exponentially small relative to (1).
If \(D\ge D_{\min}:=e^{-35\ell^2}E^2/q\), the progression width
\(H\) satisfies
\(e^{-.195\Lambda}\le H/z_a\le e^{-29.5\ell^2}\).
For the lower bound multiply \(D_{\min}\) by \(T_{\min}\)
and divide by the upper scale \(2EG/q\);
\(M_G^{-1}\) and \(e^{-35\ell^2}\) cost only \(o(\Lambda)\).
The upper bound uses \(D\le E^2/q\) and
\(T_b\le 1+(L_G+1)/b_1\).
Thus the two-sided weighted AP result bounds the average
of the first weight on the fibre by
\((1+o(1))\nu_a\). Its hypotheses on modulus and tuning
are automatic from (1), D's bound, and continuity.
The other weight is constant along the fibre.
For the upper bound, omit the restrictions \(q\nmid g_0g_1\)
and use the full first moment upper estimate for b.
Consequently these pair contributions are at most
\((1+o(1))\nu_a\nu_b/q\).

For \(D<D_{\min}\), use the rough AP result with \(u'=2\).
Indeed \(6D(z_a/H)\ll z_a/T_{\min}\le
 e^{(4.19+o(1))\Lambda}\ll(y/2)^3\).
This gives an upper bound \(L^C\nu_a\nu_b/q\).
For each b, the points a satisfying the small determinant
condition lie in a strip of width \(O(e^{-35\ell^2}E)\);
the non-skewed tile comparison bounds their count by
\(O(e^{-35\ell^2}E^2/q)\).
The relative contribution is \(O(L^C e^{-35\ell^2})=o(1)\).
The diagonal contributes at most \(\mu\), since \(0\le Y_a\le1\).
Summing the well-separated pair bounds over r gives
\[
 \mathbb E_I W_{\rm rat}^2
 \le(1+o(1))q^{-1}\sum_{r}W_r^2+o(\mu^2)
 =(1+o(1))\mu^2
\]
by (2) and (5). Thus Chebyshev gives
\(\Pr_I(W_{\rm rat}<3\mu/4)=o(1)\).

## 5. Exact rational point pruning

For each non-boundary primitive a and each dyadic
\(p\in(y/2,y]\), the probability of
\(qp^2\mid a_1g_1-a_2g_0\) in I is \(O(1/(qp^2))\).
In fact the map of the two coordinates onto
\(\mathbb Z/(qp^2)\) is surjective because \(\gcd(a_1,a_2)=1\);
uniform residues have probability exactly \(1/(qp^2)\),
and the block coordinates are pointwise \(1+o(1)\) times
uniform modulo \(qp^2\), since \(L_G\gg qp^2\).
This avoids any distinction according to whether p divides
a coefficient. Summing over all points and these p gives
expected square-pruning count \(O((E^2/q)/y_{\min})=o(\mu)\),
using \(\sum_{p>y/2}p^{-2}=O(1/y)\) even by all integers.
By Markov the deleted count is less than \(\mu/8\) except
with probability o(1).

For \((g_0,g_1)\in G_{\rm box}\) with the non-skewed residue
and \(q\nmid g_0g_1\), every \(p\mid N\) is greater than
\(B>E^2/q\) and different from q. The joint congruence
\(a_1g_1-a_2g_0\equiv0\bmod p\) defines a sublattice of
index qp, because the coefficient pair is primitive modulo p.
Two different primitive positive points in it would have
nonzero determinant divisible by qp, impossible in this box.
The gcd-to-N guard removes at most \(O(L)\) points.
As each weight is at most 1, after these deletions the actual
qualifying set \(\mathcal R_q(g_0,g_1)\) has at least
\(\mu/2\ge e^{3.80\Lambda}\) points, except with probability o(1).
Its possible extra rounding-boundary points only increase its size.

## 6. Slope-bin clustering, including rounding-boundary points

Partition \([3,8]\) into \(M_{\rm bins}\) equal slope bins
(using half-open endpoints except the last).
For every non-skewed r, the points of its lattice in each
bin lie in a strip of width \(O(E/M_{\rm bins})\),
so tile comparison bounds their number by
\(O(E^2/(qM_{\rm bins}))\).
This bound includes rounding-boundary points.

On a qualifying point the exact weight formula gives
\(\widetilde w\ge1/(4u)\) after the dyadic-squarefree guard.
Therefore on the non-skewed event, the indicator of membership
in \(\mathcal R_q\) is at most
\[
 4u_{\rm cap}\sum_{(y,u)\in\mathcal C_a}
   \mathbf1_{\{q\nmid g_0g_1,\ a_1g_1\equiv a_2g_0\bmod q\}}
                  \widetilde w_{y,u}(z_a).
\]
Here the sum is over at most four candidates even on threshold
strips, and every candidate's reference density is within \(L^C\)
of the other box densities. Thus the same first-moment and
long-fibre rough estimates, with an additional polynomial
factor in L, apply to the expansion of \(\sum_\alpha N_\alpha^2\).
The diagonal is bounded by \(L^C\mu\).
For short fibres use the strip expectation for the second
point and the count \(O(E^2/(qM_{\rm bins}))\) for the
first point. The contribution is at most
\[
 L^C M_{\rm bins}^{-1}
          e^{-.19\Lambda}(E^2/q)\mu
 \le L^C M_{\rm bins}^{-1}
          e^{(-.19+17/96+o(1))\Lambda}\mu^2 .
\]
For long fibres the rough AP condition with \(u'=2\) holds
for every D by the cancellation in Section 4.
The joint expectation is at most \(L^C\nu_a\nu_b/q\),
with the reference density for each candidate. Summing the
same-bin count and using (2) and uniform density comparability
gives at most \(L^C M_{\rm bins}^{-1}\mu^2\).
These bounds include all qualifying points, not only the
non-boundary subset used for the first-moment lower bound.

Since the adjacent-bin sum is at most
\(3\sum_\alpha N_\alpha^2\) by \(2xy\le x^2+y^2\),
its expectation on the non-skewed and nonzero-residue event
is at most \(L^C e^{-(.19+o(1))\Lambda}\mu^2\).
Markov at \(e^{-.18\Lambda}(\mu/2)^2\)
gives failure probability \(o(1)\).
Together with Section 5, this proves the two rationally good
root requirements with probability \(1-o(1)\) in each block,
intersected with \(G_{\rm box}\). Section 1 then gives the
claimed uniform base-pair conclusion.

## 7. Readiness boundary

The rational-root smoothing input of source Lemma 4.3 is now
covered by this written argument under the stated QRH and
classical lattice inputs. Together with
[enlarged local moments](randomized_local_moments.md) and
[fibre coupling/readiness transfer](randomized_fibre_coupling.md),
this removes the previous specifically rational-root distribution
gap in the written readiness analysis. The precise coefficient
sampler approximation, leading-coefficient and derivative events,
actual history validity (including all recursive/fallback size
guards), and square-certificate construction still must be
audited and formalized. No unconditional randomized algorithm
endpoint or additional completed Lean milestone is claimed.
