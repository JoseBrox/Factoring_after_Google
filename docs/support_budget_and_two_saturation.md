# Residual-support budgets and complete 2-primary extraction

**Status (27 November 2026):** proved a factorization-free exact
residual-span membership oracle, an explicit support-growth budget,
and complete extraction of the 2-primary subgroup represented by the
rational span of a pooled relation matrix. The latter can factor N
even when the residual-free rank is zero. The uniform subexponential
bound on support escapes, or uniform construction of a dependent
residual row, is **not proved**. The uniform deterministic half-scale
factoring theorem remains open. One-third work remains deferred.

This continues [the adaptive rank-or-residual theorem](adaptive_rank_or_residual.md).
It addresses the requested residual-span membership and dimension
problem directly, and also supplies a different sufficient endpoint
that need not wait for pure-base rank at all.

## 1. Exact factor-free saturation of a gcd-free basis

Given finitely many positive rational residuals, first reduce their
numerators and denominators to coprime integers. Compute a gcd-free
basis of all their numerator and denominator integers:
pairwise coprime d_j>1 and exact nonnegative integer exponents.
Use the gcd splitting procedure of the preceding notes. Replace each
d_j by its maximal perfect-power root e_j, multiplying that column's
exponents by the extracted power k_j, so d_j=e_j^k_j and e_j is not
a proper integer power.

The maximal power is found by testing integer exponents from
floor(log_2 d_j) down to two, using exact binary-search integer roots.
This is polynomial bit time in the input bit length. Coprimality of
distinct bases is preserved. Write nu for the true rational-prime
valuation map.

**Lemma 1.** The homomorphism
\[
 \iota:\mathbb Z^s\longrightarrow
       \bigoplus_{p\mid\prod_j e_j}\mathbb Z,\qquad
       z\longmapsto\sum_j z_j\nu(e_j)
\]
is injective and its image is saturated in its rational span.

Indeed the prime supports of the e_j are nonempty and disjoint.
Since e_j is not a proper integer power,
the gcd of its nonzero prime valuations is one.
If a rational number z_j times every one of these valuations
is integral, Bezout's identity gives z_j integral.
Apply this separately in each disjoint support. The proof uses
the unknown prime valuations only to establish the statement;
the algorithm never needs to find those primes.

This is stronger than ordinary gcd-free refinement when a basis
contains, for example, a fourth power of a prime or a composite
perfect power. It also handles composite power-free bases whose
nonzero valuations are not all one, such as 3^2*5^3.

### An exact fast residual-span membership oracle

Let the previous residual rows have rational-prime span W,
and encode them in the normalized e_j basis. Prepare a rational
row-echelon basis, retaining the representations in the old rows.
For a candidate residual rho=x/y in lowest positive terms:

1. Repeatedly divide x and y by each e_j, accumulating its integral
   numerator-minus-denominator exponent z_j.
2. If either leftover is not one, reject membership in W.
3. Otherwise solve the exact row-span problem for the vector z
   using the already prepared echelon basis.

**Theorem 2.** This test is necessary and sufficient for
nu(rho) in W. If it accepts, it also gives the rational
coefficients expressing nu(rho) in the old rows.

Proof. If nu(rho) is in W, it is in the rational span of the
nu(e_j). Its true prime coordinates are integral, so Lemma 1
forces every basis coefficient to be an integer. Uniqueness of
prime factorization now forces the two repeated-division
leftovers to be one (the reduced numerator and denominator
cannot cancel further). The exact linear test is therefore
equivalent to membership. Conversely any accepted representation
in basis coordinates gives the true valuation relation by
applying iota. End proof.

All tests have polynomial bit cost in the old pool description
and candidate sizes. In particular, for a fixed old pool we do
**not** have to recompute a gcd-free basis for every candidate
lattice point. This permits exhaustive use of the determinant-
scale rectangle and every admissible dyadic shift at each
adaptive separation attempt. An unsuccessful membership test
can still share most of its prime support with the pool:
membership concerns proportional valuations within each old
composite base as well as the linear span across bases.

## 2. A precise, computable support budget

The previous adaptive theorem guarantees that each completed
attempt either gives a new pure-base relation or adds an
independent residual direction (or returns a factor).
Suppose the small base contains all primes at most Z which
are units modulo N; the sieve returns any proper gcd first.
Every retained residual therefore has all its primes >Z.

