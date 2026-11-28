# Partial class annihilators and polynomial ambiguous-form coordinates

28 November 2026. **Status:** two unconditional algebraic/algorithmic results with explicit input-sensitive cost bounds. For odd D, ambiguous form coordinates remove the exponential 2-rank cost of the earlier witnessed square readout, without factoring D. A collision harvest after an arbitrary public exponent constructs a verified annihilator, or a smaller collection of useful annihilated words. The quarter-scale consequence requires a small residual powered subgroup (or bounded residual orders) and the original supplied-packet initialization. Neither arithmetic supply condition is proved in general.

This continues [the class-coset obstruction](quadratic_coset_rank_obstruction.md), [supplied-annihilator extraction](class_annihilator_square_membership.md) and [compact quadratic packet reduction](compact_quadratic_packet_walks.md). The basic smooth-class-order strategy is classical: Schnorr and Lenstra, *A Monte Carlo factoring algorithm with linear storage*, Math. Comp. 43 (1984), 289–311, [primary paper](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1984c/artc.pdf). The point of this continuation is to replace the full smooth-order requirement by witnessed relations in the kernel of a public exponent, and to exploit the special arithmetic of quadratic 2-torsion. Generic birthday collision and Smith-normal-form methods are not claimed as new finite-group algorithms.

## 1. Exact binary coordinates on quadratic 2-torsion

Let \(D>4\) be an **odd** integer, not necessarily squarefree. Put \(A=\mathbb Z[\theta]\), \(\theta^2=-D\), with discriminant \(-4D\), and let C be its proper invertible ideal class group. Use the same primitive positive definite reduced form convention as the [class-coset proof](quadratic_coset_rank_obstruction.md): \(-a<b\le a\le c\), and \(b\ge0\) when \(a=c\). The classical proper ideal/primitive form correspondence and inversion/reduction theorem apply to this order, not just maximal orders.

A divisor \(t\mid D\) is unitary if \((t,D/t)=1\). Write \(I_t=(t,\theta)\). Its index is t, and \(I_t^2=tA\), since the products generate \(t^2,t\theta,-D\), whose integer generators have gcd t. Thus \(I_t\) is invertible and its class has order dividing two. For coprime unitary divisors, multiplication gives the ideal of their product. In particular \(I_D=\theta A\) is principal. If \(D\equiv1\bmod4\), also use \(I_2=(2,1+\theta)\), of index two and with \(I_2^2=2A\): the integer generators 4 and \(-(1+D)\) have gcd 2, and the remaining product yields \(2\theta\). For odd unitary t, \(I_2 I_t=(2t,t+\theta)\). The latter equality follows from the integer CRT or the two coprime ideal congruences.

**Theorem.** The 2-torsion of C is the vector space of unitary-divisor coordinates of D, with an additional independent coordinate at 2 if \(D\equiv1\bmod4\), modulo the single relation corresponding to D. This statement concerns the whole prime powers in D, not merely the odd valuations of a rational divisor.

Proof of surjectivity. Inversion sends a form to \((a,-b,c)\); by unique reduction the order-two classes have \(b=0\), \(b=a\), or \(a=c\). The discriminant relation gives the following explicit representing divisor:
\[
 d(a,b,c)=
 \begin{cases}
 a,&b=0\text{ or }b=a,\\
 2(a-b/2),&a=c\text{ in the remaining case}.
 \end{cases}                                                     \tag{1}
\]
When \(b=0\), \(ac=D\) and primitivity makes a a unitary divisor. When \(b=a=2t\), \(D=t(2c-t)\), t and c are odd, and \((t,2c-t)=1\). This forces \(D\equiv1\bmod4\), and the class is that of \(I_2I_t\). In the remaining \(a=c\) case write \(b=2r\). Then \(D=(a-r)(a+r)\). Because D is odd and \((a,2r)=1\), a is odd, r even, \(D\equiv1\bmod4\), and \(t=a-r\) is unitary. The unimodular substitution with columns \((1,-1),(0,1)\), followed by an integral shear, takes the form to \((2t,2t,a)\), representing \(I_2I_t\). This proves the claimed representation for every order-two class.

