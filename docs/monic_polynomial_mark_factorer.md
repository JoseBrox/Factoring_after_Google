# Beyond the two-thirds schedule: monic fields and polynomial marks

**Status (2026-11-26):** new algebraic construction, a proved reduction to
one precisely stated covariance hypothesis, and a finite extraction
experiment. **The covariance hypothesis is open.** This is not an
unconditional improvement on the L_N[2/3,O(1)] deterministic bound, nor a
new complete Lean proof.

## 1. What must change

In our original two-field construction the base has log m of order
L^(1-a), with degree L^a. The common leading coefficient and perturbation
scale must accommodate both m and A^d. Since log A exceeds the factor-base
and root-window scales, in particular exceeds L^a, this gives the competing
requirements h >= 1-a and h > 2a for the search exponent h. The old
two-prefix estimate introduces further restrictions. Merely substituting
GRH for the near-one zero-density estimate does not eliminate this
algebraic barrier. Likewise, a nonuniform list of good perturbations or
a list requiring two-thirds-scale preprocessing is not an improvement
to uniform worst-case factoring.

We replace the high leading coefficient by **surplus degree** and
replace the scalar mark X-a by a polynomial g of substantially smaller
degree. The marks, rather than pairs of independently perturbed fields,
provide the variables for smoothness and rank. All marks are enumerated;
we seek a one-mark distribution result, not concentration of a random
matrix over two marks.

## 2. Explicit monic, totally real fields

Let n be the binary length of the odd input N. Work for sufficiently
large n, with small cases handled by a deterministic fallback. Choose
d=2*3^j, the smallest such integer at least 8 sqrt(n), and put D=d/2,
m=2^ceil(4n/d). Thus d=Theta(sqrt(n)), log m=Theta(sqrt(n)).
Let ell be a prime of polynomial size in n with ell>4d,
ell congruent to 2 or 5 modulo 9, and gcd(2ell,N)=1.

Use the integer centers
\[
 r_{1,k}=12\ell k+2k,\qquad r_{2,k}=12\ell k+6\ell,
 \qquad 1\le k\le d,
\]
and P_i(X)=prod_k(X-r_{i,k}). The centers are even and interlaced;
within each field the spacing is at least 12ell, and across both fields
the minimum spacing exceeds 4ell. They all lie in (0,14ell d).
Let
\[
 e_1(X)=\ell(X^D+1),\qquad e_2(X)=X^D+1.
\]
Take C_i to be the base-m digit polynomial of the least nonnegative
residue of
\[
 -(P_i(m)+e_i(m))(2\ell)^{-1}\pmod N.
\]
Its degree is strictly less than D: m^D >= 2^(2n)>N.
For any integers u_i,v_i of absolute value at most U=2^floor(sqrt(n)),
define
\[
 f_i=P_i+e_i+2\ell C_i+
           2\ell(X-m)(u_i+v_i X).
\]

**Proposition 1.** All these pairs are monic, irreducible over Q,
have degree d, and satisfy f_i(m)=0 modulo N. They have d distinct real
roots in the indicated order. Modulo ell, f_1 splits into distinct
linear factors, while f_2 is irreducible. Construction and exact
verification of the root brackets take polynomial bit time in n for
polynomially bounded ell.

Proof: the correction has degree at most D; thus all higher
coefficients, including the leading 1, are unaltered. At m the
base-digit correction enforces the congruence, and the perturbation
vanishes. Modulo 2 the reduction of either polynomial is
\[
 X^d+X^D+1=\Phi_{3^{j+1}}(X).
\]
The order of 2 modulo 3^(j+1) is 2*3^j: its order modulo 3 is 2,
and v_3(2^2-1)=1, so lifting the exponent gives the claim.
The cyclotomic polynomial is irreducible over F_2 by the Frobenius
orbit of a primitive root of unity. Monicity gives irreducibility
over Q. The reduction of f_1 modulo ell is prod_k(X-2k), with
distinct roots. For f_2 it is the same cyclotomic polynomial as
above. Every ell in the chosen two residue classes has order 2
modulo 3 and v_3(ell^2-1)=1, so that same Frobenius argument proves
irreducibility over F_ell.

