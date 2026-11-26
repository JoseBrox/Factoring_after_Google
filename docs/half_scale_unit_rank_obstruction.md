# A quantitative obstruction to short paired-unit coverage

**Status (26 November 2026): proved obstruction to a restricted
certificate-generation strategy.** It does not disprove the full
half-scale search, whose compact products can have very large log
vectors. In particular, it is not a lower bound for integer factoring.

The [ramified-target construction](ramified_target_construction.md)
solves the initial ideal valuation equation and leaves membership of
one particular unit-log vector in the span of the available shared
unit relations. We now prove that simply supplying enough more
ordinary small units cannot solve that membership uniformly.

## 1. Most balanced inputs have no small order for any small base

Fix constants A>0 and 0<delta<1/2. For each positive integer b let
P_b be the primes in [2^(b-1),2^b), let X_b=floor((2b)^A), and put
T_b=floor(2^((1/2-delta)b)).

For any integer a with 2<=a<=X_b, and sufficiently large b, a is
coprime to every p in P_b. If ord_p(a)<=T_b, then p divides the
positive integer
\[
 M_a=\prod_{j=1}^{T_b}(a^j-1).
\]
The factor a^1-1 is allowed to equal 1. Since log M_a is at most
(T_b(T_b+1)/2) log a, there are at most
T_b(T_b+1)log(a)/(2(b-1)log 2) distinct such primes in P_b.
Union over all a gives at most
\[
 O\left(\frac{X_b T_b^2\log(2X_b)}{b}\right)
\]
bad primes. By the prime number theorem the fraction of P_b this
represents is O(X_b log(2X_b) 2^(-2delta b))=o(1).

Thus for a fraction 1-o(1) of ordered pairs of distinct primes
p,q in P_b, both primes satisfy
\[
 \operatorname{ord}_p(a),\operatorname{ord}_q(a)>T_b
 \qquad(2\le a\le X_b).                                    \tag{1}
\]
Their products N=pq are balanced squarefree semiprimes of bit
length n in {2b-1,2b}. Since n<=2b, this covers all bases a<=n^A.
In particular, taking delta=1/6, the order of every polynomially
bounded base exceeds floor(2^(b/3)), which is exponential in n.

This argument uses only the ordinary PNT and elementary counting
of prime divisors; there is no conjecture about primitive roots.
It also applies to all the separating targets from our QRH
witness argument, by choosing A to bound the fixed polynomial
target interval. The semiprimes in (1) have no small prime factors
and are not perfect powers, so the usual initial guards do not
remove them.

## 2. Discrete logarithm-and-valuation lattices

Let K_1,K_2 be totally real fields of degrees d_1,d_2. For each
field let S_i be a finite set of nonzero prime ideals and let
G_i be any subgroup of K_i^* whose nonzero valuations are
supported on S_i. For an element alpha in G_i define
\[
 \mathcal V_i(\alpha)=
 \left((v_{\mathfrak p}(\alpha))_{\mathfrak p\in S_i},
       H_i(\log|\sigma(\alpha)|)_{\sigma:K_i\hookrightarrow\mathbb R}\right),
\]
where H_i is the orthogonal projection onto the sum-zero hyperplane,
expressed in orthonormal coordinates. Use the direct sum V of these
maps on G_1 times G_2. The first coordinates are integer-normalized
valuations; no weighting depending on the size of the primes is
used.

The additive image is discrete and any nonzero vector has length
greater than 1/3. Indeed, if a finite coordinate is nonzero its
absolute value is at least 1. Otherwise the two elements are
algebraic units, so their logarithm vectors already have sum zero.
If a non-torsion unit u had log norm at most 1/3, then every real
embedding would satisfy
\[
 e^{-2/3}\le|\sigma(u)|^2\le e^{2/3}<2.
\]
It would follow that the nonzero integer Norm(u^2-1) has absolute
value strictly between 0 and 1, a contradiction. If u^2=1, all
logs vanish. The kernel of V is consequently contained in the
four sign pairs; signs need not belong to the particular subgroup.

A discrete additive subgroup in a finite-dimensional real vector
space is a lattice in its real span. In particular, if k independent
vectors span a subspace W, the intersection of the image lattice
with W is a rank-k lattice. The covolume of this intersection is
at least (3 sqrt(k))^(-k): the open cube of side 2/(3 sqrt(k))
in orthonormal coordinates contains no nonzero point, and the
strict-volume form of Minkowski's convex-body theorem gives the
bound. This works at every rank, without a basis of the full
S-unit group.

### Small-span denominator lemma

Let v_1,...,v_M be lattice vectors, each of Euclidean length at
most H>=1, and let x be any other vector of the same lattice.
If x lies in the real span of the v_j, of positive rank k,
then
\[
 Qx\in\sum_j\mathbb Z v_j\quad\text{for some positive integer }
 Q\le H^k(3\sqrt{k})^k .                                   \tag{2}
\]
Select k independent vectors from the original list and use the
lattice intersection just described. Their sublattice has
covolume at most H^k by Hadamard; its index in the intersection
is a positive integer Q at most the bound in (2). The quotient
group of order Q is killed by Q. If k=0, membership requires
x=0 and one can take Q=1. Neither the size of the list nor the
size of x enters the positive-rank denominator bound.

