# A discriminant diameter bound for low-height terminal charts

27 November 2026. **Status:** proved unconditional binary-form theorem, with an explicit obstruction to the shared transformed-lattice quarter-scale route. This strengthens the weaker necessary height ledger in [beyond one-third](beyond_one_third_research.md), §3. It is not a lower bound for factoring, nor for arbitrary algebraic elements or nonprojective changes of primitive element. No smoothness or distribution theorem is needed.

## 1. Local content and discriminant

Let \(F\in\mathbb Z[X,Y]\) be a primitive homogeneous degree-d form with nonzero discriminant, \(d\ge3\). Let \(A\in {\rm GL}_2(\mathbb Q)\), and let \(G\) be the primitive integral form proportional to \(F\circ A\), unique up to sign. Write \(\Delta_F=|\operatorname{disc} F|\) and \(\Delta_G=|\operatorname{disc} G|\); both are positive integers.

At each prime \(p\), write a local Smith decomposition
\[
 A=p^u U\operatorname{diag}(1,p^a)V,\qquad
 U,V\in {\rm GL}_2(\mathbb Z_p),\quad u\in\mathbb Z,\quad a=a_p(A)\ge0.
\]
Unit scalar factors are absorbed into U,V. The integer a is the difference of the two elementary-divisor valuations, independent of the decomposition. Scalar factors \(p^u\) cancel in primitive normalization, while U,V preserve local content and discriminant valuation. Thus it suffices to study \(F_0\circ\operatorname{diag}(1,p^a)\), with \(F_0=F\circ U\) locally primitive.

Factor \(F_0=C\prod_{i=1}^d(\alpha_i X+\beta_iY)\) over an algebraic closure of \(\mathbb Q_p\), using the extended valuation \(v(p)=1\). Normalize every linear factor to have \(\min(v(\alpha_i),v(\beta_i))=0\); allow \(v(0)=+\infty\). By multiplicativity of the nonarchimedean Gauss norm, \(v(C)=0\), because \(F_0\) is locally primitive. Define
\[
 w_i=\min(v(\alpha_i),a+v(\beta_i)),\qquad 0\le w_i\le a,\qquad c=\sum_i w_i .
\]
Then c, an integer, is exactly the p-adic valuation of the coefficient content after the cyclic lattice transformation. If both weights are positive then both \(\beta_i,\beta_j\) are units, and \(v(\alpha_i),v(\alpha_j)\ge w_i,w_j\). Hence for every pair
\[
 v(\alpha_i\beta_j-\alpha_j\beta_i)\ \ge\ \min(w_i,w_j).
\]
The same inequality is immediate when one weight is zero. Since \(\min(w_i,w_j)\ge w_iw_j/a\) for \(a>0\), the binary discriminant identity gives
\[
 \begin{split}
 v_p(\Delta_F)&\ge 2\sum_{i<j}\min(w_i,w_j)\\
 &\ge\frac{c^2-\sum_i w_i^2}{a}
 \ \ge\ \frac{c^2}{a}-c .
 \end{split} \tag{1}
\]
The stronger piecewise-linear version is \(v_p(\Delta_F)\ge a k(k-1)+2ka\theta\) when \(c/a=k+\theta\), \(k=\lfloor c/a\rfloor\), \(0\le\theta<1\): order the weights and move mass toward the largest weights until all but at most one are 0 or a. Each such move cannot increase the sum of pairwise minima. Only (1) is needed below.

The exact discriminant transformation is
\[
 v_p(\Delta_G)=v_p(\Delta_F)+d(d-1)a-2(d-1)c . \tag{2}
\]
This holds with all multiplicities and contents, including a root at infinity. It follows directly from the determinant of each pair of linear factors; scaling a degree-d form by a scalar scales the discriminant by that scalar to power \(2d-2\). Combining (1) and (2) gives
\[
 v_p(\Delta_G)\ge \frac{(da-c)^2}{a}-(da-c)
\]
and, more importantly,
\[
 \boxed{
 v_p(\Delta_F)+v_p(\Delta_G)
 \ \ge\ \frac{2}{a}(c-da/2)^2+\frac{d(d-2)}2\,a
 }\quad(a>0). \tag{3}
\]
For \(a=0\) the local discriminant valuations are equal, and the weaker nonnegative right side \(d(d-2)a/2\) holds trivially. This proof includes nonmaximal orders and arbitrarily high ramification. In particular removing large polynomial content cannot make the sum of the two discriminant costs disappear.

At a good simple finite root of F mod p, an index-p^a cyclic lattice along that root has content valuation at most a: at most one weight is positive in the local factorization, since the reduction has multiplicity one. If a=1 and the lattice line lies in that root, the coefficient content has valuation exactly one. Thus (2) alone gives an increase of at least \((d-1)(d-2)a\) at such a prime. More generally, if the lattice line has reduction multiplicity r, then \(c\le ra\). Equation (1) shows why even a deliberately repeated root with \(c\) comparable to da consumes a large discriminant budget. These statements refer to polynomial content, not merely divisibility of particular values.

## 2. Global diameter

