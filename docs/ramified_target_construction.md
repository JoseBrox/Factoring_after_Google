# Prescribed ramified target: eliminating the initial ideal-rank problem

**Status (26 November 2026): proved written construction, with an exact
finite arithmetic check.** This eliminates the need to obtain the
particular target valuation vector by a smoothness argument. It does
not yet eliminate the unit-log membership problem or establish
uniform deterministic factoring at the half scale.

The appropriate next target is the single vector membership in
[the exact targeted certificate criterion](targeted_half_scale_search.md),
rather than the full covariance hypothesis of the original monic
polynomial-mark proposal.

## 1. Construction

Let \(n\) be the bit length of an odd composite \(N\), and let \(d\)
be the least power of two at least \(8\sqrt n\). Put
\[
 t=\lfloor\sqrt{\lfloor\log_2 n\rfloor}\rfloor,\quad
 k=\lceil d/t\rceil,\quad J=\lceil20d/t\rceil,\quad r=d-k-J,\quad
 m=2^{\lceil n/k\rceil}.
\]
Work for sufficiently large \(n\), so in particular \(r\ge2\).
Then \(r=d-O(d/\sqrt{\log n})\), \(r<d\),
\(m^k\ge2^n>N\), and \(\log m=O(\sqrt{n\log n})\).
All parameters are obtained by integer arithmetic.

Let \(\ell\) be an odd prime polynomially bounded in \(n\).
If \(\gcd(\ell,N)>1\), check and return a proper divisor.
Otherwise put
\[
 R_j=3\ell(2j+1)\ (1\le j\le d),\quad
 P(X)=\prod_{j=1}^d(X-R_j),\quad
 Q(X)=\prod_{j=1}^r(X-R_j).
\]
The centers are odd multiples of \(\ell\), positive, distinct and
uniformly separated. Check \(\gcd(m-R_j,N)\) for all \(j\).
For all sufficiently large \(n\), \(0<m-R_j<N\), so any nonunit
gives a proper divisor. If none occurs, \(4\ell Q(m)\) is a unit
modulo \(N\).

Choose \(h_{1,0}=0\), and choose \(h_{2,0}\) from \(\{0,2\ell\}\)
so that
\(P(0)+1+Q(0)h_{2,0}\equiv2\pmod4\).
This is possible because \(P(0),Q(0)\) are odd.
For \(c_1=\ell,\ c_2=1\), let \(T_i\) be the base-\(m\)
digit polynomial of the integer in \([0,N-1]\) congruent to
\[
 -(P(m)+c_i+Q(m)h_{i,0})(4\ell Q(m))^{-1}\pmod N .
\]
The degree of \(T_i\) is less than \(k\). Set
\[
 f_i(X)=P(X)+c_i+Q(X)(h_{i,0}+4\ell T_i(X)).
\]
These monic polynomials have degree \(d\); the corrections apart
from \(c_i\) have degree at most \(d-J-1\), and
\[
 f_i(m)=0\bmod N,\qquad
 f_1(R_j)=\ell,\quad f_2(R_j)=1\quad(1\le j\le r).        \tag{1}
\]

For the first field, all nonleading coefficients are divisible
by \(\ell\). Its constant is \(\ell\bmod\ell^2\), since
\(P(0)\) is a multiple of \(\ell^d\) and \(Q(0)\) a multiple
of \(\ell^r\). Hence \(f_1\) is Eisenstein at \(\ell\).
It is irreducible over \(\mathbb Q\), and over \(\mathbb Q_\ell\)
it defines a totally ramified extension of degree \(d\).
There is exactly one prime \(\mathfrak l\) above \(\ell\),
its norm is \(\ell\), and \((\ell)=\mathfrak l^d\).

For the second field, because \(d\) is a power of two,
\(P(X)\equiv(X+1)^d=X^d+1\pmod2\).
Its correction is even, and the chosen constant is \(2\bmod4\).
Thus \(f_2\) is Eisenstein at 2, hence irreducible. It need not
be inert at \(\ell\): the exact norm-one condition in (1) already
makes every specified second-field mark a unit.

## 2. Effective real-root and height bounds