For the kernel, take a unitary t with \(I_t=\alpha A\). Because the ideal is integral, \(\alpha=x+y\theta\in A\), and \(x^2+Dy^2=t\). If y is nonzero this forces \(t=D\); otherwise \(\alpha\) is scalar and equality of the ideals forces \(|x|=1\), since \(I_t\) contains \(\theta\). In the extra-2 case, multiply by the principal \(I_D\) if necessary to represent the class by \(I_2I_t\) with \(t\le\sqrt D\). Its index is \(2t<D\) for \(D>4\). The norm equation for a principal generator again forces y=0, but a scalar generator of \(I_2I_t\) would have to divide the coefficient 1 of \(\theta\) in \(t+\theta\). Thus a principal even-index ideal of this type is impossible. The kernel is exactly the single D relation, as asserted. End proof.

### Polynomial membership without factoring D

Given any list of order-two class keys, compute their d values by (1). Start with D as one divisor block (and the block 2 when permitted). Refine by gcd with each supplied d, splitting a block only when its gcd is a proper nontrivial divisor. All odd blocks are unitary divisors of D, so the resulting pairwise coprime blocks retain the full prime powers. Each supplied d is exactly the product of a subset of blocks. These subset vectors embed faithfully into the true prime-power coordinate space; a linear relation in the compressed coordinates holds precisely when it holds in the actual coordinates. Include the vector for D as a quotient relation.

Consequently binary elimination decides whether a queried order-two class belongs to a span of earlier classes and, if so, gives explicit binary coefficients. One may refine from scratch for each query, in polynomial bit work in the number of keys and \(\log D\); it does not enumerate either prime factors or \(2^r\) products. Verify each returned word by class composition. The even factor 2 is a separate coordinate, not merged into D.

This replaces the top-element table in [the earlier annihilator theorem](class_annihilator_square_membership.md), §§3–4. In order-descending cyclic basis construction and the subsequent bitwise coordinate extraction, every top query is a class of order dividing two. Hence the same proofs and polynomial number of group operations apply with the new divisor-span solver. We obtain a witnessed class-square algorithm **polynomial in the actual binary annihilator and generator data**, with no \(2^r\) cost, for odd D. The proof does not cover even D, whose extra 2-adic conductor cases require a separate treatment.

### A stronger factoring-specific rank bound

Suppose \(D=kN\) with odd k coprime to odd N. Test \((d,N)\) for every queried ambiguous divisor d; a proper gcd is success. If no such gcd occurs, every d contains either all the prime-power blocks belonging to N or none. Toggling the principal D vector removes the entire N part. Thus, for the subgroup whose cyclic 2-primary basis has been constructed without a factor exit, its 2-rank satisfies
\[
 \boxed{r\le r_*=\omega(k)+\mathbf1_{D\equiv1\bmod4}.}                \tag{2}
\]
Use any known upper bound on \(\omega(k)\) if k has not been factored. This argument uses the actual independent top elements of the cyclic basis, so no genus-character test or assumption of a small full class-group rank is needed.

## 2. Collision harvest after a partial exponent

Let G be the abelian subgroup generated by s supplied ideal classes \(g_i\), represented by compact states as in the earlier notes. Let H be a **known upper bound** on \(|G|\), for example \(H=8D+1\) for a single order. This is not a supplied annihilator. Choose any explicit positive integer E. Define the residual group and its actual size by
\[
 Q=G^E=\langle g_i^E\rangle,\qquad R=|Q|.
\]
R need not be known. We construct relations among the powered generators, using exact canonical class keys, rather than mixing reduced norms and factoring their rational residuals. The main cost will depend on R, not \(|G|\). Precompute the powers \(g_i^E\).

For a batch cap K choose a power of two T with \(T\ge128Ks(2H+1)\). Independently sample \(x\) uniformly from \(\{0,\ldots,T-1\}^s\), compute its key
\[
 q(x)=\prod_i (g_i^E)^{x_i}.
\]
Keep a dictionary of pending samples, with at most one pending word per class key. When a match is found, remove both words and retain their signed difference v. These collision pairs are disjoint, and their selection depends only on the class keys. Each yields the exact, publicly verifiable relation
\[
 \boxed{\beta_v=\prod_i g_i^{v_i},\qquad \beta_v^E=1.}              \tag{3}
\]
The word \(\beta_v\) is in the original group; only the collision test is in Q. Class arithmetic and explicit word storage have polynomial bit overhead. Class equality may be calculated on canonical keys; when a modular correction is required, recompute using compact guarded states. A proper gcd exit in such a computation is success. The proofs analyze abstract class keys without conditioning on the absence of a guard exit.

### Uniform collision bound