For exact real-root brackets put
\[
 \eta=\frac1{4(\ell d)^{\lfloor d/8\rfloor}} .
\]
At r_{i,k} +/- eta, the product of the absolute distances to
the other centers is at least
(6ell)^(d-1)(k-1)!(d-k)! >= (3ell)^(d-1)(d-1)!.
Thus the log of |P_i| at either endpoint is at least
(7/8)d log(ell d)-O(d+log(ell d)).
For |X|<=14ell d+1, the log of an upper bound on the total
correction is at most
\[
 (d/2)\log(\ell d)+O(d+\sqrt n+\log(\ell d)).
\]
This follows by bounding every coefficient of the correction
by O(ell(1+m)(1+U)) and using degree D.
The gap tends to infinity uniformly. Therefore the original
opposite signs persist. There are d disjoint sign brackets of
a degree-d polynomial, so every root is real and simple, one
per bracket. The brackets of the two fields are disjoint too.
All coefficients have O(d log(ell d)+sqrt(n)) bits, and evaluating
P_i(m), the modular correction, and endpoint signs by integer
Horner arithmetic uses polynomial bit time. In particular,
there is no requirement log U >= d log A or log U >= log m.
The resultant of the two fields is nonzero, also directly from
their different irreducible factorizations modulo ell. End proof.

## 3. Enumerate polynomial marks

Fix 0<epsilon<1/12, and set
\[
 s=\lceil n^{1/4}\rceil,\quad
 H=2^{\lceil n^{1/4+\epsilon}\rceil},\quad
 B=2^{\lceil n^{1/4+\epsilon/2}\rceil}.
\]
All rounded powers can be computed by integer root/power comparisons
for rational epsilon; this suffices for every requested positive
epsilon by decreasing it. Enumerate the nonzero integer polynomials
g of degree at most s with |g_j|<=2H. There are at most
(4H+1)^(s+1)=exp(O(n^(1/2+epsilon))) marks. The four perturbation
coordinates can be enumerated too within exp(O(sqrt(n))) time.

Let theta_i be a root of f_i, R=30ell d, and define
A_i(g)=|Res(f_i,g)|=|Norm(g(theta_i))|. Since s<d and f_i
is irreducible, A_i(g) is a positive integer, and
\[
 \log A_i(g)\le d\log((s+1)2H R^s)=O(n^{3/4+\epsilon}).
\]
Also |g(m)|<N eventually; it is nonzero, because the coefficients
have absolute value smaller than m/2 and the leading nonzero
term dominates the sum of the lower ones. Thus a nonunit g(m)
gives a proper gcd immediately.

Put
\[
 D_{\rm bad}=|\operatorname{disc}(f_1)
        \operatorname{disc}(f_2)\operatorname{Res}(f_1,f_2)|.
\]
It has polynomial bit length and ell does not divide it.
Enumerate the degree-one root labels (i,p,r) for p<=B,
p not dividing D_bad, and f_i(r)=0 modulo p, by elementary
prime and residue enumeration. Retain a mark if both A_i(g)
are squarefree and B-smooth, with no prime divisor of D_bad.
Compute these tests by trial division up to B, not by calling
a factoring oracle on the norms.

For retained g define V_(i,p,r)(g)=1 if g(r)=0 modulo p,
and 0 otherwise. Since p does not divide the discriminant, the
power order is p-maximal and the usual Dedekind factorization
identifies these with the integer valuations of the principal
ideal (g(theta_i)). Squarefree norm implies exactly one
degree-one prime ideal to exponent 1 above each rational
prime dividing the norm. Higher residue degrees or repeated
valuation would contradict squarefreeness. Excluding the
resultant ensures distinct root residues across the two fields
at each allowed prime. Consequently there are no unrecorded
valuations. Monicity avoids the nonmonic offset entirely.

