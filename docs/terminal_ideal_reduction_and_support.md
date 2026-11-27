# Terminal ideal reduction and a bounded-height number-field support theorem

27 November 2026. **Status:** two unconditional results clarifying the next quarter-scale interface. The first is a constructive ideal-norm reduction using exact lattice arithmetic. The second bounds the support of low-norm, bounded-archimedean-height elements uniformly in the field discriminant and signature. Neither supplies a full relation-generation theorem. These follow the [projective diameter bound](projective_discriminant_barrier.md), [norm-one interpolation rigidity](norm_one_terminal_interpolation.md) and [probe-free unit certificate](exact_descent_unit_certificate.md).

## 1. Constructive terminal ideal move, without a binary-form envelope

Let A be an explicitly given order in a totally real degree-d number field K. Let \(\mathfrak a\subset A\) be a nonzero integral invertible ideal, given by a lattice basis in the order. Write \(q=[A:\mathfrak a]\), \(D_A=|\operatorname{disc} A|\). Assume an explicit ring homomorphism \(\psi:A\to\mathbb Z/N\) carrying 1 to 1 is known. It is surjective, and its kernel I is an ideal of index N.

Apply ordinary LLL with parameter \(3/4\) to the ideal lattice in the real Minkowski embedding. This can be done with exact integral Gram entries \(\operatorname{Tr}_{K/\mathbb Q}(b_i b_j)\) of the provided ideal basis, which are positive definite for a totally real field; the multiplication table and trace are sufficient. Standard exact LLL has polynomial bit complexity in the lattice/Gram data. The covolume is \(q\sqrt{D_A}\). Its first reduced vector is a nonzero \(\alpha\in\mathfrak a\) satisfying
\[
 \|\sigma(\alpha)\|_2\le2^{(d-1)/4}(q\sqrt{D_A})^{1/d}.
\]
By AM–GM on its d squared absolute conjugates,
\[
 |N_{K/\mathbb Q}\alpha|
 \le 2^{d(d-1)/4}d^{-d/2}\sqrt{D_A}\,q.
 \tag{1}
\]
Because \(\mathfrak a\) is invertible, the ideal \(\mathfrak b=(\alpha)\mathfrak a^{-1}\) is integral and invertible and
\[
 [A:\mathfrak b]=|N_{K/\mathbb Q}\alpha|/q
 \le 2^{d(d-1)/4}d^{-d/2}\sqrt{D_A}.
 \tag{2}
\]
Here \((\alpha)\subset\mathfrak a\), and norm multiplicativity for invertible ideals of an order follows by local principal generation, or by the determinant of their lattice multiplication maps. The bound is independent of the requested ideal norm q. All ideal operations and the two norm indices can be verified by exact rational integer-lattice calculations. One need not compute the maximal order. An order with large discriminant is not automatically a useful input to this theorem.

There is also a modular-unit guarantee. If the RHS of (1) is strictly less than N, then \(\psi(\alpha)\ne0\bmod N\), since \((\alpha)\subset I\) would imply \(N\mid[A:(\alpha)]=|N_{K/\mathbb Q}\alpha|\). Thus the gcd of \(\psi(\alpha)\) with N either gives a proper divisor or equals one. If it is a unit, we have a verified compact algebraic move that replaces the ideal valuation vector of \(\mathfrak a\) by that of \(\mathfrak b\), using \((\alpha)=\mathfrak a\mathfrak b\).

For general signature the same norm bound up to a fixed exponential-in-d factor can be obtained by a rational approximation of the positive Minkowski Gram form; this extension is not needed for the present theorem, and the exact implementation above is only asserted for totally real orders. The classical LLL bound is the only algorithmic lattice input.

### Quarter-scale consequence and precise missing transition

Write \(L=\log N\), \(\Lambda_{1/4}=L^{1/4}(\log L)^{3/4}\) and \(B=\exp(\Theta(\Lambda_{1/4}))\). If a shared order is available with
\[
 d^2+\log D_A=O(L^{1/2}(\log L)^{1/2}),
\]
then the residual norm in (2) has log-size at most this half-scale quantity. Its complete factorization by the existing one-third route, if that written theorem is validated, would cost \(\exp(O(L^{1/6}(\log L)^{5/6}))\), which is subleading at the quarter scale. A classical unconditional half-scale integer factorer instead gives a quarter-scale factorization cost for this residual. Neither fact proves that the residual is B-smooth or that all its prime-ideal factors lie in a small common support.

