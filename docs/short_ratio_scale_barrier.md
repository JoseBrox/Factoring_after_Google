# A volume–smoothness barrier for direct rational-fibre methods

**Status:** proved, unconditional counting obstruction for a specified architecture; not a lower bound on integer factoring. 27 November 2026.

This continues the [short-ratio lattice aggregation](primitive_ratio_lattice_aggregation.md), [narrow-band streaming](narrow_band_streaming_atoms.md), and [labelled-rank](depth_free_character_rigidity.md) routes. It explains why changing only the smoothness scale of those constructions cannot produce an exponent below \(1/2\). The obstruction also applies to a succession of smooth rational certificates when their final reduced height remains at the determinant scale.

## 1. Uniform support theorem

Let \(N\ge 3\), \(t=\ln N\), \(B=e^b\), and \(u=t/b\). Assume \(b=t^{\alpha+o(1)}\) for some fixed \(0<\alpha<1\). A positive integer is \(B\)-smooth if all its prime divisors are at most \(B\); include 1. Let \(S\) be any set of unit shifts modulo \(N\), of cardinality \(K\), and \(M\ge1\).

Define the covered unit residues to be those of the form
\[
a=s\,y/x\bmod N,\qquad s\in S,\qquad
x\ge1,\quad y\ne0,\quad \gcd(xy,N)=1,\quad
x|y|\le M,
\]
where \(x,|y|\) are \(B\)-smooth. No rectangular box, coprimality between numerator and denominator, squarefreeness, or prime-band restriction is required. The shifts can depend arbitrarily on the public modulus, but the assertion counts coverage of the whole unit group by this one set of shifts.

For every \(0<\sigma<1\), write
\[
Z_B(\sigma)=\prod_{p\le B}(1-p^{-\sigma})^{-1}.
\]
Then the fraction \(F\) of units covered satisfies
\[
F\le\min\left\{1,\frac{2K M^\sigma Z_B(\sigma)^2}{\varphi(N)}\right\}.
\tag{1}
\]

Indeed, each admissible positive pair \((x,|y|)\) contributes at most two residues per shift. Dropping the unit conditions only increases the number of pairs. Since \(1\le (M/(x|y|))^\sigma\) whenever \(x|y|\le M\), extending the resulting sum to all positive smooth pairs gives \(M^\sigma Z_B(\sigma)^2\). This is a direct Rankin bound, using only unique factorization and finite Euler products.

In particular, put \(M=N e^h\), \(h\ge0\), and take \(\delta=(\ln u)/b\), \(\sigma=1-\delta\). For all sufficiently large \(N\), \(\delta=o(1)\) and \(\sigma\ge3/4\). The uniform estimate
\[
\ln Z_B(1-\delta)=O\left(\ln b+\frac{u}{\ln u}\right)
\tag{2}
\]
follows as below. Also, if \(N\) has \(m\) distinct prime divisors in increasing order \(p_i\), then \(p_i\ge i+1\) and hence
\[
\varphi(N)/N=\prod_i(1-1/p_i)\ge 1/(m+1),\qquad m\le t/\ln 2.
\]
Consequently
\[
F\le\min\left\{1,\exp\left(
h+\ln K-u\ln u+
O(\ln t+\ln b+u/\ln u)\right)\right\}.
\tag{3}
\]
The omitted term \(-\delta h\) in the exponent is nonpositive.

### Proof of (2)

Expand the logarithm of the finite Euler product into positive terms. The prime-power terms of order at least 2 are \(O(1)\) uniformly for \(\sigma\ge3/4\), by comparison with \(\sum_{n\ge2}n^{-3/2}\). For the first powers, Chebyshev's elementary upper bound \(\pi(z)\ll z/\ln z\) and partial summation give
\[
\sum_{p\le B}p^{-1+\delta}\ll \frac{e^{\delta b}}{b}
 +\int_{\ln 2}^b \frac{e^{\delta v}}{v}\,dv.
\]
The integral up to \(1/\delta\) is \(O(\ln b)\). In the remainder substitute \(w=\delta v\); the integral is bounded by
\(\int_1^{\ln u}e^w\,dw/w\ll u/\ln u\), as is seen by splitting at \((\ln u)/2\). The endpoint term \(u/b\) is also \(O(u/\ln u)\). This proves (2), with absolute constants for all sufficiently large parameters in the specified range. No smooth-number asymptotic, zero-free region, GRH, or distribution hypothesis is used.

