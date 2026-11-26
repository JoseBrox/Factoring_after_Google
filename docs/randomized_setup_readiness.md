# Setup sampler and global readiness assembly

**Status:** written assembly of the enlarged distribution and readiness
argument (C1) from the QRH weighted AP estimates, the root smoothing,
local-moment and fibre notes, and the explicitly identified classical
LLL/reduced-basis and homogeneous-form convolution results. The actual
Lean finite sampler, tree and arithmetic-machine implementation have
not been certified. This does not establish C2–C5 or the full randomized
complexity theorem.

Use the randomized manuscript's exact parameters, in particular
\(d=(1/2+o(1))U,\ G=e^{(43/8+o(1))\Xi}\),
\(W=e^{(8+o(1))\Xi}\), \(W_{\rm cut}=\lceil We^{-\widehat\Xi}\rceil\),
\(\Lambda_0=\lceil32\widehat\Lambda\rceil\).
The polynomial lattice and its affine coset are those of the manuscript.
We use the short-tile bound proved in
[the fibre-coupling note](randomized_fibre_coupling.md), with no
evaluation constraints and no auxiliary q-condition. Its tile radius
is at most \(\eta=(d+1)2^{(d+3)/2}G\) rounded upwards.
Thus
\[
 \eta/W_{\rm cut}\le e^{-(13/8+o(1))\Xi},
 \qquad (d-J-4)\log G=(43/16+o(1))L>L .
 \tag{1}
\]
These are the only enlarged scale comparisons needed for the
polynomial sampler.

## 1. Exact box mixture and finite approximation

Put \(\alpha=\Lambda_0/W,\ \zeta=e^{-\alpha}\).
For integers \(R\in[W_{\rm cut},W]\) let
\(\pi(R)=\zeta^R-\zeta^{R+1}\) for \(R<W\),
and \(\pi(W)=\zeta^W\).
Set \(Z_1=\sum_R(2R+1)\pi(R)\) and
\(Q(R)=(2R+1)\pi(R)/Z_1\).
If one samples a radius with law Q and then a uniform integer
in its centered interval, the mass of \(c\in[-W,W]\) is
\(\zeta^{\max(|c|,W_{\rm cut})}/Z_1\), by telescoping.
The ratio of the unnormalized truncated-layer weight to the
desired \(\zeta^{|c|}\) is between \(e^{-\alpha W_{\rm cut}}\) and 1.
In \(d+1\) independent coordinates this ratio differs from 1 by
\(O((d+1)\alpha W_{\rm cut})=e^{-(1+o(1))\Xi}\).
The same relative comparison persists after restricting to the
affine mod-N lattice and normalizing.

For the finite implementation use the source's dyadic approximation
\(\widehat\zeta\) with error at most \(2^{-P}\),
\(P=\lceil8\widehat{\log M}\rceil\).
Since \(8\log 2>5\), this is at most \(W^{-5}\) eventually.
Uniformly for \(R\le W\),
\(\widehat\zeta^R/\zeta^R=1+O(W^{-4})\), and
\((1-\widehat\zeta)/(1-\zeta)=1+O(W^{-4})\)
because \(1-\zeta\asymp\Lambda_0/W\).
Thus the exact radius law formed from \(\widehat\zeta\)
has pointwise relative error \(O(W^{-4})\).
Its cumulative unnormalized tail from a to W is the finite geometric
identity
\[
 \sum_{R=a}^W(2R+1)\widehat\pi(R)
 =(2a+1)\widehat\zeta^a+
       2(\widehat\zeta^{a+1}-\widehat\zeta^{W+1})/(1-\widehat\zeta).
\]
In particular cumulative probabilities can be evaluated without
enumerating W radii, using repeated squaring and controlled rational
interval arithmetic as in the source sampler.
Each positive radius probability is at least \(W^{-3}\) eventually:
\(Z_1\le 2W+1\) since the total \(\pi\)-mass is at most 1, while
\(\widehat\zeta^W=e^{-(32+o(1))\Lambda}\gg W^{-1/2}\) and
\(1-\widehat\zeta\gg W^{-1}\).
Evaluation to error \(2^{-5P}\), then rounding to the
\(2^{-4P}\)-grid, preserves monotonicity because consecutive
tails differ by much more than the rounding error.
The resulting radius masses have relative error \(O(W^{-2})\),
uniformly, and binary search using \(4P\) fair bits samples
that dyadic law exactly. This is the finite source construction,
not enumeration of exponentially many radii. An implementation-level
bit proof of the interval arithmetic remains required.

