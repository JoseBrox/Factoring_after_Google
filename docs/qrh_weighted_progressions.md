# A QRH proof of the enlarged weighted smooth progression asymptotic

**Status:** written mathematical derivation conditional on the uniform
Dirichlet seven-eighths zero-free theorem in [the QRH audit](quasi_rh_audit.md),
and on classical strong PNT (already separately Lean-certified). Not a
Lean proof of this analytic result. This proves the main two-sided
weighted progression assertion in the enlarged randomized contract
by a different argument. The [continuation](weighted_rough_bad_child.md) separately proves the rough upper bound, bad-child estimate, tuned-scale comparability and emptiness of the actual source exceptional sets under QRH. The polynomial-slice and readiness contracts remain open.

Use the manuscript's \(L=\log N,\ \ell=\log L,\ U=(L/\ell)^{1/3},\
\Lambda=U\ell,\ \Xi=U\Lambda\). All estimates below are uniform as
\(N\to\infty\), with \(u,y,m,z_0,R\) in the stated admissible range:
\[
 \log y\ge(17+o(1))\Lambda,\quad \log y=O(\Xi),\quad
 U/30\le u,\quad 4u\le .96U,\quad
 m\le y^{u/2-1/16},\quad \omega(m)\le 2L.
\]
In particular \(u\to\infty,\ u/\log y=O(1/\ell)\),
\(\log(u\log y)=O(\ell)\), and \(\ell^C=o(\Lambda)\) for fixed \(C\).
Let \(h=4u-1,\ F=(4u)!,\ X=z_0\), and \(g=\gcd(X,m)\le y^{3/10}\).
The tuning condition is
\[
 |\log X-(h+1)(\log y-(\log2)/2)|\le2.
\]
Write \(A=X-mR,\ B'=X+mR,\ H=2mR\). Assume the manuscript's
\(A e^{-.2\Lambda}\le H\le A e^{-29\ell^2}\), so \(A\asymp X\)
and \(H/X\le e^{-29\ell^2}\).

For ordered prime tuples \(p_i\in(y/2,y]\), put \(P=\prod_{i=1}^h p_i\).
The target density is
\[
 \nu(X;y,u)=F^{-1}\sum_{\mathbf p} P^{-1}
                 {\bf1}_{X/y\le P\le2X/y}.
\]
We will prove
\[
 \frac{1}{2R+1}\sum_{t=-R}^R\widetilde w_{y,u}(X+mt)
 =\nu(X;y,u)(1+O(e^{-28\ell^2})).
 \tag{1}
\]
In particular for sufficiently large \(N\) the desired error
\(e^{-27\ell^2}\nu\) holds. No exceptional conductors are needed for
this particular assertion. No assumption is made that other exceptional
sets in the source are defined solely by zero location.

## 1. Density, tuning and short-scale continuity

Put \(a=(\log2)/2\), and let \(D=\#\{p:y/2<p\le y\}\),
\(M=\sum_{y/2<p\le y}1/p\). Strong PNT by partial summation, uniformly
for any subinterval of the dyadic interval, gives
\[
 D\asymp y/\log y,\qquad
 M=(\log2/\log y)(1+O(1/\log y)).
\]
For \(T_p=\log(p/y)+a\in[-a,a]\), the normalized measure with mass
\(1/(Mp)\) at \(T_p\) has CDF differing by
\(O(e^{-c\sqrt{\log y}})\) from the normalized continuous density
proportional to \((\log y-a+t)^{-1}\) on \([-a,a]\). This follows
from the PNT partial summation error, uniformly in the interval
endpoint, divided by \(M\). That continuous density is
\((1+O(1/\log y))/(2a)\), bounded above and below by absolute
positive constants.

Use inverse CDF coupling for a single coordinate: a uniform random
variable on \([0,1]\), inserted into the generalized inverses of the
two CDFs, produces a discrete coordinate and a continuous coordinate
with distance \(O(e^{-c\sqrt{\log y}})\). Indeed the continuous CDF
has derivative bounded below and the sup CDF error bounds its values
at the discrete inverse from both sides. Use independent uniforms for
the \(h\) coordinates. The total error in their sum is
\(O(h e^{-c\sqrt{\log y}})=o(1)\), uniformly. The product continuous
density is bounded below by \((1-O(1/\log y))^h\) times the
product uniform density, hence by a positive constant times it.

The target event for the sum of the \(h\) coordinates is
\([d-a,d+a]\), where \(d=\log X-(h+1)(\log y-a)\) satisfies
\(|d|\le2\). Under the product uniform distribution it has probability
\(\gg h^{-1/2}\) even if we use the inner interval
\([d-a/2,d+a/2]\). For clarity, restrict the first sixteen coordinates
to \([d/16-a/128,d/16+a/128]\), which lies in \([-a,a]\) and has
fixed positive probability. Their sum differs from \(d\) by at most
\(a/8\). The other \(h-16\) coordinates have a symmetric unimodal
density: convolution with the uniform density preserves symmetry and
monotonicity on the positive half-axis (differentiate the sliding
integral, or compare its intervals). Chebyshev's inequality places
at least a fixed positive probability inside
\([-2a\sqrt h,2a\sqrt h]\). Divide this interval into \(O(\sqrt h)\)
intervals of length at most \(a/2\); the centered interval of length
\(a/2\) has at least as much mass as each, by unimodality.
This proves the claim with a uniform constant for every \(h\ge39\).
The inverse-CDF coupling therefore gives
\[
 \nu(X;y,u)\gg M^h/(F\sqrt h).
 \tag{2}
\]
Stirling's estimate (or integration of \(\log x\)) and
\(h/\log y=o(1)\) show that the right side exceeds
\(\tfrac12(5u\log y)^{-4u}\) eventually: the exponential advantage
per factor is \(5e\log2/4>1\), and the losses are polynomial in
\(u\). Also \(u\log y=O(U\Xi)=O(L)\), so \(4u\le .96U\) gives
\[
 \tfrac12(5u\log y)^{-4u}\ge e^{-.97\Lambda}.
\]
The assertion is uniform even at the largest admissible \(y\).

An additional estimate used below follows by conditioning on the
first \(h-1\) coordinates: the probability of the sum lying in an
interval of length \(b\) is \(O(b+e^{-c\sqrt{\log y}})\). It follows
that changing \(\log X\) by at most \(b\le 1\) changes \(\nu\) by
at most \(O(\sqrt h(b+e^{-c\sqrt{\log y}}))\nu\), using (2).
In particular changes of size \(O(e^{-29\ell^2})\) have relative
error \(O(e^{-28.5\ell^2})\) eventually. This also controls tuples
in boundary intervals of that size, without differentiating a
step function.

Let \(J\) be the dyadic prime set with primes dividing \(m\) removed.
Its cardinal \(D_J\asymp y/\log y\) and mass \(M_J\) satisfy
\(M-M_J\le4L/y\). By the union bound, tuples containing a removed
prime have total reciprocal mass at most \(h(M-M_J)M^{h-1}\).
Relative to (2) this is \(O(h^{3/2}L\log y/y)\), smaller than
\(e^{-C\ell^2}\) for every fixed \(C\). The restricted density
\(\nu_J\) and the unrestricted density can thus be interchanged in
all estimates in this proof.

## 2. Uniform twisted prime sums from QRH

The uniform interior log-derivative estimate (1) in
[the witness note](quasi_rh_witnesses.md) gives
\[
 |L'/L(s,\chi)|\ll\log(q(|\Im s|+4)),
 \qquad 15/16\le\Re s\le2
\]
for every nonprincipal character of modulus \(q\), not necessarily
primitive. For \(|t|\le T=y^{10u}\), \(q\le m\), this implies
\[
 \left|\sum_{p\in J}\chi(p)p^{it}\right|
 \le D_J y^{-1/100} .
 \tag{3}
\]
Here is the proof of the sharp interval version needed for (3).
For any subinterval of \([y/2,y]\), approximate its indicator
from outside by a smooth weight on \(v=n/y\) with transition width
\(\eta_0=y^{-1/64}\), derivatives of order \(j\le2\) bounded by
\(C_j\eta_0^{-j}\), and second derivative \(L^1\) norm
\(O(\eta_0^{-1})\). Such a weight is obtained by convolving an
interval enlarged by \(\eta_0\) with a fixed compactly supported
smooth nonnegative mollifier rescaled to \(\eta_0\).
The discrepancy in the von Mangoldt sum is bounded absolutely by
\(O((y\eta_0+1)\log y)\), since only endpoint intervals are affected.
The Mellin transform of the weight on any line
\(15/16\le\sigma\le2\) is \(O(\eta_0^{-1}/(1+v^2))\), by two
integrations by parts in log coordinates.
Mellin inversion and absolute convergence on line 2 give the
integral of \(y^s \widehat w(s)(-L'/L)(s-it)\). Shift to line
\(15/16\): QRH eliminates poles, and the horizontal segments tend
to zero by the bound just stated. The shifted integral is
\[
 O\big(y^{15/16+1/64}\log(q(|t|+4))\big).
\]
Prime powers contribute \(O(\sqrt y(\log y)^2)\). Abel summation
divides out the \(\log p\) weights using the uniform subinterval
bound (with \(|p^{it}|=1\)); no derivative in \(t\) is introduced.
Deleting at most \(2L\) primes costs \(O(L)\). Since
\(\log(q(T+4))=O(u\log y)=O(L)\) and \(\log y\gg\Lambda\),
the displayed bounds are \(o(D_J y^{-1/100})\). This proves (3).
The contours and Mellin inversion here require standard analytic
lemmas to be formalized, not merely the zero-location theorem.

## 3. The exact gcd reduction and principal term

By the exact identity in [the free-factor note](weighted_progression_reduction.md),
every contributing tuple has \(\gcd(P,m)=1\):
a prime factor of \(P\) dividing \(m\) would divide \(X\), contrary
to \(p>y/2>y^{3/10}\). Thus we may restrict tuples to \(J^h\).
Write \(m'=m/g,\ X'=X/g\). The free integer \(k\) must be divisible
by \(g\); write \(k=gk'\). Then the congruence is
\(Pk'\equiv X'\pmod {m'}\), where \(X'\) is a unit, and
\(y/(2g)<k'\le y/g\).

For any interval \(I\) of real length \(b\), including arbitrary
open/closed endpoint conventions, the number of integers in it
coprime to \(m'\) is
\[
 b\,\varphi(m')/m'+O(b e^{-60\ell^2}+\exp(O(\ell^3))).
 \tag{4}
\]
To prove this, apply the upper and lower Bonferroni truncations of
inclusion-exclusion through adjacent even/odd levels near
\(r=\lceil100\ell^2\rceil\) to the prime divisors of \(m'\).
A divisor \(d\) contributes \(b/d+O(2)\), so the floor errors total
at most \((1+\omega(m'))^{r+2}=\exp(O(\ell^3))\).
The difference of successive main sums is at most
\((\sum_{p\mid m'}1/p)^r/r!\) (or at the adjacent level).
The j-th distinct prime divisor is at least \(j+1\), so the sum
is \(O(\log(2L+1))=O(\ell)\), and the last expression is
\(o(e^{-60\ell^2})\). If there are fewer primes than the truncation
level, use the exact inclusion-exclusion instead.
This argument is uniform and elementary. Also
\(\varphi(m')/m'\ge1/(1+\omega(m'))\) by the same ordering of
the prime divisors. In particular (4) is useful even for highly
composite moduli.

For an interval \([A_1,B_1]\) whose endpoints differ from \(A,B'\)
by \(o(H)\) and with \(H_1=B_1-A_1\asymp H\), set
\(b_P=|[A_1,B_1]\cap[yP/2,yP]|\), continuous length.
The principal character contribution before division by
\(F(2R+1)\) is
\[
 \frac1{\varphi(m')}\sum_{\mathbf p\in J^h}
 \#\{k':\gcd(k',m')=1,\ y/(2g)<k'\le y/g,\
                         A_1\le gPk'\le B_1\}.
\]
Each intersecting tuple has \(P\asymp X/y\) and
\(H/(gP)\gg y^{.7} e^{-.2\Lambda}\), which dominates
\(\exp(C\ell^3)\) for every fixed \(C\).
Apply (4) to the actual intersection interval of length \(b_P/(gP)\);
an additive error \(O(H/(gP)e^{-50\ell^2}\varphi(m')/m')\)
per potentially intersecting tuple absorbs both errors uniformly.
Tuples with no intersection need no error. After normalization the
total error is \(O(e^{-49\ell^2}\nu)\), by (2) and the boundary
probability bound in Section 1.

The main contribution is
\[
 \frac1{F m(2R+1)}\sum_{\mathbf p\in J^h} b_P/P.
\]
Outside boundary intervals of log-width \(O(H/X)\) at \(X/y,2X/y\),
\(b_P=H_1{\bf1}_{X/y\le P\le2X/y}\); always
\(0\le b_P\le H_1\). Section 1 controls the boundary tuples.
Since \(m(2R+1)=H+m\), \(m/H\) is exponentially small
(\(m\le y^{u/2}\), \(X=y^{4u}e^{-O(u)}\)).
If \(|H_1/H-1|=O(e^{-30\ell^2})\), the normalized principal
contribution is consequently
\[
 \nu(X;y,u)(1+O(e^{-28.5\ell^2})).
 \tag{5}
\]
This proves the main-term comparison with actual integer coprimality,
without requiring a uniform PNT in progressions for the free factor.

## 4. High moments eliminate the cost of the large modulus

It remains to control the nonprincipal characters in the sharp
interval. Use upper/lower log-window weights \(w_\pm\), formed by
convolving respectively the log interval enlarged/contracted by
\(\eta=e^{-\Lambda/2}\) at both ends with the nonnegative triangular
probability density supported in \([-\eta,\eta]\).
Then \(0\le w_-\le{\bf1}_{[\log A,\log B']}\le w_+\le1\),
including the endpoints. For the principal character (5) applies
by sandwiching each weight between indicators with endpoints moved
by at most \(2\eta\); the resulting relative length change is
\(O(\eta X/H)=O(e^{-.29\Lambda})\).

Write \(A_\chi(t)=\sum_{p\in J}\chi(p)p^{it}\) and
\(B_\chi(t)=\sum_{y/(2g)<k'\le y/g}\chi(k')(k')^{it}\).
Fourier inversion and character orthogonality modulo \(m'\) express
the contribution for either weight as the integral of
\[
 \frac{\widehat w_\pm(t)\,g^{it}}{2\pi F(2R+1)\varphi(m')}
       \sum_{\chi\bmod m'}\overline{\chi(X')}A_\chi(t)^h B_\chi(t).
\]
Choose a Fourier sign convention consistently; only absolute
values of the nonprincipal terms are used. The Fourier transform
satisfies \(\int|\widehat w_\pm(t)|dt=O(1+\log(1/\eta))=O(\Lambda)\)
and \(\int_{|t|>T}|\widehat w_\pm(t)|dt=O(\eta^{-2}T^{-2})\),
by the explicit transforms of an interval and a triangular density.
All sums are finite; inversion is absolutely integrable.

For \(m'=1\) there are no nonprincipal characters. Otherwise
put \(j=\lfloor\log m'/\log y\rfloor\le u/2\).
The products of \(j\) primes of \(J\) lie in \([1,m']\);
if \(j>0\), equality to \(m'\) is impossible by coprimality.
They are injective as *integers* upon reduction modulo \(m'\)
(the ordered tuples themselves need not be injective).
Unique factorization bounds the multiplicity of any such product
by \(j!\). Exact character orthogonality gives
\[
 \sum_{\chi\bmod m'}|A_\chi(t)|^{2j}
 \le \varphi(m')\,j!D_J^j,
 \tag{6}
\]
including \(j=0\), since there are \(\varphi(m')\) characters.
For example expand \(A_\chi^j=\sum_d a_d d^{it}\chi(d)\);
the orthogonal sum is \(\varphi(m')\sum_d a_d^2\),
with \(\sum_d a_d=D_J^j,\ a_d\le j!\).

For nonprincipal characters and \(|t|\le T=y^{10u}\),
(3) supplies the remaining \(h-2j\) factors, while
\(|B_\chi|\le y/g+1\). Combining (3), (6), and the Fourier
\(L^1\) bound, the absolute nonprincipal contribution is at most
\[
 C\Lambda\,\frac{(y/g+1)D_J^h}{F(2R+1)}
       \frac{j!}{D_J^j}\,y^{-(h-2j)/100}.
\]
Divide by (2), use \(M\ge D_J/y\), and
\((2R+1)\ge H/m,\ X=y^{h+1}e^{-O(u)},\
H\gg X e^{-.2\Lambda}\). The relative error is at most
\[
 C\Lambda\sqrt h\, e^{O(u)+.2\Lambda}
           \frac{m'j!}{D_J^j}\, y^{-(h-2j)/100}.
\]
Now \(m'<y^{j+1}\), \(D_J\gg y/\log y\),
\(h-2j\ge3u-1\), so its logarithm is at most
\[
 \left(1-\frac{3u-1}{100}\right)\log y
       +O(u\ell)+.2\Lambda+O(\ell).
\]
This tends to minus infinity on the scale \(u\log y\), uniformly,
since \(u\to\infty,\ \log y/\ell\to\infty\). It is far smaller
than \(-28\ell^2\). For \(|t|>T\) use
\(\sum_\chi |A_\chi(t)|^h\le\varphi(m')D_J^h\). The relative
tail bound is \(O(\sqrt h\,e^{O(u)+.2\Lambda}m'\eta^{-2}T^{-2})\);
\(T=y^{10u}\) overwhelms \(m'\le y^{u/2}\) and all other factors.
This finishes the proof of (1) by the upper and lower sandwiches.

## 5. Remaining scope and formalization

The argument gives the density lower bound and short-scale
continuity, plus the main two-sided weighted progression asymptotic
for all moduli in the required enlarged range with the stated gcd
restriction. It permits setting the exceptional set for this
particular assertion to empty, conditional on QRH. The [continuation](weighted_rough_bad_child.md) supplies separate proofs of nearby tuned-scale comparability, rough upper bound, bad-child rarity and the actual source exceptional-set assertion. The polynomial coupling, all-history conditional moments, global readiness and algebraic square certification still require separate proofs. They are not consequences of (1).

Lean priorities: certify the moment inequality (6) for actual
Dirichlet characters and ordered prime tuples; the finite
Bonferroni formula and its floor errors; then the actual Mellin
and Fourier estimates from QRH and PNT; then the measure coupling
and uniform constants. The existing Prefix and Smooth modules
supply much of the finite unique-factorization and character
orthogonality infrastructure. No new axiom should encode (1).
