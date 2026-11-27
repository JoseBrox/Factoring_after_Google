# Square-aware resultant transport and a binary anchor presentation

27 November 2026. **Status:** exact unconditional norm/image identities, a constructive interpolation theorem and coefficient-height obstructions for a new square-aware descent interface. This complements [uniform masked anchor supply](uniform_masked_anchor_supply.md) and [shared-base norm transport](shared_base_norm_transport.md). The new interface can remove *all* relative unit-log costs for bridged expressions, not merely reduce their dimension. It does not prove a sub-one-third factoring algorithm or the required raw relation-supply density.

The distinction from exact multiplicative relation extraction is important: for factoring we need a **known modular square correction**, not necessarily a square root in a number field or exact cancellation of every unit logarithm. A claim that something is a square in the residue ring without an explicit known root is not sufficient.

## 1. Norm identities with modular polynomial cofactors

Let \(f\in\mathbb Z[X]\) be monic irreducible of degree d, \(K=\mathbb Q(\theta)\), \(f(\theta)=0\), and t a known root of f modulo N. Let \(\psi\) be evaluation on the localized power order. For an explicit polynomial mark \(P\), write \(u=P(\theta)\); the norm is the integer
\[
 n=\operatorname{Norm}_{K/\mathbb Q}(u)=\operatorname{Res}(f,P).
\]
Assume both its value at t and its norm are units modulo N, tested explicitly. A proper gcd is success; a nonunit with gcd N is rejected for this interface. The norm condition is stronger than the unit condition at a single modular root. For a fraction of two explicit marks apply all formulas multiplicatively to numerator and denominator with the same unit guards. Compact power products are not expanded.

Over \(R=\mathbb Z/N\), suppose an explicit monic factorization (not necessarily into irreducibles, not necessarily coprime) is given:
\[
 \bar f=(X-t)^e\prod_{\lambda}g_\lambda^{m_\lambda},
 \qquad e\ge1\text{ odd}.
\]
It always exists with e=1 and a single monic quotient by synthetic division. Put \(v=P(t)\bmod N\) and \(b_{\lambda,P}=\operatorname{Res}_R(g_\lambda,\bar P)\). The universal monic resultant product identity gives
\[
 n=v^e\prod_\lambda b_{\lambda,P}^{m_\lambda}\pmod N.
 \tag{1}
\]
It holds over arbitrary commutative rings, including composite moduli and repeated factors; one proof uses the universal polynomial identity for resultant multiplicativity over the integer polynomial ring and specializes. Equivalently a monic polynomial defines a free finite algebra, and its resultant with P is the determinant of multiplication by P. All factors on the right of (1) are units under the norm guard.

It follows that
\[
 \boxed{
 \psi(u)=n\prod_{\lambda:\,m_\lambda\ {\rm odd}}
                b_{\lambda,P}^{-1}\,c^2\pmod N,\qquad
 c=v^{-(e-1)/2}\prod_\lambda b_{\lambda,P}^{-\lfloor m_\lambda/2\rfloor}.
 }\tag{2}
\]
Every factor c is explicitly computed without taking any modular square root. In particular if
\[
 \bar f=(X-t)g^2 \tag{3}
\]
then \(\psi(u)=n\,\operatorname{Res}_R(g,\bar P)^{-2}\). In this special family **every** term of a public compact row can be transferred to its rational norm, with a known square correction. This is stronger for sealed-square extraction than reducing to a norm-one relative unit and paying the entire relative unit-log rank. It applies also to non-totally-real fields, and does not require the degree to be odd except as implied by (3). No root of a cofactor polynomial, Galois conjugate, unit basis or factorization of N is required.

More generally, (2) permits shared cofactor labels: a known modular polynomial factor \(g_\lambda\), together with a mark P, specifies the same public unit \(b_{\lambda,P}\) every time it occurs. Exact equality of these resultant residues suffices for identifying two labels; it is not necessary for their integer polynomial lifts to agree. A product of terms whose residual resultant exponents are even has a known square correction from the products of these public residues. This includes correlations across distinct fields and modular maps. It is not necessary that each field individually satisfy (3).

## 2. A square certificate on actual public generators

Collect the rational signed norms, other rational correction factors, and all distinct residual resultant unit values of (2) for the actual rows. Construct a common gcd-free basis of the rational integer numerators and denominators (plus the sign generator -1); perfect-power extraction or even a finer verified basis is allowed. The generators for the cofactor labels are the actual public residues, not abstract prime ideals. Their numerical values are verified units. This gives a finite generator list \(b_j\) with verified decompositions
\[
 s_i=c_i^2\prod_j b_j^{V_{ji}},\qquad
 z_\ell^2=d_\ell^2\prod_j b_j^{C_{j\ell}},
 \tag{4}
\]
where the first rows have sealed roots \(h_i^2=s_i\), the anchors have publicly known roots \(z_\ell\), and the exponents may be reduced to 0 or 1 by absorbing every even part into the explicit roots \(c_i,d_\ell\). The sign -1 is treated just like another unit generator; do not assume it has a known square root. Negative exponents use verified modular inverses. Gcd-free refinement and exponent operations may be performed on the compact data without integer prime factorization. It suffices to have a verified representation by generators; for exact rational squareclass testing one can replace each gcd-free integer basis by its maximal perfect-power root and discard the resulting even powers.

