# Linear norm-pairing budget and a nonlinear cubic alternative

28 November 2026. **Status:** elementary unconditional rank/discriminant obstruction for polynomial square-pairing on linear lattices, and exact analysis of the proposed constant-square slices in the fixed cubic. This screens a specified norm-envelope mechanism, not factoring algorithms in general. It complements [compact quadratic packet reduction](compact_quadratic_packet_walks.md) and [the projective discriminant theorem](projective_discriminant_barrier.md).

## 1. Local square pairing in a general order

Let A be a finite free commutative Z-algebra of rank d whose rational algebra is separable (a product of number fields is allowed). Write \(\Delta_A\ne0\) for the discriminant of the regular trace pairing. Let \(\Lambda\subset A\) be a full-rank integer lattice of index J, not necessarily an ideal or a ring. Fix a prime p. The image \(V\) of \(\Lambda\) in \(A/pA\) has codimension c, and \(v_p(J)\ge c\) by integer Smith normal form.

Over an algebraic closure of \(\mathbb F_p\), the Artinian algebra \(A/pA\) splits as a product of s local algebras of lengths \(e_1,\ldots,e_s\), each with residue field the algebraic closure. Their geometric characters \(\ell_i\) are independent linear functions on the full algebra. The determinant of multiplication is the polynomial
\[
 {\cal N}(x)=\prod_{i=1}^{s}\ell_i(x)^{e_i},\qquad \sum_i e_i=d.
 \tag{1}
\]
Indeed on each local factor multiplication by x is the sum of its residue scalar and a nilpotent operator; its determinant is the scalar to the length of the factor. The corresponding trace pairing factors through the s residue scalars: \(\operatorname{Tr}(xy)=\sum_i e_i\ell_i(x)\ell_i(y)\). Its rank modulo p is at most s, even when p divides some e_i. Consequently
\[
 v_p(\Delta_A)\ge d-s. \tag{2}
\]

Assume \({\cal N}|_V\) is not the zero polynomial (in particular this is necessary if a vector of the lattice has unit norm modulo p). Group the restrictions \(\ell_i|_V\) by proportionality over the algebraic closure. Let there be g groups; let \(E_j\) be the sum of the lengths in group j. All restrictions are nonzero. The residue-character map from V has image dimension at most g and kernel dimension at most \(d-s\), hence
\[
 c\ge s-g. \tag{3}
\]
Let o be the number of groups with odd \(E_j\). Because every even group has length at least two and every odd group length at least one, \(d\ge 2g-o\). Combining (2)–(3) proves
\[
 \boxed{
 v_p(J)+v_p(\Delta_A)\ge d-g\ge (d-o)/2 .
 }\tag{4}
\]
The number o is exactly the number of distinct odd linear factors of the norm form on V, by unique factorization over the algebraic closure. In particular a polynomial square identity on the lattice has o=0. The proof does not assume that p is unramified, the order monogenic, the lattice primitive, or the algebra a field. Ramification, index in a larger order, and coincidences of linear restrictions are all included. One must retain the nonzero-norm guard; a lattice with identically zero norm modulo p is not a square certificate.

A statement just about numerical square values at a few marks is not the polynomial-square hypothesis. Nor does an arbitrary efficiently computable square correction have to be a polynomial function on V. If a polynomial identity is inferred from equality of two polynomial functions on a finite vector space, check that the degrees in every variable are smaller than p; otherwise the implication can fail.

## 2. Global consequence for the generic lattice norm ceiling

Let N be squarefree, and suppose at each p|N the norm polynomial on the reduced lattice has at most o odd factors. Equation (4) gives
\[
 \boxed{
 J|\Delta_A|\ge N^{(d-o)/2},\qquad
 J\sqrt{|\Delta_A|}\ge N^{(d-o)/4}.
 }\tag{5}
\]
For arbitrary nonsquarefree N the same argument gives the displayed bounds with \(\operatorname{rad}N\) in place of N. We do not silently infer higher p-adic divisibility from a mod-p rank argument.

For a total-real order, the Minkowski covolume of the linear lattice is \(J\sqrt{|\Delta_A|}\) (for other signatures use the convention counting each complex pair twice in squared Euclidean norm; the same determinant results). Intersecting with an invertible ideal of index Q coprime to J gives a lattice of index JQ, by the integer lattice CRT; after dividing the norm by Q, the ordinary determinant-based Hermite/LLL upper envelope still contains \(J\sqrt{|\Delta_A|}\). If coprimality fails, the actual intersection index must be computed. Thus increasing d while imposing a polynomial square norm modulo N does not give a smaller **uniform envelope**: for o=0, even d≥4 forces the covolume factor to be at least N, already too large for a strict contraction of an N-scale packet by this envelope alone. The d=2 definite order of [compact packet walks](compact_quadratic_packet_walks.md) realizes the lower squarefree-N scale \(N^{1/2}\) up to its multiplier and a constant.

This is not a lower bound on the actual norm of every short element. Exceptional norm-controlled elements, nonlinear constraints, different modular square corrections, or constructions not based on this determinant envelope remain possible.

## 3. Constant-square slices in the cubic

