# Rough weighted progressions and bad-child rarity

**Status:** written proof of the rough upper bound and bad-child estimate
in the enlarged randomized contract, using strong PNT and the stated
bad-conductor cardinality bound (or the empty set for the QRH proof of
the main weighted AP assertion). Not yet a Lean proof. This complements
[the main weighted progression proof](qrh_weighted_progressions.md).
All parameters and notation are those of that note and source
Lemmas 3.5(4)(b) and 3.6(3). Here \(H\le X/2\), without the
short-window lower bound required by the two-sided asymptotic.
As in the source, \(u'\) is an integer.

## 1. Sharper lower bound at the tuned scale

Let \(h=4u-1\), \(a=(\log2)/2\), and \(M=\sum_{y/2<p\le y}1/p\).
The CDF coupling from Section 1 of the main weighted progression
proof transfers the probability for the sum of \(h\) independent
uniform coordinates on \([-a,a]\) to the weighted prime tuple.
The continuous density is \(1+O(1/\log y)\) times uniform,
pointwise, so their \(h\)-fold product densities have ratio \(1+o(1)\)
uniformly. The coupling error in the sum is
\(O(h e^{-c\sqrt{\log y}})=o(1)\).

For completeness, the uniform sum has density
\[
 f_h(x)=\frac1{2\pi}\int_{\mathbb R}
            \left(\frac{\sin(at)}{at}\right)^h e^{-itx}\,dt
 \qquad(h\ge2).
\]
Substitute \(t=w/(a\sqrt h)\). On \(|w|\le\sqrt h\),
\(|\sin(w/\sqrt h)/(w/\sqrt h)|^h\le e^{-c_1w^2}\)
for an absolute \(c_1>0\), by continuity and the Taylor series
at zero. For fixed \(w\) the expression converges to \(e^{-w^2/6}\),
and \(e^{-iwx/(a\sqrt h)}\to1\) uniformly on each bounded x-range.
For the rest, \(|\sin v/v|\le\rho<1\) on \(1\le|v|\le2\),
and \(|\sin v/v|\le1/|v|\) on \(|v|\ge2\). Thus the absolute
tail in the scaled integral is \(O(\sqrt h(\rho^h+2^{-h}))\).
Dominated convergence gives
\[
 a\sqrt h\,f_h(x)=\sqrt{3/(2\pi)}+o(1)
\]
uniformly for bounded \(x\). Integrating over \([d-a,d+a]\),
\(|d|\le2\), with the endpoints moved by the coupling error,
shows that
\[
 \nu(X;y,u)
 =(1+o(1))\frac{\sqrt{6/\pi}}{\sqrt h}\frac{M^h}{F}
 \ge \frac{M^h}{2F\sqrt u},\qquad
 M\ge\frac{1}{2\log y}.
 \tag{1}
\]
This derivation is effective by truncating the Gaussian integral,
using the displayed dominating bounds and the Taylor remainder.
The constant \(1/2\) is strictly smaller than the limiting
\(\sqrt{6/\pi}/2\). It avoids the large ineffective constant
in the simpler lower bound.

## 2. An unconditional rough upper bound

Write \(n=k p_1\cdots p_h\), with \(y/2<k\le y\) integral and
\(y/2<p_i\le y\) prime. For a contributing tuple in the progression,
split \(n=CQ\), where
\[
 C=k p_1\cdots p_{u'},\qquad Q=p_{u'+1}\cdots p_h.
\]
Every prime in \(Q\) is coprime to \(m\): otherwise it divides X,
contrary to the gcd restriction \(g=\gcd(X,m)\le y^{.3}<y/2\).
For fixed \(Q\), \(C\equiv X Q^{-1}\pmod m\), and
\(C\in[(X-H/2)/Q,(X+H/2)/Q]\).
If any tuple contributes then
\[
 Q<\frac{5X}{4(y/2)^{u'+1}},\qquad
 H/(mQ)>\frac{4H(y/2)^{u'+1}}{5mX}\ge 24/5
\]
by the rough prefix hypothesis. Hence the number of possible \(C\)
is at most \(1+H/(mQ)\le 2H/(mQ)\).

Every fixed \(C\) has at most \((u'+1)!\) representations of the
indicated type. Indeed each prime factor of \(k\) greater than \(y/2\)
forces \(k\) to equal that prime. The prime-factor multiset of C
therefore has either exactly \(u'\) dyadic primes (in which case k
is uniquely forced by the remaining small factors), exactly \(u'+1\)
dyadic primes (in which case k is one of them), or no representation.
Repeated primes can only decrease the factorial bound.

Sum over Q and divide by \(F(2R+1)\), using \(H=m(2R)\).
The normalized weight is at most \(2(u'+1)!M^{h-u'}/F\).
Divide by (1), and use \((u'+1)!\le (u'+1)^{u'+1}\):
\[
 \frac{\sum_{t=-R}^R\widetilde w_{y,u}(X+mt)}{2R+1}
 \le 4\sqrt u\,(u'+1)\{2(u'+1)\log y\}^{u'}\,\nu(X;y,u).
\]
This is stronger than the manuscript's required
\(20\sqrt u\,(u'+1)\{3(u'+1)\log y\}^{u'}\nu\).
It does not require the QRH statement, any good-conductor restriction,
or the short-window lower bound.

## 3. Bad-child reciprocal mass

Use the exact bad-prime definition in source Lemma 3.6(3):
\(B<p\le y\) and either \(p\in\mathcal Q_{\rm exc}\), \(p\mid b\),
\(p\mid Y_{\rm forb}\), or \(p\nmid b\) and the special-q lattice
for \(a b^{-1}\pmod p\) is skewed. Here the primitive pair
\((a,b)\) satisfies \(\max(a,b)\ge y\), and
\(Y_{\rm forb}\le N^{J^2+2J}\). The enlarged range satisfies
\(J=O(\ell)\) and \(y\le Q_0<N\).

For a skewed prime in \((P_1/2,P_1]\), there is a nonzero integral
vector \((v,w)\) with norm less than
\(\sqrt{P_1}/S_{\rm skew}\), \(p\mid vb-wa\).
The determinant cannot vanish because \((a,b)\) is primitive,
and the short vector has norm less than \(\max(a,b)\).
For \(P_1\ge B\) the number of such vectors is
\(O(P_1/S_{\rm skew}^2)\); each nonzero determinant has
\(O(L)\) prime factors by the input size bounds. Consequently the
number of skewed primes in that dyadic interval is
\(O(L P_1 e^{-\Lambda})\).
The contribution from primes dividing \(bY_{\rm forb}\) is
\(O(L\ell^2)\) over the whole range. Even using the original
generous \(|\mathcal Q_{\rm exc}|\le e^{1.49\Lambda}\) bound,
each dyadic interval contains at most
\(P_1 e^{-.95\Lambda}\) bad primes eventually, since
\(P_1\ge B\) and \(\log B=(18+o(1))\Lambda\).
Summing reciprocals over \(O(\log y)\) dyadic intervals gives
\[
 M_{\rm bad}:=\sum_{p\in\mathcal P_{\rm bad}}\frac1p
 \le e^{-.94\Lambda}.
 \tag{2}
\]
All inequalities are effective in the widened parameter range.

## 4. Bad-child weighted rarity

Now assume the source's stronger prefix condition
\((y/2)^{u'}\ge6m X/H\) and
\(g\le\min(B,y^{.3})\).
For every bad prime dividing a contributing n, \(p\nmid m\):
if it divided m then it would divide g, but \(p>B\ge g\).

If a bad prime equals one of the h specified dyadic primes,
by the union bound put it in a fixed tail slot (multiply the
count by h). There is such a slot since \(u'\le2u<h\).
The count for C is the same as in Section 2; sum over the
specified bad prime and the other \(h-u'-1\) tail primes.
The normalized contribution is at most
\(2h(u'+1)! M^{h-u'-1}M_{\rm bad}/F\).

Otherwise a bad prime divides the free factor k. For fixed such
p and tail Q, \(C/p\) is an integer in a single residue class
modulo m, in an interval of length \(H/(pQ)\). Since \(p\le y\),
\[
 H/(mpQ)>\frac{4H(y/2)^{u'+1}}{5mpX}
          \ge \frac{24}{5}\frac{y/2}{p}\ge12/5.
\]
Thus its number of possibilities is at most \(2H/(mpQ)\).
Each has at most \((u'+1)!\) representations for C by Section 2.
Summing over p and Q gives a normalized contribution at most
\(2(u'+1)!M^{h-u'}M_{\rm bad}/F\).

Combining the cases and dividing by (1) yields
\[
 4\sqrt u\,(u'+1)! M^{-u'}(h/M+1)M_{\rm bad}.
\]
With \(u'\le2u\), (1), (2), and \(\log y=O(\Xi)\),
the factor \(4\sqrt u\,(u'+1)(h/M+1)\) is polynomial in L,
hence is eventually less than \(e^{.01\Lambda}\). The bound is
therefore at most
\[
 \{3(u'+1)\log y\}^{u'} e^{-.93\Lambda},
\]
as required. No unproved equidistribution statement was used in
this bad-child estimate.

This leaves nearby tuned-scale comparability, polynomial fibre
coupling, conditional moments and global readiness, square
certification and their Lean formalizations. The main weighted
AP asymptotic remains conditional on the actual QRH result and
its analytic consequences.