Let b_ell be 1 on all d labels above ell in field 1 and 0 elsewhere.
These labels exist because ell<=B eventually. Since deg g<d,
ell cannot divide the norm in field 2 except when g is zero
modulo ell; the latter is excluded by squarefreeness.

## 4. Exact extractor and conditional complexity

For a pair of fields define L(g) to consist of the two vectors
of real logs log|g(theta_i,k)|, each projected orthogonally to
its sum-zero subspace. The sufficient extraction conditions are
\[
 b_\ell\in\operatorname{im}_{\mathbb Q}V,\qquad
 L(\ker_{\mathbb Z} V)\text{ spans }\mathbb R^{2d-2}.
 \tag{E}
\]
Here span is real linear span after identifying the projected
spaces with Euclidean spaces, not an assertion that the lattice
is all of Euclidean space.

**Proposition 2.** Under (E), a deterministic algorithm of
polynomial bit cost in the number of marks, B and n constructs
a positive E with ell^E=1 modulo N (or returns a proper factor).

Proof: exact rational elimination and determinant clearing give
c^(0) integral, Vc^(0)=-E_0 b_ell for E_0>0, and an integral
basis of the rational kernel. The principal fractional ideals show
that
\[
 \ell^{E_0}\prod_g g(\theta_1)^{c^{(0)}_g},\qquad
 \prod_g g(\theta_2)^{c^{(0)}_g}
\]
are algebraic units. Every integral kernel vector similarly
produces a pair of units. Projection removes the log of the
rational scalar ell. Thus the projected vectors of c^(0) and
the kernel lie in the product of the two full log-unit lattices.

The effective reconstruction in effective_number_field_recovery.md
applies here. Its requirements on log sizes and root isolation
hold: if M=(s+1)2H R^s, each |g(theta_i,k)|<=M and, by the
nonzero integral norm, each is at least M^(-(d-1)).
Hence all logs and the logarithms of derivative bounds for g on
the isolating intervals have polynomial size in n. Root bisection
and certified logarithm computation give the required error
2^(-P) in polynomial time in n and P. The determinant bounds
and unit-lattice separation give polynomial bit length in n
and the row dimension for P and the reconstructed rationals.
More explicitly, any non-torsion unit has log vector of norm
>1/3, by the nonzero integer Norm(unit^2-1). Minkowski gives
a lower covolume exp(-O(d log d)) in the orthonormal log
coordinates. Integer pivot determinants have bit size polynomial
in the row dimension and n. Greedy determinant selection with
a certified threshold finds 2d-2 independent log columns under
(E). Coordinates of the particular log vector in this basis
are rational, with denominators bounded by the ratio of the
selected determinant to the unit-lattice covolume; Cramer's
rule bounds numerators as well. Certified dyadic precision
polynomial in the logarithms of these bounds followed by
continued fractions recovers them. Clearing their denominators
Q gives c with Vc=-E_0 Q b_ell and Lc=0.

Both resulting units have every real absolute value 1, hence
are +/-1. Clear the negative powers to identities of polynomials
in the integral monic orders, without evaluating the full
ring of integers modulo N. Indeed both sides of each cleared
identity belong to Z[theta_i], and that order has a well-defined
evaluation theta_i -> m modulo N. Since g(m) and ell are units,
the identities give ell^(2E_0 Q)=1 modulo N. Verify this equality
exactly. The output exponent has polynomial bit size in the row
dimension and n. All steps, including failed rank/precision
guards, can be capped by explicit polynomial bounds from the
same determinant and separation estimates; no search over
an exponential denominator range is used. End proof.

### No common-annihilator saturation is needed

