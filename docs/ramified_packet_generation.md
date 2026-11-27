# Prescribed ramified packets, exact norms, and cross-map compression

27 November 2026. **Status:** constructive packet-generation theorem, exact norm gluing for several known modular maps of one field, and a capacity bound for principal ramified packets in totally real extensions. This is an advance on the input side of [shared-base norm transport](shared_base_norm_transport.md): full-fibre structure need not be assumed for selected base primes. It does not establish a uniform supply of sufficiently many useful low-norm marks or a new factoring complexity exponent.

## 1. A shared field in which all requested primes have a unique ideal

Let F be a totally real odd-degree field with an explicit order A and a verified evaluation \(\psi_0:A\to\mathbb Z/N\). F=Q is allowed. Write \(I=\ker\psi_0\). Supply a nonempty finite set of distinct prime ideals \(\mathfrak p_i\) of A at good rational primes (A is locally maximal there, and the ideals are invertible), with their rational primes coprime to N. The ideals and residue arithmetic are explicit. Choose an odd relative degree \(d\ge3\).

We first choose \(a\in A\) satisfying
\[
 v_{\mathfrak p_i}(a)=1\quad\text{for all i},\qquad \psi_0(a)\in(\mathbb Z/N)^\times .
\]
This is possible constructively: choose a nonzero class of each \(\mathfrak p_i/\mathfrak p_i^2\) and any unit image modulo I, then use CRT. To find the first class, use a lattice basis of the proper invertible ideal \(\mathfrak p_i\) and test which basis elements lie outside \(\mathfrak p_i^2\). CRT is applicable because all these moduli are pairwise comaximal. Alternatively, if a supplied base reduction already satisfies these valuation-one and unit guards, use its element a. In that case the residual part of (a) is whatever the actual base reduction gives; we do not claim a new bound on it.

Choose public unit residues \(t_1,\ldots,t_d\) modulo N satisfying \(\prod_i t_i=\psi_0(a)\). The first d-1 may be arbitrary; set the last to the balancing quotient. We seek a monic polynomial \(g(T)\in A[T]\) of degree d, with constant term \(-a\), nonleading coefficients in every \(\mathfrak p_i\), and
\[
 \psi_0(g)(T)=\prod_{\ell=1}^d(T-t_\ell)\quad\text{over }\mathbb Z/N.
 \tag{1}
\]
The constant term in (1) is correct since d is odd. For each of the other nonleading coefficients the simultaneous congruences are solvable by CRT modulo I and the \(\mathfrak p_i\).

We can even arrange that \(K=F(\vartheta)\), \(g(\vartheta)=0\), is totally real. Here are explicit size guards for that optional version. Let Q be N times the product of the rational primes below the supplied prime ideals. The ideal \(QA\) is contained in every coefficient modulus. Representatives of the corrections in a fixed integral basis can therefore have coordinates in \([0,Q)\). Take a positive integer \(M\ge1\) bounding \(|\sigma(a)|\) and \(Q\sum_j|\sigma(\omega_j)|\) for all real embeddings \(\sigma\) of F, with \(\omega_j\) the integral basis of A. Such an integer has polynomial bit length in the explicit data: the absolute values of the eigenvalues of each integral multiplication matrix are bounded by its maximum absolute row sum. No embedding approximation is necessary to obtain this coarse bound.

Choose an integer S divisible by the product of the supplied rational primes and satisfying
\[
 S>8dM\,(4(d+1))^{d-1}.
\]
Start with the monic product \(P(T)=\prod_{\ell=0}^{d-1}(T-\ell S)\), whose constant term is zero and whose other nonleading coefficients lie in all the supplied primes. Add the coefficient corrections chosen by CRT to reach (1), and use the exact constant \(-a\). Each correction has absolute value at most M at every embedding. On the endpoints of the bracket \(\ell S\pm S/4\), the absolute product is at least \((S/4)(3S/4)^{d-1}\), with opposite signs at the two endpoints. The total absolute correction is at most \(d M((d+1)S)^{d-1}\), smaller by the strict choice of S. Thus for every real embedding of F the d brackets contain d distinct real roots. All coefficient and guard bit lengths are polynomial in the degree and actual input batch bit length. This construction may have large coefficient heights; it is not a small-discriminant theorem.