If \(Vx+Cy=0\) over \(\mathbb F_2\), with nonzero sealed binary vector x, take the indicated products of the actual equations (4). Every generator exponent sum in this product is even as an integer, so its root is computed by ordinary modular powering. Including the explicit c's and d's gives a known square root w of \(\prod_i s_i^{x_i}\prod_\ell z_\ell^{2y_\ell}\). The [known-square anchor theorem](uniform_masked_anchor_supply.md), §1, gives a proper-factor probability at least one half before private exposure, conditional on the public success transcript. All modular congruences are checked again. This is a true square certificate, not an assumption that even prime-ideal valuations imply a known field square root.

The exact binary progress criterion is consequently simpler than the old integer-label criterion. Let \(U=\operatorname{im}_{\mathbb F_2} V\), \(E=\operatorname{im}_{\mathbb F_2} C\), and split an incoming anchor batch into old and new label coordinates \(B_o,B_n\). Put \(H_2=B_o(\ker_{\mathbb F_2}B_n)\). Its strict useful gain on the old sealed targets occurs exactly when
\[
 \boxed{H_2\cap(U+E)\not\subseteq E.}\tag{5}
\]
This follows by taking the intersection of the old numerator \(U+E\) with the enlarged denominator \(E+H_2\). New generator labels need cancel only modulo two, since their even powers have explicit square corrections. There is no even Smith obstruction in this actual generator presentation. Using (5) with mere ideal valuations instead would be unsound. A binary kernel of dimension one containing a nonzero sealed coefficient suffices for the split; there is no further sign constraint when the sign generator was included.

For example, consider fields all of whose remaining cofactor factors occur in paired copies for each old mark. After (2) the cofactor block is zero on the paired combinations, and the rank of the resulting binary columns is the rank of their rational norm squareclasses alone. The actual savings are measured on the supplied row span, not by comparing unused ambient labels. This identifies an additional arithmetic correlation to seek: equal or paired resultant labels, rather than equal entire ideals or integer-canceled independent modular-image ports. The mask-bank theorem applies directly to these binary generators with novelty budget equal to core dimension.

**Important scope.** This is an alternative to, not a proof of, the exact S-unit certificate. On row terms for which the cofactor block does not cancel one must keep its rank. Treating every distinct cofactor value as an independent public generator can yield no compression at all. No uniform distribution of those residues, nor density of repeated labels, is assumed.

## 3. Exact norm interpolation in the square-cofactor family

The shape (3) can be forced by an explicit construction; no field selection heuristic is needed. It is useful for producing controlled test blocks and for isolating the exact compatibility condition on a proposed new anchor.

**Theorem.** Supply odd composite N, any integer t, and k≥1 pairs of integers \((a_i,n_i)\) which are units modulo N, with all \(a_i-a_j\) units modulo N for \(i\ne j\). Supply known units \(w_i\) with
\[
 n_i\equiv a_i w_i^2\pmod N.
 \tag{6}
\]
In polynomial bit time in the actual supplied data (and a small auxiliary prime as below), one can construct a monic irreducible polynomial f of odd degree \(d=2k+1\), known modular root t, and integer marks \(r_i\) such that
\[
 \begin{split}
 \psi(\theta-r_i)&=a_i,\\
 \operatorname{Norm}_{K/\mathbb Q}(\theta-r_i)&=n_i b_i^2
       \quad\text{with known nonzero integers } b_i,\quad (b_i,N)=1,\\
 \bar f&=(X-t)g^2,\quad g\text{ monic of degree k over }R.
 \end{split}\tag{7}
\]
No new rational **squareclass** support beyond the supplied \(n_i\) is introduced by this construction. Its coefficient heights can be large; it is not a small-discriminant theorem.

Proof. Choose an odd prime \(\ell>2k+1\) not dividing \(N\prod_i n_i\). It can be found by a polynomial bounded sieve in the total bit length of the inputs: the number of forbidden prime divisors is at most that bit length, and the ordinary prime number theorem (or explicit elementary prime-count lower bounds) gives sufficiently many primes below a sufficiently large fixed power of that length plus k. A proper gcd with N may be returned instead. No factoring of the supplied n_i is required.