Use the verified fixed zero-free strip from our QRH integration
and the written uniform smoothed estimate in quasi_rh_witnesses.md.
For a nonprincipal character modulo q, the weighted sum with
weight (1-t)_+ is O(X^(15/16) log(q+2)); for the principal it is
X/2+O(X^(15/16)+log(q)log(X)), by removing the finitely many
prime-power terms at primes dividing q. The nonnegative weight
\[
 w(t)=(1-t)_+-\tfrac32(1-4t/3)_+
                  +\tfrac12(1-2t)_+
\]
is supported on [1/2,1] and has integral 1/16. It therefore
has the same character error and principal main term X/16.
Prime powers of exponent >=2 contribute O(sqrt(X) log^2 X).

For two distinct hidden odd primes p,q dividing N, orthogonality
in the unit group modulo 9pq shows there are primes ell in
(X/2,X] with ell congruent to 2 modulo 9 and with either
prescribed pair of Legendre signs at p,q. Indeed the indicator
has a character expansion whose absolute coefficient sum is 1
and whose principal coefficient is 1/24. The main term dominates
uniformly for X=2^(128 ceil(log_2(n+2))) and n sufficiently large.
One can first trial-divide to X; then p,q>X, so there are no
overlapping moduli or divisibility exceptions.

If v2(p-1)=v2(q-1), choose opposite Legendre signs. If they
differ, choose a nonsquare at the prime with larger valuation.
The two 2-parts of ord_p(ell) and ord_q(ell) then differ.
For any positive E with ell^E=1 modulo N, write E=2^t E_odd;
the first point of the chain ell^(2^j E_odd) becoming 1 at one
prime differs from that at the other. A gcd with N at a suitable
level returns a proper divisor. This only requires an order
multiple of the *individual base*, not p-1 for all hidden primes.

**Conditional theorem.** Suppose for every sufficiently large
surviving non-perfect-power composite N and every target ell in
the above polynomial interval and residue classes, at least
one enumerated pair of fields satisfies (E) (it suffices that
this holds for a separating ell). Then complete deterministic
factorization takes
\[
 \boxed{\exp(O_\epsilon((\log N)^{1/2+\epsilon}))}
\]
bit operations. All enumeration, matrix, root, valuation,
norm and reconstruction costs above have this bound. Polynomial
primality and perfect-power tests, early gcds, and recursion on
proper factors add only polynomial overhead in n, with at most
O(n) recursion nodes. A trial-division fallback makes the
algorithm correct and terminating on every input regardless of
the hypothesis; its use on arbitrarily large inputs would
invalidate the claimed time bound. No cutoff depending on
unknown factors is used in the algorithm.

## 5. A new, sufficient one-mark covariance contract

We now reduce (E) to a concrete probability statement that does
not require estimating a second mark jointly with the first.

Write x_j=r_j/R for the 2d centers from both fields, in their
joint order, and w=d^(-4)/100. They are separated by at least
c/d for an absolute c>0. Take J=4d+1 coefficient boxes, indexed
by a baseline and by (j,h) with 1<=j<=2d, h=1,2. Their reference
polynomials in t are
\[
 G_0(t)=1,\qquad G_{j,h}(t)=t-x_j-hw.
\]
For a fixed positive constant K, choose each box of g by
\[
 |g_k R^k/H-[t^k]G_b|\le
        \delta,\qquad
 \delta=\frac{w n^{-K-3}}{s+1},\quad 0\le k\le s.
\]
These lie inside the enumerated coefficient cube. Every coordinate
interval has length at least exp((1+o(1))log H) and is much
longer than B^C for every fixed C, since s log R=o(log H)
and log B=o(log H).

For each box b let lambda_b be the reference full log vector:
log H plus log|G_b(x_j)| in its j-th coordinate. Let lambda(g)
be the actual full log vector at the 2d roots. The root bracket
error is exponentially smaller than any inverse power of n.
On each box the value error in g(Rt)/H is at most
(s+1)delta plus the root displacement error (the reference
linear polynomial has derivative 1). Every reference absolute
value is at least w. The mean-value theorem for log, followed
by the Euclidean bound on 2d coordinates, gives uniformly
\[
 \|\lambda(g)-\lambda_b\|_2\le n^{-K}.
 \tag{L}
\]

