# Uniform square masks on correlated conic sampling laws

27 November 2026. **Status:** exact unconditional correlated initialization and uniform-refresh theorem. It extends [the mask-bank coverage theorem](uniform_masked_anchor_supply.md) to a genuinely different class of raw sampling laws. The arithmetic core-rank and density hypothesis at quarter scale remains open. This note does not claim that a conic parametrization by itself supplies smooth or low-rank norms.

The previous masking law uses a uniform private unit h and its public square s. In a descent construction, it can be advantageous to reveal additional **correlated public data** having a known square-root correction. The hidden CRT signs must nevertheless remain independent, and refresh of an arbitrary target must reproduce the same *joint* public law, not just its square marginal. The following construction achieves both, without a modular square-root or factorization oracle.

## 1. Sampling a finite quadratic norm-one group

Let \(R=\mathbb Z/N\), N odd, and \(c\in R^\times\). Form the explicit rank-two R-algebra
\[
 A_c=R[T]/(T^2-c),\qquad \overline{x+yT}=x-yT.
\]
For \(x,y\in R\) write \(n(x,y)=x^2-cy^2\). The algebra element \(x+yT\) is a unit if and only if n is a unit: sufficiency follows from the displayed conjugate inverse, and necessity follows by taking the norm of an inverse. Its multiplication table is available without any knowledge of the factors of N.

Sample x,y uniformly and independently in R, conditioned on n being a unit (a proper gcd with N can terminate successfully). Compute
\[
 C=\frac{x^2+cy^2}{x^2-cy^2},\qquad
 D=\frac{2xy}{x^2-cy^2}.
 \tag{1}
\]
Then \(C+DT=(x+yT)/(x-yT)\) has norm one. In fact (1) is **exactly uniform** on the norm-one group
\[
 {\cal T}_c=\{C+DT:C^2-cD^2=1\}.
 \tag{2}
\]
Here is a proof over all odd moduli, including repeated prime powers.

By CRT it is enough to prove the group statement over \(\mathbb Z/p^a\). If c is a square modulo p, its unit square root lifts by the usual simple-root Hensel induction, so \(A_c\) is isomorphic to the product of two copies of \(\mathbb Z/p^a\), with conjugation interchanging them. The map \(u\mapsto u/\bar u\) is onto (2) in this case. If c is a nonsquare modulo p, the reduction is the field \(\mathbb F_{p^2}\), whose multiplicative norm is onto \(\mathbb F_p^\times\). Lift any prescribed residue-norm preimage to a unit in the algebra. The remaining discrepancy for a specified full unit norm belongs to \(1+p\mathbb Z/p^a\); it is a square there because this finite group has odd order. Multiplication by the corresponding base scalar corrects it, since the base scalar has norm its square. Thus the norm from \(A_c^\times\) to \(R^\times\) is surjective also in the nonsplit case. The homomorphism \(u\mapsto u/\bar u\) has kernel exactly the fixed units \(R^\times\) (2 is invertible). Its image is contained in the norm-one kernel and has the same cardinality, by norm surjectivity. This proves it is onto. Uniform input on the finite unit group therefore gives uniform output, locally and globally. This proof uses finite field cyclicity and elementary Hensel lifting only to establish the law; the program performs (1), not local factorization.

The unit sampling has polynomial expected bit cost in \(\log N\). Indeed at each prime p the forbidden norm-zero pairs are one pair in the nonsplit case, and the union of two lines (2p-1 pairs) in the split case. Hence
\[
 \Pr(n(x,y)\text{ unit})\ge
          \prod_{p\mid N}(1-1/p)^2\ge(\omega(N)+1)^{-2}.
\]
The last bound uses the increasing prime ordering \(p_j\ge j+1\). Exact uniform residue draws and capped rejection can be implemented with polynomial overhead. Gcd exits only improve the algorithm. The distributional arguments below refer to the ideal unit-conditioned sampler; an actual capped version is coupled to it, with cap failures charged separately.

## 2. A correlated sealed-root initialization

Fix public units \(\kappa,q\in R^\times\) and one known pair \((h_0,z_0)\) satisfying \(z_0^2-\kappa h_0^2=q\). The pair need not have unit h0. For example q=1 and \((h_0,z_0)=(0,1)\) works for every κ. The conic
\[
 {\cal C}_{\kappa,q}=\{(h,z)\in R^2:z^2-\kappa h^2=q\}
\]
is the norm-q fibre in \(A_\kappa\). Since q is a unit, every point represents a unit. Multiplication by a uniform element of \({\cal T}_\kappa\) acts simply transitively on this fibre, using the given basepoint. Thus (1) constructs a uniform point, without factoring N.