Choose r_i modulo N by \(r_i=t-a_i\). Choose r_i modulo \(\ell\) to be distinct nonzero residues with quadratic sign \((r_i/\ell)=(-n_i/\ell)\). There are \((\ell-1)/2\ge k\) residues of each sign, so greedily selecting them is possible by enumeration in polynomial time in \(\ell\). Lift r_i by CRT into \([0,N\ell)\). The r_i are distinct both modulo N (with unit differences) and modulo \(\ell\). Let \(C=\prod_{i<j}|r_i-r_j|\), taking C=1 when k=1; it is coprime to \(N\ell\). The number C may be large, but will occur only squared in the exact norms.

Since d is odd, \(r_i^d/(-n_i C^2)\) is a square in \(\mathbb F_\ell^\times\). Find a nonzero square root by finite enumeration, and choose a positive integer \(c_i\) congruent to that root modulo \(\ell\) and to 1 modulo N. Set \(b_i=Cc_i\). Prescribe the exact integer values
\[
 F_i=-n_i b_i^2 .
\]
They satisfy \(F_i\equiv r_i^d\bmod\ell\). Lagrange interpolation gives an integer polynomial \(I(X)\) of degree less than k with \(I(r_i)=F_i\): the denominator \(\prod_{j\ne i}(r_i-r_j)\) divides C, hence divides \(b_i^2\). The size of C and of these coefficient numerators is polynomial in the actual input bit length (for instance \(\log C=O(k^2\log(N\ell))\)); exact rational operations followed by integrality checks suffice.

Let \(P_0(X)=\prod_i(X-r_i)\). Over R interpolate the residues \(b_i w_i\) at the r_i by a degree-less-than-k polynomial \(G_0\), using the unit differences. Put \(g=\bar P_0+G_0\), monic of degree k. Then \((X-t)g^2\) is monic of degree d and has values \(F_i\bmod N\) by (6). Thus it is congruent to I plus a multiple of \(P_0\) modulo N. This last assertion follows by monic division: the remainder difference of degree less than k vanishes at all k marks, and the Vandermonde determinant is a unit. The same argument modulo \(\ell\) shows \(X^d-I\) is divisible by \(P_0\) there.

Choose a monic integer polynomial Q of degree \(d-k=k+1\) with the two prescribed monic quotient reductions modulo N and modulo \(\ell\), and set \(f=I+P_0 Q\). We may choose the lifts modulo \(\ell^2\) so that \(f(0)\equiv\ell\bmod\ell^2\): first lift any coefficients satisfying the \(\ell\)-congruences, then adjust the constant coefficient of Q by a multiple of \(\ell\), since \(P_0(0)\) is a unit modulo \(\ell\). Finally use CRT modulo \(N\ell^2\) for the nonleading coefficients of Q. The resulting f is monic, congruent to \(X^d\bmod\ell\), and Eisenstein at \(\ell\), hence irreducible over Q. Its degree is odd, so \(\operatorname{Norm}(\theta-r_i)=-f(r_i)=n_i b_i^2\). Its modular root and full square-cofactor identity follow by construction. All norms are unit-evaluable; all b_i can be stored unfactored as explicit square corrections. This proves the theorem.

If the pairwise difference guard fails with a proper gcd, return the divisor. Exact repeated modular images can be treated separately; the theorem does not claim arbitrary inconsistent multiple norm prescriptions at identical marks.

**Why (6) is not an innocent technical condition.** It is essential for obtaining this particular square-cofactor interpolation with a *prescribed* norm squareclass. Indeed any such construction itself supplies a square root of the ratio \(n_i/a_i\) by (2), after removing the known b_i. Thus dropping (6) for arbitrary supplied norms and arbitrary sealed square images would already solve a modular square-root problem. The theorem does not manufacture an unknown square-root relation by adjusting defining-polynomial coefficients. This is the precise boundary of the constructive direction. For correlated packets where ratios or their products already have known square corrections, it is useful as a clean representation of the joint norm data with no extra unit-log budget. Merely choosing the same square-cofactor construction for each sealed image does not prove new anchors.

## 4. Discriminant obstruction to the naive small-height version

The square-cofactor structure cannot be added to a small-height monic field for free. Here is an exact bound, including prime-power moduli.