The 2d paired differences lambda_(j,2)-lambda_(j,1) have their
j-th coordinate exactly log 2. In the i-th coordinate for
i != j the magnitude is O(w d/|i-j|), by separation and the
mean-value theorem. Consequently both the maximum row sum
and column sum of the off-diagonal absolute error matrix are
O(w d log d)=o(1). Its Euclidean operator norm is at most
the square root of their product. The matrix of paired
differences thus has smallest singular value at least
(log 2)/2 eventually. This is an explicit archimedean design,
with only inverse-polynomial windows, not windows of
exponentially small width in d.

### Exact local CRT law before smoothness

For any fixed number t of distinct allowed root labels, impose
their linear vanishing conditions on g. At a prime p with t_p
labels, the residues are distinct, and the first t_p coefficients
form a square Vandermonde matrix invertible modulo p. Given all
coefficients except the first t=max t_p, the probability of the
conditions with those first t coefficients uniform modulo
Q=prod_p p is exactly prod_p p^(-t_p). The proof is the
surjectivity of each Vandermonde system, then CRT; no
distribution of the roots is presumed. For integer uniform
coefficients in any box, each residue count differs from the
interval length/Q by at most 1. The actual probability is
therefore (1+O_t(Q/W_min)) prod_p p^(-t_p), where W_min is
the minimum number of integers in a coordinate interval.
For fixed t this relative error is smaller than n^(-A) for
every fixed A. This does NOT hold automatically after conditioning
on both norms being squarefree smooth.

### The open hypothesis (COV)

For each target ell (or for enough separating targets), there
is a pair of fields and a subset F of allowed labels containing
the d target labels, such that the following conditions hold.
In each box retain the marks of Section 3 with all their nonzero
valuation entries in F, and use the uniform distribution on these
marks. Each distribution is nonempty. Write V_r for the 0/1
entries, p_(b,r)=E_b V_r and
\[
 \bar p_r=J^{-1}\sum_b p_{b,r}>0,\qquad Z_r=V_r/\sqrt{\bar p_r}
 \quad(r\in F).
\]
Let a_i be supported on the labels in field i with entries
sqrt(bar p_r) log(p_rational), where p_rational is the prime
of the label. The two a_i are nonzero and have disjoint supports.
By exact norm factorization
\[
 a_i\cdot Z(g)=\sum_{k=1}^d\lambda_{i,k}(g).
 \tag{N}
\]
Require, for an absolute constant C and a fixed K>C/2+5,
\[
 \boxed{\frac1J\sum_b\operatorname{Var}_b(v\cdot Z)
       \ \ge n^{-C}\|v\|_2^2\quad
          (v\perp a_1,a_2).}
 \tag{COV}
\]
The quantifiers matter: the same pair and the same F must work
in all boxes, and K,C are fixed independently of N, with the
displayed inequality for K. Rare or problematic non-target rows
may be removed by F, but marks hitting a removed row must be
discarded, not simply have that entry ignored.

**Proposition 3 (proved).** (COV) implies (E).

