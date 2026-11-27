# Square-target lattices and factor-free parity pooling

**Status (27 November 2026):** proved exact parity-only span
membership and extraction, square-preserving lattice balancing,
and a sparsity obstruction to relying on two-ratio collisions.
New finite searches split both inputs on which earlier greedy
rank and primary-readout searches stalled. Uniform deterministic
half-scale coverage is **not** proved. No new Lean milestone
is counted; one-third work remains deferred.

This continues [primary pooling](primary_pool_extraction.md) and
[residual support budgets](support_budget_and_two_saturation.md).
Instead of requiring an integer or rational dependence of all
prime valuations, retain squareclasses together with explicitly
known modular square roots. This allows the usual square
congruence extraction without either factoring the residuals
or computing full integer relation rank.

## 1. Square-preserving balancing

Let \(N\) be odd, \(t\) a known unit modulo \(N\), and take
\(a=t^2\bmod N\). For all sufficiently large \(N\) put
\[
 h=\lfloor\sqrt{(N-1)/5}\rfloor,\qquad
 J=\min\{j\ge0:4^j>h^2\},\qquad
 S=\lfloor\sqrt N\rfloor+1.
\]
At least one shifted multiplier \(4^j a\), \(0\le j\le J\),
has no nonzero lattice vector in \([-h,h]^2\).

Indeed, if every shift had a short vector \((x_j,y_j)\),
orient it with positive first coordinate. Both coordinates
are nonzero because \(h<N\) and the multipliers are units.
The congruence
\[
 y_{j+1}x_j-4y_jx_{j+1}\equiv0\pmod N
\]
is an integer identity, since its absolute value is at most
\(5h^2<N\). The rational slopes therefore increase in
absolute value by a factor of four per step, contradicting
the height bound at the two endpoints, as \(4^J>h^2\).

Exact floor-sum counting identifies a good shift in polynomial
bit time. The argument of
[dyadic balancing](power_shift_pooled_relations.md)
then constructs a primitive shortest vector of sup norm
between \(h+1\) and \(S\), or a proper factor. Its companion
basis vector can be chosen with sup norm at most
\(N/(h+1)+S/2<4S\). The basis determinant is exactly \(N\).
Thus in a sufficiently enlarged box there are many
primitive candidates, not just multiples on one line.
Every candidate retains an explicitly known modular root:
\[
 y\equiv (2^j t)^2 x\pmod N.
\]
For \(H\le\sqrt N B^C<N\) with fixed \(C\), enumeration of
all primitive pairs at all these shifts costs
\(\operatorname{poly}(\log N)(1+H^2/N)(J+1)\),
by [the primitive lattice theorem](primitive_ratio_lattice_aggregation.md).
A nonunit coordinate produces a proper gcd. This theorem
does not assert smoothness or a useful parity dependency.

More generally root shifts by any fixed unit integer \(d\)
give multiplier shifts by \(d^2\). Use
\((d^2+1)h^2<N\) in the same proof. In particular \(d=4\)
preserves the Jacobi sign of the known root.

## 2. Exact squareclass membership without factoring

The squareclass of a nonzero signed rational number means
its class in \(\mathbb Q^\times/\mathbb Q^{\times2}\),
including its sign coordinate. Its other coordinates are
true prime valuations modulo two.

Let \(d_1,\ldots,d_s>1\) be pairwise coprime nonsquare
integers. They need not be prime, squarefree, or factored.
Their squareclasses are independent: their prime supports
are disjoint and each has a nonzero odd-valuation vector.

For a candidate \(r=x/y\), \(y>0\), put \(Z=|x|y\).
For each \(d_i\), compute the part \(Z_i\) of the remaining
integer supported on \(d_i\), by repeatedly dividing out
the gcd with \(d_i\). This strips the full prime-power
part without knowing the primes. Let \(Z_0\) be the
remaining integer after all these steps.

**Theorem 1.** The squareclass of \(r\) belongs to the span
of \(-1,d_1,\ldots,d_s\) exactly when \(Z_0\) is a square
and, for each \(i\), either \(Z_i\) or \(Z_i d_i\) is a square.
In the first case the coefficient of \(d_i\) is zero, in
the second it is one. The two cases are mutually exclusive.
The coefficient of \(-1\) is the sign of \(r\).

Proof: on the disjoint support of \(d_i\), the odd valuation
vector of \(Z_i\) must be zero or equal to that of \(d_i\).
The square tests express precisely these conditions, and
the test outside the basis handles all new primes. The
squareclass of \(Z\) equals that of \(|x/y|\) since
\(Z/(|x|/y)=y^2\). This proves necessity and sufficiency.
All tests are exact integer gcds, divisions and square roots,
of polynomial bit cost. End proof.

