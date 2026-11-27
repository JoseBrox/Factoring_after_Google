# Fixed-field glued packet reduction with known-square images

27 November 2026. **Status:** new unconditional constructive joint ideal/rational-image transition for supplied factored packets, with one explicit totally real cubic field independent of the requested primes; exact gluing-order identities and finite pooled relation-supply experiments. The result does not establish a quarter-scale bound, because the uniform residual norm ceiling remains polynomial in N and the requisite factored initial packets have not been generated at quarter scale. This follows [normalized norm lattices](normalized_norm_lattice_supply.md), [known-square anchors](uniform_masked_anchor_supply.md) and [shared-base norm transport](shared_base_norm_transport.md).

## 1. The common gluing order for repeated targets

Let \(A\) be an explicit order in a separable rational algebra, with two jointly surjective modular maps \((\psi_0,\psi_1):A\to R^2\), \(R=\mathbb Z/N\). In the normalized polynomial model assume
\[
 \bar H=(X-t_0)(X-t_1)D^2,\qquad
 \gcd((t_1-t_0)D(t_0)D(t_1),N)=1.
\]
Write \(\kappa(C)=\operatorname{Res}(D,C)\bmod N\). For all elements whose multiplication determinant is a unit modulo N, the monic resultant identity gives
\[
 \operatorname{Norm}_A(C)\equiv\psi_0(C)\psi_1(C)\kappa(C)^2\pmod N.
 \tag{1}
\]
The following identities use actual orders and finite free algebras, not a heuristic about ideal classes.

Define the suborder and its modules
\[
 B=\{C\in A:\psi_1(C)=\psi_0(C)\},\qquad
 L(u)=\{C\in A:\psi_1(C)=u\psi_0(C)\}\quad(u\in R^\times).
\]
Their indices in A are exactly N. The conductor of B in A is the joint kernel I of the two evaluations: if \(aA\subset B\), use surjectivity to evaluate a times elements with residue pairs (1,0) and (0,1), forcing both evaluations of a to be zero. In particular \(\operatorname{disc}B=N^2\operatorname{disc}A\), not the smaller discriminant of the ambient order.