Define the projective index measure
\[
 {\cal I}(A)=\prod_p p^{a_p(A)} .
\]
It is unchanged by multiplying A by a nonzero rational scalar or by integral unimodular changes of coordinates on either side. For an integer full-rank matrix of Smith invariants \(s_1\mid s_2\), it is \(s_2/s_1\), not necessarily the absolute determinant. Summing (3) over p yields
\[
 \boxed{\Delta_F\Delta_G\ge{\cal I}(A)^{d(d-2)/2}.} \tag{4}
\]
The inequality is purely arithmetic and does not depend on the conditioning of A at the real place.

For coefficient sup norms \(H_F,H_G\), the usual Mahler-measure discriminant bound can be derived directly, including a simple root at infinity. Factor a binary form over \(\mathbb C\) as \(C\prod(\alpha_iX+\beta_iY)\) with \(\max(|\alpha_i|,|\beta_i|)=1\). The Vandermonde matrix of the d rows \((\alpha_i^{d-1},\alpha_i^{d-2}\beta_i,\ldots,\beta_i^{d-1})\) has determinant, up to sign, \(\prod_{i<j}(\alpha_i\beta_j-\alpha_j\beta_i)\). Every row has Euclidean norm at most \(\sqrt d\). Hadamard therefore bounds the absolute discriminant by \(d^d|C|^{2d-2}\). The elementary logarithmic circle integral for a linear factor gives \(|C|=M(F(X,1))\), even if a factor Y occurs. Jensen's inequality for the logarithm and Parseval give \(M(F(X,1))\le\sqrt{d+1}\,H_F\). Consequently
\[
 \log\Delta_F\le d\log d+(d-1)\log(d+1)+2(d-1)\log H_F.
\]
The corresponding estimate for G and (4) imply
\[
 \boxed{\log{\cal I}(A)\le
 \frac{4(d-1)(\log H_F+\log H_G)
       +4d\log d+4(d-1)\log(d+1)}{d(d-2)}.} \tag{5}
\]
All logarithms are natural. No discriminant factorization or number-field arithmetic is needed to apply the bound.

For an arbitrary fixed original form F (possibly of very large height), consider a family \(F_i=\operatorname{primitive}(F\circ A_i)\) of projectively transformed models. Apply (5) to \(F_i,F_j,A_i^{-1}A_j\), because the transformed forms are rationally proportional. If every model has height at most H, then
\[
 \log{\cal I}(A_i^{-1}A_j)
 \le \frac{8(d-1)\log H+4d\log d+4(d-1)\log(d+1)}{d(d-2)}.
 \tag{6}
\]
This is a pairwise bound; it does not charge the original form height.

**Local uniqueness consequence.** At any prime p whose logarithm exceeds the right side of (6), the lattices \(A_i\mathbb Z_p^2\) are all homothetic: the relative local Smith difference is zero. They cannot impose different projective lines or different primitive cyclic-index depths there. This is the lattice formulation of the diameter bound; it does not require the coordinates to be integral globally.

## 3. Implication for the quarter-scale research

Write \(L=\log N\). The proposed terminal regime in [the transformed-height ledger](beyond_one_third_research.md), §3, has
\[
 d=L^{1/2+o(1)},\qquad \log H\le L^{1/2+o(1)},\qquad
 \log B=L^{1/4+o(1)}.
\]
The right side of (6) is only \(L^{o(1)}\), much smaller than \(\log B\). Thus **one shared projective binary-form family cannot provide different low-height terminal charts at any of the large request primes \(p>B\)**. In particular two distinct primitive index-prime special lattices for distinct primes cannot both lead to low-height models of the same F: at each of those two primes their relative Smith difference is one, even if F itself is allowed to have very large height. Two different lines at the same prime likewise have positive relative Smith difference.

If the original form itself is low-height, (5) excludes even one such index-p chart. This rules out the suggested escape of just forcing ramified polynomial content in a common low-height form; the obstruction remains valid for arbitrary high valuations, by (3). It also extends to \(\alpha>1/4\) whenever the proposed degree and height satisfy \(\log H/d+\log d/d=o(\log B)\). For example the weaker ledger \(d\ge L^{1-2\alpha-o(1)}\), \(\log H\le L^{2\alpha+o(1)}\) ensures this for every fixed \(1/4\le\alpha<1/3\), since \(4\alpha-1<\alpha\).

There is no contradiction with the earlier *single* transformed-height ledger: one can start with a large-height form and design one favorable chart. What is now ruled out is sharing that form across distinct large-prime charts with uniformly low coefficient heights. A common chart can still contain many imposed divisibilities; (6) does not show that they yield independent useful relations after normalization. Nor does it bound actual small values of a high-height polynomial at selected points, changes of primitive element of higher degree, arbitrary ideal-lattice reduction, or different fields.

**Research decision.** Stop trying to get the quarter scale solely by projective special-lattice changes of a single binary form, even with repeated-root content. Favor constructions controlling the *actual* norms of marks, rather than a uniform binary-form height envelope, and charge the rank of the resulting shared unit subgroup. The [exact unit certificate](exact_descent_unit_certificate.md) remains available for these routes. The separate norm-one interpolation continuation tests this alternative constructively.