Let S_t be the product of the normalized gcd-free bases of the
retained independent residual rows after attempt t. Its prime
support is exactly the union of their true supports. Set S_0=1
for an empty pool. To remove from a positive integer x all primes
in the support of S, repeatedly divide x by gcd(x,S) until that
gcd is one; denote the resulting integer by out_S(x).
This is an exact polynomial-bit-cost operation without
factoring either integer.

For a newly retained independent residual rho=x/y define
\[
 c_t=\operatorname{out}_{S_{t-1}}(x)
       \operatorname{out}_{S_{t-1}}(y).
\]
For a pure-base rank gain set c_t=1. Let C_t=prod_(i<=t)c_i.
Each outside-base prime at its first appearance divides c_i
for that attempt, and no prime is new at two different
attempts. Thus
\[
 \operatorname{rad}(S_t)=\operatorname{rad}(C_t)\mid C_t.
\]
The radicals are used only in the proof. The algorithm stores
the ordinary integer products or their exact descriptions.

**Theorem 3 (support-budget bound).** If r_t is the independent
residual rank after t completed attempts, and d_t the pure
base rank, then
\[
 r_t\le\omega(C_t)\le
       \left\lfloor\frac{\log C_t}{\log(Z+1)}\right\rfloor,
 \qquad d_t=t-r_t.                                      \tag{1}
\]
For Z=1 the same formula uses the lower bound 2 on primes.
Indeed the residual rows are independent in a vector space
with dimension at most the number of distinct true primes
in their support. Each such prime exceeds Z, and its product
with the other distinct primes divides C_t. The second
identity is the previous rank-or-residual theorem.

A sharper computable upper bound on r_t uses the product of
the first R distinct primes greater than Z instead of (Z+1)^R.
If that product exceeds C_t, then r_t<R. Prime generation
for this test can use the deterministic sieve, with cost
polynomial in Z and the bit length of C_t by the ordinary
PNT bound for the R-th next prime. All comparisons can be
made with integers, without approximating logarithms.

For example, if all further residuals after a finite prefix
remain supported on S_t, their independent rank is forever
bounded by log(C_t)/log(Z+1). Hence at most that bound plus
the base dimension many completed total attempts can occur
before full pure rank (or a factor). More generally, if there
are at most K support-escaping retained rows, and every
residual coordinate is <=H, then C_t<=H^(2K) and
\[
 r_t\le\frac{2K\log H}{\log(Z+1)}.                        \tag{2}
\]
A uniformly bounded K=exp(O(b)), or a directly proved bound
log C_t<=exp(O(b)), over the necessary attempts would give
the requested subexponential rank budget at the half scale
b=Theta(sqrt(log N log log N)). The previous separation
theorem supplies the resulting strict rank gains.

**The missing uniform assertion is a bound on these escapes
or their total log mass before the prescribed number of
attempts.** Equation (1) is an a posteriori bound, not a
proof of that assertion. Taking t itself to be half-scale
makes the trivial bound C_t<=H^(2t) half-scale in bit length,
but does not guarantee rank gain: the right side of (2)
can then exceed t. We do not use this circular argument.

### Support-aware all-shifts selection

Use the previous exact dual-weight exponent separation rule.
For its new multiplier, enumerate the entire primitive
rectangle at each j=0,...,J, not merely the first balanced
shift. A proper coordinate gcd already factors N. The
primitive-rectangle enumeration theorem handles skew and
collinear cases too, so the total list still has half-scale
size. At least one balanced shift supplies a primitive unit
pair or a proper gcd.

Apply Theorem 2 to each stripped ratio and immediately take
a member of W if one exists. The separation theorem turns
every such membership into a strict pure-rank increase.
If none exists, choose the ratio minimizing the exact
integer c_t above, with a deterministic height tie-break.
In particular a support-preserving independent direction
is preferred to any support escape. There is no claim
that the greedy minimum is globally optimal over future
attempts.