## 3. A barrier to the full-rank small-unit strategy

Use the actual fields and modular evaluation maps of the
ramified-target construction. Put g_1(X)=X-R_1, so that
its field norms are ell and 1 and its modular evaluation
is a unit a=m-R_1. The pair
\[
 \xi=\left(g_1(\theta_1)^d/\ell,\;g_1(\theta_2)^d\right)
\]
is a pair of algebraic units: in the first field both the
numerator and ell generate the same principal ideal
\mathfrak l^d. Its projected log vector is exactly
x=d L(g_1), the remaining target vector of that construction.

Both components of xi are represented in localized polynomial
orders, with the rational denominator ell evaluating to a unit.
Their modular images have ratio ell^(-1). A *shared unit pair*
means two algebraic units represented in these localized orders
whose images modulo N agree. The existing ratios of the
prescribed linear marks are examples.

Suppose x is in the span of log vectors of shared unit pairs,
all of length <=H. Their rank k is at most D=d_1+d_2-2.
By (2) some Q<=H^k(3 sqrt(k))^k makes the logarithm of
xi^Q equal to that of a product of these pairs. The quotient
has zero logs and hence is a sign pair. Clearing negative
powers in the localized orders and taking the ratio of
modular images gives
\[
 \ell^{2Q}=1\bmod N.                                      \tag{3}
\]
The sign ambiguity is the only reason for the factor 2.
In particular every hidden prime p divides ell^(2Q)-1.

For an input satisfying (1) and a target ell in its range,
rank-zero membership is impossible, and (2)-(3) imply
\[
 \log H\ \ge\ \frac{\log T_b-\log 2}{k}
                         -\log(3\sqrt{k}).                \tag{4}
\]
If d_1,d_2=O(sqrt(n)), then k=O(sqrt(n)).
Taking delta=1/6 gives the necessary lower bound
log H=Omega(sqrt(n)). For the smaller degree
d_i=O(sqrt(n/log n)) developed in the companion full-degree
search, it gives log H=Omega(sqrt(n log n)).

Consequently **no number of shared unit pairs of polynomially
bounded log norm can contain this target in their real span**
on these inputs. Increasing the count of such units to
exp(O(sqrt(n log n))) cannot help: one still selects at most
D independent columns. In particular a strategy based solely
on constructing a polynomial-height basis of explicit paired
units is not a uniform solution of the remaining problem.
Here polynomially bounded refers to the logarithm vector, or
to ordinary coefficient *bit lengths* polynomial in n, not to
compact power-product encodings of very large units.

This strengthens the earlier proof that the r-1 specified
ratio pairs alone do not suffice. The stronger obstruction
applies even to arbitrary new explicit shared units with
small log norms. It does not apply to the compact units
produced by taking large integer combinations of many
nonunit marks.

### A regulator interpretation

Let G_i be the units of the full ring of integers that
belong to the localization of Z[theta_i] at all elements
evaluating to units modulo N, and are themselves invertible
in that localization. Evaluation on the localization is
well-defined. This subgroup contains Z[theta_i]^*, which
has full unit rank: an order contains c O_K for some
nonzero integer c, and the units congruent to one modulo
c O_K form a finite-index subgroup of O_K^* lying in the
order together with their inverses.

Let G=G_1 times G_2, and let U_N be the kernel of the
homomorphism taking a pair to the ratio of its modular
images. Both have full log rank D, since the ratio group is
finite. The pair xi belongs to G. If its log class has
order Q_0 in log(G)/log(U_N), the sign argument gives (3)
with Q_0. Thus
\[
 [\log G:\log U_N]\ge Q_0\ge\operatorname{ord}_p(\ell)/2.
\]
Using the same lattice separation for log G gives
\[
 \operatorname{covol}(\log U_N)\ \ge\
 \frac{\operatorname{ord}_p(\ell)}{2(3\sqrt D)^D}.           \tag{5}
\]
This is a lower bound for the regulator of the *shared*
congruence subgroup. It is not a lower bound of this size
for the individual fields' regulators. For almost all
balanced inputs it is exponential in n for the degrees in
question, whereas a full-rank list of shared unit pairs with
polynomial log norms would have determinant exp(O(D log n))
=exp(o(n)). This explains the obstruction geometrically.

## 4. A minimum-rank requirement on the original polynomial marks

There is a similar obstruction that applies before constructing
units. Let g_j be any finite family of nonzero polynomial
marks with both field values nonzero and unit modular images.
Include all finite prime-ideal coordinates of the marks and
the target tau=(ell,1) in V. Suppose the marks' V-vectors
have norms at most H and a target certificate exists.