For each powered generator, the class of its exponent has period at most H. The distribution of a uniform exponent in \([0,T)\) modulo its period differs from uniform by total variation at most H/T. The product map from the cyclic generator groups onto Q has constant-size fibres. Coupling all s coordinates and K words therefore changes the entire key sequence from K independent uniforms on Q by total variation at most \(KsH/T\).

For t desired disjoint collision pairs, take an integer \(K\) divisible by 8 and
\[
 K\ge 8(t+\sqrt{tR}).
\]
In the ideal uniform law, until t matches have occurred, during the second half of the batch at least \(K/2-2(t-1)\ge K/4\) keys are pending. Thus the conditional next-match probability is at least \(K/(4R)\), or success has already occurred if this exceeds one. Extend the match process by dummy successes after reaching t. The probability of fewer than t matches is bounded by the lower-tail probability of a binomial variable with \(K/2\) trials and probability \(K/(4R)\). For completeness its mean is \(\mu=K^2/(8R)\ge8t\); Markov applied to \(2^{-X}\) bounds that probability by \(2^t(1-K/(8R))^{K/2}\le\exp(t\log2-\mu/2)\le e^{-3t}\). The coupling adds at most \(1/128\). The argument is uniform in the prior public data with the fixed group and independently sampled words. No distribution of smooth reduced norms has been used.

## 3. Construct a verified full annihilator when the residual group is modest

In the first s disjoint collision pairs, their signed difference vectors are rationally independent with probability at least \(1-s/\lfloor T/H\rfloor\), conditional on any key transcript with enough pairs.

To prove this claim, condition on all the class keys. The integer words are then independent over their own key fibres. Suppose previous disjoint differences span a proper rational subspace. Choose a nonzero linear functional vanishing on that subspace and a coordinate where it is nonzero. Condition on the second word of the new pair and all other coordinates of the first. Its remaining coordinate is uniform in one nonempty congruence class modulo the order of its powered generator, because its class key is fixed. The fibre has at least \(\lfloor T/H\rfloor\) members. At most one satisfies the prescribed linear equation. This proves the claim by the union bound, without assuming that integer collision differences themselves are uniformly distributed in a relation lattice.

Retain s independent rows v as a full-rank integer relation matrix V. Its row lattice is in the kernel of \(\mathbb Z^s\to Q\). Hence the largest positive Smith invariant factor d of V kills Q, since Q is a quotient of \(\mathbb Z^s/\operatorname{row}_{\mathbb Z}V\). In particular
\[
 \boxed{M=Ed,\qquad g_i^M=1\text{ for every }i.}                    \tag{4}
\]
The determinant \(|\det V|\) may replace d if desired. Verify the resulting annihilator on every original generator by exact class powering. This supplies an annihilator without computing \(|G|\), its invariant factors or the class number. Hadamard gives \(\log d\le s(\log T+\tfrac12\log s)\); Smith computation is polynomial bit time in the actual relation matrix.

A batch of size \(O(s+\sqrt{sR})\) therefore succeeds with probability bounded below by \(3/4\), with polynomial overhead in s, \(\log H,\log K,\log E\) and the class arithmetic data. The expensive class sampling step takes \(O(Ks\log T)\) group operations after precomputation. If R is unknown, double the cap until the verified result is obtained. With fresh batches, once the threshold is reached every conditional failure probability is at most \(1/4\); the geometrically increasing costs have summable expected tails (also with fixed polynomial factors in their logarithms). This gives an actual input-sensitive expected bound, not an algorithm assuming the value of R is supplied. A quarter-scale implementation caps this branch and rejects a failed epoch.

An alternative classical stage-two construction can use a bound J on each **individual** order of \(g_i^E\), even if their generated group Q is much larger than J. Use baby steps \(1,h,\ldots,h^{b-1}\), \(b=\lceil\sqrt J\rceil\), and giant steps \(h^{bj}\) for \(1\le j\le\lceil J/b\rceil\). A positive collision exponent \(bj-i\) is an annihilator of h. The true order at most J ensures such a collision (and an earlier baby-step duplicate already gives an order multiple). Verify each obtained exponent and take their lcm times E. This costs \(O(s\sqrt J)\) class operations, with polynomial bit overhead; it is the standard bounded-order baby-step/giant-step argument, not a new order-distribution theorem. It covers some large residual-group cases that do not meet the small-R condition. This optional branch has a direct proof here, but was not separately implemented in the tests below.

## 4. Only a few independent annihilated words are needed for factoring