The independent residual list is then augmented only once
per attempt. Its base exponents, dual weights and rank
certificates have the bit bounds from the previous adaptive
theorem. With H<=sqrt(N) B^C, B=2^b, and at most B^D attempts
for fixed constants C,D, the enumeration, membership
tests, support stripping and exact rational arithmetic
still have exp(O(b)) total bit cost. One can also restrict
or augment candidate sets using the proven local CRT
completion bounds; the finite experiment below exhausts
the dyadic shifts instead of making new CRT prescriptions.

## 3. A different endpoint: 2-primary extraction with nonzero residuals

Ordinary pure-base rank is stronger than what is needed for
a proper gcd. We can exploit every collected relation even
when its residual row is independent over the rationals.

Take the full pooled signed relation matrix, including the
small base and every residual gcd-free basis element, now
made power-free as in Section 1. Denote the disjoint-support
integer bases by g_1,...,g_m, all coprime to odd N, and
\[
 \varphi:\mathbb Z^m\longrightarrow
       (\mathbb Z/N\mathbb Z)^\times,\qquad
 \varphi(v)=\prod_i g_i^{v_i}\bmod N .
\]
Each input integer row v has verified image in {1,-1}.
Choose any rationally independent subset of the rows and
let L be the integer row lattice generated by twice that
subset. Then phi(L)={1} and the rational span is unchanged.
Put
\[
 W=(\mathbb Q L)\cap\mathbb Z^m,\qquad
 L_2=\{v\in\mathbb Z^m:\exists k\ge0,\ 2^k v\in L\}.
\]

By Lemma 1 applied to all bases, using composite power-free
gcd-free columns loses no integral vector in the true-prime
rational span. In particular roots that require dividing
an old composite power have not been silently missed.

**Lemma 4.** The image phi(L_2) is exactly the 2-primary
subgroup of phi(W).

One inclusion follows from phi(L)=1. Conversely, for v in W
whose image has 2-power order, there is a positive integer
d with dv in L. Write d=2^k t with t odd. Then tv in L_2.
Raising phi(tv) to an inverse of t modulo the 2-power
order of phi(v) recovers phi(v), so the latter lies in
phi(L_2). The same argument covers every element of
the 2-primary subgroup of phi(W). This proves the equality.

Thus it suffices to compute only the 2-saturation, not full
Smith normal form or factorization of a determinant.

### Elementary polynomial-cost 2-saturation

Keep an independent integer row basis for the current
lattice. Find a nonzero binary dependency among its rows
modulo 2 by ordinary F_2 elimination. Its selected rows
have an even integer sum. Replace any one of the selected
rows by half that sum; leave the others unchanged.

The new lattice contains the old one, since the replaced
old row equals twice the new row minus the other selected
rows. It is contained in the 2-saturation of the old
lattice and has the same rational span. The determinant
of the row transformation is 1/2, so every nonzero
maximal minor is divided by two. Fix any initial nonzero
maximal minor. Its initial bit length bounds the number
of replacements. Hadamard's inequality gives a bound
O(r(log M+log(r+1))) when there are r independent rows
and the initial entry bound is M>=2. At a replacement
the maximum absolute entry increases by at most r, so
the eventual entry bit lengths remain polynomial.

When the current rows are independent modulo 2, their
lattice is 2-saturated: if 2v is an integral combination
of the rows, reducing modulo 2 shows that all combination
coefficients are even, so v is already in the lattice.
Iterate the assertion to remove any power of two. The
successive inclusions in L_2 and the final saturation
therefore prove that the final lattice is exactly L_2.

After h replacements every current generator image is
killed by 2^h, inductively, since the square of the new
image is a product of old images. All powers and images
can be evaluated by binary modular arithmetic. The whole
calculation has polynomial bit cost in the input matrix
and integer base sizes. The proof does not require the
factorization of N or of any residual. The finite tests
also verify the number of replacements against the
2-adic valuation of the gcd of all initial maximal minors;
enumerating all minors is **only a small-test oracle**,
not part of the polynomial-cost algorithm.

### Complete extraction from the 2-primary subgroup

Given finitely many units z_i killed by 2^h, first compute
their exact 2-power orders by repeated squaring. If any
terminal nonidentity involution is other than -1 modulo N,
take gcd(z-1,N) to obtain a proper factor.