For a putative linear dependence of the rows of the retained
matrix, including an intercept and all projected log rows, write
\[
 A+v\cdot Z(g)+y\cdot\lambda(g)=0,
\]
where y has sum zero in each field. Decompose
v=v_perp+t_1 a_1+t_2 a_2. By (N) this is
A+v_perp dot Z+tilde y dot lambda=0, with
tilde y=y+t_1 1_1+t_2 1_2. Taking within-box variances and
using (L) and (COV) gives
\[
 \|v_\perp\|\le n^{C/2-K}\|\widetilde y\|.
\]
The mean vector mu_b of Z satisfies the automatic bound
\[
 \|\mu_b\|^2=\sum_r p_{b,r}^2/\bar p_r
       \le J\sum_r p_{b,r}\le J n\le n^2
\]
eventually: every mark has fewer than n nonzero entries from the
joint norm-size bound, and J<=n. Taking means of the dependence,
\[
 |A+\widetilde y\cdot\lambda_b|
       \le(n^{1+C/2-K}+n^{-K})\|\widetilde y\|.
\]
Subtract the paired equations; the Euclidean norm of the vector
of paired differences applied to tilde y is at most
2 sqrt(2d)(n^(1+C/2-K)+n^(-K))||tilde y||.
The singular-value lower bound just proved is inconsistent with
this for nonzero tilde y. Hence tilde y=0 and v_perp=0.
Since y has the two zero sums, t_1=t_2=0 and y=0; then A=0.
All the rows in question are independent over R.

In particular the retained rational valuation matrix has full
row rank on F, so b_ell is in its rational image. Full joint
row rank also implies the projected log map on the real
valuation kernel is onto. The valuation matrix is integral,
so a rational kernel basis can be cleared to give an integral
one spanning that same real kernel. All marks have zero
valuation outside F. Extending columns by zero rows and using
the entire enumerated mark set cannot destroy the two extraction
properties. This proves (E), without knowing F or the reference
probabilities algorithmically. End proof.

## 6. What remains, and how to pursue it

The important unresolved problem is a simultaneous squarefree
smooth-value distribution theorem for two resultants as g
varies over high-dimensional integer boxes. This is not the
old one-dimensional smooth-AP theorem: the two resultants are
nonlinear correlated functions of the same coefficients. The
CRT calculation alone cannot prove (COV). In particular,
knowing the sizes of the resultants or the density of ordinary
smooth integers is insufficient. For typical sizes the ordinary
smoothness benchmark has exponent u log u =
O(n^(1/2+epsilon/2) log n)=o(n^(1/2+epsilon)); this is only
a parameter plausibility check, not a density assertion.

The next analytic goal is conditional insertion laws for one
mark, with zero, one and two prescribed degree-one ideals.
The two directions in (N) must be projected out before seeking
a spectral lower bound. Such estimates may produce (COV)
without controlling the original two-point Gram variance,
because the actual algorithm exhausts the mark set.

For a potential one-third-scale refinement, take s approximately
n^a, log H approximately n^h, log B approximately n^b.
With h>a the enumeration exponent is a+h, and the ordinary
smoothness benchmark has exponent 1/2+h-b. Matching that
benchmark would require a+b>=1/2. The local CRT proof above
additionally requires h>b, which forces a+h>1/2. Without that
last constraint the exponent inequalities allow values
arbitrarily close to 1/3 (a,h near 1/6, b near 1/3), provided
the field perturbations are restricted to the smaller budget.
This is a concrete motivation for a stronger high-dimensional
congruence/smoothness theorem, not evidence that it is true.

No use of the external int-fac proof sources is needed in
Propositions 1-3. Our prior two-thirds-plus-epsilon unconditional
claim and its formalization remain separate. The new half-scale
claim is conditional, and cannot be advertised as a proved
general factoring improvement.


### A finite matrix criterion for the required moment estimates

A possible route to (COV) is a categorical prime-occupation model
with two norm constraints. The following exact matrix lemma records
the necessary error scale; it does not assert the model for resultants.

Write A for the matrix with columns a_1,a_2 and let D_b be a real
symmetric positive definite matrix. If D_b >= kappa I, then
\[
 S_b=D_b-D_b A(A^T D_b A)^{-1}A^T D_b
\]
satisfies v^T S_b v >= kappa ||v||^2 on v perpendicular to A.
Indeed
\[
 v^T S_b v=\min_t (v-At)^T D_b(v-At)
       \ge\kappa\min_t\|v-At\|^2=\kappa\|v\|^2.
\]
Here the two columns of A are independent by their disjoint
nonzero supports. The matrix S_b is the covariance of the
corresponding Gaussian after imposing two linear constraints;
it is only a *reference* for the discrete covariance to be
estimated, not an identity for conditioned categorical variables.

