# Exact valuation descent and a probe-free unit certificate

27 November 2026. **Status:** new written unconditional algebraic reduction and certificate theorem, using a published polynomial-time ideal-refinement theorem and certified real linear algebra on unit lattices. It removes the factorial-in-degree probe length of the KeyBreak certificate. It does not by itself establish the relation supply, a smaller first L-parameter, or a numerical improvement on [U14.2](keybreak_u142_proof.md). The principal use is to permit polynomially growing field degrees in a potential scale-breaking descent.

## 1. Why the parity certificate is a degree barrier

The KeyBreak U construction, The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 Nov. 2026, [source](https://crypto.sjtu.edu.cn/factoring.pdf), SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9, §5.2–5.4 and Appendix E, collects rows whose large good ideal valuations are even. To distinguish nonrational square classes it samples degree-one prime ideals at rational primes of bit length at least comparable to \((2d)!\). Its odd-degree exceptional-zero argument is unconditional, but the explicit bit-length choice forces work of order at least \(\exp(\Omega(d\log d))\) for that implementation. A terminal field with degree \(d=(\log N)^{\delta+o(1)}\), \(\delta>\alpha\), cannot use those probes in time \(\exp((\log N)^{\alpha+o(1)})\).

A square-class test for a single compact product is not an efficient way of finding an arbitrary dependence among many square classes. Nor does an even valuation imply that a principal ideal is a square of a principal ideal. The following construction avoids both problems by demanding **exact** cancellation of large good valuations, and extracting an ordinary multiplicative relation rather than a square-class relation. Crucially, a relation over the integers must retain at least one odd exponent after removing torsion; multiplying a relation indiscriminately by 2 destroys the hidden-root probability.

## 2. Exact cancellation uses the same formal incidence estimates

Use the source's odd-degree accepted fields \(K_a=\mathbb Q(\theta_a)\) and modular evaluation on the localized polynomial order. Let the bad rational primes in field a divide the integer \(D_a^*\) of source E.1 (raw content, leading coefficient or discriminant); assume each used atom is nonzero and its modular evaluation is a verified unit. The source ordinary internal candidate at a good target \((q,s)\) has
\[
 |F(P)|=q u,\quad u\in S_{Y_{i+1}},\quad q>Y_{i+1},\qquad a\equiv s b\pmod q.
\]
Thus it has valuation exactly one at the requested good prime ideal. Its other good large ideal factors are at lower levels. Pass-through labels are advanced until active; bad and small ideals are terminal.

Make the following change to a completed row. Give a top atom the same sign as before. If an occurrence of atom P has signed integer multiplicity c and contains a good large ideal \(\mathfrak q\) of valuation \(e>0\), require a child relation for \(\mathfrak q\), with signed multiplicity \(-ec\). Require this also when e is even. By induction on the strictly descending prime cutoffs the child cancels the exact valuation \(ec\) at its parent, introducing only smaller requests. Every occurrence has at most as many distinct children as the corresponding **formal** incidence list, so no additional factor of e is introduced into the number of search states. The integer weight on a path is a product of the valuations along it. Each valuation is at most the bit length of the atom norm; for the U schedules that is \(O(n)\), \(n=\operatorname{bitlength}N\). At depth \(O(\log n)\) weights have bit length \(O((\log n)^2)\). The compact row stores weights, not e expanded copies of a child tree.

The rational modular correction of each occurrence is raised to the same signed multiplicity c, using the exact identities in source E.6. For internal occurrences the identity is
\[
 1=\frac{Q}{G(P)}(a-bm_N)\pmod N.
\]
Hence the verified row identity \(R_i=h_i^2=q_i\prod_a\psi_a(\gamma_{ia})\pmod N\) still holds, including all inserted children. The rational factor \(q_i\) is a signed product of the known Q and base primes. The field products \(\gamma_{ia}\) are compact signed atom products. Now
\[
 v_{\mathfrak p}(\gamma_{ia})=0\quad
 \text{at every prime ideal outside }
 S_a=\{\mathfrak p:\mathfrak p\text{ lies over }p\le B\text{ or }p\mid D_a^*\}.
 \tag{1}
\]
This is zero, not just even.

The U40 relation-supply proof was deliberately formulated using formal incidence counts \(X_{\ell q}\) that include even valuations, raw-content primes, terminal incidences and all finite root labels; see source B.6 and [U40 §6](keybreak_u40_proof.md). Redefine a good parent recursively using only candidates all of whose **distinct actual** child labels, including even ones, are good. The same candidate-deletion inequality bounds the loss by the sum of those formal incidences. Its proof does not depend on which subset of the formal incidences is made a required request. Consequently the ordinary and semismooth tail bounds, incoming profile comparisons, linear bad-mass recurrence, top pool and stopped Search proof apply to this stronger good-state definition with exactly the same bounds on the number of requests. A bad/terminal label still has zero bad indicator. This argument also applies to the original square-root exceptional-mass transfer of U100. It does not reuse a good set defined for odd-only cancellation.

The source factor lists already give the multiplicities at good labels (source E.1). At bad primes we do **not** attempt to compute a maximal order or to infer exact prime-ideal valuations from rational norm valuations. Instead use the factor-refinement construction below.

## 3. Exact S-unit relation lattice without factoring bad norms

We state the general input. Suppose R sealed unit squares \(R_i=h_i^2\) have verified public expressions
\[
 R_i=q_i\prod_{a=1}^J\psi_a(\gamma_{ia})\pmod N
\]
where the fields have odd degrees \(d_a\), every rational \(q_i\) is given as a signed power product of a fixed set of b rational primes, and each \(\gamma_{ia}\) is a compact power product of integral atoms and inverses in a localized order that maps to \(\mathbb Z/N\). All inverted elements map to units. Suppose (1) holds, with finite known upper cardinality bounds \(s_a\ge |S_a|\); the prime ideals themselves need not be explicitly represented. Assume
\[
 R\ge b+\sum_{a=1}^J(s_a+d_a-1)+2.
 \tag{2}
\]
All fields, atoms, signed exponents and rational correction exponents are provided explicitly in binary, with the exponentiation represented compactly.

Use Guoqiang Ge, *Recognizing units in number fields*, Math. Comp. 63 (1994), 377–387, [paper](https://cr.yp.to/bib/1994/ge.pdf), Props. 6.2–6.3, p.386 (the exact statements were rechecked; the PDF page-image request failed but its full extracted text was accessible). The theorem is polynomial time in the size of the order multiplication table and the elements, uniformly in the degree. It refines the given principal ideals over a computed overorder into pairwise comaximal proper invertible ideals with integer exponents. The extensions of those ideals to the full ring of integers are proper and pairwise comaximal. In particular their nonempty prime-ideal supports are disjoint, and the exponent map detects exactly whether any compact power product is a unit.

For the nonmonic source fields use \(\beta_a=A_a\theta_a\) as in E.1/E.6, with monic integral defining polynomial \(g_a\). Apply Ge to \(\mathbb Z[\beta_a]\), the list of integral atoms \(A_a(a-b\theta_a)\), and \(A_a\) itself. The signed exponents of the latter encode all denominators caused by the nonmonic coordinate. Both \(A_a\) and all relevant atom images are invertible modulo N. No full-ring modular evaluation of an overorder produced by Ge is needed.

For field a, multiply Ge's integer exponent matrix by the matrix of compact row expressions. The resulting integer linear map \(V_a:\mathbb Z^R\to\mathbb Z^{t_a}\) has kernel exactly the vectors whose corresponding field product is a unit. Moreover **its rank is at most \(s_a\)**, not the total number of refined ideals:
if a refined ideal has a prime-ideal divisor outside \(S_a\), its exponent must be zero in every row by (1), since its support is disjoint from all other refined ideals. Every other nonzero coordinate has a nonempty disjoint support inside \(S_a\), so there are at most \(s_a\) such coordinates. This argument works even when Ge's ideals are not prime and even at primes dividing the defining discriminant. It does not require the algorithm to discover which supports occur. Add the b exact rational valuation rows, obtained by integer sums of the stored rational exponents.

Let \(U\subset\mathbb Q^R\) be the rational kernel of this combined integer matrix. An integral basis of \(U\cap\mathbb Z^R\), or simply a rational basis cleared of denominators at this stage, can be computed by exact integer/rational linear algebra in polynomial bit time. Its dimension is at least \(R-b-\sum s_a\). For any integral element of this lattice each field product is now a true algebraic unit and the rational correction is a sign.

## 4. Certified logarithmic kernel in arbitrary odd-degree fields

We need an exact rational description of the remaining kernel without enumerating units, computing a regulator, invoking GRH or introducing an exponential \(2^{d_a}\) extension. This generalizes the project's [effective reconstruction](effective_number_field_recovery.md) for totally real fields and [factor refinement](full_degree_factor_refinement.md).

For a number field K of degree d, take the log vector of a unit using all d embeddings, duplicating conjugate complex embeddings. Its coordinates sum to zero. Dirichlet's unit theorem gives a lattice of rank \(r_1+r_2-1\le d-1\) whose kernel consists of roots of unity. We use only the lattice property and the following elementary effective separation.

**Logarithmic gap.** Any nonzero log-unit vector has norm at least \(5^{-d^2}/10\). Indeed, if some log coordinate has absolute value at least \(\log 2\), this is immediate. Otherwise all conjugates of the unit have absolute value between \(1/2\) and 2. A non-torsion unit has an embedding with \(|\sigma(u)|\ne1\), by Kronecker's theorem (or the bounded coefficients of powers argument). Then \(z=\sigma(u)\overline{\sigma(u)}-1\) is a nonzero algebraic integer of degree at most \(d^2\), since the compositum of the two degree-at-most-d fields has degree at most \(d^2\). Every conjugate of z has absolute value at most 5. Its nonzero integer norm gives \(|z|\ge5^{-(d^2-1)}\). On the interval \([1/2,2]\), \(|t^2-1|\le 8|\log t|\), by the mean value theorem in log coordinates. This proves the claimed gap. No quantitative Lehmer conjecture is used.

For the direct product of fields the minimum nonzero vector length is at least \(\epsilon=5^{-d_{\max}^2}/10\). Put \(D_{\mathrm{tot}}=\sum d_a\). If a rank-r sublattice of the product is generated by linearly independent log vectors, its determinant is at least \((\epsilon/\sqrt r)^r\), by Minkowski applied in its span to the open cube of side \(2\epsilon/\sqrt r\). This holds for *every* sublattice rank, not just a full-rank unit system.

Take a cleared integer basis \(u_j\) of U. Compute the concatenated log vector \(w_j\) of the compact field products for each \(u_j\), as a sum of the logarithms of the individual atom embeddings multiplied by the binary exponents. This requires only polynomially many bits of precision: algebraic root isolation/approximation in variable degree is polynomial in the integer polynomial data and the requested precision; the absolute values of nonzero embedded integral atoms are bounded below by the inverse product of the upper bounds for the other embeddings, using their nonzero integer norm. For rational denominators use the same bounds separately. The elementary interval logarithm algorithm and polynomial-precision matrix estimates in effective_number_field_recovery.md apply to absolute values of the complex embeddings as well (use the real square of the absolute value). In particular we need not expand a product with exponent of exponentially large numerical magnitude. Its logarithmic vector size has logarithm bounded by a polynomial in the binary input length, including the exponent bit lengths. An explicit uniform upper bound \(H\ge 1\) for all \(\|w_j\|\) with polynomial bit length follows by summing these absolute logarithm bounds times the absolute exponents.

Here are the exact rank and recovery steps. Select independent columns greedily by Gram determinants. For k independent columns the Gram determinant is at least \((\epsilon/\sqrt k)^{2k}\), and for dependent columns it is zero. Using dyadic approximations with Euclidean error \(2^{-P}\), the entrywise Gram error is at most \(3H2^{-P}\) and all entries at most \(4H^2\). The Leibniz determinant bound \(k!k(4H^2)^{k-1}3H2^{-P}\) is smaller than one quarter of the gap for a polynomially large P, uniformly for \(k\le D_{\mathrm{tot}}\). This determines the exact rank, including rank zero, using rational comparisons. If \(w_1,\ldots,w_r\) are the selected independent columns, the subgroup they generate has determinant at most \(H^r\) and index at most
\[
 D_*=\left\lceil H^r(\sqrt r/\epsilon)^r\right\rceil
\]
in the intersection of their real span with the product unit lattice. The intersection is a rank-r lattice because it contains the selected subgroup and is discrete. Thus the rational coordinates of any other \(w_j\) in these columns have denominators dividing that index, bounded by \(D_*\). Cramer's rule applied to the Gram system, with the determinant lower bound and entrywise upper bounds, gives polynomial bounds on the bit lengths of the numerators. Increasing P by a polynomial amount makes the exact rational solution of the approximated Gram system differ by less than \(1/(4D_*^2)\) in every coordinate. To see the required precision, use the same determinant perturbation bound, the adjugate formula and subtract the two systems; logarithms of all inverse determinant and cofactor bounds are polynomial in \(D_{\mathrm{tot}},\log H,\log(1/\epsilon)\). Continued fractions recover each coordinate uniquely. Thus the exact rational nullspace of the concatenated log columns, and therefore the subspace \(W\subset U\) with all log vectors zero, is computable in polynomial bit time.

Its codimension in U is at most \(\sum(d_a-1)\), so (2) gives \(\dim W\ge2\). For every integer vector in W each field product is a root of unity, necessarily \(1\) or \(-1\) because the degree is odd. The rational product is likewise a sign.

## 5. Preserve an odd coefficient and eliminate the sign

Choose one real embedding of each odd-degree field. The sign of each input atom at that embedding is computable by certified algebraic sign isolation (the atom is nonzero). The sign of a compact product is just the product of signs to the exponents mod 2. Let \(b_i'\in\mathbb F_2\) be the combined sign bit of the i-th rational correction and all its field components. This is a linear form \(b'\) on integer row exponents reduced modulo 2. On W it is the exact sign of the torsion product. We do not need to compute signs of enormous expanded products.

The lattice \(L_W=W\cap\mathbb Z^R\) is saturated: if a nonzero integer multiple of an integer vector lies in W, the vector lies in the rational subspace W. Hence \(L_W/2L_W\to\mathbb F_2^R\) is injective (if \(v=2w\) in \(\mathbb Z^R\), then \(w\in L_W\)). Its image has dimension \(\dim W\ge2\). Compute a saturated basis by clearing the rational linear equations defining W and finding an integer kernel basis with the usual polynomial-bit-time Hermite/Smith normal form algorithms (Kannan–Bachem). The sign functional has kernel of codimension at most one on this image. Binary linear algebra therefore selects an integer vector \(c\in L_W\) with at least one odd coordinate and \(b'\cdot c=0\bmod2\). This avoids the false inference that an arbitrarily denominator-cleared rational basis must already have full mod-2 rank.

Since the exact rational/field products equal signs and their total sign is +1, evaluation gives
\[
 \prod_{i=1}^R R_i^{c_i}=1\bmod N .
 \tag{3}
\]
All field equalities can be read in the localized polynomial orders, where they hold because the corresponding elements are equal as field elements. No map from the full ring of integers modulo N is asserted. Verify (3) directly by public modular powering and verify the odd-coordinate condition **before** exposing any private root. Negative exponents use inverses of verified units. This verification also ensures safe failure if an implementation of any preceding certificate step is wrong.

Finally use the source's sealed-root fibre law (E.5): conditional on the entire verified public transcript, \(h_i\) are independent uniform choices in their unit square fibres. Since some \(c_i\) is odd, the product \(X=\prod h_i^{c_i}\) is uniform among the \(2^{\omega(N)}\) roots of 1 in the unit group. In particular \(X^2=1\) by (3), and for odd composite N having at least two distinct prime divisors, \(\gcd(X-1,N)\) is a proper factor with conditional probability \(1-2^{1-\omega(N)}\ge1/2\). The argument includes repeated prime powers. As in the original algorithm, a failed extraction discards these private roots; it does not condition them on successful prior exposure.

**Theorem.** Under the explicit input conditions (1)–(2) and the verified public row identities, a deterministic algorithm polynomial in the total binary length of the public field/atom/compact-exponent data produces a verified public relation (3) with an odd coefficient. Independent sealed private roots then give the stated proper-factor probability. It uses no sampled quadratic-character primes, maximal-order or class-group oracle, regulator computation or square-root reconstruction. The theorem includes variable odd degrees and arbitrary signatures.

## 6. Consequences and limits

For exact U40/U14.2-style descent, one may take
\[
 b\le\pi(B)+J,\qquad
 s_a\le d_a\bigl(\pi(B)+b(|D_a^*|)\bigr).
\]
Here the second b denotes the bit-length function, not the count of rational prime labels. In particular a public row bound satisfying (2) is of the same first-parameter size as the original source's bound. The fields' data have polynomial bit length in \(n,d_a\) and the coefficient heights. All occurrence counts and binary weight lengths are charged. If the total row-data size is \(L_N[\alpha,O(1)]\), the theorem's polynomial cost is also \(L_N[\alpha,O(1)]\), **even if \(d_{\max}\) is a larger power of \(\log N\) than \(\alpha\)**. In the source certificate that would fail because of the factorial probe bit length. This is a genuine removal of one degree restriction, not a heuristic smaller-probe claim.

The precise polynomial degree of Ge's full ideal-refinement implementation and of the exact matrix implementation has not been optimized. Therefore we do not claim a better numerical constant than U14.2 from this replacement, though it can replace the source certificate if only the first L-parameter is being targeted. We do not use polynomial bit cost in an exponent's **numeric value**: all field atom inputs to Ge are explicit integral elements of polynomial height, and all later products use compact exponent vectors. The shape and relation-supply barrier remains. In particular creating a distinct field for every new row would grow the rank bound (2) along with the number of rows and does not by itself yield a dependence.

The next concrete goal is to use this certificate with high-degree terminal fields and target-dependent small atom lattices, or exact norm-controlled shared marks, without paying the original low-degree private-shape and terminal rational-smoothness costs simultaneously. This is now a relation-generation problem; the large-degree character-separation cost is no longer an obligatory part of its certificate.