These are invertible B-ideals in its rational algebra (fractional ideals are allowed), and
\[
 \boxed{L(u)L(v)=L(uv),\qquad L(u)^{-1}=L(u^{-1}),\qquad A L(u)=A.}\tag{2}
\]
Proof: away from N, B and L(u) are both A locally. At each rational prime dividing N, polynomial CRT using the two simple endpoints and the coprime cofactor gives a unit \(\alpha\) of the localized A with residue components \((1,u,1)\). Such a unit lift exists: its residue is a unit modulo the appropriate prime power, and the localized ring is finite over a local integer ring. Then \(L(u)=\alpha B\) locally, because division by \(\alpha\) imposes diagonal equality of the two endpoint values. Multiplication and inversion give (2) locally at all primes, hence globally as exact integer lattices. The last identity follows from the same unit local generators. All products can be computed as HNF of the pairwise products of integral basis elements. The units-Picard exact sequence for this pullback also identifies \(u\mapsto[L(u)]\) as the gluing map into \(\operatorname{Pic}(B)\), with kernel the ratios \(\psi_1(a)/\psi_0(a)\) of \(A^\times\). Compare C. Weibel, *The K-book*, Ch. I, Thm. 3.10, [text](https://www.maths.ed.ac.uk/~v1ranick/papers/kbook). The explicit identities above do not require computing either Picard group.

### A single anchor universe

Use the localization at integers coprime to N, denoted \(A_{(N)}\), and similarly \(B_{(N)}\). An integral C with unit norm modulo N is a unit in \(A_{(N)}\) by the multiplication adjugate formula. If C and C' are guarded representatives of the same target ratio u, their quotient belongs to \(B_{(N)}^\times\). By (1), every norm of an element of this group has an explicitly known modular square root, computed by the common endpoint value times the cofactor correction, with multiplicative extension to fractions.

Because the degree of A is even, clearing an integer denominator coprime to N changes its norm by an actual rational square. Thus the group of all possible within-target **rational norm squareclass differences** is exactly
\[
 E_B=\{[\operatorname{Norm}_A(\alpha)]:\alpha\in B_{(N)}^\times\}
       \subset\mathbb Q^\times/(\mathbb Q^\times)^2 ,
 \tag{3}
\]
for every guarded target u. The inclusion from differences follows by the quotient; for the reverse inclusion multiply one guarded representative by \(\alpha\), and clear its integer denominator coprime to N. Its ratio remains u and its norm squareclass changes by the desired class. This proves that searching a single common anchor order can replace searches for pairs of new representatives for every fixed target.

For clarity, the unrestricted group (3) is not a finite small-rank factor base. If W is the group of norm squareclasses of \(A_{(N)}^\times\), reduction of rational classes modulo N followed by quotienting by modular squares gives a well-defined homomorphism
\[
 W\longrightarrow R^\times/(R^\times)^2.
\]
It is onto by the endpoint/cofactor CRT. Its kernel is precisely \(E_B\): choose a guarded representative C of a kernel class, let u be its endpoint ratio, and use (1) to see that u is a modular square. For existence only take a guarded element D with ratio a square root of u. Then \(CD^{-2}\) belongs to \(B_{(N)}^\times\) and its norm has the desired rational squareclass. This does **not** give a public algorithm for the latter step without the unknown root. Computing membership in the unrestricted norm-image group is not an efficient known-square certificate. We need a finitely generated bank with explicit correction data and an actual useful coverage bound.

## 2. A joint ideal reduction with no unmatched modular port

We first give the direct method for a totally real field of even degree with (1). Let \(\mathfrak a\subset A\) be an explicitly supplied integral invertible ideal coprime to NA, of index q. Put \(J=\mathfrak a\cap B\). The coprimality implies that \(\mathfrak a\) maps onto \(A/NA\); hence
\[
 [A:J]=Nq,\qquad [B:J]=q,\qquad AJ=\mathfrak a.
 \tag{4}
\]
The last statement follows locally at primes dividing N from \(\mathfrak a=A\), \(J=B\), and at the others from \(B=A\). The same local argument shows J invertible as a B-ideal. Construct J by the kernel of the single linear endpoint congruence on the supplied ideal basis, using integer HNF or extended gcds.

Choose a nonzero \(\alpha\in J\) with norm coprime to N. The actual ideal quotient \((\alpha)\mathfrak a^{-1}\) is integral and invertible and has index \(|b|\), where \(b=\operatorname{Norm}_A(\alpha)/q\) is a signed integer. Equation (1) gives
\[
 \boxed{qb\equiv c^2\pmod N,\qquad c=\psi_0(\alpha)\kappa(\alpha)\in R^\times.}\tag{5}
\]
This is a joint transition from the rational norm label q to b with a **known square correction**. The modular image has been paid for by membership in B; no arbitrary image port remains. In particular all rows with repeated or correlated q packets can be pooled by their rational residual squareclasses. The next section removes the necessity of a new field for each packet.

### A uniform, guarded residual ceiling

The following elementary bound makes the guarantee independent of the original ideal norm q. In any explicit totally real degree-d field, let \(J\) be a full-rank ideal of an order B and let \(M_B\ge1\) bound the absolute values of every embedding of every vector in a fixed integral basis of B. Exact LLL is performed using the positive trace Gram matrix. Its first vector \(b_1\) satisfies \(\|b_1\|_2\le2^{(d-1)/4}\operatorname{covol}(J)^{1/d}\). Since the field has no zero divisors, multiplying \(b_1\) by the d basis elements of B gives d independent vectors of J, of lengths at most \(M_B\|b_1\|\). Hence \(\lambda_d(J)\le M_B\|b_1\|\). Every vector in the LLL basis has length at most \(2^{(d-1)/2}\lambda_d(J)\): the last Gram-Schmidt length is at most \(\lambda_d\) by projecting d independent shortest vectors, the Lovasz inequalities bound earlier Gram-Schmidt lengths, and size reduction gives the stated bound on each basis vector.

After trial division at all primes at most \(R_0=2d\,\operatorname{bitlength}(N)+1\), sample independent coefficients in \(\{0,\ldots,R_0-1\}\) on this basis. For every p dividing N, the image of J contains 1 in \(A/pA\) (use coprimality and the defining congruence). Each geometric linear character of that finite commutative algebra thus defines a nonzero linear form on the coefficient space. Its probability of vanishing is at most \(1/R_0\): condition on all but one nonzero coordinate, working over an algebraic closure of \(\mathbb F_p\), and use that the interval is shorter than p. There are at most d characters at any p and at most \(\operatorname{bitlength}N\) such primes. The union bound gives a unit norm with probability greater than one half. A proper gcd is success. This is a genuine guard argument, unlike asserting the first LLL vector is a unit.

AM-GM on the d real conjugates now gives, on acceptance,
\[
 |\operatorname{Norm}\alpha|
 \le d^{-d/2}(dR_0 M_B)^d
        2^{3d(d-1)/4}\operatorname{covol}(J).
\]
Using (4) and \(\operatorname{covol}(A)=\sqrt{|\Delta_A|}\), we have the uniform bound
\[
 \boxed{|b|\le N\sqrt{|\Delta_A|}\,
           d^{-d/2}(dR_0M_B)^d2^{3d(d-1)/4}.}\tag{6}
\]
The polynomial-bit-time sampling and LLL steps work with the explicit ideal/order data, no regulator or maximal order required. This bound is far too large to imply quarter-scale residual supply. It illustrates the cost of the missing modular-image transition. The rank criterion, not the norm ceiling alone, determines whether a given batch is useful.

## 3. A preliminary shared quartic and its height problem

For any supplied finite list of odd rational request primes \(q_i\nmid N\), set \(Q=\prod_i q_i\), and choose an odd integer m coprime to NQ with \(m^4>8NQ\). For example \(m=2NQ+1\) is always sufficient; near the fourth-root threshold can be used if the gcd guards pass. Let
\[
 H=X(X-m)(X+m)^2-NQ .
\]
This is monic of degree four and irreducible modulo 2, where it is \(\Phi_5\), whose order of 2 modulo 5 is four. Thus H is irreducible over Q. Its signs at \(-2m,-m,-m/2,0,2m\) alternate, since \(3m^4/16>NQ\); it is totally real. It has the two endpoint maps at 0,m and the squared cofactor \(D=X+m\) modulo N.

For every q_i the residues 0 and m are simple roots modulo q_i (derivatives \(-m^3\) and \(4m^3\)); the root ideals \((q_i,\theta)\), \((q_i,\theta-m)\) are invertible of index q_i in the power order, even though the other factor can be repeated modulo q_i. This follows from the coprime simple linear Hensel factor: the local component in the order is \(\mathbb Z_{q_i}\), and the ideal is q_i on that component and the full order on the others. Thus a packet of k distinct odd primes has \(2^k\) possible orientation ideals with exactly the same rational norm. Apply (4)–(5) to each chosen orientation. No principal-prime-ideal hypothesis is used.

The problem is that the discriminant and coefficient heights grow with Q, even if an individual requested q is tiny. The finite tests below confirm that this inflates residual norms rapidly. The stronger fixed-field construction avoids this defect altogether.

## 4. A single fixed cubic for every rational request

**Theorem.** For odd N, choose any odd integer m with \((m,N)=1\) and \(4m^3>27N\). Set
\[
 f=X(X-m)^2-N,\qquad A=\mathbb Z[\theta],\qquad f(\theta)=0 .
 \tag{7}
\]
This is one explicit totally real cubic field, independent of all requested primes. For every supplied factored positive packet q coprime to N (including arbitrary exponents), there is a uniform polynomial-bit-cost ideal construction, followed by guarded randomized exact norm reduction, giving a signed integer b coprime to N and a known modular unit c with
\[
 \boxed{b\equiv q c^2\pmod N.}\tag{8}
\]
The guaranteed upper bound on \(|b|\) depends on N and the fixed field, but not on the original packet norm or its exponents. A proper gcd exit is always allowed. The sharper finite variants below use several choices of ideal over each request prime.

Proof of field properties. Modulo 2, f is \(X^3+X+1\), with no root in \(\mathbb F_2\), hence irreducible. Signs at \(0,m/3,m,2m\) alternate, proving three distinct real roots. Its discriminant is exactly
\[
 \Delta_A=N(4m^3-27N).
 \tag{9}
\]
The modular map \(\psi(C)=C(0)\) is a ring homomorphism; the repeated cofactor gives the universal exact identity
\[
 \operatorname{Norm}_A(C)\equiv C(0)C(m)^2\pmod N .\tag{10}
\]
This is the key reason a high-dimensional field unit cancellation is not needed for this particular transition.

For any supplied rational prime p of the packet, use a simple linear root ideal if one is found. Regardless of local factorization, the scalar ideal \(pA\) is invertible, has index \(p^3\), and is coprime to NA. Thus each prime can be assigned an invertible ideal of odd norm exponent (one or three); if p is unramified the odd total degree also ensures an odd-degree residue factor. Only the linear-root and scalar cases are needed by the construction. Known prime inputs permit polynomial-time randomized finite-field polynomial factoring, or just the scalar fallback; there is no need to factor N. At bad primes the scalar fallback remains valid. Multiply the chosen ideals to the supplied exponents, giving an integral invertible ideal \(\mathfrak a\) of index
\[
 Q_1=q a^2
\]
for an explicit positive integer a. The scalar choice simply contributes the additional square to the index. Ideal multiplication/HNF and exponentiation are polynomial in the actual ideal bit sizes. If the exponent values themselves are huge, expansion into an explicit ideal may have huge cost: we do not claim polynomial cost only in their binary lengths in that case.

Reduce \(\mathfrak a\) in the **fixed cubic**, using trace-Gram LLL, and choose a guarded \(\alpha\in\mathfrak a\). Write
\[
 \operatorname{Norm}_A\alpha=Q_1 b_1,\qquad
 v=\operatorname{least\ signed\ residue}(\psi(\alpha)),\qquad k=C_\alpha(m)\bmod N .
\]
Equation (10) gives \(Q_1 b_1 v\equiv(vk)^2\). Thus take
\[
 b=b_1v,\qquad c=vk/(q a)\pmod N .
\]
Both are units and (8) follows. Equivalently this is the gluing order in the fixed separable algebra \(A\times\mathbb Z\), with condition \(t=\psi(\alpha)\bmod N\) on the rational component t; the multiplication determinant is \(t\operatorname{Norm}\alpha\), a known square modulo N. The cubic is the only field needed. In particular **its discriminant does not contain the product of the request primes**, unlike the quartic construction.

The guarded bound proved above, now applied to \(\mathfrak a\) as an A-ideal of covolume \(Q_1\sqrt{\Delta_A}\), gives
\[
 |b|\le (N/2)\sqrt{\Delta_A}\,
            3^{-3/2}(3R_0M_A)^3\,2^{9/2} .\tag{11}
\]
All fixed-field constants are explicit. For the power basis \(1,\theta,\theta^2\), the sign brackets in the proof bound \(M_A\le 4m^2\). Formula (11) has no dependence on q or \(Q_1\). This removes the batch-height inflation from changing fields, not the N-scale cost of the square congruence itself.

**Near-cusp choice.** Choose m just above \((27N/4)^{1/3}\), odd and coprime to N. After trial division up to \(2\operatorname{bitlength}N+3\), at most \(\omega(N)\) consecutive odd choices in that scan can be excluded (each remaining prime excludes at most one). Thus \(m=(27N/4)^{1/3}+O(\log N)\) constructively, or a factor is found. From (9),
\[
 \Delta_A=O(N^{5/3}\log N).
\]
This is a genuine reduction of the field discriminant compared with choosing an arbitrary constant factor above the threshold, but not enough for a quarter-scale residual estimate.

## 5. Joint metric and pooling

For a fixed cubic ideal \(\mathfrak a\), one need not first reduce \(\alpha\) and then choose its least residue image. Reduce the four-dimensional lattice
\[
 J'=\{(\alpha,t)\in\mathfrak a\times\mathbb Z:
                    t=\psi(\alpha)\bmod N\}.
\]
It has coefficient index \(NQ_1\); a basis consists of the supplied ideal basis with its constant coefficients appended as last coordinates, and the vector \((0,N)\). Choose the exact positive metric
\(\|\sigma(\alpha)\|_2^2+w^2t^2\) for any rational positive w. Its covolume is \(wNQ_1\sqrt{\Delta_A}\). The norm objective is \(|t\operatorname{Norm}\alpha|/Q_1\); AM-GM cancels the scale w, so a first LLL vector has formal residual bound \(2^3\,4^{-2}N\sqrt{\Delta_A}\). This is only a usable bound if its norm and modular correction are units. No guard is assumed for that vector. A small collection of distinct weights and basis combinations is a legitimate candidate generation method; every resulting modular identity is checked. The independent cubic reduction supplies the uniform guarded fallback.