By Eisenstein at any supplied prime, g is irreducible over F. At each such good prime it is Eisenstein over the corresponding DVR; hence the extension is totally ramified, with a unique prime \(\mathfrak P_i\) over \(\mathfrak p_i\), ramification index d and residue degree one, and \(v_{\mathfrak P_i}(\vartheta)=1\). This follows either from the local Eisenstein theorem or directly from the valuations of the conjugate roots of an Eisenstein polynomial. In particular
\[
 \operatorname{Norm}_{K/F}(\vartheta)=a,\qquad
 \operatorname{Norm}_{K/F}(\mathfrak P_i)=\mathfrak p_i.
 \tag{2}
\]
There are d known compatible evaluation maps on \(A[\vartheta]\), obtained by \(\vartheta\mapsto t_\ell\) and the original evaluation on A. The order and its multiplication table are explicit. No prime factor of N is needed, and no search for roots of an arbitrary polynomial modulo N is hidden in the construction.

### Consequence for active labels

The relative projection of [shared-base transport](shared_base_norm_transport.md), (5), vanishes identically on the field-specific valuation at each of these primes: the fibre has length one, \(e=d,f=1\), so \(v-e f^T v/d=0\). This holds for *every* element of the extension, not only deliberately copied base elements or deliberately completed Galois orbits. A primitive degree-one mark \(\vartheta\) itself has valuation one, so total ramification avoids the primitive-content obstruction of an inert prime. At an inert good prime, the reduction of the power basis is a basis of a field over the residue field, and a reduced-degree polynomial atom can vanish there only when all its coefficients vanish modulo the base prime. Total ramification permits genuine degree-one occurrences.

Thus we can choose compatible fields after the current batch of public request primes is known, and guarantee that their relative valuation directions at those primes all transfer to the common base. The actual row-rank saving is still the intersection formula of the companion note; using more copies does not create independent target information.

## 2. Particularly simple exact norm packet over Q

For \(F=\mathbb Q\), let \(Q_0=\prod_i q_i>1\) be the product of supplied distinct rational primes coprime to N. Set \(a=Q_0\). The construction can omit total reality if not needed: prescribe the nonleading coefficients of
\[
 g(T)=T^d+Q_0 a_{d-1}T^{d-1}+\cdots+Q_0 a_1T-Q_0
\]
by (1), using \(0\le a_j<N\). Its coefficient bit lengths are \(O(\log Q_0+\log N)\). For the totally real version use the bracket construction in §1. In either version,
\[
 (\vartheta)=\prod_i\mathfrak P_i,\qquad
 \operatorname{Norm}_{K/\mathbb Q}\vartheta=Q_0,\qquad
 \vartheta^d/Q_0\in\mathbb Z[\vartheta]^\times .
 \tag{3}
\]
Indeed the valuations at every \(q_i\) are exactly one, and the norm identity excludes every other prime. The unit is in the power order because the polynomial equation writes it as \(1-\sum_{j=1}^{d-1}a_j\vartheta^j\), and its multiplication determinant is 1, so its inverse is in the order too.

This is an exact norm-controlled *packet* of arbitrary supplied rational requests: the norm factorization is already known, and the image of the mark in any of the d maps is the chosen public \(t_\ell\). One can set one of the \(t_\ell\) to 1, obtaining a literal unsealed identity with active valuations one at every requested prime. If one chooses \(t_\ell\) adaptively from public rows, all evaluation-map choices must be recorded in the row history. A balancing root is not an additional independently sealed private root.

For example, (3) makes the modular product of all d images equal to the exact known rational packet \(Q_0\), despite arbitrary heights of the defining polynomial. It does not give independent norm-controlled marks for each \(q_i\) separately, which is an essential distinction.

## 3. Cross-map norm gluing without a Galois field

The construction above gives a complete known factorization of g over the modular ring. The following compression uses that property for *arbitrary* field elements. Let \(K/F\) be any degree-d extension presented by a monic polynomial g over A, with d known modular roots counted with multiplicity satisfying (1). For each explicit integral mark \(\gamma=h(\vartheta)\), the resultant identity gives
\[
 \boxed{\psi_0(\operatorname{Norm}_{K/F}\gamma)
                   =\prod_{\ell=1}^d\psi_\ell(\gamma).}\tag{4}
\]
This is the universal monic resultant product identity, valid over the composite ring by polynomial specialization. The roots need not be distinct. For fractions it holds provided all needed evaluations of numerator and denominator are units; a unit image of the relative norm suffices for all of its component images to be units. We explicitly check these guards. Neither Galois normality of K/F nor identification of the modular maps with rational automorphisms is assumed.

Suppose a row has a component in the base and one in each of the d modular copies of this field:
\[
 s=\psi_0(\gamma_0)\prod_{\ell=1}^d\psi_\ell(\gamma_\ell).
\]
Choose the d-th copy as reference. With the guards just described, the exact cross-map transition is
\[
 s=\psi_0\bigl(\gamma_0\operatorname{Norm}_{K/F}\gamma_d\bigr)
       \prod_{\ell<d}\psi_\ell(\gamma_\ell/\gamma_d).
 \tag{5}
\]
There is no exponent multiplication at all, so no parity loss. The d-th field component disappears; the common algebraic factor has become a single base norm. This is not the same as identifying arbitrary elements in different modular copies. Such an identification would be invalid without (4).

