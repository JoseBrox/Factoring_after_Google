# Quadratic class-coset norm ranks: an obstruction and a small-subgroup alternative

28 November 2026. **Status:** proved uniform affine-support bound for minimum-norm ideal-class representatives, with a consequent obstruction to quarter-scale rank supply from sufficiently large uniformly sampled class cosets. Also a constructive exact alternative for sufficiently small generated class subgroups, and an elementary lower bound on subgroup size from split-prime generators. The intermediate-subgroup and deliberately correlated sampling regimes remain open. No new complete factoring complexity theorem is claimed.

This follows [compact quadratic packet reduction and class walks](compact_quadratic_packet_walks.md), [masked anchor supply](uniform_masked_anchor_supply.md), and [the distinct-input multiway obstruction](multiway_norm_parity_barrier.md). The new bound concerns *independent class sampling even for repeated copies of one target*. It does not impose small norms on the original target packets, and allows all square factors of the reduced norms and arbitrary affine offsets. It is not a smoothness heuristic or a lower bound on all possible factoring methods.

## 1. Minimum norms and their exact multiplicities

Let \(D\) be a positive integer and \(A_D=\mathbb Z[\sqrt{-D}]\), of discriminant \(\Delta=-4D\). Write \(C_D\) for its finite proper invertible ideal class group. The order need not be maximal, and D need not be squarefree. We use the classical proper-ideal/primitive-form correspondence and unique reduced form convention \(-a<b\le a\le c\), with \(b\ge0\) when \(a=c\); see Cox, *Primes of the Form \(x^2+ny^2\)* (1989), Theorems 2.8 and 7.7, and the [standard reduction summary](https://flintlib.org/doc/algorithms/number-theory/binary-quadratic-forms.html). The same convention is implemented in our preceding exact walk script.

For a class \(x\in C_D\), put \(n(x)=a\) for the leading coefficient of its reduced form. This is the minimum norm of an integral invertible ideal in the class: the reduced positive definite norm form has \(c\ge a\), \(|b|\le a\), hence its value on any nonzero integer vector \((i,j)\) is at least \(a(i^2-|ij|+j^2)\ge a\), with equality at \((1,0)\). Equivalently, reducing an invertible ideal by the conjugate-quotient rule (2) in the preceding note obtains that minimum. Put
\[
 X=\left\lfloor\sqrt{4D/3}\right\rfloor,\quad
 \ell=\log X,\quad
 \nu(x)=(v_p(n(x))\bmod 2)_p .
\]
In the sequel D is sufficiently large, so \(X>1\). The vectors are actual rational norm squareclasses, with finite support. Because \(4ac-b^2=4D\), every reduced form has \(1\le a\le X\).

For fixed \(a\), write \(b=2r\). Then \(c=(r^2+D)/a\), and the convention on b makes r a single representative of its residue modulo a. Thus
\[
 \#\{x:n(x)=a\}\le R_D(a),\qquad
 R_D(a)=\#\{r\bmod a:r^2\equiv-D\bmod a\}.                 \tag{1}
\]
This is an upper bound even at bad primes of a nonmaximal order; dropping primitivity or reduction only enlarges the count. The function \(R_D\) is multiplicative by CRT. If \(p\nmid2D\), \(R_D(p^j)\le2\) for every \(j\ge1\) by simple-root lifting. At every other prime,
\[
 R_D(p^j)\le 4p^{\lfloor j/2\rfloor}.                    \tag{2}
\]
To see this, put \(v=v_p(D)\). When \(j\le v\), the congruence is a square-zero condition modulo \(p^j\), with exactly \(p^{\lfloor j/2\rfloor}\) solutions. If \(j>v\), a solution requires \(v=2w\) even and \(r=p^w z\) with z a unit. The residual unit-square equation modulo \(p^{j-2w}\) has at most two solutions for odd p and at most four for p=2; each has \(p^w\) lifts in the original equation. This proves (2). For p=2 the unit-root bound follows, for modulus \(2^m\) with \(m\ge3\), from \((z-z_0)(z+z_0)\equiv0\bmod2^m\): one factor has valuation one and the other must be divisible by \(2^{m-1}\). The smaller moduli are immediate.

## 2. Uniform counting of any low-dimensional affine parity space

Allow a fixed set \(P_0\) of discarded rational prime coordinates. It can contain arbitrary terminal primes, not necessarily small ones. Let \(\nu_0\) denote projection to the remaining coordinates. Let V be any affine subspace of dimension at most r in this binary coordinate space. It may depend arbitrarily on previously sampled public data. We count the full reduced classes satisfying \(\nu_0(x)\in V\).

If the intersection of V with attained vectors is nonempty, its linear span has dimension at most r+1. Choose a basis **from the attained vectors** in the intersection. Each vector has support of cardinality at most \(\ell/\log2\), because the product of its distinct prime divisors is at most \(n(x)\le X\). Consequently all classes counted by this affine constraint have norm parity supported on one set \(P\) of at most
\[
 M=|P_0|+(r+1)\ell/\log2                                  \tag{3}
\]
primes. This set is the union of the basis supports and \(P_0\); it is proof-only and need not be computable by the algorithm. This step is essential: a rank constraint need not mean that each norm is smooth, nor that its original label coordinates are small. The bound also allows the affine offset and the original basis of V to have arbitrarily large prime support, since it is the actual attained intersection that is counted.

Put \(Z_P(\sigma)=\prod_{p\in P}(1-p^{-\sigma})^{-1}\). For \(3/4\le\sigma<1\) with \((1-\sigma)\log\log(3D)\le1\), we have the following **uniform absolute count**:
\[
 \boxed{
 \#\{x\in C_D:\nu_0(x)\in V\}
 \le X^\sigma Z_P(\sigma)^2\exp(O(\log\log(3D))).
 }                                                            \tag{4}
\]
The O constant is absolute and independent of r, the affine offset, the chosen subgroup, and the discriminant.

Proof. Drop parity restrictions at primes dividing \(2D\). Apply Rankin's inequality to the sum of \(R_D(a)\) over \(a\le X\) with all valuations outside \(P\cup\{p:p\mid2D\}\) even. The unrestricted good-prime factors at p in P are bounded by
\[
 1+2\sum_{j\ge1}p^{-j\sigma}\le(1-p^{-\sigma})^{-2}.
\]
At good p outside P, retain only the even exponents, giving a factor at most \((1-p^{-2\sigma})^{-2}\). The latter product is at most \(\zeta(2\sigma)^2=O(1)\). At a bad prime use (2); writing \(x=p^{-\sigma}\), \(y=p^{1-2\sigma}\), its unrestricted factor is at most
\[
 1+4(x+y)/(1-y).
\]
Its logarithm is \(O(p^{-1+2(1-\sigma)})\), since \(x\le y\le2^{-1/2}\). To bound the sum over bad primes, write \(T=\log(3D)\). For \(p\le T^2\), the guard on \(\sigma\) gives \(p^{2(1-\sigma)}\le e^4\), so even summing over all integers to \(T^2\) costs \(O(\log T)\). For \(p>T^2\), there are \(O(T)\) primes dividing \(2D\), and their decreasing weights are at most \(e^4/T^2\), giving \(O(1/T)\). This proves the claimed logarithmic factor and (4). In particular no conductor square part has been treated as squarefree or ignored. End proof.

Choose a real \(Y=e^b\) with \(\pi(Y)\ge M\). Because the Euler factor is decreasing in p, \(Z_P(\sigma)\le Z_Y(\sigma)=\prod_{p\le Y}(1-p^{-\sigma})^{-1}\). For \(U=\ell/b\to\infty\), take
\[
 \delta=\frac{\log U}{b},\qquad \sigma=1-\delta ,
\]
assuming the guards on \(\sigma\) in (4) hold. The elementary estimate used in [the earlier parity bound](projected_norm_parity_barrier.md) is
\[
 \log Z_Y(1-\delta)
 \ll \log(2b)+\frac{U}{\log U}.                              \tag{5}
\]
For completeness, the prime-power terms of order at least two in the Euler logarithm are uniformly bounded. Chebyshev's upper bound for primes and partial summation bound the first-power terms by a constant times \(e^{\delta b}/b+\int_{\log2}^{b}e^{\delta t}dt/t\). Up to \(1/\delta\) the integral is \(O(\log(2b))\); above that point substitute \(w=\delta t\) and split at \(w=(\log U)/2\), bounding the integral by \(O(U/\log U)\). This proves (5). Substitution into (4) gives
\[
 \boxed{
 \log\#\{x:\nu_0(x)\in V\}\le
 \ell-U\log U+
 O\left(\log\log(3D)+\log(2b)+U/\log U\right).
 }                                                            \tag{6}
\]
If the set is empty the logarithmic assertion is interpreted as automatic.

For **any** subgroup \(H\subset C_D\), any class \(a_0\), and a uniform \(x\in a_0H\), divide (4) or (6) by \(|H|\). There is no assumption of uniform distribution of the rational leading coefficients. Their actual multiplicities have been counted before dividing. This applies in particular to H equal to the squared subgroup generated by the explicit step ideals of the compact walks.

## 3. Consequence at quarter scale, including repeated-target samples

Write \(L=\log N\), \(\Lambda=L^{1/4}(\log L)^{3/4}\). Suppose \(D=kN\) with \(1\le k\le N^{C_0}\) for fixed \(C_0\), and suppose \(r+|P_0|\le e^{C_1\Lambda}\) for fixed \(C_1\). Choose \(b=(C_1+2)\Lambda\). The ordinary PNT (even a Chebyshev lower bound suffices) ensures \(\pi(e^b)\ge M\) eventually. Here \(\ell\asymp L\), \(\delta=O(\log L/\Lambda)=o(1)\) and \(\delta\log\log(3D)=o(1)\). All guards hold. Set
\[
 Z=U\log U=\Theta_{C_0,C_1}\big(L^{3/4}(\log L)^{1/4}\big).
\]
By (6) the relative error in Z is o(1), uniformly over these D, subgroups, and affine spaces. We obtain the central obstruction:
\[
 \boxed{\Pr_{x\ {\rm uniform\ in}\ a_0H}
 [\nu_0(x)\in V]\le
 \min\{1,\ (X/|H|)\exp(-(1-o(1))Z)\}.}                      \tag{7}
\]
This is not an assumption that all primes appearing in a low-rank core are small. In particular square factors of unbounded permitted size, arbitrary shared odd prime labels, and repeated targets are all allowed.

If \(|H|\ge X\exp(-(1-\eta)Z)\) with fixed \(\eta>0\), the probability in (7) is at most \(\exp(-(\eta-o(1))Z)\). Thus a quarter-scale-dimensional affine core of mass at least \(\exp(-O(\Lambda))\) cannot exist in such a coset. Conversely the existence of that core would necessitate
\[
 \log(X/|H|)\ge (1-o(1))Z.                                  \tag{8}
\]
The constants in Z depend on the proposed rank budget. Equation (8) is a necessary subgroup-size condition, not a sufficient one.

### Adaptive streams and many representations of one target

Suppose a public algorithm has an initial anchor span of rank at most \(\exp(O(\Lambda))\) and generates at most \(\exp(O(\Lambda))\) additional rows. At each step, conditional on the complete prior public history, the row is \(\nu_0(x)+w\), where x is a fresh uniform class in an adaptively specified coset satisfying the above large-subgroup size guard. The offset w may be arbitrary prior data. It may also be the sum of other twist components, provided those are revealed first and the stated conditional uniformity of x still holds. These are explicit distribution hypotheses, not a claim about all dependent class moves.

The event that a new row lies in the span of the earlier rows and anchors means exactly that \(\nu_0(x)\) lies in a fixed affine translate of that span, conditional on the history. Apply (7). The conditional failure probability is \(\exp(-\Omega(Z))\), regardless of whether the public target is a fresh independent square or one already used many times. A union bound over the full capped pool shows that, with probability \(1-\exp(-\Omega(L^{3/4}(\log L)^{1/4}))\), every row increases rank relative to all earlier rows and the pre-existing anchors. In particular no nonempty subset of those newly sampled rows can cancel modulo those anchors. Unlike the distinct-input norm bound, this uses *fresh uniform class samples*, not fresh distinct public residues.

The argument also rules out a low-rank difference core formed from two independently sampled such classes with common target: reveal one of the classes first, and use its parity as the offset. Tag selection can only restrict the counted event. A deliberate algebraic correlation between two samples need not meet conditional uniformity and is not excluded.

Approximate uniform class sampling of §5 in the compact walk note can achieve total variation \(\exp(-cZ)\) for any desired fixed c, by increasing the binary exponent precision by \(O(Z)\) bits. This is polynomial in L and suffices for the same union bound. Analyze hypothetical abstract output classes, counting a proper gcd during the actual walk as immediate success. We do not condition on the absence of an intermediate gcd exit and then assert uniformity. The theorem is an obstruction to parity relations from the sampled norm rows; it does not bound the probability of those separate factor exits. Nor does it apply to new anchors deliberately constructed *from* a fresh class before its row is tested, or to arbitrary dependent carry identities along a composition path.

## 4. The full squared subgroup is generally far too large

We give a verified arithmetic size comparison, rather than assume that the full class group has heuristic size.

### An elementary 2-rank bound for every order here

Inversion on proper form classes sends \((a,b,c)\) to \((a,-b,c)\). By unique reduction, a class of order dividing two is represented by a reduced form with \(b=0\), \(|b|=a\), or \(a=c\). For the first type \(ac=D\) and \((a,c)=1\) by primitivity; there are at most \(2^{\omega(D)}\) such ordered factor pairs. In the second type \(a=2t,\ b=a\) under the canonical convention, and \(t(2c-t)=D\). Primitivity gives \((2t,c)=1\), so the gcd of these two factors divides 2. In the third type \(b=2r\) with \(r\ge0\), \((a,2r)=1\), and \((a-r)(a+r)=D\), again with gcd dividing 2. The corresponding factor pair determines the form in each type. For pairs whose gcd divides 2, each odd prime power of D must be assigned entirely to one side; the 2-adic exponents have at most four assignments (one side has exponent zero or one). This bounds both types by \(4\cdot2^{\omega(D)}\), allowing harmless double counting. Hence
\[
 \boxed{|C_D[2]|=[C_D:C_D^2]\le 9\cdot2^{\omega(D)}.}         \tag{9}
\]
The equality follows from the kernel/image count for squaring in a finite abelian group. Every subgroup G of \(C_D\) likewise satisfies \([G:G^2]=|G[2]|\le9\cdot2^{\omega(D)}\). This proof needs no fundamental-discriminant hypothesis or explicit genus-character computation.

### Effective class-size bound, with its precise exception

Assume now N odd and squarefree, \((k,N)=1\), \(1\le k\le N^{C_0}\). Let \(d_K<0\) be the fundamental discriminant of \(\mathbb Q(\sqrt{-kN})\), and f the conductor of the order \(A_D\), so \(-4D=f^2d_K\). In particular \(N\le |d_K|\le4N^{1+C_0}\). Use Tatuzawa, *On a theorem of Siegel*, Japanese J. Math. 21 (1951), 163–178, [primary PDF, Theorem 2, p.164](https://www.jstage.jst.go.jp/article/jjm1924/21/0/21_0_163/_pdf). The actual theorem page was rechecked: for \(0<\epsilon<1/2\), conductor \(q\ge\max(e^{1/\epsilon},e^{11.2})\), one has \(L(1,\chi)>0.655\epsilon q^{-\epsilon}\) for primitive real characters, with at most one exception. Its imaginary quadratic class-number application is also explicit on that page; compare Hopkins–Stopple, *Lower bounds for the principal genus of definite binary quadratic forms*, Integers 10 (2010), 257–264, [Theorem 2, p.259](https://math.colgate.edu/~integers/k21/k21.pdf), whose page image was checked.

For each fixed N take the **same** parameter \(\epsilon=2/L\) for all its candidate twists. Then the guard holds eventually, and
\[
 L(1,\chi_{d_K})\gg_{C_0}1/L
\]
apart from at most one fundamental field among all these twists. This does not claim that the exceptional field is identifiable, or that a varying parameter gives one global exception over all input sizes. It is an effective uniform assertion with the specified common parameter.

Use the imaginary quadratic class number formula and the ring class number formula for the order (Cox, 1989, [Theorem 7.24, p.146](https://www.math.utoronto.ca/~ila/Cox-Primes_of_the_form_x2%2Bny2.pdf); the stated formula was rechecked):
\[
 |C_D|=h(d_K)\frac{f}{[O_K^\times:A_D^\times]}
                  \prod_{p\mid f}(1-\chi_{d_K}(p)/p).
\]
For the large fields here the unit index is one, since both unit groups are \(\{\pm1\}\). Moreover \(\prod_{p\mid f}(1-1/p)\ge1/(\omega(f)+1)\gg_{C_0}1/L\) by ordering distinct primes. Thus, for the nonexceptional fields,
\[
 |C_D|\gg_{C_0}X/L^2,\qquad
 \log(X/|C_D^2|)\le O_{C_0}(\log L+\omega(D)).               \tag{10}
\]
In particular the large-coset obstruction applies to the **full squared subgroup** if \(\omega(D)=o(Z)\). This includes balanced squarefree semiprimes and any fixed coprime twist k, and more generally B-rough squarefree inputs with \(\log B\gg\Lambda\) and twists having \(o(Z)\) prime factors: \(\omega(N)\le L/\log B=o(Z)\). For a subgroup \(H\subseteq C_D^2\) of relative index \(\exp(o(Z))\) the same conclusion holds. More quantitatively, (8) and (10) imply that a subgroup supplying a quarter-scale affine core in these fields must have
\[
 \boxed{[C_D^2:H]\ge \exp((1-o(1))Z)}                       \tag{11}
\]
under \(\omega(D)=o(Z)\).

For a fixed balanced semiprime input, two fixed coprime twists of distinct squarefree parts yield distinct fundamental fields, so at most one can be exceptional at the chosen parameter. For k=1 and squarefree N in a dyadic interval \([Y,2Y]\), use a common \(\epsilon=2/\log Y\); the fields are distinct, giving at most one exceptional N in that interval. More generally, among integer twists up to K the exceptional field can only occur at one squarefree part of k, accounting for at most \(\sqrt K\) choices. This observation does not prove that the *step-generated subgroup* has large relative size or that a particular twist bank meets the small-\(\omega(D)\) guard.

**Stronger full-coset rank corollary.** For balanced semiprimes and a fixed coprime twist in a nonexceptional field, (10) has logarithmic loss \(O(\log L)\). Fix \(0<\beta<1\). If the affine rank of the entire squared coset were at most \(\exp(L^\beta)\), choose instead \(b=2L^\beta\) in (6). The guards remain valid and \(U\log U\asymp_\beta L^{1-\beta}\log L\), which dominates the class-size loss and the errors. This would give mass \(o(1)\) for a set that has mass one. Hence, eventually on this family, the full coset affine rank exceeds \(\exp(L^\beta)\) for *every fixed* \(\beta<1\). Thus the desired general quarter-scale bound on the entire residual squareclass span is false, not merely unproved. This assertion is about the rank over rational primes, not the small abstract rank of the genus quotient.

## 5. A constructive alternative for genuinely small squared subgroups

There is a useful exact extraction endpoint that needs no norm factor-base rank bound if the subgroup is small enough. It is conditional on the explicit subgroup size and the supplied factored-packet initialization, not a solution of either.

Work with the compact guarded ideal states from the preceding note in one fixed twist with \(4k<3N\). Suppose m independent sealed square targets \(s_i=h_i^2\) have supplied reduced invertible ideal states \(A_i\), with known unit corrections \(n(A_i)\equiv s_i c_i^2\bmod N\). For example these are supplied factored packets, not assumed free general factorizations. Let G be generated by their proper classes and any supplied extra unit-norm ideal classes. Put \(H=G^2\), so it is generated by the squares of all these generators.

For any generator state with public target u and correction c, compact composition with itself gives a state of class its square, target \(u^2\), and explicit correction d. Relabel its target as 1, replacing d by \(ud\). Thus every generator of H has a known-square state. Use exact canonical reduced form keys for all comparisons, not norm equality alone (norm equality would suffice for the final certificate, but does not identify a class).

Here is a capped public algorithm.

1. Enumerate H by breadth-first multiplication by its squared generators, keeping one guarded compact known-square state per canonical class key. Finiteness of the group ensures closure under the supplied generators gives their whole subgroup, even without explicitly listing inverse edges. If the enumeration hits the chosen cap, abandon this branch; it is not evidence that an unenumerated class is outside H. A verified proper gcd during any composition terminates successfully.
2. Maintain a dictionary of complete H-cosets generated by the previously retained independent target classes, each entry with a guarded compact state and a bitmask indicating which target residues its state represents. Start with the dictionary for H and zero target bitmask. Test each next target class for dictionary membership. If absent, multiply every previous dictionary entry by the target state, toggling its bit in the label. The old and new cosets are disjoint because the target class was absent, and their union is the new quotient span since \(G/H\) has exponent two. Check the cap also on these expansions.
3. When a target class is present, let its equal-class dictionary state represent \(\prod_{j<i}s_j^{x_j}\), with known correction d. The two minimum norms are identical, so
\[
 \frac{s_i}{\prod_{j<i}s_j^{x_j}}\equiv(d/c_i)^2\bmod N .
\]
Verify this publicly. Its signed sealed coefficient vector has an odd coordinate i. Only now form the corresponding signed product of private roots, compare to the known correction root, and take a gcd. Conditional on the entire preceding public transcript, the resulting root-of-unity factor is uniform on the \(2^{\omega(N)}\) possibilities. Hence proper split probability is at least one half for odd non-prime-power input. The dictionary selection and verification use no private sign.

By (9) the quotient has dimension at most \(\log_2(9\cdot2^{\omega(D)})\), so \(m>\omega(D)+\log_2 9\) guarantees a dependency among these target classes unless a cap or proper factor exit occurs. The dictionary stores at most \(|G|=|H|[G:H]\le9|H|2^{\omega(D)}\) class keys. Its work is polynomial in the actual supplied generator/target data, \(\log(kN)\), and \(|H|2^{\omega(D)}\), using the compact state composition and checked square corrections. In particular if \(|H|2^{\omega(D)}\le e^{O(\Lambda)}\) and initialization is available on that scale, this branch has quarter-scale cost without factoring any intermediate residual norms or bounding their rational norm-squareclass rank.

The same algorithm works in a finite direct product of twists by using tuples of canonical keys and the product of the minimum norms, with the correction being the product of component corrections. The 2-rank budget is then the sum of the individual bounds, and the size cap must be charged for the actual generated subgroup of that direct product. It is not enough that each single component subgroup be small if their product is too large.

This endpoint illustrates the distinction between genus rank and actual rational norm rank: **if the full squared subgroup is large, knowing the genus quotient has small rank is not an algorithm for finding its square preimages**. The dictionary actually computes a witnessed membership in the squared subgroup. One must not replace that membership search by a genus-character test alone.

### Many small split generators need not produce a small subgroup

There is also a useful elementary size constraint on the positive branch. Suppose G contains one chosen prime-ideal class above each of s distinct odd split primes \(p\le B\), \(p\nmid D\). For every integer \(1\le j\le s\) with \(B^j<\sqrt D\), the products over j-element subsets have pairwise distinct rational norms \(a=\prod p\). Their HNF ideals have basis \((a,0),(r,1)\) with \(r^2\equiv-D\bmod a\) by CRT, because the local choices are simple linear root ideals. The associated form is primitive: \(a\) is squarefree and at each divisor p its middle coefficient \(2r\) is a unit. Choose the canonical representative of r modulo a with \(-a<2r\le a\). Its last coefficient \((D+r^2)/a>a\), so it is already reduced, with leading coefficient a. Distinct norms give distinct proper classes. Therefore
\[
 |G|\ge {s\choose j},\qquad
 \boxed{|G^2|\ge {s\choose j}/(9\cdot2^{\omega(D)}) .}        \tag{12}
\]
For \(D=kN,\ \log D=O(L)\), \(s\ge e^{c\Lambda}\), \(B\le e^{C\Lambda}\) with fixed positive c,C, choose \(j=\lfloor L/(4C\Lambda)\rfloor\) eventually. Then \(B^j<\sqrt D\), \(j\ll s\), and \(\log {s\choose j}\ge j\log(s/j)=\Omega_{c,C}(L)\). Since \(\omega(D)=o(L)\) by the elementary product-of-distinct-primes bound, the squared subgroup is exponentially large in L. Simply adding a quarter-scale-sized bank of distinct small split ideals therefore cannot force the small-subgroup branch. Equation (12) does not show that the subgroup is as large as the near-full threshold of §3, and does not settle the sizes of groups generated by a bounded number of small primes.

## 6. Exact finite check and research decision

Run [verify_class_coset_rank.py](../verification/research/verify_class_coset_rank.py) using Python 3.13.5 and SymPy 1.14.0, with the previously checked rank-two ideal arithmetic module in the same directory. It exhausts the small reduced forms, computes the squared subgroup by squaring *every* class, partitions the complete group into its cosets by explicit ideal composition, and uses exact integer-bitset elimination for norm and affine-difference ranks. It also checks the local root count bounds and the affine support containment, with an independent short-middle-coefficient enumerator on the smaller fixtures. Nonmaximal-order examples are included. The finite computations are not extrapolated to establish (7).

The exact small-subgroup certificate test uses explicitly factored public square representatives, keeps all class keys and correction data public, and verifies the final square relation before accessing the private roots. The proof of the branch is independent of these finite examples. See the [verification receipt](../verification/research/README.md#quadratic-class-coset-rank-obstruction-and-small-subgroup-readout).

The conclusion is that an unrestricted quarter-scale upper bound for full-coset rational norm ranks is impossible, and a near-full subgroup mixed by independent square exponents is also the wrong supply mechanism. The remaining substantive regime is a suitably chosen proper subgroup of very large index but not necessarily small absolute size, or an arithmetic correlation between samples that deliberately violates the fresh-uniform-class assumption. The latter must generate *useful odd target relations*, not just the norm-neutral relation between a class and its inverse. A different approach might compute witnessed square membership directly rather than enumerate it. Neither the existence of such a subgroup with sufficient low-rank core mass, nor a uniform quarter-scale square-membership/initial-packet algorithm is established here. We have narrowed the required new arithmetic theorem, not proved a sub-one-third factoring exponent.