Otherwise choose a generator g among them of maximal
order 2^k. If k=0 all images are one. If k>0 then
g^(2^(k-1))=-1 mod N. For every other generator u,
perform the following bit-lifting computation, beginning
with v=u. At step j=0,...,k-1 we have
v^(2^(k-j))=1. Compute z=v^(2^(k-j-1)).
If z=1, leave v unchanged. If z=-1, replace v by
v*g^(-2^j). In that case its tested power becomes one
since g^(2^(k-1))=-1. If z is any other involution,
return gcd(z-1,N). In the absence of a factor the
invariant holds at the next step and the final v is one.
The accumulated bits explicitly express u as a power
of g.

**Theorem 5 (complete 2-primary readout).** In polynomial
bit time in the pooled relation description, the
algorithm either factors N or certifies that the image
of the entire integral rational span W has cyclic
2-primary subgroup, with only the involutions 1 and
possibly -1. It finds a proper factor whenever that
subgroup contains a nontrivial square root of unity.

This is precisely complete for the stated source of
2-primary information: the known row span and its
integer saturation. It does not assert that other
operations on the collected data could not factor N.
In particular, if a vector in W has differing local
two-primary order behavior, its 2-primary component
can supply a nontrivial involution and the complete
readout will find one. Testing each original generator
alone would not justify this completeness: combinations
can have an involution different from the individual
maximal-order involutions, which is why the bit-lifting
stage above is included.

The extraction cost stays within half scale for a
half-scale list of verified raw relations with the
previous polynomial exponent bit bounds. It may be
run in parallel with, or after each round of, the
pure-rank elimination. In fact the saturation lattice
depends only on the rational span, not on choosing
a particular independent subset.

### A useful rank-zero example

Use N=10403, H=102, small base {2}. Enumerating the
primitive rectangle at the already prescribed
target T=27 and dyadic shift j=2 includes (x,y)=(98,25).
The exact congruence is
\[
 2^{29}98=25\bmod10403 .
\]
The outside-base valuation of this row is
2 nu(7)-2 nu(5), which is nonzero. Consequently
even this one-row rational space has **zero
residual-free rank**. But halving its integer
exponent vector yields
\[
 z=2^{15}\cdot 7/5=102\bmod10403,\qquad z^2=1\bmod10403,
 \qquad \gcd(z-1,10403)=101.
\]
Here the actual prime factors 5 and 7 can be
obtained from the residuals 25 and 49 solely by
perfect-power extraction. The one-row relation
was found by the earlier unmodified target/shift
enumeration; the input factorization was not used
to generate it.

The number of parity dependencies or the 2-adic
saturation index alone cannot guarantee a factor.
For example the integral span of (1,1,1) at
bases (2,3,13) modulo 77 has image one because
2*3*13=78. Multiplying its known relation by
2^j makes its lattice index arbitrarily large
while the saturated image remains trivial.
This is a precise caution about using parity
rank deficiency as a replacement for the
missing uniform coverage theorem.

## 4. Verified tests and unsuccessful cases

The following exact finite tests were executed locally with
Python 3.13.5, using standard-library integer/rational arithmetic
and the previously checked lattice code. The new script and its
local dependencies match their committed Git blobs byte-for-byte.

### Power-free bases and 2-primary extraction

[verification/research/two_primary_pool.py](../verification/research/two_primary_pool.py)

Git blob: 4b46eaf2b3ced5db0aefd753bcb4259093a5e7c6

SHA-256: b101aafe0687177279bedd875439a9fa48e719af22bbd1dcdb64cdb5293dd25d

Observed output:

    power-free gcd basis: 998 integer checks and grouped composite fixture
    2-group extraction comparisons: 4832
    2-saturation index comparisons by maximal-minor gcd: 150
    zero-pure-rank saturation fixture: 10403 H 102 P [2] raw rows [(2, 27, 0, 41, -77), (2, 27, 1, 79, -43), (2, 27, 2, 79, -86), (2, 27, 2, 98, 25)] rank 3 2-steps 4 factor 101
    single-row half exponent root: 102 factor 101
    zero-rank prefixes checked: 4
    adaptive saturation: 100160063 residual rank 25 pure rank 0 2-saturation steps 25 cyclic order 2 factor None
    adaptive saturation: 1000036000099 residual rank 25 pure rank 0 2-saturation steps 25 cyclic order 2 factor None