**Proposition.** Let \(f\in\mathbb Z[X]\) be monic of degree d with nonzero discriminant and suppose \(\bar f=h\,g^2\) over \(\mathbb Z/N\), with g,h monic and \(\deg g=m\). Then
\[
 N^m\mid\operatorname{disc} f.
 \tag{8}
\]
Proof. In the free rank-d algebra \(\mathbb Z[X]/(f)\), multiplication by \(f'\) has determinant equal to the discriminant up to sign. Choose monic integer lifts of h,g and put \(J=hg\) (degree \(d-m\)). The polynomials
\[
 1,X,\ldots,X^{d-m-1},\quad J,XJ,\ldots,X^{m-1}J
\]
form an integral unimodular basis by their monic successive leading terms. Modulo N, \(\bar f'=g(h'g+2hg')\), so multiplication by \(f'\) annihilates each of the last m basis vectors, since \(gJ=\bar f\). The corresponding m columns of the integer multiplication matrix in this basis are divisible by N. Taking the determinant proves (8), without any assumption about the residue characteristic, separability of g, or N being squarefree.

The elementary discriminant bound proved in [the projective diameter theorem](projective_discriminant_barrier.md) for a monic polynomial with coefficient sup norm H is
\[
 |\operatorname{disc} f|
 \le d^d(d+1)^{d-1}H^{2d-2}.
\]
Consequently in the shape (3), \(m=(d-1)/2\), one necessarily has
\[
 \log H\ge\tfrac14\log N-O(\log d).
 \tag{9}
\]
For polynomially growing degrees this excludes a uniform half-scale coefficient-height envelope, much less a quarter-scale one. Exact small actual norms at selected marks, as in §3, are not excluded. The generic discriminant-based ideal-reduction bound is also very large in this family, even if some selected norms are tiny.

There is a related obstruction for *shared* modular cofactors of distinct low-height fields. Let f,F be coprime monic integer polynomials of degrees d,e, with monic common divisor g of their reductions modulo N of degree m. Then
\[
 N^m\mid\operatorname{Res}(f,F).
 \tag{10}
\]
Use multiplication by F in \(\mathbb Z[X]/(f)\), and a monic lift of \(\bar f/g\) times the first m powers of X as the last m basis vectors, exactly as above. Since \(\bar F\) is divisible by g, these m columns vanish modulo N. Hadamard on the Sylvester matrix gives
\[
 m\log N\le
 e\log H_f+d\log H_F+
 \tfrac e2\log(d+1)+\tfrac d2\log(e+1).
 \tag{11}
\]
Thus two distinct coprime polynomials whose degrees and log heights are each at most \(L^{1/2+o(1)}\), \(L=\log N\), can have only \(L^{o(1)}\) common modular cofactor degree (up to the indicated logarithmic factors). They cannot share a degree comparable to \(L^{1/2}\) in this regime. This does not exclude cancellation by a large family of small-degree overlaps, exact norm-controlled large-height polynomials, or equality of actual resultant residues without a shared polynomial factor. It does exclude a direct attempt to cancel nearly the entire cofactor by a single additional low-height field.

## 5. Relation to uniform quarter-scale supply

The combined [mask-bank theorem](uniform_masked_anchor_supply.md) and (2)–(5) give a more precise sufficient condition for a quarter-scale factoring algorithm. A square-only public sampler may produce arbitrary correlated row blocks; the fields may vary with the sampled square. After known-square norm transport it suffices that a core of mass \(\exp(-O(\Lambda_{1/4}))\) use a common generator span of binary rank \(\exp(O(\Lambda_{1/4}))\), with actual polynomially charged computation/data on that scale. For example, rational norm supports restricted to primes at most \(\exp(O(\Lambda_{1/4}))\), plus an unmatched cofactor-resultant span of that dimension, would suffice. Exact square parts of norms can be large and need not be factored. There is no separate bound on the number of discarded field-unit directions on the bridged terms. The sampler must be independent of the private root; even if fields are constructed from the *public* square, (2) must produce known correction roots by public arithmetic.

This removes the earlier requirement to prove a new uniform adaptive anchor probability separately from the raw representation theorem, and gives a stronger finite transport mechanism that may permit many fields without paying a separate unit rank for each. What is still missing is the **raw representation core**: either produce sufficiently many correlated small-norm terms with paired modular resultant labels, or construct a sampler that achieves the rational norm squareclasses together with explicit known corrections directly. The interpolation theorem cannot be used to assume that correction. The height obstructions (9)–(11) show why simply adding the new cofactor constraints to the old low-height coefficient schedule fails. No quarter-scale probability estimate or complete factoring theorem is claimed.

## 6. Exact checks

The [tested script and receipt](../verification/research/README.md#uniform-masked-anchors-and-affine-core-collision-supply) verify 24 explicitly constructed square-cofactor fields, all 60 prescribed exact norm lifts, 98 additional mark identities passing the norm-unit guard, and 128 shared-modular-divisor resultant divisibilities (including repeated prime powers). The 22 failed unit guards were counted separately. The test verifies coefficient CRT, Eisenstein and discriminant divisibility, and checks all resulting square corrections by modular arithmetic. The construction uses supplied compatible ratios (6); it does not solve those ratios as unknown square-root problems. No asymptotic supply or full code implementation is inferred.