There is a nonlinear alternative in the earlier cubic \(f=X(X-m)^2-N\), with m odd, unit modulo N, \(4m^3>27N\). The simple modular evaluation is the integer constant coefficient \(\ell(C)=C(0)\). The norm identity is
\[
 {\cal N}(C)\equiv \ell(C) C(m)^2\bmod N .
\]
Let \(\mathfrak a\) be an invertible ideal coprime to NA of index Q, in the explicit power order \(A=\mathbb Z[\theta]\). Put \(g\mathbb Z=\ell(\mathfrak a)\); g divides Q because \(QA\subset\mathfrak a\). Exact integer elimination supplies a vector \(t\in\mathfrak a\) with \(\ell(t)=g\) and a basis of \(K=\mathfrak a\cap\ker\ell\). All vectors in the affine slice
\[
 \alpha=g z^2 t + v,\qquad v\in K
\]
have constant coefficient \((gz)^2\). For any integer z coprime to N, the guarded norm gives
\[
 b={\cal N}(\alpha)/Q,\quad
 b\equiv Q\big(gz C_\alpha(m)Q^{-1}\big)^2\bmod N .\tag{6}
\]
This eliminates the earlier separate rational image port and the N-index gluing congruence, at the price of an archimedean affine-slice search. The square constant coefficient is chosen by public integer arithmetic, not by solving an unknown modular square-root problem.

The slice's determinant makes its limitation explicit. Write \(\theta_i\) for the three real conjugates. Newton's identities give
\[
 \operatorname{Tr}(\theta^2)=2m^2,\quad
 \operatorname{Tr}(\theta^3)=2m^3+3N,\quad
 \operatorname{Tr}(\theta^4)=2m^4+8mN .
\]
The rank-two kernel in the ambient order has basis \(\theta,\theta^2\), so its squared covolume is
\[
 2m^2(2m^4+8mN)-(2m^3+3N)^2=N(4m^3-9N).
\]
Since the image of the ideal under \(\ell\) is \(g\mathbb Z\), its kernel has index \(Q/g\) in this ambient rank-two kernel (apply the exact sequence of the linear functional). Thus
\[
 \boxed{\det K=(Q/g)\sqrt{N(4m^3-9N)}.} \tag{7}
\]
The squared dual norm of \(\ell\) on the real embedding space is \( (4m^3-9N)/(4m^3-27N)\ge1\), by the covolume relation for a primitive linear functional. Even the near-cusp discriminant reduction in the original cubic does not reduce (7) to a sub-N-scale factor when \(m\asymp N^{1/3}\).

When g=1, any nonzero vector \(\beta\in K\) can be written \(\theta\gamma\) with integral \(\gamma\in\mathfrak a\). In fact \(\theta\) has norm N, so is invertible modulo \(\mathfrak a\), using its multiplication adjugate and \((Q,N)=1\). Hence its product \(\theta\gamma\in\mathfrak a\) implies \(\gamma\in\mathfrak a\). The irreducible cubic ensures nonzero norm, and
\[
 |{\cal N}(\beta)|\ge NQ,\qquad
 \|\sigma(\beta)\|_2\ge\sqrt3(NQ)^{1/3}.
\]
Exact Gauss reduction in K bounds the longer basis length by a constant times \(\det K/\lambda_1(K)\) (size reduction and the rank-two determinant formula). With \(m^3=O(N)\) and g=1 this upper bound is \(O((NQ)^{2/3})\). Choose z=1, start at t, and round the two affine kernel coordinates by nearest plane in the real trace Gram metric. The orthogonal distance of the slice \(\ell=1\) from zero is at most one by the dual norm formula. The parallel rounding error is at most half the sum of the reduced kernel basis lengths. This gives a vector in the slice with norm \(O(1+(NQ)^{2/3})\), before the modular unit guard.

To enforce the latter, after trial division at primes at most \(2\operatorname{bitlength}N+1\), add independently sampled small integral multiples of the two kernel basis vectors. Their reduction maps onto the two-dimensional constant-zero coefficient space modulo every prime p dividing N: the kernel index \(Q/g\) is a unit. The form \(C(m)\) is nonzero on that space because m is a unit. The union bound on the two-coordinate affine linear condition gives a unit correction with probability at least one half when the coefficient interval has length \(2\operatorname{bitlength}N+1\). This is an exact guarded square-slice construction. Its simple uniform residual estimate in the g=1 case is only
\[
 |b|\ll (\operatorname{bitlength}N)^3 N^2 Q ,
\]
using AM-GM on the three real conjugates. It is not a useful replacement for the definite quadratic bound (1) in the companion note. Better actual slices could exist; this is an upper envelope, not their lower bound. The square-slice construction was analyzed here rather than subjected to a full comparative cubic numerical experiment; we prioritized the stronger exact quadratic transition and tested its nonprincipal compact walks instead.

## 4. Conclusion

The new local pairing budget identifies an intrinsic determinant cost for linear square-norm schemes, independent of how their number-field presentations are chosen. The cubic slice escapes the linear pairing hypothesis, but its explicit kernel geometry does not give the needed uniform contraction. The definite quadratic construction is consequently the stronger current packet reducer, with exact norm bound and compact nonprincipal class walks. The remaining research problem is a quarter-scale bound on actual residual rank or class-coset core mass, not another proof of the existence of modular square corrections.
