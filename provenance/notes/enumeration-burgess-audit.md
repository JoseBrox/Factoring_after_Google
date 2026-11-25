# Independent audit of the enumeration and quadratic-field Burgess inputs

Date: 2026-11-25. Scope: Lemma 4.2 and Lemma 6.3(1), with the specific preceding facts they use, in the pinned Cogentic deterministic factoring paper. This is an ordinary mathematical audit, not a formal verification or a certification of all other sections of that paper.

## 1. Findings and exact proof contract

| Input | Finding | Action required in a final proof |
|---|---|---|
| Quadratic part of Lemma 4.2 | The elementary reduction proof checks through. The permitted complexity is polynomial in the **numeric discriminant**, not its bitlength. | Use its elementary cycle proof, with exact coefficients if desired. |
| Biquadratic part of Lemma 4.2 | Its claimed complexity can be obtained by the independent algorithm in Section 2 below. The source's long approximate infrastructure walk is unnecessary for this complexity class. | Substitute the direct weighted lattice algorithm below; do not import an unexamined infrastructure implementation. |
| Proposition 6.2 | False as written: it counts only roots in the base finite field for a general polynomial. | Count roots in an algebraic closure, or restrict the proposition to products of linear factors. All applications in Lemma 6.3 have that restricted form. |
| Lemma 6.3(1) | The varying-discriminant, prime-or-semiprime proof checks through after that correction. In particular, the small factor of a semiprime is explicitly handled. | Retain the hypotheses, including the least-prime guard and triviality on every unit. |

Thus these two inputs do not need to remain conjectural assumptions of an order-splitting theorem. The proof contract is specific: establish the order-test and compatible-root construction; establish the bounded-norm ideal-character assembly and local compatibility; apply the enumeration algorithm below to enforce its hypotheses; apply the audited Burgess estimate; then prove the chosen positive-average lower bound and parameter contradiction. This note supplies the enumeration and Burgess portions. It does not replace the character-assembly or order-test proofs.

For the original source theorem, the remaining assembly is its Lemma 3.1, Lemma 5.1, and the parameter/synthesis argument in Section 6. For the improved sparse method, the corresponding assembly is the field-specific cocycle proof and triangle Gram proof in the existing sparse note, supplemented by the ramification lemma in `splitting-provenance-audit.md`. The original full Walsh family and original smooth-number parameter choice are not needed for that improvement. Conversely, the improved sparse construction is not needed to close a general-factorization proof that can use the source's slower order splitter.

## 2. Independent replacement for Lemma 4.2

### 2.1 The complexity distinction that simplifies the proof

The requested complexity is

\[
\operatorname{poly}(|\Delta_F|,Z,\log N)
\quad\hbox{or}\quad
\operatorname{poly}(|\Delta_E|,Z,\log N).
\]

It is therefore permissible to store algebraic integers having coefficient bitlength polynomial in the numeric discriminant. In particular, a real quadratic fundamental unit with logarithm at most \(D\log D/2\) is inexpensive enough for this statement even when its numeric size is enormous. This is the main reason that exact quadratic arithmetic followed by direct weighted lattice reduction suffices.

The construction below has exactly the output needed by Lemma 4.2: modular images of a generating set of the unit group, and at least one generator of each principal integral ideal of norm at most \(Z\) that is coprime to \(N\). It can instead output a verified proper divisor when an intermediate small ideal norm has a nontrivial gcd with \(N\).

### 2.2 Quadratic fields: a finite exact algorithm

For an imaginary quadratic field, enumerate all algebraic integers of absolute norm at most \(Z\). In the representation \((x+y\sqrt{-D})/2\), the inequality \(x^2+Dy^2\leq4Z\) gives polynomially many pairs. Exact integral-basis membership selects the algebraic integers. Norm one gives all units, and every generator of an ideal of norm at most \(Z\) is included.

For a real quadratic field of discriminant \(D\), use primitive ideals

\[
 I(a,b)=a\mathbb Z+\frac{b+\sqrt D}{2}\mathbb Z,
 \qquad b\equiv D\pmod2,
 \qquad 4a\mid D-b^2.
\]

Every nonzero integral ideal is uniquely \(m I(a,b)\), with norm \(m^2a\). The reduced pairs obey

\[
0<\sqrt D-b<2a<\sqrt D+b.
\]

They satisfy \(1\leq a,b\leq\lfloor\sqrt D\rfloor\); there are fewer than \(D\) pairs. The exact Gauss step is