The initialization samples such a point privately, requires h a unit, and reveals only
\[
 s=h^2,\qquad z,\qquad z^2-\kappa s=q .
 \tag{3}
\]
A proper gcd from h is success, a zero/nonunit failure can be rejected. Further acceptance tests may be arbitrary public predicates of (s,z) and independent public data. For any accepted public pair, the remaining possible h's are exactly all the unit square roots of s: every such root with the fixed z is a point of the same conic. Uniform point sampling therefore gives the uniform root fibre conditional on the public pair. Independent samples have independent private sign fibres after conditioning on their public pairs and any further public-only selection. This is precisely the symmetry needed by the previous certificate, not an assertion that the marginal distribution of s is the uniform square group.

If all prime divisors of N are large, the unit guard has high acceptance probability: reduction of the uniform norm-q fibre modulo p is uniform on the finite-field norm fibre (surjectivity follows from the same unit-ratio sampling and lifting). At most two of its \(p-(\kappa/p)\) points have h=0. Thus the total nonunit-h probability is at most \(\sum_{p\mid N}2/(p-1)\); the same estimate holds for z if it is required to be a unit. For smaller exceptional moduli, keep these tests as raw failures or verified gcd exits rather than assuming positive accepted density.

The companion z is valuable public information: for example with q=1, κ=-1 we have \(1-s=z^2\) with an explicitly known root, and with κ=q=1 we have \(1+s=z^2\). Public identities involving those companions may be used as known-square anchors. Their actual rational/algebraic representation costs must still be charged. Sampling a root by a procedure that publishes its choice of sign, or retaining the private parametrizing u in the public row, would invalidate the fibre argument.

## 3. Exact refresh of a fixed correlated target

Given **any** valid public pair \((s,z)\) from (3) with s a unit, one can generate a fresh pair with exactly the original conic law and a known square multiplier, without using a private root of s.

Use (1) with \(c=\kappa s\) to obtain uniform \((C,D)\) in \({\cal T}_{\kappa s}\). Define the public quantities
\[
 a=C+Dz,\qquad z'=Cz+\kappa sD,\qquad s'=s a^2 .
 \tag{4}
\]
They satisfy \(z'^2-\kappa s'=q\). If a is not a unit, perform the same gcd/rejection test as for a nonunit h in the initialization. All arithmetic in (4) is public and polynomial bit cost apart from the already charged rejection.