For a sealed public square representative \(s=q t_0^2\), with q its supplied positive squarefree part, each packet reduction gives a public norm parity row
\(b\equiv s(c/t_0)^2\pmod N\).
This permits exactly the [pooled-target certificate](normalized_norm_lattice_supply.md#5-pool-every-useful-representation-of-the-same-sealed-target). Repeated choices of prime ideal orientations, reduced elements, metric weights and even different fixed fields can all be pooled in one rational squareclass matrix. No new field-unit coordinates are introduced. A scalar fallback may be rank-neutral; it must not be counted as an independent useful relation just because its index is different. The useful dimension is the rank of the augmented norm/target matrix minus the norm rank, as before.

The critical remaining obstacle is to supply many small-rank **residual b classes**. Formula (11) only contracts arbitrarily large packets with actual height beyond its N-scale ceiling. Reducing the numerical size of a huge exponent by using an ideal of the corresponding power does not automatically improve a rational squareclass, since even exponents can already be dropped. For the relevant squarefree packets of size at most N, (11) is not a contraction theorem. Nor does this construction supply factorization of the public square representatives at quarter scale. The small experimental representatives below were factored as input data, not treated as a free subroutine in an asymptotic algorithm.

## 6. Relation supply: finite checks and next step

The new experiments are described in [the exact verification guide](../verification/research/README.md#fixed-field-glued-packet-reduction). They show that replacing a packet-dependent quartic by the fixed cubic materially reduces residual norm heights and, on several small inputs, produces useful sealed parity directions. This is a real constructive improvement to the earlier joint transport interface. It neither implies a uniform lower bound on useful parity density nor establishes the required initialization.

The most promising immediate continuation is to combine the fixed cubic packet move with the previous normalized norm lattice **on already supplied small prime factorizations**, and investigate whether a shared recursive residual pool admits a uniform height and rank contraction. Its advantage is that changing the field or ideal orientation does not add unit-log directions: the certificate uses actual rational norms and known square corrections. The current proof gives no quarter-scale bound on that pool, and no new general factoring exponent is claimed.