If the stronger bound \(d^2+\log D_A=O(\Lambda_{1/4})\) holds, every residual norm itself is at most \(B^{O(1)}\); the whole residual ideal universe can then be included in a support budget \(B^{O(1)}\) (use the ideal count in §2 below). This is an actual norm-bound mechanism, not the uniform binary-form height envelope ruled out by the projective diameter theorem.

The move does **not** solve the modular side. Replacing a valuation of \(\mathfrak a\) by multiplication/division by \(\alpha\) introduces the public modular image \(\psi(\alpha)\), for which (1)–(2) give no small rational representation or shared support. It may be an essentially arbitrary residue, even if \(\mathfrak b\) has norm one. The example \(K=\mathbb Q,\ \alpha=q\) makes the distinction clear. No algorithm may omit this image from its row identity. One still needs a shared supply of small-discriminant orders with known evaluation maps, and a joint algebraic/rational move that controls the modular images or their combined residual rank. This is an exact alternative interface to the failed projective-coordinate approach.

## 2. Field-uniform support bound

Let K be any number field of degree d, of arbitrary signature and discriminant. For \(0\ne\gamma\in K\), write its principal fractional ideal in the maximal order in lowest terms,
\[
 (\gamma)=\mathfrak a/\mathfrak b,\quad
 \mathfrak a,\mathfrak b\text{ coprime integral ideals}.
\]
Define \(\mathcal E_K(X,A)\) to be the elements satisfying
\[
 N\mathfrak a\,N\mathfrak b\le X,\qquad
 \sum_{\sigma:K\hookrightarrow\mathbb C}
       |\log|\sigma(\gamma)||\le A ,
 \qquad X\ge1,\ A\ge0 .
\]
Embeddings include both members of every complex conjugate pair. The bound below counts arbitrary fractional elements, not just smooth norms or elements of one fixed power basis.

**Theorem.** Uniformly in K,
\[
 \#\mathcal E_K(X,A)
 \le 2e\,d^2 X(1+\log(2X))^{2d}
       \big(1+2A\sqrt d\,(\log(3d))^3\big)^{d-1}.
 \tag{3}
\]
For d=1 the last factor is interpreted as one.

**Finite ideals.** For \(s=1+1/\log(2X)>1\), dropping coprimality increases the number of ideal pairs. Rankin and the Euler factors give
\[
 \#\{(\mathfrak a,\mathfrak b): N\mathfrak aN\mathfrak b\le X\}
 \le X^s\zeta_K(s)^2
 \le eX\zeta(s)^{2d}
 \le eX(1+\log(2X))^{2d}.
\]
At p the number of prime ideals over p is at most d and their residue degrees are at least one, proving the zeta comparison. The last bound is the elementary integral upper bound on the rational zeta sum. No hypothesis about the zeros of either zeta function is involved.

