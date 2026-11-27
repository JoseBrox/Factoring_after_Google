# Hensel-normalized norm lattices and pooled sealed-target relations

27 November 2026. **Status:** unconditional exact uniform representation theorem, exact lattice-index and localization identities, and finite norm-lattice search with positive and negative results. The quarter-scale arithmetic supply theorem remains open. This follows [paired norm affine lifts](paired_norm_affine_lift.md), §4, and [square-aware binary presentation](square_resultant_norm_transport.md). Replace prescribed endpoint values by one homogeneous ratio condition, and permit controlled nonunit cofactor resultants before exact normalization.

## 1. One modular condition

Fix odd composite N, \(R=\mathbb Z/N\). Let \(D\in\mathbb Z[X]\) be monic of degree \(r\ge1\), \(d=2r+2\), and H monic of degree d, with
\[
 H\equiv (X-t_0)(X-t_1)D^2\pmod N,\qquad
 \gcd((t_1-t_0)D(t_0)D(t_1),N)=1. \tag{1}
\]
The two endpoint roots are simple modulo every prime dividing N. The full cofactor can be nonseparable modulo N. We do not require irreducibility over Q: norms are multiplication determinants in \(\mathcal A=\mathbb Z[X]/(H)\). For archimedean embedding statements separately require nonzero discriminant.

Such an environment is easy to construct: take \(t_0=0,t_1=1,D=X^r+1\), and lift (1). Adding a constant \(aN\) preserves the congruence; at most d-1 values of a give a repeated complex root (a repeated root must be a root of the unchanged derivative). Thus a separable lift can be chosen by an explicit finite discriminant scan. No small-discriminant claim is made. The previous fixed-offset construction in paired norm affine lifts has a repeated endpoint at zero and is **not** silently assumed to satisfy these new simple-root guards.

For any public unit \(u\in R^\times\), consider the homogeneous lattice of degree-less-than-d coefficient vectors satisfying
\[
 C(t_1)\equiv uC(t_0)\pmod N. \tag{2}
\]
Its index in \(\mathbb Z^d\) is N, by the jointly onto endpoint evaluations (linear interpolation with unit denominator). For \(n=\operatorname{Res}(H,C)\), multiplicativity gives
\[
 \boxed{n\equiv u\big(C(t_0)\operatorname{Res}(D,C)\big)^2\pmod N.} \tag{3}
\]
This is an actual rational norm squareclass representative of u with known square correction. Test the correction for being a unit: a proper gcd is success, a zero/nonunit with full gcd N is rejected. This is simpler than prescribing both endpoint values as separate digit interpolants, and permits ordinary lattice reduction.

Equation (3) does not assume the input is a square or use its private root. It does not imply a small norm or a low-rank supply.

## 2. Hensel-normalized norm transport