Put
\[
 \eta=[4(\ell d)^{\lfloor J/4\rfloor}]^{-1}.
\]
At \(X=R_j\pm\eta\), the product of distances to the other
centers is at least \((3\ell)^{d-1}(j-1)!(d-j)!\).
Consequently
\[
 \log|P(X)|\ge(d-J/4)\log(\ell d)-O(d+\log(\ell d)).
\]
This uses \((j-1)!(d-j)!\ge(d-1)!/2^{d-1}\) and
\(\log((d-1)!)=(d-1)\log d-O(d+\log d)\).
The log of an upper bound for the absolute correction
\(c_i+Q(X)(h_{i,0}+4\ell T_i(X))\) is at most
\[
 (d-J)\log(\ell d)+O(d+\log m+\log(\ell d)).
\]
Indeed all the \(Q\) factors are \(O(\ell d)\), the digit
coefficients are bounded by \(m-1\), and the remaining
degree is less than \(k\). The strict margin is
\((3/4)J\log(\ell d)-O(d+\log m+\log(\ell d))\).
Using the explicit bounds
\[
 J\ge20d/t,\qquad
 \log(\ell d)\ge \tfrac12(\log2)t^2,\qquad
 \log m\le(\log2)(dt/64+1),
\]
the term from \(\log m\) in the correction is smaller than
the leading margin (its coefficient is one, from the bound on
the base digits), and the remaining \(O(d+\log(\ell d))\)
terms are smaller still. In particular the margin tends to
infinity. Opposite signs persist on both sides of every center.
There are \(d\) disjoint sign brackets for a degree-\(d\)
polynomial, so all roots \(\theta_{i,j}\) are real and simple.
These estimates can alternatively be verified by exact
rational endpoint signs for each constructed pair.

The coefficient bit lengths and bracket bit lengths are
polynomial in \(n\), and all construction, sign checks and
root approximations have polynomial bit complexity at any
polynomial requested precision. The only exceptional small
input range in this construction is finite; the general
factoring complexity is still not established.

## 3. The particular valuation target is solved exactly

Use the marks \(g_j(X)=X-R_j\), \(1\le j\le r\).
Their evaluations are units modulo \(N\) by the gcd guards.
Since \(d\) is even and the polynomials are monic,
\[
 \operatorname{Norm}_{K_1/\mathbb Q}g_j(\theta_1)=\ell,\qquad
 \operatorname{Norm}_{K_2/\mathbb Q}g_j(\theta_2)=1 .
\]
The first principal ideal is exactly \(\mathfrak l\)
(because its norm is the rational prime \(\ell\)), and the
second element is an algebraic unit. Therefore the valuation
matrix of the specified marks has just one nonzero row:
\[
 V=(1,1,\ldots,1),\qquad b=(d).
\]
The desired rational valuation-image condition is now
**unconditional**: \(c_0=(-d,0,\ldots,0)\) and \(E_0=1\)
give \(Vc_0=-b\). No primes in the norms need to be discovered
or tested for smoothness. The target is ramified, with
the ramification index correctly included in \(b\).

Let \(L_j\) denote the projected paired log vector of \(g_j\).
The particular log vector
\[
 x=dL_1
\]
belongs to the product log-unit lattice (the units represented
by its negative are
\(\ell/g_1(\theta_1)^d\) and \(1/g_1(\theta_2)^d\)).
For \(2\le j\le r\), the ratios
\[
 u_{i,j}=\frac{\theta_i-R_j}{\theta_i-R_1}
\]
are paired units. They have the same modular images
\((m-R_j)/(m-R_1)\) through the localized orders. Their
paired log vectors are \(L_j-L_1\). Thus the one-vector
membership criterion starts with \(r-1\) explicitly available
kernel columns and a known target. Arbitrary additional
marks can be used to enlarge the valuation kernel; they need
not meet any squarefree-density or full-covariance condition.

## 4. Why the explicit units alone do not suffice

One must not infer target log cancellation simply from the
large number of shared units. In fact the \(r\) second-field
log columns of the above specified marks are independent
for large \(n\).

Put \(R=10\ell d\). Write \(B\) for the \(d\)-by-\(r\)
second-field full log matrix; its columns already have sum
zero since their norms equal one. For \(i\ne j\), the
distance \(|\theta_{2,i}-R_j|/R\) is bounded above by 1 and
below by \(c|i-j|/d\) for a fixed positive constant \(c\).
The factorial bound
\(\sum_{a=1}^d\log(d/a)=O(d)\) implies that the off-diagonal
errors in \(B_{ij}-\log R\) have both row and column absolute
sums \(O(d)\). By the norm-one identity,
\(B_{jj}=-(d-1)\log R+O(d)\). Consequently
\[
 B=(\log R)(\mathbf 1_{d\times r}-dI_{d\times r})+\mathcal E,
 \qquad \|\mathcal E\|_{2\to2}=O(d),
\]
where \(I_{d\times r}\) consists of the first \(r\) columns
of the identity matrix. The operator norm bound follows
from the square root of the product of maximum row and
column absolute sums, including the diagonal errors.
The Gram matrix of the leading term is
\((\log R)^2(d^2I_r-d\mathbf 1_{r\times r})\);
its smallest eigenvalue is \(d(d-r)(\log R)^2\).
As \(d-r\ge20d/t\) and \(\log R\gg\log n\),
the leading smallest singular value is \(\gg
d\log R/\sqrt t\), which dominates \(O(d)\).
Therefore \(B\) is injective.