\[
a'=\frac{D-b^2}{4a},\qquad
b'=\lfloor\sqrt D\rfloor-
 ((\lfloor\sqrt D\rfloor+b)\bmod 2a'),
\]

and the ideal identity is

\[
\frac{-b+\sqrt D}{2}I(a,b)=a I(a',b').
\]

The step permutes the reduced pairs: the displayed formula recovers the previous \(b\), and then \(a\), from \((a',b')\). The cycle through \(\mathcal O_F\) has length below \(D\). The inverse of its product of the multipliers \((-b+\sqrt D)/(2a)\) is a fundamental unit \(\varepsilon>1\).

For completeness, the point distinguishing this unit from an arbitrary power is the backward-step argument. If a reduced principal ideal has a positive generator \(0<\sigma_1(\gamma)<1\), applying the inverse reduction step replaces it by a generator \(\gamma'\) with

\[
\sigma_1(\gamma)<\sigma_1(\gamma')\leq1.
\]

To prove the upper bound, write a hypothetical larger generator in the inverse reduced basis. The corresponding old generator has the form
\(va+u(-b_{-1}+\sqrt D)/2\). The bounds on its two embeddings force \(u\in\{-1,0,1\}\); each choice contradicts either \(0<\sigma_1(\gamma)<1\) or the required bound on \(|\sigma_2(\gamma)|\). There are only finitely many reduced pairs, and each inverse multiplier is bounded away from one. Repeated inverse steps must therefore reach the generator 1. Hence every positive unit is a power of the cycle unit and every reduced principal ideal occurs on that cycle. This is the source's elementary proof on PDF pp. 16–17, and its inequalities check through.

Each inverse cycle multiplier is below \(\sqrt D\), so

\[
\frac25<\log\varepsilon<\frac12D\log D.
\]

An arbitrary primitive ideal of norm \(a\leq Z\) is reduced in \(O(\log Z)\) steps followed by at most one normalization step. Indeed, when \(a>\sqrt D\), choose \(\widetilde b\equiv b\pmod{2a}\) with \(|\widetilde b|\leq a\); the new norm is \(|D-\widetilde b^2|/(4a)\leq a/4\). The final reduced pair is principal exactly when it lies on the principal cycle. Tracking the exact multipliers recovers a generator. The products involve \(O(D+\log Z)\) quadratic numbers whose numerator and denominator bitlengths are polynomial in \(\log(D+Z)\); storing and reducing these products costs polynomial time in \(D\) and \(\log Z\).

Multiply the recovered generator by an appropriate power of \(\varepsilon\) to arrange

\[
\left|\log\left|\frac{\sigma_1(\gamma)}{\sigma_2(\gamma)}\right|\right|
<3\log\varepsilon.
\]

An approximate logarithm with a fixed error margin suffices to choose the power; exact norm and integrality checks certify the algebraic output. Its exponent and coefficient bitlength are polynomial in \(D\) and \(\log Z\). This provides both exact algebraic generators and certified logarithmic approximations when requested.

Enumerating \(a\leq Z\), residues \(b\pmod{2a}\), and \(m\) with \(m^2a\leq Z\) costs polynomial time in \(Z\). Modulo an odd \(N\), denominators in the integral-basis representation are invertible. A generator with norm coprime to \(N\) has invertible modular image: apply the conjugate-norm identity, or the adjugate of its multiplication matrix. Thus this exact version supplies part (1) of Lemma 4.2 with the advertised polynomial bound.

### 2.3 Exact four-dimensional setup

Let \(E=\mathbb Q(\sqrt{d_1},\sqrt{d_2})\) be biquadratic and let \(F_i=\mathbb Q(\sqrt{d_i})\) be its three quadratic subfields. Write \(D_E=|\Delta_E|\). The standard biquadratic discriminant identity gives \(D_E=|\Delta_{F_1}\Delta_{F_2}\Delta_{F_3}|\), so the subfield discriminants are polynomially bounded in \(D_E\).

The ring of integers can be constructed by a constant-size exact search. Set

\[
L=\mathbb Z+\mathbb Z\sqrt{d_1}+\mathbb Z\sqrt{d_2}+\mathbb Z\sqrt{d_3}.
\]

Then \(4\mathcal O_E\subset L\). One direct verification is to write \(x=a_0+\sum_i a_i\sqrt{d_i}\): integrality of the trace and of each relative trace \(x+\tau_i(x)\in\mathcal O_{F_i}\) implies \(4a_i\in\mathbb Z\) for all four coordinates. Test the 256 cosets of \(L\) in \(\frac14L\) by checking that the characteristic polynomial of multiplication is monic with integral coefficients. Hermite normal form then gives an integral basis. All operations are in dimension four and have polynomial bit cost.

Enumerate all Hermite-normal-form sublattices of this integral basis of index at most \(Z\), and test closure under multiplication by the basis of \(\mathcal O_E\). These are precisely the integral ideals of norm at most \(Z\). A crude \(Z^{O(1)}\) bound suffices; no efficient-in-\(\log Z\) enumeration is claimed.

Fix one enumerated ideal \(\mathfrak B\), with norm \(B\). For each real quadratic subfield \(F_i\), compute

\[
\mathfrak n_i=N_{E/F_i}(\mathfrak B)
=(\mathfrak B\tau_i(\mathfrak B))\cap\mathcal O_{F_i},
\qquad N_{F_i/\mathbb Q}(\mathfrak n_i)=B.
\]

Ideal multiplication and contraction are fixed-dimensional integer lattice operations. If any \(\mathfrak n_i\) is nonprincipal, then \(\mathfrak B\) is nonprincipal. Otherwise the quadratic algorithm gives a balanced generator \(\gamma_i\) of \(\mathfrak n_i\), and a fundamental unit \(\varepsilon_i\). In a totally real biquadratic field there are three such subfields; in a CM biquadratic field there is one.

### 2.4 The parity reduction

Suppose \(\mathfrak B=(\beta)\). For every real subfield,

\[
N_{E/F_i}(\beta)=\pm\gamma_i\varepsilon_i^{2k_i+e_i},
\qquad e_i\in\{0,1\}.
\]

Set \(\beta'=\beta\prod_i\varepsilon_i^{-k_i}\). This still generates \(\mathfrak B\). The relative norm of \(\varepsilon_i\) to its own subfield is \(\varepsilon_i^2\), and its relative norm to a different quadratic subfield is its rational norm, hence has absolute value one. Consequently

\[
\left|N_{E/F_i}(\beta')\right|
=\left|\gamma_i\varepsilon_i^{e_i}\right|.
\]

This gives at most eight possible vectors of archimedean absolute values for \(\beta'\), known from \(\mathfrak B\) without knowing its original generator.

More explicitly, choose the first real embedding of \(F_i\) so that \(\varepsilon_i>1\), put

\[
\delta_i=\log|\sigma_{i,1}(\gamma_i)/\sigma_{i,2}(\gamma_i)|,
\qquad \ell_i=\log\varepsilon_i,
\]

and let \(s_{ik}\in\{\pm1\}\) record the restriction of the \(k\)-th embedding of \(E\) to \(F_i\). For a chosen parity tuple define

\[
T_k=-\frac14\sum_i s_{ik}(\delta_i+2e_i\ell_i).
\]

For the true parity tuple,

\[
\log|\sigma_k(\beta')|=\frac14\log B-T_k.
\]

In the totally real case this follows from

\[
\beta'^2 N_{E/\mathbb Q}(\beta')
=\prod_{i=1}^3 N_{E/F_i}(\beta').
\]

In the CM case it follows from \(\beta'\overline{\beta'}=N_{E/F^+}(\beta')\). Complex conjugate embeddings receive equal weights. Since \(|\delta_i|<3\ell_i\) and \(\ell_i\leq D_i\log D_i/2\), all \(|T_k|\) are \(O(D_E\log D_E)\). A substantially sharper bound is unnecessary.

### 2.5 One weighted LLL call per parity tuple

Equip the Minkowski image of \(\mathfrak B\) with the weights \(e^{T_k}\). For complex embeddings use the conventional \(\sqrt2\) weights on the two real coordinates of each complex embedding. For the true parity tuple every archimedean absolute value of \(\beta'\), after weighting, equals \(B^{1/4}\). Its Euclidean length is therefore \(2B^{1/4}\).

Every nonzero \(x\in\mathfrak B\) satisfies \(|N_{E/\mathbb Q}(x)|\geq B\): the integral principal ideal \((x)\) is contained in \(\mathfrak B\). Since the total logarithmic weight is zero, the arithmetic-geometric mean inequality shows that every such vector has Euclidean length at least \(2B^{1/4}\). Thus \(\beta'\) is a shortest vector in this weighted lattice.

Compute a rational approximation to the weighted basis with relative operator error at most \(1/1000\), clear its common denominator, and run exact \(\delta=3/4\) LLL in dimension four. The relative error ensures that each true shortest vector has length at most \(1.01\) times the length of the first reduced basis vector in the approximating metric. The standard reduced-basis inequalities

\[
|\mu_{ij}|\leq\tfrac12,
\qquad \|b_i^*\|\geq2^{-(i-1)/2}\|b_1\|
\]

then put its integer coordinates in a fixed box. Backward substitution gives, for example, the safe box \([-8,8]^4\). Enumerate that box, convert every vector back to an exact element of \(\mathfrak B\), and test its absolute norm. A vector of norm exactly \(B\) generates \(\mathfrak B\); if \(\mathfrak B\) is principal, the true parity tuple guarantees at least one such vector. No search over an exponentially large archimedean ball is required.

For \(\mathfrak B=\mathcal O_E\), retain **all** norm-one candidates from every parity tuple, and also retain the fundamental units of the real subfields. Every unit \(u\) is \(u'\prod_i\varepsilon_i^{k_i}\), where the corresponding balanced \(u'\) is one of the enumerated shortest vectors. These finitely many candidates and subfield units therefore generate \(\mathcal O_E^*\), including all roots of unity. This point requires retaining all qualifying candidates for the unit ideal, rather than merely its first generator.

### 2.6 Certified precision and bit complexity

The ideal HNF has entries at most polynomial in \(Z\). The unweighted embedding basis and its inverse have norms bounded by a polynomial in \(D_E,Z\): this follows from their entry bounds, the adjugate formula, and their nonzero determinant. The diagonal weights have logarithms bounded by \(O(D_E\log D_E)\). Thus the weighted matrix and its inverse have logarithmic norm

\[
O(D_E\log D_E+\log(Z+2)).
\]

Taking that many bits, with a sufficiently large absolute constant, makes entrywise rational approximation a relative operator approximation with the stated error. Square roots, logarithms, and exponentials can be computed by interval arithmetic with polynomial bit complexity at this precision. For exponentials, first divide the argument by a suitable power of two, use a convergent Taylor expansion on a bounded interval, and then square with an explicit error bound. This does not require a unit-cost real-arithmetic model.

After clearing denominators, the LLL input entries have bitlength polynomial in \(D_E\) and \(\log Z\). Exact LLL has polynomial bit complexity; the original 1982 theorem is sufficient. We do not rely on the source's more specific cubic bound for its chosen Gram-Schmidt implementation. The output change-of-basis coefficients and the exact field arithmetic also have polynomial bitlength. Repeating over \(Z^{O(1)}\) ideals and at most eight targets preserves \(\operatorname{poly}(D_E,Z,\log N)\).

The modular maps are evaluated only after exact algebraic membership/norm checks. If \(1<\gcd(B,N)<N\), return this factor. Because \(B\leq Z<N\), a gcd larger than one cannot equal \(N\). If the gcd is one, the norm identity proves that every generator image is a unit. Denominators in the explicit integral basis divide four and are invertible since \(N\) is odd. The supplied compatible roots ensure that these evaluations define the required ring homomorphism.

This establishes the output and complexity required from the biquadratic enumeration lemma. It removes, rather than assumes, the source's repeated infrastructure-step precision analysis.

## 3. Repair of Proposition 6.2

The source's proposition states a Weil bound using the number \(m\) of distinct roots **in \(\mathbb F_p\)** of a general polynomial that is not a constant times a square. This is false. For

\[
p=5,\qquad f(X)=X^3+2X,
\]

the only root in \(\mathbb F_5\) is zero, whereas

\[
\sum_{x\in\mathbb F_5}\left(\frac{f(x)}5\right)=-4.
\]

The printed bound would be zero. The correct theorem counts distinct roots in an algebraic closure. Equivalently for this proof, restrict the proposition to a product of linear factors over \(\mathbb F_p\). Every polynomial used in the sixteenth-moment argument is exactly

\[
f(X)=\prod_{r=1}^{16}(X+c_r),
\]

with some root of odd multiplicity. It is monic and is not a constant times a square, and all its distinct roots are already in the base field. Therefore the needed bound \(\left|\sum_x\chi_p(f(x))\right|<16\sqrt p\) follows from the standard theorem with no loss and no change to any exponent.

The original source cites Schmidt, *Equations over Finite Fields*, Chapter II, Theorem 2C', p. 43. The correct algebraic-closure formulation is also explicitly stated in the primary research papers listed in Section 6 below.

## 4. Audit of Lemma 6.3(1)

### 4.1 Hypotheses that must be retained

The field is quadratic, with discriminant absolute value \(D\). The modulus \(q\) is either an odd prime or the product \(p_1p_2\) of two distinct odd primes. It obeys

\[
P^-(q)>D,
\qquad D\leq q^{1/200}.
\]

A supplied square root defines \(\phi:\mathcal O_F\to\mathbb Z/q\mathbb Z\). The pulled-back quadratic character is one on **every unit**. The ideal \(\mathfrak b\) has norm \(B_0\leq\sqrt D\). The summation parameter satisfies

\[
q^{3/10}\leq W\leq q^{2/5}.
\]

The conclusion is

\[
\left|
\sum_{\substack{\gamma\in(\mathfrak b\setminus\{0\})/\mathcal O_F^*\\
1\leq|N\gamma|\leq B_0W}}
\chi(\phi(\gamma))
\right|
\leq C D^2 Wq^{-1/4000},
\]

with an effective absolute constant. None of these hypotheses is supplied by a generic character-sum citation; the source proves this particular uniform version explicitly.

### 4.2 Orbit representatives and lattice geometry

For an imaginary quadratic field, the orbit sum is the sum over a disk of radius \(\sqrt{B_0W}\), divided by the number of units. For a real quadratic field, choose the unique representative with positive first embedding and logarithmic absolute ratio in \([0,2\log\varepsilon)\). Partition this interval into pieces of width at most one. There are at most \(D^2\) pieces, by the audited fundamental-unit bound. Rescale the two embeddings on the \(k\)-th piece by \(e^{-k/2},e^{k/2}\); the corresponding region lies in a square of side \(4\sqrt{B_0W}\).

The rescaled lattice of an ideal of norm \(C_0\) has covolume between \(\frac12\sqrt D C_0\) and \(\sqrt D C_0\), and sup-norm minimum at least \(\sqrt{C_0/2}\). These bounds remain uniform even when the real fundamental unit is very large, because the rescaling preserves the product of the two coordinates.

The planar lattice-counting lemma is valid. A shortest Euclidean vector is primitive; completing it by a vector of least perpendicular height and reducing its projection gives a basis contained in a disk of radius less than \(2V/\mu\). Its centered fundamental parallelogram gives the claimed rectangle upper and lower bounds. Disjoint open sup-norm balls give the packing bound. In particular there is no hidden assumption that the lattice is uniformly round.

### 4.3 Parameters and boundary errors

For \(q\geq2^{8000}\), put

\[
\epsilon_0=\epsilon_1=q^{-1/4000},\quad
B=q^{1/32},\quad
\ell\asymp\epsilon_0\sqrt{B_0W},\quad
A=\frac{\epsilon_1\ell}{4\sqrt{B_0}B}.
\]

The explicit source grid obeys

\[
\tfrac18q^{0.11825}\leq A\leq\tfrac14q^{0.16825}.
\]

The ratio of lattice boundary thickness to \(\ell\) is below \(\epsilon_1\). The orbit-region boundary is covered by a constant number of graphs with Lipschitz constant one, including the hyperbola arcs in the real case. It meets \(O(\epsilon_0^{-1})\) grid cells. Lattice counting therefore bounds its contribution by \(960Wq^{-1/4000}\) for each archimedean strip.

Let \(\mathcal A\) be the nonzero algebraic integers in the unscaled box of radius \(A\) whose images are units modulo \(q\), and let \(\mathcal B_k\) be the points of \(\mathfrak b\) in the rescaled box of radius \(\sqrt{B_0}B\). The source's bounds

\[
\frac{A^2}{\sqrt D}<|\mathcal A|<\frac{16A^2}{\sqrt D},
\qquad
\frac{2B^2}{\sqrt D}<|\mathcal B_k|<\frac{16B^2}{\sqrt D}
\]

are valid. Removing the kernel of the small prime factor requires care, and is explicitly covered: when \(p_1\leq A\), count its sublattice by covolume; when \(p_1>A\), use the packing estimate. The other factor \(p_2>\sqrt q\) has no nonzero point in the small \(A\)-box because its points have norm at least \(p_2\), whereas these norms are less than \(\sqrt q\).

The products \(\beta\omega\) have sup norm at most \(\epsilon_1\ell/2\). Translating an interior cell by such a product loses at most

\[
\frac{16\epsilon_1\ell^2}{\sqrt D B_0}
\]

terms. All numerical margins have the correct direction under the stated parameter range.

### 4.4 Collision lifting and the second moment

For one interior cell define

\[
\nu(z)=\#\{(\gamma,\beta):
\gamma\in\mathfrak b\cap Q,
\ \beta\in\mathcal A,
\ \phi(\gamma)/\phi(\beta)=z\}.
\]

The first moment is at most

\[
K=\frac{128A^2\ell^2}{DB_0}.
\]

An equality of two ratios implies
\(\delta=\gamma_1\beta_2-\gamma_2\beta_1\in\mathfrak b\mathfrak q_F\), an ideal of norm \(B_0q\). Here \(\mathfrak b\) is coprime to \(\mathfrak q_F\), because \(B_0\leq\sqrt D<P^-(q)\). On the other hand,

\[
|N\delta|\leq16B_0WA^2\leq B_0q^{0.7365}<B_0q.
\]

Thus \(\delta=0\) exactly. Fixing \((\gamma_1,\beta_2)\), a matching \(\beta_1\) generates an ideal divisor of \((\gamma_1\beta_2)\), whose norm is below \(q^2\). A quadratic field has at most \(\tau(n)^2\) ideal divisors over an integer norm \(n\). The effective elementary bound \(\tau(n)\leq C n^{1/800}\), and the bound \(6\log q\) for generators of one ideal in the box, give

\[
\sum_z\nu(z)^2\leq C_1q^{3/500}K.
\]

The generator count uses the explicit positive lower bound on \(\log\varepsilon\), so no field-dependent constant is hidden. The divisor constant is enormous but effective; it has no dependence on the input.

### 4.5 The sixteenth moment, including unbalanced semiprimes

Put \(T(z)=\sum_{\omega\in\mathcal B_k}\chi(z+\phi(\omega))\). For every prime \(p_j\mid q\), the map \(\psi_j:\mathcal B_k\to\mathbb F_{p_j}\) is injective if \(p_j>8B^2\). This is always true for the larger prime factor, and for a prime modulus. Otherwise every fiber has size at most \(32B^2/p_j\), by ideal-lattice packing.

Expand \(\sum_z|T(z)|^{16}\) over ordered 16-tuples. There are three disjoint cases.

1. Every individual algebraic integer occurs an even number of times. There are \(O(|\mathcal B_k|^8)=O(q^{1/2})\) such tuples. Use the trivial character-sum bound \(q\).
2. Some residue modulo \(p_1\) has odd multiplicity. For a semiprime, injectivity modulo \(p_2\) then ensures an odd multiplicity there as well. The corrected Weil bound gives \(O(\sqrt q)\) per tuple, across \(O(|\mathcal B_k|^{16})=O(q)\) tuples.
3. Individual multiplicities are not all even, but residues modulo \(p_1\) have even multiplicity. This requires a semiprime with \(p_1\leq8B^2\). Pairing the 16 positions and using the fiber bound gives \(O(qp_1^{-8})\) tuples. The character bound is at most \(16p_1\sqrt{p_2}=16\sqrt q\sqrt{p_1}\). Their total is \(O(q^{3/2}p_1^{-15/2})\).

Consequently

\[
\sum_{z\bmod q}|T(z)|^{16}\leq C_2q^{3/2}.
\]

This third case is the essential protection against an arbitrarily small factor of the semiprime. Assuming both maps injective would be a fatal gap, but the source does not make that assumption.

### 4.6 Hölder and the power saving

Apply Hölder to
\(\nu^{7/8}(\nu^2)^{1/16}(|T|^{16})^{1/16}\). Divide by \(|\mathcal A||\mathcal B_k|\), substitute the preceding bounds, and obtain

\[
\frac{1}{|\mathcal A||\mathcal B_k|}\sum_z\nu(z)|T(z)|
\ll\frac{\ell^2}{B_0}
D^{1/16}
\left(\frac{B_0}{A^2\ell^2}\right)^{1/16}
B^{-2}q^{3/32+3/8000}.
\]

The source's exact final exponent is

\[
\frac1{3200}+\frac1{16000}-\frac3{80}
+\frac1{32000}-\frac{15}{256}+\frac3{32}+\frac3{8000}
=-\frac1{640}<-\frac1{4000}.
\]

Thus every interior cell contributes at most \(C\ell^2B_0^{-1}q^{-1/4000}\). There are at most \(16B_0W/\ell^2\) cells. Add the boundary contribution and the at most \(D^2\) real strips. This yields the asserted \(CD^2Wq^{-1/4000}\).

For \(q<2^{8000}\), the elementary ideal count \(\sum_{n\leq W}\tau(n)\leq W(1+\log W)\) is absorbed into a fixed effective constant. Hence no ineffective small-modulus exception remains.

## 5. Applying the bound to the sparse order splitter

After the bounded-norm character-assembly proof, every ideal class has an inverse representative of norm at most \(\sqrt D\). Multiplying an ideal in that class by its representative gives a principal ideal, so summing Lemma 6.3(1) over the at most \(D\) classes yields the unrestricted ideal sum bound

\[
|U_F(W)|\leq C D^3Wq^{-1/4000}.
\]

With the ramification-tolerant Gram lemma, only primes dividing \(q\) need be excluded from the positive average. At \(X=q^{1/3}\), a prime modulus exceeds \(X\), so no correction is needed. For \(q=p_1p_2\), also \(p_2>X\). If \(p_1\leq q^{1/50}\), subtract the contribution divisible by its nonselected degree-one prime ideal, which is its character times \(U_F(X/p_1)\); here

\[
q^{47/150}\leq X/p_1\leq q^{1/3},
\]

inside the permitted Burgess range. If \(p_1>q^{1/50}\), the elementary ideal-divisor bound makes that correction at most \(Xq^{-1/50}(1+\log X)\). Thus the coprime sum is still exponentially small in \(\log q\) when \(\log D=o(\log q)\).

No large primorial inclusion-exclusion is necessary in this version. The exact required algorithmic guards are that the least prime factor exceed the field discriminants, every ideal norm threshold used to enforce the cocycle and compatibility conditions, and the tested rational-prime threshold. Trial division establishes those guards without knowing the active prime or semiprime. The active character itself is a proof device supplied by the order-test lemma; the algorithm does not compute it.

The supplied-order cost retains its linear factor in \(\operatorname{bitlen}(M)\): each tested modular unit is processed by binary powering and a repeated-squaring gcd chain in \(O(\operatorname{bitlen}(M)\operatorname{poly}(\log N))\) bit operations. The enumeration algorithm depends polynomially on \(\log N\), not on the numeric size of \(M\), and cannot remove the cost of reading a supplied long exponent. This is separate from the harder task of constructing such an exponent in a general-factorization algorithm.

## 6. Sources and verification boundaries

- Pinned primary source: Google Research, *Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction*, commit `4a7bc8ab0bc770e71a259b7966c500496b99010a`, PDF blob `973002e0eb92acf3964fc020ca52ba6f1ac384ac`; PDF pp. 15–26. [Repository PDF](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf). Local checked extraction: `audit/sources/deterministic-paper.txt`.
- A. K. Lenstra, H. W. Lenstra Jr., L. Lovász, *Factoring polynomials with rational coefficients*, Math. Ann. 261 (1982), 515–534. [Author-hosted original paper](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1982f/art.pdf). Its reduced-basis inequalities and polynomial bit complexity are sufficient; no special modern lattice routine is assumed.
- W. M. Schmidt, *Equations over Finite Fields: An Elementary Approach*, Lecture Notes in Mathematics 536 (1976), Chapter II, p. 43. [Publisher record](https://link.springer.com/book/10.1007/BFb0080437).
- The correct distinct-roots-in-a-splitting-field character-sum statement is explicitly printed in the primary research article *Ample simplicial complexes*, Appendix A, Theorem A.1. [Accepted manuscript](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/75407/Farber%20Ample%20simplicial%20complexes%202021%20Accepted.pdf?isAllowed=y&sequence=2). It is also stated as Lemma 2.1 in *Explicit constructions of Diophantine tuples over finite fields*. [Publisher article](https://link.springer.com/article/10.1007/s11139-024-00888-5).

The finite-field counterexample and exact rational exponent identity are independently reproducible in `verify_enumeration_burgess_audit.py`. Those computations check those two specific claims. They do not establish the universal analytic estimate or certify a lattice implementation; those are mathematical arguments given above. No implementation of the full enumeration algorithm or factoring algorithm has been executed in this audit.