## 2. Lattice points in the sampled box

For each vector of radii \(\boldsymbol R\), all at least \(W_{\rm cut}\),
write \(B_{\boldsymbol R}=\prod_i[-R_i,R_i]\cap\mathbb Z^{d+1}\).
The lattice has index N. Every half-open fundamental tile contains
exactly N integer points, since it contains exactly one representative
of each quotient coset. Compare the union of tiles centered in
\(B_{\boldsymbol R}\) with its coordinatewise inner/outer
\(\eta\)-neighborhoods. Counting these integer boxes and using (1)
gives uniformly
\[
 \#(\widetilde{\mathcal L}_N\cap B_{\boldsymbol R})
 = N^{-1}\prod_i(2R_i+1)
    (1+O((d+1)(\eta+1)/W_{\rm cut})).
 \tag{2}
\]
An exact uniform draw from the lattice-box intersection is obtained by
drawing a uniform integer point in the expanded box of radii \(R_i+\eta\)
and mapping it to its unique tile center by rational basis coordinates.
Accept precisely when that center lies in the sampled box. Every accepted
center has exactly N preimages in the expanded box, so the law is
uniform. Equation (2) gives acceptance probability \(1-o(1)>3/4\)
uniformly. The basis reduction and tile-coordinate computation are
the source's exact LLL and integer matrix algorithms.

With the prescribed polynomial proposal cap, the box rejection
failure is \(e^{-\Omega(L^2)}\). Each auxiliary finite uniform integer
draw can be implemented by rejection from the next power-of-two range,
so its own cap gives the same exponential bound, even after the
polynomial number of draws in the setup. The output law can be coupled
to the uncapped sampler with disagreement \(e^{-\Omega(L^2)}\).
One must account for cap failure as a failure outcome, rather than
silently conditioning away its probability.

Combining (2) with the product radius law, the mass at an allowed
lattice point is proportional to
\(\prod_i\widehat\zeta^{\max(|c_i|,W_{\rm cut})}\)
up to a uniform relative error
\[
 O((d+1)W^{-2}+(d+1)(\eta+1)/W_{\rm cut})
 = e^{-(13/8+o(1))\Xi}+O((d+1)W^{-2}).
\]
The layer truncation has the larger relative error
\(e^{-(1+o(1))\Xi}\). Consequently the total variation error of the
capped polynomial sampler (including its failure mass) relative to
\(P_{\rm Lap}\) is at most \(e^{-\Xi/2}\) eventually, as required.
This is a quantitative transfer of the source sampler to the enlarged
parameters; it still uses its classical LLL and finite-precision
arithmetic algorithms rather than a fully formal machine model.

## 3. Core and sup-norm tails

Under the unconditioned product law \(P_0\), each coordinate satisfies
\(\mathbb E e^{\alpha|c_i|/2}\le2.1\) eventually by the
truncated geometric sum formula. Thus
\[
 P_0(\|c\|_1>.24W)\le e^{-.12\Lambda_0}2.1^{d+1}
            = e^{-(3.84+o(1))\Lambda},\qquad
 P_0(\|c\|_\infty>W/2)\le C(d+1)e^{-\Lambda_0/2}.
\]
Use the same tile comparison as in Section 2, now weighting each point
by \(w(c)=e^{-\alpha\|c\|_1}\). On interior tiles the weight varies
by a relative \(O(\alpha(d+1)\eta)=e^{-\Omega(\Xi)}\);
boundary tiles all have sup norm at least \(W-2\eta\).
Their total weight is negligible relative to the unconditioned mass
\(Z_0\ge (W/\Lambda_0)^{d+1}\) (up to a constant to the power \(d+1\),
obtained from the central coordinate interval). In fact the ratio
is bounded by \((C\Lambda_0)^{d+1}e^{-(32+o(1))\Lambda}
=e^{-(31+o(1))\Lambda}\).
The same estimate bounds the lattice boundary mass multiplied by N,
by counting complete tiles of N integer points.
Thus the normalizers have ratio
\(NZ_{\rm Lap}/Z_0=1+o(1)\).
An interior tile whose center has l1 norm greater than W/4 has all
points of l1 norm greater than .24W, by (1).
A tile whose center has sup norm greater than 5W/8 has all points
of sup norm greater than W/2. The preceding comparison gives
\[
 P_{\rm Lap}(\|c\|_1>W/4)\le e^{-2.5\Lambda},
 \qquad
 P_{\rm Lap}(\|c\|_\infty>5W/8)\le e^{-5\Lambda}.
 \tag{3}
\]
These estimates include the exponentially small boundary corrections.