Fix nonnegative depths \(j_0,j_1,j_g\). Set
\[
 e=j_0+j_1+(d-2)j_g,\qquad K_0=1+\max(j_0,j_1,j_g).
\]
Using Newton lifting at the two simple roots, compute \(a_0,a_1\bmod N^{K_0}\) with \(H(a_i)=0\bmod N^{K_0}\) and \(a_i=t_i\bmod N\). Each step from modulus \(N^b\) to \(N^{b+1}\) uses \(a\mapsto a-H(a)H'(a)^{-1}\bmod N^{b+1}\). The derivative is a unit. The lift works over arbitrary odd composite N, including prime powers, and does not require the prime factorization of N. The monic quotient G in
\[
 H\equiv(X-a_0)(X-a_1)G\pmod {N^{K_0}}
\]
has degree d-2 and \(\bar G=\bar D^2\). The three factors are pairwise comaximal over the modular ring: \(a_1-a_0,G(a_i)\) are units. We need not lift a factorization of the repeated polynomial \(D^2\).

Let \(\Lambda_j(u)\) be the full-rank integer coefficient lattice of C with constraints
\[
 \begin{split}
 C(a_i)&\equiv0\bmod N^{j_i}\quad(i=0,1),\\
 C\bmod G&\equiv0\bmod N^{j_g}\quad\text{coefficientwise},\\
 w_1&\equiv u w_0\bmod N,\qquad w_i=C(a_i)/N^{j_i}\bmod N .
 \end{split} \tag{4}
\]
Put \(Q=(C\bmod G)/N^{j_g}\bmod N\). Divisions are exact integer divisions before reduction, not inversion of N. The normalized quantities are well defined using precision \(K_0\), independent of the integer lifts.

**Theorem.** For every \(C\in\Lambda_j(u)\), the signed integer norm \(n=\operatorname{Res}(H,C)\) is divisible by \(N^e\), and
\[
 \boxed{n_*=\frac{n}{N^e}\equiv
          u\big(w_0\operatorname{Res}(D,Q)\big)^2\pmod N.} \tag{5}
\]
Moreover
\[
 \boxed{[\mathbb Z^d:\Lambda_j(u)]=N^{e+1}.} \tag{6}
\]

Proof of (5). For the proof only, lift the endpoints and their monic quotient to precision \(N^{e+1}\). The normalized quantities modulo N are unchanged because \(e+1\ge K_0\). By specialization of the universal resultant identity,
\[
 n\equiv C(a_0)C(a_1)\operatorname{Res}(G,C)\pmod {N^{e+1}}.
\]
Use monic remainder invariance in the last resultant; its remainder is divisible coefficientwise by \(N^{j_g}\). Scaling a polynomial in the second argument of a resultant with monic first argument G multiplies its resultant by the scalar to power \(\deg G\). Thus the cofactor contribution is \(N^{(d-2)j_g}\operatorname{Res}(G,Q')\), where \(Q'\bmod N=Q\) is the lifted divided remainder. The endpoints contribute \(N^{j_0+j_1}\) times their normalized values. Divide the integer congruence by \(N^e\), and use \(G=D^2\bmod N\) and (4). This proves (5), including exact divisibility for repeated prime powers of N.

Proof of (6). Polynomial CRT modulo \(N^{K_0}\) identifies the free degree-less-than-d coefficient module with the two scalar coordinates and the degree-less-than-(d-2) cofactor remainder. The three divisibility conditions have total index \(N^e\); dividing by these powers and reducing modulo N gives an onto normalized-coordinate map. The remaining equation \(w_1-u w_0=0\) cuts its index by exactly N. Equivalently, build a basis by CRT from one normalized endpoint pair \((1,u)\), one extra second endpoint divisible by \(N^{j_1+1}\), and the \(d-2\) cofactor coordinate vectors scaled by \(N^{j_g}\), then adjoin \(N^{K_0}\mathbb Z^d\) and take integer HNF. All matrices have explicit polynomial bit size in \(d,\log N,(1+\max j_i)\log N\). The theorem requires polynomial cost in the actual depth/precision data; it does not promise a cost polynomial in \(\log j_g\) alone.

### Uniform usable correction, separately from shortness

After preprocessing primes up to \((r+1)(d-1)n+2\), where \(n=\operatorname{bitlength}N\), a good vector with a unit correction in (5) can always be found in polynomial time in the explicit lattice data. Given any integer basis \(b_0,\ldots,b_{d-1}\), consider \(C_z=\sum_{i=0}^{d-1}z^i b_i\). For each prime \(p\mid N\), the map \(C\mapsto(w_0,Q)\) from the lattice onto \(\mathbb F_p\oplus\mathbb F_p[X]_{<d-2}\) is onto by the CRT proof of (6). Consequently \(w_0(C_z)\) and \(Q(C_z)(\alpha)\), for every distinct root \(\alpha\) of D over an algebraic closure of \(\mathbb F_p\), are nonzero polynomials in z of degree at most d-1. Across p and these at most r+1 tests per p, fewer than \((r+1)(d-1)n+1\) z values are forbidden in an interval shorter than every p. Scan such an interval, using only gcds and the public resultant. A proper factor exit can occur sooner. Alternatively coefficients independently uniform in an interval of length \(M\ge2(r+1)n\) shorter than every p pass the guards with probability at least 1/2, by the nonzero linear-form bound \(1/M\) and the union bound. This avoids large moment-curve coefficients in a randomized implementation.

This proves uniform polynomial-time **existence and construction of a normalized representation** for every u and every explicitly bounded depth. The bound is in the actual basis size; neither argument shows that a guarded vector lies among the shortest few vectors.

## 3. Exact norm objective and height cost

A fully exact candidate-generation metric, usable even when H is not a field polynomial, is the Frobenius norm of the multiplication matrix \(M_C\) in any fixed rational basis of \(\mathcal A\otimes\mathbb Q\). The linear map \(C\mapsto M_C\) is injective (apply multiplication to 1). Its Gram matrix is positive definite rational and can be cleared to an integer Gram matrix. Hadamard, or AM-GM on the singular values, gives
\[
 |n_*|\le N^{-e}\big(\|M_C\|_F/\sqrt d\big)^d .
\]
This motivates ordinary exact LLL on flattened multiplication matrices, not just power-basis coefficients. The tested implementation uses basis \(X^i/s^i\) for an explicit small integer s and clears the common denominator. Every determinant and correction is then checked exactly; the LLL metric is only a way of selecting candidates.

For separable H the scaled real/complex Minkowski embedding instead has lattice covolume \(N^{e+1}\sqrt{|\operatorname{disc} H|}\). It uses the Euclidean norm counting conjugate complex embeddings twice. The standard LLL first-vector bound, followed by AM-GM, gives for that first vector the formal bound
\[
 |n_*|\le 2^{d(d-1)/4}d^{-d/2}N\sqrt{|\operatorname{disc}H|}. \tag{7}
\]
There is no depth term left: removing \(N^e\) from the norm also increased the lattice index by \(N^e\). If the first vector has zero norm or nonunit correction, (7) is not a bound for a usable representation. In a totally real separable algebra the embedding Gram matrix is the exact trace Gram; in general a certified complex metric is possible but was not implemented here.

Normalization is not a free reduction of the general Minkowski envelope. It is an exact method for varying the shape of the norm lattice and searching for better actual elements. The global discriminant/height obstruction for a repeated modular cofactor remains valid. One must not substitute the normalized integer norm into a fixed-field bounded-actual-norm counting theorem requiring the undivided field norm.

## 4. Principal and localized equivalence of depth lattices

Suppose now
\[
 H=P D^2+N T,\quad P=(X-t_0)(X-t_1),\quad
 \deg T<d,\quad
 \gcd(T(t_0)T(t_1)\operatorname{Res}(D,T),N)=1 . \tag{8}
\]
The last product is nonzero and a unit. Put \(\Delta=t_1-t_0\), \(D_i=D(t_i)\), \(T_i=T(t_i)\), and let
\[
 W=(X-t_0)^{j_0}(X-t_1)^{j_1}D^{2j_g}\quad\text{in }\mathcal A,
\]
\[
 S=T_0^{j_0}T_1^{j_1}\operatorname{Res}(D,T)^{2j_g},\qquad
 \rho=\Delta^{j_1-j_0}D_0^{j_g-j_0}D_1^{j_1-j_g}\pmod N.
\]
Negative exponents in \(\rho\) are permitted unit inverses. Define
\(u'=u\rho^2 T_0^{j_0} T_1^{-j_1}\pmod N\).

**Localized depth theorem.** Multiplication by W is an injection of \(\Lambda_0(u')\) into \(\Lambda_j(u)\) with index exactly \(|S|\). In particular
\[
 \boxed{T=1\ \Longrightarrow\
 \Lambda_j(u)=W\Lambda_0(u\rho^2),\quad
 \operatorname{Res}(H,WC')/N^e=\operatorname{Res}(H,C').} \tag{9}
\]
For arbitrary T satisfying (8), every \(C\in\Lambda_j(u)\) has
\(\widetilde C=|S|W^{-1}C\in\Lambda_0(u')\) (the inverse is in the rational algebra), with exact norm identity
\[
 \boxed{\operatorname{Res}(H,\widetilde C)=S^{d-1}n_*.} \tag{10}
\]
A unit correction is preserved by these maps when applicable. When \(j_0=j_1=0\), S is a rational square and the target change is a known square mask. Hence (10) preserves the entire rational squareclass. In general its squareclass discrepancy is supported on just the two fixed rational values \(T_0,T_1\), not on a new set of depth-dependent prime factors.

Proof. At the two lifted endpoints the first-order Hensel formula is
\[
 (a_i-t_i)/N\equiv
       -T_i/((t_i-t_{1-i})D_i^2)\pmod N.
\]
It implies that the normalized endpoint values of W are units with ratio
\[
 w_0(W)/w_1(W)=\rho^2T_0^{j_0}T_1^{-j_1}\pmod N .
\]
The signs cancel: \(t_0-t_1=-\Delta\), and the sign from the two first-order formulas is canceled by the parity of the powers of \(-\Delta\).

In the lifted cofactor algebra, P is a unit and \(P D^2=-NT\), since H vanishes there. Thus \(D^2/N=-T/P\) in the sense of normalized cofactor residues, a unit modulo N by (8). This verifies cofactor divisibility of W and that its normalized cofactor is a unit. Multiplying any vector of \(\Lambda_0(u')\) by W therefore gives a vector in \(\Lambda_j(u)\), preserving the unit guards. The normalized endpoint ratio is u by the definition of \(u'\).

Next use the monic resultant identities
\[
 \operatorname{Norm}_{\mathcal A}(X-t_i)=H(t_i)=NT_i,\qquad
 \operatorname{Norm}_{\mathcal A}(D)=N^r\operatorname{Res}(D,T).
\]
The signs are as displayed because d is even. The second identity evaluates H at the roots of D, or uses monic remainder invariance. Consequently \(\det M_W=N^e S\ne0\). Multiplication is injective and multiplies the index of the base lattice by \(|N^e S|\). By (6), the image index in \(\Lambda_j\) is \(|S|\). For T=1 this proves equality, and dividing the multiplicative norm identity by \(N^e\) gives (9). For general T the finite quotient of order \(|S|\) is killed by \(|S|\), so \(\widetilde C\) is an integral vector in the base lattice. Since d is even,
\[
 \operatorname{Norm}(\widetilde C)=
 |S|^d\operatorname{Norm}(C)/(N^e S)=S^{d-1}n_*.
\]
Because S is coprime to N, norm-unit status is preserved. End proof.

This is stronger than uniform-depth scaling. In the T=1 family, **the full normalized norm sets**, before any height or search cutoff, are identical under an explicit square mask for every triple of depths. Hence on uniform square (or unit) queries, depth changes cannot improve unrestricted arithmetic supply. They can still change LLL search geometry and the accessible bounded-height subset. For general T the possible additional effect is represented by fractional lattice denominators supported on the fixed values in S; clearing denominators may increase actual mark height. We do not infer equality of bounded-height samples, or principal ideal equivalence over the unlocalized order. For \(T=X+1\), \(D=X^2+1\), and cofactor depths only, \(S=2^{2j_g}\). One must not call those shifts independent new class-group directions.

## 5. Pool every useful representation of the same sealed target

Selecting just one minimum norm per target may miss all useful correlations. Let \(s_i=h_i^2\) be independently sealed unit squares, and let \(n_{ij}\equiv s_i c_{ij}^2\pmod N\) be any public collection of guarded normalized norms for each target, generated using only s_i and public data. All corrections are known units.

Construct an exact common rational squareclass matrix V of the signed integers \(n_{ij}\), including the sign coordinate. Gcd-free factor refinement followed by testing each positive coprime basis element for being an integer square suffices; no factoring of the norms is necessary. A nonsquare basis element has some odd prime valuation, and disjoint supports make these axes linearly independent in rational squareclasses. Let T be the binary target-label matrix, with one column \(e_i\) for each occurrence j of target i. Then
\[
 \boxed{\dim T(\ker V)
       =\operatorname{rank}_{\mathbb F_2}\binom V T
                           -\operatorname{rank}_{\mathbb F_2} V.} \tag{11}
\]
This is rank-nullity applied to the two kernels. It counts only genuinely useful sealed directions, not relations with all target exponents even.

If \(x\in\ker V\) with \(Tx\ne0\), form the known root of \(\prod n_{ij}^{x_{ij}}\) by exact squareclass cancellation, including even powers of the positive gcd-free bases. Divide by the corresponding product of the c's. This gives a known root of \(\prod s_i^{\sum_j x_{ij}}\). Verify the congruence before exposing private roots. The latter product of roots has an odd exponent of at least one independently sealed root; hence the checked proper gcd succeeds with conditional probability at least one half. This uses the [known-square anchor theorem](uniform_masked_anchor_supply.md), not an unproved square-root step.

Equivalently, subtract one representative for each target from all its other representations, creating known-square identity anchors. Their span E consists of within-target differences. The quotient rank of target representatives modulo E is \(\operatorname{rank}V-\dim E\), and useful target dimension is \(k-\operatorname{rank}V+\dim E\). This follows because the kernel of T is exactly generated by within-target differences. Retaining all candidates can strictly increase useful parity even when the smallest norms have full rank. It is also a way to evade the distinct-input hypothesis of [the multiway parity barrier](multiway_norm_parity_barrier.md). It does not guarantee common small rank or useful directions at quarter scale.

## 6. Exact experiments and limitations

Run [verify_normalized_norm_lattice.py](../verification/research/verify_normalized_norm_lattice.py), Python 3.13.5, SymPy 1.14.0. Tested and committed blob 3a642a6a2efeafca6b1b2757271b9bb8422d9797, SHA-256 d03314a39abe14f70de01555bf7b8da0bcf21251c4d2f478e34148e637ba398f. Modes single, principal, and pool (optionally with explicit fixture moduli) allow separately bounded runs. We verified Hensel lifts, actual integer resultants, HNF index/equalities, exact modular corrections, LLL lattice preservation and independent augmented-rank comparison. No numerical root/rank tolerance was used.

### Single selected norms

Degree d=6, D=X^2+1, t0=0, t1 just above the fourth root of N (increment if needed to be a unit), sixteen ordinary public units per environment. For each of four depth triples and two metrics, consider 44 candidates (six basis vectors, 30 pairwise sums/differences, eight bounded random combinations). Total 22,528 exact normalized norm checks, with 512 selected guarded minimum norms. Every one of the 32 sixteen-row matrices has rank 16, and none of the 512 selected norms has absolute squareclass supported at primes ≤101.

For zero depth, the integer-truncated mean bit length of the selected norms is:

| N | Coefficient metric | Multiplication-matrix metric |
|---:|---:|---:|
| 899 | 34 | 26 |
| 10403 | 49 | 40 |
| 1022117 | 90 | 62 |
| 100160063 | 124 | 86 |

This is a genuine reduction in candidate norm size on these fixtures, not a proof of useful density. Changing depth sometimes improves the selected norm and sometimes worsens it. Uniform depth (1,1,1) reproduces the zero-depth outputs.

### Localization identities and pooling

The principal depth theorem was checked on 240 lattice equalities and exact normalized norm identities, including the prime-power-containing modulus 315. The general localized theorem was checked on 144 additional integer inclusion/index, denominator-clearing and normalized norm identities.

For pooling, use 12 distinct public square targets per modulus with privately sampled uniform unit roots (reject duplicate squares publicly). Use depths (0,0,0), (0,0,1), (0,0,2), both metrics, and all 44 candidates. Compare H=P D^2+N with H=P D^2+N(X+1); each has the required simple endpoint guards. All representation generation and rank choices are independent of private roots. Deduplicate identical (target, signed norm) pairs after checking square corrections. Exact results:

| N | Perturbation T | Distinct guarded (target,norm) pairs | Norm rank | Useful target dimension (11) | First relation gcd |
|---:|---|---:|---:|---:|---:|
| 899 | 1 | 2517 | 2514 | 1 | 31 |
| 899 | X+1 | 2538 | 2532 | 3 | 1 |
| 10403 | 1 | 2752 | 2752 | 0 | — |
| 10403 | X+1 | 2785 | 2785 | 0 | — |
| 1022117 | 1 | 2881 | 2881 | 0 | — |
| 1022117 | X+1 | 2888 | 2888 | 0 | — |
| 100160063 | 1 | 2935 | 2935 | 0 | — |
| 100160063 | X+1 | 2933 | 2933 | 0 | — |

Total 25,344 candidate checks, 22,279 unit-guarded candidates, 22,229 distinct guarded pairs. Useful target dimensions 1 and 3 occur in the smallest modulus only. One actual private-root draw gave factor 31; the other first witness gave trivial gcd 1. These experiments deliberately ignore earlier proper gcds from failed unit guards (both factors occur among such guards in each tiny test modulus), so reported ranks measure relation supply instead of accidental small-modulus exits. Equal-norm public square-correction comparisons produced no additional proper gcd. This is not a factoring timing experiment. The nonconstant perturbation is not claimed to have a nonprincipal ideal at N; the localized theorem describes its possible effect.

**Research conclusion.** There is now a simpler exact uniform fixed-algebra norm sampler, and normalization gives legitimate access to deep nonunit cofactors. Nevertheless the principal depth family is only a masked copy of the old norm set, and small perturbations add only controlled fixed denominator support. Pooling multiple representations is mathematically sound and sometimes finds useful directions, but the larger finite fixtures give no rank gain. The next viable step must change the actual supply of bounded-height norms, for example by genuinely different ideal classes or by a structured factorization of marks producing several smaller actual norm factors. The multiway obstruction in the companion note explains why merely increasing the number of independent determinant-scale targets cannot remedy this. No quarter-scale bound, improved one-third constant, full factoring implementation or new Lean milestone is claimed.