The 4,832 subgroup tests use independent exhaustive finite subgroup
enumeration for small moduli, verifying that a factor is obtained
if and only if the tested generated 2-group has a nontrivial
involution. The 150 index tests compare the exact number of
2-saturation replacements against independently computed maximal
minor gcds, on relation matrices deliberately manufactured with
a known group annihilator solely for that unit test. The actual
N=10403 fixture and the adaptive pools are generated by the
previous exact relation algorithms without the input factors.

The last two fixtures are important negative evidence: running
the stronger extractor on the two previously stalled 25-call
local-CRT adaptive pools does not give a factor. Their complete
2-primary readout yields only the cyclic sign group. The new
algorithm is a strictly broader endpoint, not a uniform guarantee.

### Residual-span membership and support-aware search

[verification/research/support_budget.py](../verification/research/support_budget.py)

Git blob: d92c670da06efb8dadb27bc3967bf99bf6fad3ed

SHA-256: 9cf119043da1de7ab2360aae82e56fb505f8d111981c431ffed7cf8a585373d8

Observed output:

    factor-free membership comparisons: 1199
    support-aware: 100160063 P 17 H 30024 recycle False residual rank 1 pure rank 0 support escapes 1 support-only directions 0 new support log2 upper bound 10 max exponent bits 6 factor 10007 method lattice gcd
    support-aware: 100160063 P 17 H 30024 recycle True residual rank 24 pure rank 7 support escapes 23 support-only directions 1 new support log2 upper bound 170 max exponent bits 100 factor 10007 method pure relation
    support-aware: 1000036000099 P 17 H 3000054 recycle False residual rank 40 pure rank 0 support escapes 39 support-only directions 1 new support log2 upper bound 501 max exponent bits 228 factor None method None
    support-aware: 1000036000099 P 17 H 3000054 recycle True residual rank 18 pure rank 0 support escapes 18 support-only directions 0 new support log2 upper bound 264 max exponent bits 100 factor 1000003 method lattice gcd

The membership comparisons include grouped composite bases,
partial supports, negative cases and exact integer combinations
of old ratios. They are compared to the earlier independent
global gcd-refinement dependency solver, with further direct
coefficient checks. Every accepted pure relation is checked
by exact modular powering after doubling. Every factor returned
by a gcd is independently checked to divide N properly.
The support log2 upper bound is the bit-length envelope of
the product C_t in (1), not a count of unknown actual primes.

The all-shifts support-aware method with recycling obtains
seven pure rank gains in 31 completed attempts at N=100160063,
where the earlier first-balanced-shift adaptive dual rule had
zero pure rank after 40 attempts. The larger N is factored by
a lattice coordinate gcd with recycling, not by a pure-rank
gain or the new saturation extractor. Without recycling its
40-call search still has zero pure rank. These distinctions
prevent treating the finite successes as evidence for an
asymptotic rank lower bound.

Local dependency hashes: primitive_ratio_lattice.py
446b6eb7e1c46388db7109d4f73b61665c071e59;
target_power_balance.py deb87f2c10bd889c3e905a4c58a4def66f13d33b;
pooled_shift_relations.py 2c232588e5f6304a96c456e35245171be6a2f21a;
adaptive_pooled_rank.py 1839092a89b309131323e5a8d78b84099c33fd10.
The last file now matches the tested local executable source
after normalizing its final explanatory comment. This does not
retroactively assert byte identity for the historical test
receipt in the earlier adaptive note.

## 5. Next priority

The previous greedy gcd-overlap approach has been replaced
by exact span membership and explicit support escape accounting.
Every successful membership still implies pure rank increase
by the dual separation theorem. Complete 2-primary saturation
should be used alongside that driver because it strictly
weakens the required pure-rank endpoint.

The requested uniform residual bound would follow from a
constructive bound on the cumulative new-support budget
of the adaptive search. The present exhaustive all-shifts
rule proves that it takes the minimum support escape within
its specified candidate menu, **not** that those minima
have small cumulative mass. Alternatively seek a uniform
construction of a pooled span with a nontrivial 2-primary
involution. Neither of these existence assertions has been
proved, and the unsuccessful experiments are retained.

**No uniform deterministic L_N[1/2,O(1)] general factorer
or new Lean milestone is claimed.**