Given the coordinates, binary elimination tests membership
in an arbitrary old squareclass span. This is strictly
weaker than rational valuation-span membership: new prime
factors of even valuation do not prevent acceptance.

### Incremental parity-only basis refinement

There is also an exact batch procedure, faster in the
finite experiments than repeated global gcd refinement.
Maintain disjoint nonsquare integers with bit masks of
the previously processed rows in which their odd exponent
occurs. When processing a new integer factor \(z\) of row
\(i\), strip its part \(u\) supported on each old base \(d\).
If \(u\) is square, it contributes nothing. If \(ud\) is
square, toggle the corresponding row bit on \(d\).
Otherwise refine just the two integers \(u,d\) by the
ordinary gcd-free algorithm. Replace the old mask and new
bit according to the exact exponent parities in the
refinement. Discard square basis elements and zero masks.
Any remaining nonsquare part of \(z\), coprime to the
retained bases, becomes a new basis element. Handle the
numerator and denominator with the same row bit, since
the minus sign of the denominator valuation disappears
modulo two. Record the rational sign separately.

Induction shows that the parity vector of every processed
ratio is unchanged in the true-prime squareclass space.
The tests and local refinement make this true even if a
new value splits a previously composite basis element.
Dropping a zero mask is safe: that support has zero
contribution to all processed parity vectors. Any later
odd contribution can be introduced afresh. The bases
remain pairwise coprime and nonsquare, so their abstract
coordinates embed injectively in the true space. Each
base is a divisor of an input integer, and their number
is at most the total input bit length. Consequently the
procedure and binary elimination have polynomial bit
cost in the total list description. No prime factorization
or squarefree-kernel oracle is needed.

## 3. Complete first-level parity extraction

Take any list of verified unit congruences
\[
 r_i=y_i/x_i\equiv t_i^2\pmod N,
 \quad x_i>0,\ y_i\ne0,\quad
 \gcd(x_i y_i t_i,N)=1 ,
\]
where the \(t_i\) are known. Let \(K\) be the binary kernel
of the signed rational squareclass matrix of the \(r_i\).
For \(c\in K\), use its zero-one representative and put
\[
 R(c)=\prod_i r_i^{c_i},\qquad
 u(c)=\sqrt{R(c)}\in\mathbb Q_{>0},\qquad
 z(c)=u(c)\left(\prod_i t_i^{c_i}\right)^{-1}\pmod N.
\]
The product is a positive rational square, so its
positive square root is recovered by exact integer square
roots of the reduced numerator and denominator. All
denominators are units. The element \(z(c)\) satisfies
\(z(c)^2=1\). If it is not \(1\) or \(-1\), its gcd
with one subtracted gives a proper divisor.

**Theorem 2.** It is sufficient to test a binary basis of
\(K\). This finds a factor whenever any first-level
squareclass dependency gives a nontrivial involution.
If no factor is found, the entire checked list can be
compressed to a squareclass-independent sublist without
losing any such extraction from future rows.

Proof. For binary dependencies \(c,d\), the products of
their positive rational square roots satisfy
\[
 u(c)u(d)=u(c+d\bmod 2)
            \prod_{i:c_i=d_i=1}|r_i|.
\]
After dividing by the known roots, the extra factor is
\(\prod_{i:c_i=d_i=1}\operatorname{sign}(r_i)\) modulo \(N\).
Therefore \(c\mapsto z(c)\) is a group homomorphism into
\(G[2]/\{1,-1\}\) after taking the indicated quotient.
The statement about checking a basis follows. For the
compression statement, write each discarded row's class
as a binary combination of retained independent classes.
Its fundamental dependency has trivial image in this
quotient, or we would already have split \(N\).
Substituting these combinations into any future
dependency changes its image only by products of those
trivial images. This proves completeness for the
first-level dependencies of all rows seen so far.
End proof.

This compression is not a claim about preserving the
full rational relation span or deeper primary saturation.
Those stronger extractors can still be run separately.

For a list of \(M\) rows with coordinates of bit
length \(O(n)\), a binary kernel basis has at most
\(M\) vectors, each using at most \(M\) rows. All exact
rational products have bit lengths \(O(Mn)\); the modular
root products, gcds and square roots have polynomial bit
cost. Thus for \(M=B^{O(1)}\) the complete first-level
readout has half-scale cost. It never needs to cancel
outside-base valuations over the integers or rationals.

### A useful Jacobi-labelled sufficient condition