Now require \(E\) to kill the full 2-primary part of G, which is ensured by taking its two-adic factor at least H as a number. The residual group Q is then odd-order. Suppose the s generators represent independently sealed squares \(s_i=h_i^2\) with verified compact state corrections. For clarity all s are sealed targets in this version. Auxiliary public generators could be included with their squares or with explicit known-square images, but are not needed for the following proof.

There is a stronger sampling law for the collision harvest:
\[
 (q(x),x\bmod2)\ \text{is within } 2sH/T
 \text{ of uniform on }Q\times\mathbb F_2^s.                       \tag{5}
\]
Indeed each coordinate now has period at most \(2H\) for this combined map. Since its group generator has odd order, adding that order changes only the desired parity bit. The product homomorphism therefore has image the full displayed direct product; uniform inputs in its coordinate cyclic groups give uniform outputs by constant fibres. This proves the claimed TV bound. It holds for a single fixed public target collection; no new target input density is used.

Under the ideal law, for disjoint collisions selected solely by class keys the differences \(v\bmod2\) are independent uniform binary vectors. For any \(j\le s\), after \(t=j+8\) such matches, the projections of these parities to their first j coordinates span \(\mathbb F_2^j\) except with probability at most \(2^{j-t}=2^{-8}\), by the union bound over nonzero linear functionals. With the collision estimate and the coupling of the combined law, we can retain j independent full parity vectors with probability at least \(3/4\) in a batch of size
\[
 O(j+1+\sqrt{(j+1)R}).
\]
Actual selection may retain any independent parity vectors and stop early; the analysis uses the hypothetical full capped stream. Adaptive doubling gives the same input-sensitive expected cost as in §3 with j in place of s in the sample-count bound.

For each retained v, form its actual compact guarded state \(\beta_v\) using (3). A negative exponent is implemented by conjugating the inverse ideal class and changing the public target/correction from \((u,c)\) to \((u^{-1},uc)\), preserving the same norm. The state target is \(u_v=\prod_i s_i^{v_i}\), and E is a verified annihilator **of the subgroup generated by these particular states**, irrespective of whether it annihilates any original generator.

Set \(j=r_*+1\), where \(r_*\) is the upper bound in (2), and assume \(s\ge j\). Apply the polynomial divisor-coordinate square readout of §1 to these j states with the supplied E. Either an ambiguous divisor yields a factor or their subgroup has 2-rank at most \(r_*\), so the readout constructs a class word w and a nonzero binary selection \(z\in\mathbb F_2^j\) satisfying
\[
 w^2=\prod_{a=1}^j\beta_{v_a}^{z_a}.
\]
The overall sealed coefficient vector \(x=\sum_a z_a v_a\) is nonzero modulo two, by the independence of the retained parities. Compose the states to verify equality of the reduced class keys and their minimum norms. If the state for w has public target u, and its squared state has correction \(c_w\), while the selected product state has correction \(c_x\), equality of the common minimum norm gives the explicit verified square root
\[
 (u c_w/c_x)^2=\prod_i s_i^{x_i}\pmod N.
\]
Compare with the private product \(\prod_i h_i^{x_i}\) only after this verification. At least one x_i is odd, so conditional on the public success transcript the ratio is uniform among the unit square roots of one. A proper factor occurs with probability at least \(1/2\) on odd inputs having at least two distinct prime divisors. No independence of the composite targets \(u_v\) is assumed: only the original sealed-root fibres and the binary independence of the harvested words are needed.

For \(k=1\) this theorem requires one independent parity vector when \(N\equiv3\bmod4\), or two when \(N\equiv1\bmod4\), in the absence of an earlier proper gcd. In particular a public E that kills **none** of the original target generators can still supply all the annihilated words needed for this readout. We need not construct (4) unless a full annihilator is itself desired.

## 5. Quarter-scale interpretation and the remaining arithmetic input

Put \(L=\log N,\ \Lambda=L^{1/4}(\log L)^{3/4}\). Take \(B=\exp(O(\Lambda))\) and H as above, and construct
\[
 E=2^{\lceil\log_2 H\rceil}
       \prod_{\substack{p\le B\\p\ {\rm odd\ prime}}}
                          p^{\lfloor\log H/\log p\rfloor}.
\]
Integer powers and the exponent product may be computed by exact integer comparisons and multiplication. Its bit length and construction work are \(\exp(O(\Lambda))\) when \(\log H=O(L)\). It kills the 2-primary and all B-small primary parts of G. The power map is an automorphism on each remaining primary part, so \(R=|G^E|\) is exactly the order of the product of the B-rough Sylow subgroups of G, not just the rough part of its exponent.