**Archimedean multiplicities.** Fix one ideal pair with at least one generator \(\gamma_0\) in the restricted set. Every other generator is \(\gamma_0 u\) for an algebraic unit u. Its log vector has Euclidean norm at most \(2A\), by the defining \(\ell_1\) bounds on the two generators. The non-torsion log-unit vectors have minimum Euclidean length greater than
\[
 \epsilon_d=2/(\sqrt d\,(\log(3d))^3).
\]
To see this use Voutier, *An effective lower bound for the height of algebraic numbers*, Acta Arithmetica 74 (1996), 81–95, Corollary 2 on p.84, [DOI](https://doi.org/10.4064/aa-74-1-81-95), [primary PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7417.pdf) (the stated corollary checked against the page image). It gives \(\log M(u)>2/(\log(3e_u))^3\) for non-torsion u of degree \(e_u\ge2\). The sum of the positive log coordinates over K's d embeddings is \((d/e_u)\log M(u)\), since a unit is integral and its embeddings in K repeat those in its own field. Cauchy–Schwarz gives the stated gap. Rational units are torsion. This is a polynomial-size separation estimate, stronger than the elementary exponential gap used in our earlier certificate precision ledger, and it does not assume Lehmer's conjecture.

Dirichlet's unit lattice has real dimension \(r\le d-1\). Disjoint open balls of radius \(\epsilon_d/2\) centered at the log vectors of norm at most \(2A\) fit in the ball of radius \(2A+\epsilon_d/2\) in that span. Hence there are at most \((1+4A/\epsilon_d)^r\) distinct such vectors. The fibres of the log map have at most \(2d^2\) elements: a primitive m-th root of unity in K requires \(\phi(m)\le d\), and \(\phi(m)\ge\sqrt{m/2}\), by the prime-power Euler formula (only the factor 2 to its first power loses \(\sqrt2\)). The roots of unity of a number field form one finite cyclic group. Multiplying by the ideal-pair bound proves (3). The argument also covers log rank zero.

This is a count, not an algorithm enumerating those elements. It can replace the much weaker log-unit separation used in the earlier [exact certificate](exact_descent_unit_certificate.md), improving the dependence of certified log precision on the degrees, without changing its polynomial bit-complexity status.

## 3. Application to sealed initialization and shared terminal relations

Suppose a menu of J fields, orders and specified modular evaluation maps is fixed *before* a fresh independent private unit square s is sampled. A field in the menu may itself have been chosen adaptively using previous public rows, but condition on the complete prior history so that the menu for the next square is fixed. Any rational scalars, shifts, and alternative evaluation maps that can be used must be counted in the menu or separately. Only elements for which the particular localized order evaluation is defined and is a unit are admissible; restricting (3) to these can only decrease the support.

If a public expression is allowed to be one such element from each of at most r selected menu entries (with repetition), and each element satisfies the same bounds \(d\le D,\ X,\ A\), its total residue support has size at most
\[
 (1+J\,C(D,X,A))^r,\qquad
 C(D,X,A)=2e D^2 X(1+\log(2X))^{2D}
      (1+2A\sqrt D(\log(3D))^3)^{D-1}.
\]
Pad shorter expressions by identity factors. If a different degree bound or archimedean budget is used per field, sum its actual logarithmic support bounds instead. The support includes only actual resulting field elements; splitting a compact product into syntactic atom occurrences must not be used to undercount its norm or logarithmic height.

For a balanced odd semiprime the square group has cardinality \(\asymp N\). Hence a fixed positive success density in this regime requires
\[
 r\,[\,\log J+\log X+O(D\log(2D(1+A)(1+\log(2X))))\,]\ \ge\ L-O(1)
\]
(up to harmless absolute constants). In particular when \(D=L^{1/2+o(1)}\), \(\log X\le L^{1/2+o(1)}\), \(A\le L^{O(1)}\), and \(\log J=O(\Lambda_{1/4})\), a single field element or \(L^{1/2-\varepsilon}\) such independent bounded field parts cannot have a dense uniform-square support, for fixed \(\varepsilon>0\). One needs at least \(L^{1/2-o(1)}\) independently variable bounded field parts, or a larger total norm/archimedean budget, or a menu selected after seeing the square. A polynomial number of parts of this order is **allowed** by the time budget, so this is not an impossibility result for a growing multilevel descent. It is a quantitative obligation on a proposed direct initialization or terminal compression theorem.

This explains why the norm-one lifts in [the interpolation construction](norm_one_terminal_interpolation.md) can encode arbitrary modular targets despite having zero finite norm support: their field is selected *from those targets*. Its archimedean unit directions then contribute to the certificate's rank. One cannot silently use a fixed-menu density argument for such a target-dependent family. Compact powers with archimedean log height much larger than polynomial in L are not ruled out by the quarter-scale corollary.

**Next mathematical interface:** construct a joint ideal-reduction and modular-image transition with a genuinely compressed support/rank budget, rather than a norm-only reduction or a rank-neutral unit lift. The exact support theorem and constructive ideal move can be used together to screen candidate shared fields. No sub-one-third complexity result follows yet.