## 4. Setup algebraic checks and rare divisibilities

The affine coefficient relation forces \(f(g_0,g_1)=0\bmod N\)
by construction. The leading coefficient is \(1\bmod3\), and
the reduction of \(f(X,1)\) equals the chosen irreducible \(h_0\)
of degree d. Gauss's lemma therefore gives irreducibility over
\(\mathbb Q\); any possible content is not divisible by 3 and
any nontrivial factorization over Q would reduce to a
positive-degree factorization modulo 3. For a primitive \((a,b)\),
\(3\nmid f(a,b)\): if \(3\nmid b\), reduce to a root of \(h_0\),
and otherwise use \(3\nmid a\) and the leading term.
The coefficient bounds
\(M+1\le c_d\le M+6W+1\) and
\(|c_i|\le3W+2\) for \(i<d\) give the printed archimedean bounds,
since \(b/a\le1/3\) and
\(\sum_{i<d}(b/a)^{d-i}\le1/2\).
A monic irreducible degree-d polynomial over \(\mathbb F_3\)
can be found by enumerating the \(3^d\) monic candidates with
an exact finite-field irreducibility test, by the standard existence
theorem; \(3^d=e^{o(\Lambda)}\).
The finite search and its machine costs are distinct from the
probabilistic setup argument.

Put \(V_0=\lfloor W/(32(d+1)\Lambda_0 G)\rfloor\);
\(\log V_0=(21/8+o(1))\Xi\) so \(V_0\gg B\).
For every prime \(p>B\) not dividing \(3g_0g_1\),
shifting f by \(3(g_1X-g_0Y)v X^{d-1}\) with uniform
integer \(v\in[-V_0,V_0]\) preserves its affine mod-N lattice
and changes the leading coefficient by \(3g_1v\).
The shift satisfies the translation inequality of the fibre note
with \(\epsilon_{\rm lip}\le1/16\) and tail \(e^{-5\Lambda}\)
by (3). Its modular step is invertible, so the shifted
coefficient is divisible by p with probability at most
\(1/p+1/(2V_0+1)\le2/B\).
The *lower* translation bound applied to that event yields
\(P_{\rm Lap}(p\mid c_d)=O(e^{-5\Lambda})\).

For the derivative, with
\(\widetilde f(X)=c_d^{d-1}f(X/c_d,1)\) and
\(m_N=g_0g_1^{-1}\bmod N\), direct coefficient differentiation gives
\[
 g_1^{d-1}\widetilde f'(c_dm_N)
 \equiv c_d^{d-2}\partial_X f(g_0,g_1)\pmod N.
\]
The analogous shift \(3(g_1X-g_0Y)vY^{d-1}\)
leaves \(c_d\) unchanged and adds \(3g_1^d v\) to the right-hand
derivative factor. For every \(p\mid N\) it is a unit step.
The same argument bounds the unwanted derivative divisibility,
when \(p\nmid c_d\), by \(O(e^{-5\Lambda})\).
A union bound over \(O(L)\) divisors of N and both forms gives
failure probability o(1) for the required gcd checks.
For the root primes, the expected fraction dividing either leading
coefficient is \(O(e^{-5\Lambda})\), and Markov excludes an o(1)
fraction except with probability o(1).

## 5. Readiness assembled with actual history guards

The [rational-root smoothing](randomized_rational_root_smoothing.md)
gives at least \(4/5\) of the allowed root primes rationally good
for a \(1-o(1)\) fraction of base pairs.
Fix such a pair and draw the two polynomial coefficient vectors.
The [conditional local moments](randomized_local_moments.md)
give for each exact valid history meeting the core the required
mean, concentration, pointwise expectation and bad-child bounds.
At a root the corresponding statement is for the single active
algebraic weight on its rationally good set.