This proves multiplicative independence modulo torsion
of the \(r-1\) displayed ratio pairs. It also proves that
the specified marks alone cannot solve \(Lc=0\) with
\(Vc=-E b,\ E>0\): even the second-field log equation
would imply \(c=0\). Including rational constants does not
fix this: their projected logs vanish, but their second-field
prime-ideal valuations must vanish too, and the specified
second-field marks are units.

This obstruction is intentional and localized. The new
construction eliminates the initial target-prime ideal
supply, not the remaining paired-unit cancellation.

## 5. Half-scale target search with the ramified prime included

The exact target criterion and large-prime elimination theorem
from [the targeted search](targeted_half_scale_search.md)
continue to apply. They concern genuine prime-ideal valuations
in the full integer rings, and the ramification index is
part of the target. At the one specially ramified prime
\(\ell\) in field 1 no local factorization algorithm is needed:
\(v_{\mathfrak l}(\alpha)=v_\ell(|\operatorname{Norm}\alpha|)\)
because it is the unique prime and has residue degree one.
Other primes dividing the polynomial discriminants can still
be excluded, unless a separate local algorithm is justified.
In field 2 the specified marks have norm one; for additional
marks one can safely require that their second-field norms
be prime to every bad prime, including \(\ell\) if necessary.

Enumerate irreducible marks of degree at most \(s\) and
height at most \(H'\) with \(s(s+\log H')=O(\sqrt{n\log n})\),
and include the explicit linear marks (enlarging \(H'\) by
the polynomial size of the centers if needed). Trial division
of their norms to the resultant cutoff suffices to compute
all the allowed valuation rows. The special ramified prime
is handled as just described. The entire finite target search,
including the rank-deficient exact log-membership test, has
bit complexity \(L_N[1/2,O(1)]\), or \(\exp(O(\sqrt n))\)
for example with \(s=\lceil n^{1/4}\rceil\) and \(H'=2^{O(s)}\).
It always terminates with a verified exponent, a factor
from a gcd guard, or a rigorous absence of (T) in the searched
mark family.

The uniform analytic input for obtaining a separating target
prime is the existing verified Dirichlet/zeta zero-free strip
and our written smoothed character estimate. Enumerating a
sufficiently large polynomial dyadic interval of odd primes
provides opposite quadratic signs or a nonsquare at the
larger local two-adic valuation, as proved in the polynomial-mark
note. No new conjecture about the distribution of ramified
prime targets is needed for the construction.

**Still open:** for each surviving \(N\), prove that some
separating target's particular vector \(x\) lies in the log
span of the integral valuation kernel after the additional
bounded marks are included. The target ideal equation now
holds by construction, not by a smooth-resultant rank theorem.
The new problem is one specified paired-unit relation. It is
not known whether it always exists in this height budget.

## 6. Finite arithmetic check

The [ramified target fixture](../verification/research/ramified_target.py)
uses \(N=77,\ell=5,d=8,k=3,r=3\), with enlarged odd integer
center spacing for this small fixture. It checks the exact
CRT identities, both Eisenstein conditions, all 16 real-root
sign brackets, the six prescribed resultant norms, and the
target valuation equation with \(E_0=1\). It does not assert
a successful order certificate; the log cancellation is still
needed. The fixture uses manually chosen small degree/spacing
parameters rather than the eventual \(r=d-k-J\) formula.

This note is mathematical progress towards the half-scale
goal, not an unconditional general factorer or an additional
completed Lean milestone. The one-third program is deliberately
not being pursued before the half-scale coverage problem is solved.

## Subsequent audit

The [short-unit/rank obstruction](half_scale_unit_rank_obstruction.md)
shows that on a density-one set of balanced semiprimes no family
of polynomial-log-height shared units can span the target vector,
regardless of its cardinality. Any successful small-mark family
must have finite valuation rank Omega(n/log n), so adding a few
ordinary explicit units is not a valid uniform strategy. The
[full-degree factor-refinement search](full_degree_factor_refinement.md)
removes norm-factorization and bad-prime restrictions from the
exact decision procedure and permits more marks at half scale.
Uniform target coverage remains unproved.