Let \(\eta(z)=(z/N)\) and \(s=v_2(N-1)\). For any known
unit \(z\) killed by \(2^k\), if
\[
 \eta(z)=-1,\qquad k<s,
\]
the square chain must find a proper gcd. To see this,
suppose all local orders are equal to \(2^h\) at the
prime divisors of \(N\); otherwise the gcd chain already
splits. Then \(1\le h\le k\). At a prime \(p\mid N\),
the Legendre sign of \(z\) is negative exactly when
\(v_2(p-1)=h\), by cyclicity of \(\mathbb F_p^\times\).
Write \(N=\prod p_i^{e_i}\). The negative Jacobi sign
says that the sum of the \(e_i\) over these primes is
odd. Expanding the product modulo \(2^{h+1}\) therefore
gives \(N\equiv1+2^h\bmod2^{h+1}\), contradicting
\(h<s\). This proof also allows repeated prime factors.

In particular for \(N\equiv1\bmod4\) a first-level
dependency with \(\eta(z(c))=-1\) suffices. When using
known roots \(t_i\) all of Jacobi sign minus one, an
odd dependency whose positive rational square root has
Jacobi sign plus one gives this exit. Square-preserving
balancing with root shift base four preserves the
specified root sign. This is a concrete parity-labelled
selection goal, not a proof of its uniform attainability.
The earlier complete primary readout can also detect
involutions for which the Jacobi sign is plus one.

## 4. Same-residue collisions: automatic splitting and sparsity

Let \(H<N/2\). Suppose distinct primitive signed
rational ratios \(r_1=y_1/x_1,r_2=y_2/x_2\), with
\(1\le x_i\le H,\ 0<|y_i|\le H\), have the same
unit residue \(a\bmod N\) and the same rational
squareclass. Their quotient is a positive rational
square, say \((u/v)^2\) in lowest terms. Then
\(1\le u,v\le H\), since its unreduced numerator
and denominator have absolute values at most \(H^2\).
Moreover \(u\ne v\). It follows that \(u/v\bmod N\)
is neither \(1\) nor \(-1\), since \(u+v<N\).
It is a square root of one, so a proper factor
is obtained automatically.

For several square shifts \(s^2a\), divide each ratio
by the actual rational square \(s^2\) before deduplication.
This normalizes the residue to \(a\) and leaves its
squareclass unchanged. With shifts \(s\le B^C\),
normalized heights are at most \(HB^{2C}<N/2\)
eventually at the half scale. Thus the automatic
criterion applies to distinct normalized ratios.
One may also pool products of a fixed number of ratios
with the same residue (checking equal product length);
their square roots need not have height below \(N/2\),
so the modular gcd must be checked and can fail.

The two-ratio criterion alone is not a promising dense
search at the asymptotic scale. The following counting
obstruction explains why the longer parity dependencies
of Section 3 are essential.

**Theorem 3 (sparse two-ratio targets).** Let
\(H=\sqrt N\exp(O(b))<N/2\) with
\(b=\Theta(\sqrt{\log N\log\log N})\). The number of unit
residues \(a\bmod N\) admitting two distinct primitive
ratios of height at most \(H\) with the same signed
rational squareclass is at most
\[
 \exp\left(O\left(b+\frac{\log N}{\log\log N}\right)\right)
       =N^{o(1)} .
\]
The same conclusion applies after allowing and normalizing
any square shifts of height \(\exp(O(b))\).

Proof. Every such ordered pair gives a positive rational
root \(u/v\) as above. It has a nontrivial involution as
its residue, and
\[
 \max(u,v)^2\ge N
\]
because the nonzero integer \(u^2-v^2\) is divisible by \(N\).
There are at most \(2^{\omega(N)}\) possible involutions,
by CRT for odd prime powers. For each one, the number of
primitive unit representatives of height at most \(H\)
is bounded by \(1+18H^2/N\): if any exist, choose such a
vector, extend it to a lattice basis by Bezout as in the
primitive enumeration theorem, and use its point-count
bound, including the collinear case. This counting
argument is valid whether or not other vectors reveal
a factor during an actual enumeration.