**Uniform refresh theorem.** Conditional on any fixed starting public pair satisfying the guards, and on any earlier public history, the new private point \((ha,z')\) is uniform on the original norm-q fibre, where h is *any* unit square root of s. After the same unit and public acceptance tests, the refreshed public pair has exactly the original accepted law. The multiplier a for its square image is explicitly known.

Proof. The map \(A_{\kappa s}\to A_\kappa\) sending its generator T to \(hT\) is an algebra isomorphism, since \(h^2=s\) and h is a unit. It preserves conjugation and norm. Consequently \(C+hDT\) is uniform on \({\cal T}_\kappa\) for every fixed choice of h. The norm-q point \(z+hT\) is a unit, and
\[
 (z+hT)(C+hDT)= (Cz+\kappa sD)+h(C+Dz)T.
\]
Multiplication by this fixed norm-q point is a bijection from the norm-one group to the norm-q fibre. This proves uniformity. Equation (4) is exactly the square-mask relation for the public images. The point-level statement is independent of which h was selected; no h is used by the program. Unit tests on a coincide with unit tests on ha, and all other stated acceptance tests are public. End proof.

In particular the law holds **jointly for the square and its public companion**, which ordinary uniform square masking would not preserve. It holds at nonsplit auxiliary tori and at prime powers. For the split case κ=1 one can alternatively verify the law directly by the bijection \(u=z+h\in R^\times\), \(z=(u+q/u)/2,\ h=(u-q/u)/2\); the quadratic-algebra argument treats both cases uniformly.

## 4. Consequence for correlated anchor batches

Fix the public environment and a capped square-only representation sampler which now receives the **public pair (s,z)** in (3) and independent public coins. It does not receive h, the conic sampling parameter, or a choice of private sign. Suppose that its raw conic-public output law has a core of mass \(p\) and a lattice novelty budget M as in [the mask-bank theorem](uniform_masked_anchor_supply.md), or binary rank R for the [actual-generator square presentation](square_resultant_norm_transport.md).

Prepare the unsealed bank using independent uniform conic points, knowing their h's privately as public correction data only after the sampler has produced its row. All sample representations have known square roots for their evaluations, as before. By the same coverage theorem, a bank with \(m+1\ge2M/(\delta p)\) covers raw output mass at least p/2 except with probability δ. This does not require the success set or core to have good mass in the marginal law of s alone.

For a missing old sealed parity with its public pair (s,z), refresh by (4) and feed only (s',z') to the fixed sampler. If the refreshed representation is covered by the bank's integer span, the row ratio gives a known-square anchor with root a and active vector \(v'-v\). Exactly the same argument as equation (6) of the mask-bank theorem shows strict gain in the old integer parity criterion. For the binary presentation use \(v'+v\) and its binary quotient. The conditional gain-or-factor probability is at least p/2 on the good bank, **uniformly for every old target public pair and history**. There is no separate per-target descent incidence estimate. Use the same terminal/log rank guard as before if one is needed. Under full-group or binary generator membership one can directly return a known square root of s and compare it with the original sealed root.

A single shared list of public torus-sampling coins and representation coins can be chosen to work simultaneously for all public pairs. For each fixed pair the fresh trials have the same coverage probability. There are at most \(N^2\) possible pairs; use a union bound and \(O((\log N+\log(1/\eta))/p)\) trials, including sufficient caps for the norm-unit rejection. The list can be reused without assuming the initial pair is independent of the list: the success event is simultaneous. This is the exact analogue of the previous reusable mask bank for the new joint law.

The same construction works for a fixed number of independent conic points with specified common or separate public parameters. Refresh their coordinates independently. Their joint product law is restored exactly, and any additional **publicly tested** correlation of the resulting tuples can be included in the raw sampler's success event. It can be a rare event, provided its actual mass is charged. For a fixed exponent pattern, the product of the selected square images is masked by the square of the corresponding known product of the a's; this permits batch anchors for such a product. A union bound over all public input tuples costs a factor of the number of coordinates in the logarithmic bank length, not an exponential in that number. This claim does not say that an arbitrary change of public conic parameters or exponent pattern preserves a fixed core law or rank budget. Those are part of the environment.

Thus the sufficient quarter-scale arithmetic target has been enlarged from a uniform-square core to a **correlated-public-law** core, with a proof of the required uniform adaptive refresh. All the previous complexity and restart accounting carries over if p inverse, M (or binary rank), actual data size, and per-trial cost are at the quarter scale. There is no hidden conditional distribution of the child requests in this uniformity claim.

## 5. Boundary and research direction

This correlated initialization gives exact known-square companions and full private sign symmetry without a random smoothness claim. It does not itself make the norm supports small. For balanced squarefree semiprimes, for example, each public square value s can have at most four possible companions z when \(\kappa s+q\) is a unit, and at most four even when that value has zero components (at most two roots in each finite field). Each s has at most four private unit roots. Meanwhile the full conic has \(\prod_{p\mid N}(p-(\kappa/p))\asymp N\) points by the finite-field norm count, and removing nonunit h or z removes only \(O(p_1+p_2)\) points in the balanced two-prime case. Thus the square marginal is still bounded by \(O(1/N)\) under these ordinary guards. The earlier uniform support barrier cannot be evaded simply by asserting a dramatically concentrated square marginal. More restrictive public conditioning must pay for its actual density.

What is new is the ability to seek relations that use z as a known square-root companion, and to refresh a whole correlated incidence block uniformly while retaining a verified known-square mask. This allows arithmetic searches based on such identities as \(1-s=z^2\) and \(s+1=z^2\), without invalidating the sealed-root extraction. The next concrete target is a low binary-rank core for one such fixed structured law, using square-resultant norm transport or another explicit public generator representation. We have not proved that core or a smaller general factoring exponent. The simple conic refresh cannot replace a required arithmetic representation algorithm; it only removes its separate adaptive masking and anchor-supply problem.

## 6. Exact verification

The [standalone script and receipt](../verification/research/README.md#uniform-masked-anchors-and-affine-core-collision-supply) verify 212 exact norm-one group laws on seven small odd composite moduli, including nonsplit and prime-power components. All 1,264 tested target/private-root cases refresh onto their entire norm fibre with equal multiplicity, for 101,152 exact point transitions. The test independently enumerates the private sign fibres and compares the output support with the full conic, not just its cardinality. A refreshed hidden root is a known mask times the old root; it is **not** to be treated as another independent sealed root. Use the refreshed representation for an unsealed correction or anchor, as in §4.