With a sufficiently small odd residual group \(R\le\exp(O(\Lambda))\), polynomially charged supplied generator/target data, and an adequate number of sealed targets, §3 or §4 has quarter-scale cost. This permits large B-smooth components without enumerating them, and modest nonsmooth components without requiring that E be a global annihilator. A condition on a selected subset of targets' generated residual group suffices; no corresponding condition on the whole class group is needed. The square-root dependence on R in the number of samples is meaningful compared with the earlier whole-subgroup dictionary. Alternatively the stage-two individual-order bound in §3 may suffice even for a large R.

This is not a proof of uniform quarter-scale order supply. The standard rigorous class-group computation of Hafner and McCurley has expected \(L[1/2,\sqrt2]\) time ([JAMS 1989](https://doi.org/10.1090/S0894-0347-1989-1002631-0)); the later conditional refinement has the same first L-parameter ([AIMS 2021](https://doi.org/10.3934/amc.2021055)). Neither supplies the required quarter-scale bound. We have not proved that the relevant residual group is small in any guaranteed choice of twists or initial packets. If R is exponentially large in L, the birthday cost can also be exponentially large. The supplied factored-packet initialization remains separate. These are precise conditions on the new arithmetic problem, rather than a heuristic assertion about smooth class orders.

## 6. Exact execution receipt

Run [verify_partial_annihilator.py](../verification/research/verify_partial_annihilator.py) in modes divisors, abstract, and class. All three modes were executed successfully locally with Python 3.13.5 and SymPy 1.14.0. The final committed Git blob a7d7206d03067234a177f1283d208c875a07ef22 matches the tested file (SHA-256 22e2ebd78774ef1841d12d9cc2e933292b39ee2d9361d5a8673e38f63ea28eaa). An initial committed formatting discrepancy in two wrapped print statements was corrected and the blob rechecked. The first attempt to start a streaming container run failed before creating the file; all actual tests used completed non-streaming calls.

- Exact order-two divisor encoding on 17 odd D values, including nonmaximal orders and nonsquarefree values: 85 ambiguous classes, all 1,241 ordered top products checked against their divisor-coordinate sums, and 790 full 2-primary coordinate checks. The D=255255 fixture has 32 elements of order dividing two. The proof does not depend on these enumerations.
- 100 abstract full annihilator constructions and 100 partial-annihilator square certificates; 92 fixtures have nontrivial residual powered groups. Total 7,929 sampled words. The abstract test uses independently enumerated small residual groups to set caps and a small abstract top-table oracle; the actual quadratic readout uses divisor coordinates. Every produced full annihilator is checked on all generators; every partial certificate has a verified odd original coefficient.
- Five quadratic fixtures use explicitly factored small public square representatives to create four input states each, a fixed cap of 1,600 words, and only the known class-number upper bound (no supplied class number or residual order). The deliberately incomplete exponent uses just powers of 2 and 3. Results:

| N | Original classes killed by E (out of 4) | Word draws | Disjoint matches used | Result |
|---:|---:|---:|---:|:---|
| 899 | 0 | 3 | 1 | verified factor 31 |
| 10403 | 1 | 3 | 1 | verified public root; trivial gcd 1 |
| 1022117 | 1 | 12 | 3 | proper public guard factor 1009 |
| 100160063 | 0 | 15 | 1 | verified public root; trivial gcd N |
| 1000036000099 | 0 | 323 | 1 | verified public root; trivial gcd 1 |

There were no preliminary initialization guard factors and no cap failures in these five fixtures. All four public square-root certificates were verified before accessing the original sealed roots. Only one of those four comparisons gave a proper gcd, as the table states; the separate public guard exit is another successful factor. The three trivial comparisons are not counted as successful factorizations. A single fixed-seed run is not an estimate of asymptotic relation density.

**Research decision.** The divisor readout and partial-annihilator harvest are exact constructive replacements for full class enumeration. The remaining substantive target is a uniform arithmetic procedure that produces relevant packet classes with a provably small residual powered subgroup, or bounded individual residual orders, or a more correlated relation supply avoiding generic birthdays. A general quarter-scale factoring theorem and a new complexity record are not established. No full repository, PDF or Lean rebuild was performed.