Fix \(u,v\). The two ratios have the same sign. Put
\(g_y=\gcd(|y_1|,|y_2|)\), \(g_x=\gcd(x_1,x_2)\), and
write \(|y_1|=g_y A,\ |y_2|=g_y B'\),
\(x_1=g_x C',\ x_2=g_x D\).
The primitive conditions and the two gcd definitions
give \(\gcd(AD,C'B')=1\). Hence
\[
 AD=u^2,\qquad C'B'=v^2.
\]
There are at most \(\tau(u^2)\tau(v^2)\) ways to choose
these four positive integers. For each choice, the
number of possible pairs \(g_x,g_y\) is at most
\[
 \frac{H^2}{\max(A,B')\max(C',D)}
 \le\frac{H^2}{\max(u^2,v^2)}\le H^2/N .
\]
Allow either common sign. Multiply the bounds and use
\(\log\tau(m)=O(\log N/\log\log N)\) uniformly for
\(1\le m\le N^2\), and
\(\omega(N)=O(\log N/\log\log N)\). For completeness,
the former follows by splitting prime factors at
\((\log N)^{1/2}\): the small primes contribute at most
\(O(\sqrt{\log N}\log\log N)\) to \(\log\tau(m)\);
the total exponents of the larger primes are
\(O(\log N/\log\log N)\), and \(e+1\le2^e\).
The latter follows also by comparing the product of
distinct prime factors with a factorial. This proves
the bound on ordered pairs and hence on their residues.
For square shifts use the enlarged normalized height
\(H\exp(O(b))\), which still satisfies the hypotheses
for sufficiently large \(N\). End proof.

In particular the success probability of the two-row
test at a uniformly random unit target is \(N^{-1+o(1)}\),
using the elementary \(\varphi(N)\ge N/(n+1)\) bound
with \(n=\operatorname{len}_2 N\). This is not a
lower bound on specially targeted or adaptive algorithms.
It is a rigorous reason not to extrapolate the finite
two-row collision to a uniform dense coverage theorem.

## 5. Exact finite verification

The new standard-library script
[verification/research/squareclass_pool.py](../verification/research/squareclass_pool.py)
was executed locally using Python 3.13.5, with the
previous exact lattice and gcd-refinement routines.

Tested and committed Git blob:
`49752d8126bb6d735abed4c280faad2cb7f00e8d`.
SHA-256:
`be69e2b92cb7697a1492f9d04ee7592ed8892c268c437a261379368c64b6e8ac`.

Observed output:

    factor-free squareclass membership: 2066 exact comparisons
    online parity kernel: 1165 independent comparisons, 92 factor exits, 197 dependencies
    incremental parity refinement and batch extraction: 480 comparisons, 221 factor exits
    bounded square-shift collision: 1763 H 42 q 5 rows 10 distinct 10 root (Fraction(-1, 1617), Fraction(-12, 11), 42) factor 41
    parity certificate: 100160063 support 21 product bits 153 166 known root 21829054 involution 100150055
    square-target pool: 100160063 H 30024 target batches 2 rows 665 parity rank 272 dependencies 191 factor 10009
    parity certificate: 1000036000099 support 94 product bits 654 727 known root 592800489564 involution 466683400045
    square-target pool: 1000036000099 H 3000054 target batches 11 rows 4988 parity rank 2158 dependencies 2711 factor 1000033

The 2066 membership comparisons use independent trial
division only as a small-test oracle. The 1165 no-factor
prefix comparisons check the online basis reduction against
an independently formed true-prime parity matrix; the
92 factor exits are verified separately. The 480 batch
tests compare incremental parity refinement with the
earlier global gcd-free basis and the online extraction.
Every returned divisor is checked by integer divisibility.

The collision fixture has normalized ratio quotient
\(1/42^2\) (in the displayed order), giving the
nontrivial involution \(42\bmod1763\). The reduced
square-root height satisfies the automatic criterion even
though the general normalized height envelope for that
small fixture is too large.

The last two searches use *different square-target families*
on the inputs from the earlier stalled examples. They are
not claims that reprocessing the old 25-row pools gives a
factor. The known roots are powers of small primes with
exponents starting at the binary input length, together
with dyadic root shifts. There is no use of the input
factorization in generating their congruences.
After each batch, retain only an independent squareclass
basis if the complete first-level readout fails. In the
final successful batch, the numbers of generated rows
include candidates after the stopping point, whereas the
displayed parity rank is the independent prefix retained
at the split. The two factorizations come from the actual
displayed involutions, not an early lattice-coordinate gcd.
The square rational products are obtained by exact integer
square roots and the modular root comparison is checked.

## 6. Remaining target

Parity-only pooling permits dependence without rational
residual cancellation and permits previously unseen primes
with even valuation. It has now succeeded on both tested
difficult fixtures, using dependencies of 21 and 94
rows. The sparse-pair theorem rules out a generic dense
two-row collision strategy.

The next mathematical task is a uniform construction of
a longer binary dependency with nontrivial root image.
A rank bound by itself would only guarantee a dependency,
not a nontrivial root; trivial dependencies may be discarded
by Theorem 2. The Jacobi-labelled sufficient criterion and
square-preserving local prescriptions are concrete tools
for targeting this distinction. No uniform bound on
new odd-support directions, or uniform guarantee of a
nontrivial dependency, has yet been established. Keep the
rational-rank and deeper-primary exits in parallel.

**Uniform deterministic \(L_N[1/2,O(1)]\) factoring
remains open.**