## 2. Consequences for the project

**Corollary A (fixed exponent below one half).** Suppose \(K\le B^D\) and \(M\le NB^C\) with fixed \(C,D\ge0\). Then for every fixed \(0<\alpha<1/2\),
\[
F\le\exp(-(1-o(1))u\ln u).
\]
This follows from \(b=o(u\ln u)\) and the lower-order error in (3). In particular, for the conventional \(L_N[1/3,c]\) smoothness scale \(b=(c+o(1))t^{1/3}(\ln t)^{2/3}\), the fraction is at most
\[
\exp\left(-\left(\frac{2}{3c}+o(1)\right)t^{2/3}(\ln t)^{1/3}\right).
\]
An expected number of independent uniform unit queries to find such a representation is at least the reciprocal of this bound (or infinite for empty support). This applies only to methods which require one of these certificates; successful factor exits by another mechanism are not counted.

**Corollary B (half-scale constant test).** For \(b=(c+o(1))\sqrt{t\ln t}\) with \(c>0\), one has \(u\ln u/b\to 1/(2c^2)\). Thus if \(C+D<1/(2c^2)\), the density is at most
\[
\exp\left(-\left(1/(2c^2)-C-D+o(1)\right)b\right).
\]
Any proposed direct dense short-ratio method needs to check this inequality before optimizing constants. The reverse inequality is not a sufficient coverage theorem.

**Corollary C (global height and multilevel rational certificates).** Any product of finitely many signed \(B\)-smooth rational unit ratios, when reduced to lowest terms, remains a signed \(B\)-smooth rational unit ratio. If its final numerator times its final absolute denominator is at most \(M\), then it belongs to the same support as in (1). The number of constituents, the intermediate heights, and the amount of cancellation do not enter the bound. Hence merely allowing more rational stages or pooling within the *final* height budget does not evade Corollary A. For several shifts, use the number of distinct possible total shifts, rather than the number of stages.

**Corollary D (necessary height inflation or shift budget).** For a family of supports with density bounded below by any fixed positive constant, (3) implies
\[
h+\ln K\ge (1-o(1))u\ln u.
\]
This remains necessary for density \(\exp(-O(b))\) when \(\alpha<1/2\). At the one-third scale this is a two-thirds-scale logarithmic cost/height requirement. It is a necessary combinatorial condition, not a runtime lower bound for processing a larger height implicitly.

## 3. Exact scope and next research target

The elementary primitive-lattice enumerator of the project uses boxes of product height \(XY\le NB^{O(1)}\). Any menu of \(B^{O(1)}\) such boxes and shifts satisfies the theorem, even if the choice among the menu is adaptive. The theorem handles arbitrary signed smooth pairs and therefore also all of the more restricted balanced-band witnesses. It does not prohibit:

- a deterministic algorithm hitting a special sparse set, rather than sampling a uniform unit;
- a shift generated from a query by a method whose total range exceeds the stated budget;
- nonsmooth residual relations or certificates whose final reduced height exceeds the bound;
- independent algebraic fields or degree-growing number-field descent;
- an algorithm computing a large-height aggregate without enumerating the individual certificates.

The last two possibilities, together with a uniform deterministic half-scale selector, are now the prioritized research directions. The finite-group character estimates are no substitute for this elementary support calculation: a purported direct uniform-density lemma at smaller scale must fail at least one premise of the theorem.

Catalogue connections (private archive's November 25 family routing): N31 exact analytic floors, N42 smoothness-free relations, N45 incomplete character sums, N46 arithmetic Fourier methods, N47 recursive reductions, N48 deterministic covering, O25 lattice methods, O28 smoothness-free relations, O29 recursive large cofactors, O43 collisions, O50 spectral methods, and O52 NFS. This is a structural screen at the family level, not a re-audit of all 1,514 individual catalogue entries.

**Decision:** target a uniform deterministic \(L_N[1/2,O(1)]\) theorem first, with the arithmetic-specific hitter as its missing component. In parallel, seek a rigorously charged degree-growing descent that escapes the above architecture for randomized one-third or better. A polynomial-time algorithm is a long-range objective, not a proved or assumed input.