For example, an unconditioned categorical model in which a given
rational prime contributes at most one label in a field has a
block of normalized covariance
\[
 D_p=\operatorname{diag}(q_r/\bar p_r)
       -zz^T,\qquad z_r=q_r/\sqrt{\bar p_r}.
\]
If sum_r q_r<=1-delta_0 and q_r>=kappa_0 bar p_r, weighted
Cauchy-Schwarz gives D_p>=delta_0 kappa_0 I. The same
holds for a direct sum over the prime/field blocks. A saddle
model would have to justify not only such occupation probabilities
but also the correction from the two log-norm constraints.

Let C_b be the actual covariance matrix of Z. Suppose the average
error relative to the matrices S_b obeys the entrywise bounds
\[
 |J^{-1}\sum_b(C_b-S_b)_{rr}|\le \xi,\qquad
 |J^{-1}\sum_b(C_b-S_b)_{rs}|
            \le \xi\sqrt{\bar p_r\bar p_s}\quad(r\ne s).
\]
Then its operator norm is at most xi(1+sum_r bar p_r)<=xi(1+n).
To see this, apply the triangle inequality to the quadratic form
and use (sum sqrt(bar p_r)|v_r|)^2 <=
(sum bar p_r)||v||^2. Thus if kappa is inverse-polynomial
and xi<=kappa/[2(1+n)], (COV) follows. This shows why
suitable one-mark insertion estimates with polynomial relative
accuracy, retaining the same-prime exclusions and the norm
correction, would be enough: an error multiplied by the entire
factor-base cardinality is not necessary.

### Why simply extending the CRT calculation cannot prove this

In any of the coefficient boxes, every |g(theta_i,k)| is between
H w/2 and 2H for sufficiently large n. In particular
log A_i(g)=d log H+O(d log d). The box contains at most
(4H+1)^(s+1) marks. For an accepted mark g, let T be the
complete list of its nonzero prime-ideal labels. Uniform
residues modulo the product of its rational primes would
predict probability prod_(r in T) p_rational^(-1)
=1/(A_1(g) A_2(g)) of satisfying all these root conditions
(Vandermonde remains surjective: at most two labels per prime,
one in each field, and distinct residues). The predicted
number in the entire box is at most
\[
 (4H+1)^{s+1}\exp(-2d\log H+O(d\log d))=o(1).
\]
The actual count is at least one, since it includes g.
Therefore a uniform relative CRT asymptotic for these complete
factorization conditions is impossible, whenever any mark is
accepted. The required argument must average over many possible
factorizations or use another construction. This is a rigorous
obstruction to a termwise CRT proof, not to (COV) itself.

## 7. Reproducible finite test

Run verification/research/polynomial_marks.py (SymPy and mpmath).
The construction test uses N=1000036000099, d=54, ell=227,
and verifies the congruences and all 108 real-root sign brackets
with exact integers. The separate extraction test uses small
monic cubics X^3-19X-25 and X^3-X^2-5X+4 at m=6 modulo 77,
with target ell=5, marks of degree <=2 and coefficient bound 40,
and B=199. Direct gcd hits are deliberately suppressed in that
test so as to exercise the order certificate. It finds 123
retained marks and exact rational valuation rank 65 on the
65 observed/target rows. The resultant formula is independently
checked against SymPy on each retained norm. A numerical
logarithm solve proposes rational coefficients; the integer
valuation relation and final modular exponent are checked exactly:
5^2105280=1 mod 77, and the odd-part scan gives gcd(34-1,77)=11.
This verifies a finite algebraic/modular instance, not the
numerical log-rank decision, (COV), or any asymptotic guarantee.