Here are the consequences for the actual descent, rather than
an unweighted branching process. At a locally good node the
probability of acceptance of a uniform box point is at least
\(\mu/(2\#\mathcal B_q\cap\Lambda_{q,r})\). Multiplying by the
printed proposal cap gives at least a constant times \(L^3\)
times \(e^{.04\Lambda}\) at an algebraic node, and
\(L^3e^{.05\Lambda}\) at a root (up to negligible rounding errors).
Thus trial exhaustion has probability \(e^{-\Omega(L^2)}\)
on local goodness. The exact lattice-box sampler's own cap
and the caps on its auxiliary draws also have exponentially
small failure; even a union over the at most \(e^{O(\Lambda+\ell^2)}\)
draws in a tree leaves \(e^{-\Omega(L^2)}\).
Conditioned on acceptance before caps, the selected point has
probability at most \(2X_a/\mu\), by the uniform proposal law
and acceptance proportional to its exact weight.
Since the exceptional conductor set is empty, the clean
lattice set equals the algorithmically guarded primitive set
in the local-moment proof, once the eventual size guards hold.
There is no extra conductor computation or rejection.

The actual descendant size bounds in the manuscript show that
all form values, rational quotients and ancestor determinants
submitted to Factor are smaller than \(\sqrt N/2\) eventually.
The trivial factorization for value 1 is handled separately.
For a fixed valid history, the exact subroutine factorization
is correct independently of its running time; the deterministic
background trial division ensures termination on every coin tape.
Thus the distribution analysis does not presuppose a cheap
smoothness oracle. On accepted points avoiding the bad-child
event, every candidate child has \(p\nmid b\), is non-skewed
and is outside the exceptional set. Its residue is \(ab^{-1}\bmod p\)
and it satisfies the required polynomial root congruence.
The forbidden integer in the local bad-child estimate contains
the prior ancestor determinants, values and current differences;
hence the candidate child's required cross-value and
ancestor-determinant nondivisibilities follow. Cross-field primes
of the current point are also excluded by the same estimate.
The algorithm may skip children dividing the leading coefficient;
relaxing this skip for the upper bound on the set of possible
failure paths is harmless, since the local conditional moment
theorem uses only the root congruence and the recorded history,
not nondivisibility of that coefficient.

For a root's cross-value guard use the extra elementary shift
on the second form, \(3(g_1X-g_0Y)vY^{d-1}\).
For a root candidate child \(p>B\) of the first form that does
not already trigger the bad-child event, \(p\nmid b\).
Also \(p\nmid ag_1-bg_0=q n_{\rm rat}\) because \(n_{\rm rat}\)
is B-smooth and \(p<q\). The evaluation step is therefore a unit
modulo p. Conditional on the first form and the chosen point,
the second form is still independent under the unconditioned
root sampling, so (3) and the translation bound give
probability \(O(e^{-5\Lambda})\) of that unwanted divisibility
for each such child. The conditional weighting by root selection
is charged as in the local moment proof, and the number of
candidate children is at most \(\log_2 N\).

At each local step the resulting error on a valid slice is at
most \(e^{-24\ell^2}\) eventually, using the local concentration,
bad-child estimates, timeouts and the rare root cross-value event.
Apply the weighted backward argument in the fibre note: reveal
only the exact ancestor evaluations at a fixed history, pull
the measurable selection weight \(2X_a/\mu\) out of the next
conditional expectation, and sum over at most \(\log_2 N\)
candidate children. The local expectation sum of those weights
is at most 3. Core-nonemptiness is monotone on history extension.
This bounds failure at depth r along otherwise valid histories
by \((3\log_2 N)^r e^{-24\ell^2}\), without assuming independence
of visited nodes or conditioning on the adaptively chosen path.
As \(r_{\max}\le .65\ell\), their sum is \(O(e^{-23\ell^2})\).
Now use Markov at \(L^{-2}\) for the fresh-tree failure probability
with the tuple held fixed, and Markov over the fraction of
unsuccessful root primes. Add (3), the gcd/derivative failure
probabilities, the leading-coefficient exclusions, and the
sampler TV errors for both forms.
With probability \(1-o(1)\) the tuple has all exact setup checks
and at least \(3/4\) of its allowed root primes with fresh-tree
success probability at least \(1-L^{-2}\).
This is stronger than the printed probability \(3/4\) for
setup and uniform readiness, under the stated mathematical inputs.

## 6. Scope

The written C1 argument is assembled from the cited notes and
classical inputs. In particular the fixed zero-free strip is used
quantitatively through the weighted AP proof, not merely as a
zero-location assumption. The finite weighted backward inequalities,
the underlying exact character moment, modular arithmetic and
various lattice components are already separately formalized.
The full formal transfer must still define the actual sampler,
conditional laws and adaptive tree and prove all of their guards,
including the primitive-count and convolution lemmas. C2–C5
(ideal parity/obstruction dimension, character certification,
square extraction, and uniform bit-machine bounds) remain separate
obligations. The original conditional theorem is not promoted
to an unconditional end-to-end Lean result.