The target certificate makes V(tau) lie in their real span.
By (2), with k their rank, some positive Q bounded as in (2)
yields
\[
 V(\tau^Q\prod_j (g_j(\theta_1),g_j(\theta_2))^{c_j})=0
\]
for integral c_j. All valuations vanish, so the pair consists
of units; the projected logs vanish, so it is a sign pair.
As each mark has the same modular image in both fields, (3)
again follows.

For the polynomial-bit-height fields and marks of the
previous construction one can take H=n^C with a fixed C.
Indeed a Cauchy root bound and Horner evaluation give
log of every conjugate magnitude's upper bound polynomial
in n; for an integral nonzero mark its positive integral
absolute norm bounds every individual conjugate from below
by the reciprocal product of the other upper bounds.
The sum of its nonnegative integer valuations is at most
log_2 of its absolute norm, so the Euclidean norm of the
finite vector is polynomial in n, independent of the number
of rows. Polynomial-bit rational marks obey the same bounds
by applying this argument separately to their numerators
and denominators.

Consequently on the inputs (1), for any polynomial-bit-height
family achieving a certificate its joint valuation/log rank
satisfies
\[
 k=\Omega(n/\log n).                                      \tag{6}
\]
If k>n this is automatic; otherwise (2)-(3) give
log ord_p(ell)<=O(k log n), and use (1).
The argument applies to any subfamily supporting a certificate,
not only to the rank of the full search matrix. It follows that
a proposal using only O(d) or o(n/log n) original small marks
cannot work uniformly on balanced inputs. One cannot evade
this merely by representing their large powers compactly.

Writing the combined matrix as the stack of its true finite
valuation matrix V_f and the projected log matrix L also gives
rank(V_f) >= k-D. Thus the finite-valuation rank itself must be
Omega(n/log n) in either of our field-degree regimes, because
D=O(sqrt(n))=o(n/log n). A large number of columns supported
on a fixed small set of ideal rows cannot meet this requirement.
This applies to every successful subfamily of polynomial-bit-height
marks, even if a particular target valuation column is already known.

The earlier full search is not contradicted: it enumerates
subexponentially many marks, and its joint valuation rank can
be much larger than the archimedean rank. Large determinant
coefficients in the integral valuation kernel can yield unit
log vectors satisfying (4). These are precisely the large
compact units that a successful search must produce.

## 5. Research consequences

The remaining coverage problem is not a routine application of
Dirichlet's unit theorem or an explicit-unit construction.
The shared unit lattice has a congruence index that is very
large even when the individual fields have many short units.
A proof of uniform half-scale success must exploit at least one
of:

- relations with substantial finite-valuation rank giving large
  compact units;
- a direct construction of a large shared unit in compact form
  with the required target membership; or
- a different separation mechanism.

The next search is therefore enlarged using exact ideal factor
refinement, so that there is no need to factor individual norms,
discard bad primes, or assume smoothness for the *computation*
of the relation space. This does not prove that the necessary
relations exist. See the companion full-degree search note.

No unconditional general half-scale factoring theorem is proved
here. This is a rigorously delimited obstruction and necessary
rank/height condition, not an unsupported assertion that every
method of obtaining the target must fail.

## 6. A related reciprocal interpolation route is circular

There is a tempting one-field alternative: construct a monic
polynomial f of even degree d>=12 with f(m) a nonzero multiple
of N and d-1 independent units 1+a_j(theta-m) whose modular
images are all 1. Suppose the a_j are distinct nonzero integers
and all these units have norm ±1. Define F(t)=Norm(1+t(theta-m)),
an integer polynomial of degree d with F(0)=1 and leading
coefficient Norm(theta-m)=f(m) (d even). If F takes both signs
±1 on these d integer points, any opposite-sign pair has
distance at most 2 since their difference divides ±2. Choosing
one point of each sign shows that every point is in the union
of two intervals of integer radius 2 around the two points;
each sign set has at most five points, so their union has
at most ten. Since d>=12, all signs are therefore +1.
Then F(t)-1 has the d distinct roots 0,a_1,...,a_(d-1),
so it equals f(m) t prod_j(t-a_j). Every nonconstant
coefficient is divisible by N. Reversing this norm polynomial
shows f(X) congruent to (X-m)^d modulo N.

For any polynomial g, the multiplication norm in the power
order reduces modulo N to g(m)^d: over Z/NZ the order has
basis 1,Y,...,Y^(d-1) with Y=X-m, and g(m+Y) acts by a
triangular matrix with constant diagonal g(m). Consequently
any integral unit in this power order has g(m)^d=±1 mod N.
Even if it belongs only to the localized order, its rational
expression with denominator evaluating to a unit satisfies
the same assertion by multiplicativity, provided its actual
field norm is ±1. In particular a target unit with reduction
ell would force ell^(2d)=1 mod N. By Section 1 this is
impossible on the generic balanced inputs for polynomial
d and ell. Thus this simple way of prescribing all kernel
units cannot be turned into a uniform target-unit constructor.
This discards a specific interpolation strategy, not all
one-field or higher-degree unit constructions.