Fix a base prime \(\mathfrak p\), let f be the vector of relative residue degrees above it, and \(v_\ell\) the ideal valuation vector of the \(\ell\)-th copy. The finite-coordinate map in (5) is exactly
\[
 (x_0,v_1,\ldots,v_d)\longmapsto
 (x_0+f^Tv_d,v_1-v_d,\ldots,v_{d-1}-v_d).
\]
Its kernel consists of \(v_1=\cdots=v_d=v\), \(x_0=-f^Tv\). It saves one whole copy of the valuation space on the full ambient fibre (one dimension per prime ideal over \(\mathfrak p\)), and saves its intersection with the actual incidence span on supplied rows. The remaining log-unit rank is bounded by the base unit rank plus (d-1) copies of the field unit rank, rather than d copies. If the d-th component was identically absent from all rows, this operation is just padding with identity and there is no claimed saving. One can also combine (5) with relative norm normalization of the remaining components, using the odd-degree rule in the companion note.

This gives an additional **joint image/ideal reduction** for diagonal correlated requests. If \((\alpha)=\mathfrak a\mathfrak b\) is a chosen reduction of one ideal label, reuse the same element across all d modular copies. The d images satisfy
\[
 \prod_{\ell=1}^d\psi_\ell(\alpha)
                  =\psi_0(\operatorname{Norm}_{K/F}\alpha).
\]
The base ideal of the right side is \(\operatorname{Norm}\mathfrak a\,\operatorname{Norm}\mathfrak b\); its exact norm-down residual is shared, not d unrelated rational residues. For \(F=\mathbb Q\) the right side is simply the signed integer norm, computable by an exact determinant, even if \(\mathfrak b\) has not been factored. Combined with (5), any balanced combination of these diagonal requests cancels that same residual exactly. With an explicit base norm reduction the graph argument of [correlated transport](joint_ideal_image_transport.md) applies as before. In contrast with separate field reductions, this move uses a proved arithmetic identity coupling all the evaluation maps.

### Combining the two norm projections

If a field \(K_j/F\) of odd relative degree \(d_j\) has all its \(d_j\) compatible modular maps known, first apply the relative normalization (4) of [shared-base transport](shared_base_norm_transport.md) to each copy, with one common odd exponent. The resulting field components have relative norm one. The product of their modular images for a *common* relative norm-one factor is 1 by the complete-map norm identity (4) above. Consequently applying (5) to these normalized components drops one copy without any additional base norm factor. The remaining ratios are again relative norm one.

On a full base-prime fibre with \(m_j\) distinct primes above it in \(K_j\), the two operations leave ambient dimension
\[
 1+\sum_j(d_j-1)(m_j-1)
\]
instead of \(1+\sum_j d_j m_j\). The first 1 is the shared base valuation, each relative vector is in a codimension-one residue-degree kernel, and the complete-map diagonal removes one such vector for each j. The analogous log-unit bound is
\[
 u(F)+\sum_j(d_j-1)(u(K_j)-u(F)).
\]
As before, the actual savings are the intersection with the actual incidence span, not the ambient dimension difference. Charge all terminal coordinates introduced by norm and extension, including any other prime ideals over a base prime in the original terminal support. No savings are inferred from absent copies padded by identity.

## 4. A capacity obstruction for principal ramified packets

Total ramification is not a way to principalize arbitrarily many independent target primes at zero archimedean rank cost. There is a sharp algebraic accounting rule for the totally real construction.

Let \(K/F\) be a totally real extension of odd relative degree d, and let S be any finite set of base prime ideals totally ramified in K, with unique primes \(\mathfrak P_{\mathfrak p}\) above them. In \(\mathbb Z^S\) define the principal lattices
\[
 L_F=\{v:\prod_{\mathfrak p\in S}\mathfrak p^{v_{\mathfrak p}}
                         \text{ is principal in F}\},\qquad
 L_K=\{v:\prod_{\mathfrak p\in S}\mathfrak P_{\mathfrak p}^{v_{\mathfrak p}}
                         \text{ is principal in K}\}.
\]
Then \(dL_F\subset L_K\subset L_F\) by extension and norm. In particular the quotient \(L_K/dL_F\) is finite. We claim the stronger bound
\[
 \boxed{|L_K/dL_F|\le d^{u(K)-u(F)},}\tag{6}
\]
where \(u(E)=r_1(E)+r_2(E)-1\).

For \(v\in L_K\) choose a generator \(\gamma\) of the indicated principal ideal, and define \(T(\gamma)=\gamma^d/\operatorname{Norm}_{K/F}\gamma\). Total ramification implies its ideal is trivial, so it is a relative norm-one unit. Changing the generator by a unit multiplies \(T(\gamma)\) by \(T(U_K)\), where \(U_K\) is the unit group. Multiplying the ideal by a principal base packet in \(dL_F\) has no effect on this class. Thus the construction defines a homomorphism
\[
 L_K/dL_F\longrightarrow U_{K/F}^{(1)}/T(U_K).
\]
It is injective: if its image is trivial, there is a unit \(\epsilon\) with \(T(\gamma/\epsilon)=1\), so \((\gamma/\epsilon)^d\in F\). Since all embeddings of K are real and d is odd, at any real embedding of F there is just one possible real d-th root of this value. The element therefore has relative degree one and belongs to F. Its base ideal has support in S, because its extension has support only above S. Its valuation vector in K is d times a vector of \(L_F\), proving injectivity.

Relative norm-one units have rank \(u(K)-u(F)\) by the unit-norm argument of [shared-base transport](shared_base_norm_transport.md); they have no nontrivial torsion, since the norm of -1 is -1. Their d-th powers are in \(T(U_K)\). The target quotient has order at most \(d^{u(K)-u(F)}\), proving (6).

In particular for \(F=\mathbb Q\), if k distinct totally ramified rational primes all have principal unique prime ideals, then \(L_K=\mathbb Z^k\) and
\[
 k\le u(K)=d-1 .
\]
For a prime relative degree d, the dimension over \(\mathbb F_d\) of the principal packet space modulo base extensions is at most the relative unit rank; for composite d the order bound (6) is the correct formulation. This is a field-independent obstruction, not just a rank count for separated linear interpolation. It explains why (3) can easily supply one principal direction across arbitrarily many primes without supplying one independent direction per prime. The genuinely correlated request combination matters.

## 5. Height and supply boundary

At a totally ramified base prime \(\mathfrak p\), the relative discriminant of the monogenic local order in §1 has valuation at least d-1: the derivative \(g'(\vartheta)\) has valuation at least d-1 in the extended normalized valuation, and the residue degree is one. Equivalently use the local discriminant/different formula for the Eisenstein extension. Thus the absolute discriminant of the constructed order satisfies
\[
 \log|\Delta_{A[\vartheta]}|
 \ge d\log|\Delta_A|+(d-1)\sum_i\log \operatorname{Norm}_{F/\mathbb Q}\mathfrak p_i .
\]
This is a *lower bound on the order discriminant*, not on every actual residual norm. In particular a generic discriminant-based LLL norm ceiling for a relative degree of order \(L^{1/2}\) over a fixed-degree base and even a single large request of log-size \(L^{1/4}\) will not certify a half-scale residual. The exact norms (2)–(3) avoid that particular ceiling for the chosen mark. The construction does not show comparable bounds for many other useful marks.

The new positive facts are that one can force relative valuation packets for all currently supplied large primes, without a random split-pattern assumption, and impose complete known modular maps with exact norm coupling. The limitations are equally concrete: the norm of a single constructed mark represents one prescribed principal packet, independent principal ramified directions obey (6), and creating fields or copying rows must not be counted as novel quotient rank. The constructive next target is therefore a family of additional nonlinear norm-controlled marks and old/new-label incidences that achieves a strict saving in the actual quotient of [correlated transport](joint_ideal_image_transport.md), without increasing the relative unit/finite rank by the same amount. The quarter-scale goal remains open.


## 6. Exact finite check receipt

Run [verify_ramified_packets.py](../verification/research/verify_ramified_packets.py) with Python 3.13.5 and SymPy 1.14.0. Tested and committed blob `8226685aba49fa128a2f2d37dd3d2bf57aa0d340`, SHA-256 `0555cb84d8b4c10b92ab14e3e0afee0ec48ca9f3b4d7ffc2b985e7516d4ad423`. The executed tests check 25 constructed fields (including a repeated-root modular example), 49 local Eisenstein/discriminant guards, 289 exact norm evaluations, 144 cross-map transitions, and 200 exact rank identities. The totally real subfamily also has verified rational sign brackets. The manufactured four-square fixture modulo 1189 has public squares 4,9,535,236, relation (1,1,1,-1), and all 256 private-root fibre tuples checked; 128 give proper factors 29 or 41. This deliberately correlated example illustrates the exact gluing and parity readout, not the frequency of such rows on arbitrary inputs. The theorem is not inferred from the finite checks. No full repository, PDF or Lean rebuild was performed.
