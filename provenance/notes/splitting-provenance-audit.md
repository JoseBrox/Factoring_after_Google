# Order splitting, provenance, and a retained local-relation construction

25 November 2026. This note records independently proved algebraic extensions, an explicit complete supplied-order splitting synthesis, and a carefully scoped limitation of the existing positive-semidefinite/smooth-number argument. The two earlier imported dependencies are now supplied by the companion enumeration/Burgess audit, and the order-test/cocycle proof by the independent splitting-core audit. The resulting ordinary mathematical bound is L_N[1/2,O(1)] times the supplied exponent bitlength and polynomial logarithmic factors. This is not a formal verification, a smaller first L-parameter, or an algorithm below L[1/3].

## 1. What the previous work actually supplied

The current catalogue was reassembled from its three existing Git blobs, including the >1 MB first part through `fetch_blob`. It contains 1,514 entries. Relevant earlier entries are:

- **N1101**, position 1: construct a short input-conditioned relation whose resultant or coefficient content differs in the hidden CRT components. Its existing selected-value and coefficient-module readouts are available, but its general constructor is unresolved.
- **N1505**, position 2: construct a selected section of a succinct rank-three bundle. The selected ideal is known, and a logarithmic-size full section can be reconstructed once a suitable selected value is provided; that value is not efficiently constructed.
- **N1124**, position 3: exploit structured joint-orbit matrices. Its selected trace and initial-characteristic-coefficient evaluator applies to the stated banded/fixed-frequency matrices. It is explicitly not a general rank, determinant, or arbitrary implicit-matrix algorithm.
- **N1002**, position 4: construct/evaluate the appropriate coefficient or arithmetic-product unit information. Its many exact extraction identities do not supply the missing fast selected-product constructor.
- **N1131**, position 15 in the reassembled snapshot: find sparse relations in lattices of exponent pairs. The dimension, construction, and locally separating property remain charged.

Source: `catalogues/current/catalogue_parts/part-01.json.txt`, `part-02.json.txt`, `part-03.json.txt`, blobs `de6848d0661a3ee07f25cb579b1fb711e54b91ee`, `77716b27d8747c2fe2cac1f079c91524249d8a51`, `887b14932ee628ee0f17c021cbc7d1906c2965cf`.

The earlier November improvement notes support a narrower provenance claim than “our old ideas produced all four speedups.”

| Improvement | Actual mathematical dependency | Role of earlier catalogue ideas |
|---|---|---|
| Sparse Gram order splitting | Cogentic order tests, quadratic/biquadratic enumeration, and uniform quadratic-field Burgess bound; new triangle-compatible PSD averaging | Structural reuse of local characters, auxiliary algebras, and PSD thinking. No completed N1101/N1505 constructor is used. |
| Deterministic 2/3+epsilon investigation | A new optimization of the source parameter schedule, with its analytic and algebraic transfers handled in separate completion notes | Existing order/unit/spectral themes help identify interfaces. The new powers do not follow from an earlier proved catalogue theorem. |
| Randomized 105 to 102 | Sharper ratio-collection cap and recurrence accounting | This is new accounting of the source algorithm, not a demonstrated payoff from an old retained constructor. |
| Randomized workspace 40 to 19 | Classical black-box/Wiedemann-type sparse linear algebra and streaming accepted roots | Related to earlier structured-matrix interests; it does not invoke N1124's special implicit trace evaluator. |
| Multiple blind dependencies | A finite-group homomorphism argument | Directly applicable to the earlier collision/random-self-reduction programme, but not a proof that an older collision constructor already works. |
| Multi-field unit certificates | Generalized exact unit-lattice cancellation from the source | A useful interface for old unit/auxiliary-ring/order proposals; relation construction is still missing. |

All provenance claims here concern the supplied written proofs, not priority in the mathematical literature.

## 2. Audit of the sparse Gram algebra

The local PSD claim in `source-notes/sparse-gram-order-splitting.md` survives direct inspection. In particular, the edge signs on a splitting class form a balanced complete graph because a compatible biquadratic triangle gives

\[
\alpha_{a+b}\alpha_{b+c}\alpha_{a+c}=\chi(r)=1.
\]

No global character on absent squareclasses is needed. The four prime ideals in the biquadratic field provide precisely this triangle identity. The prime-power Euler coefficients then have the stated rank-one decompositions, and entrywise multiplication preserves PSD.

The earlier complexity conclusion imported Cogentic Lemma 4.2 (effective unit/principal-ideal enumeration) and Lemma 6.3(1) (uniform quadratic-field character estimate). The companion note `enumeration-burgess-audit.md` now gives a complete alternative enumeration argument and a full audit of the specific uniform estimate, including the necessary correction to the printed Weil proposition. Section 7 below supplies the concrete parameter and algorithmic synthesis; it is not relying on a partial inspection of those dependencies.

## 3. A new ramification-tolerant Gram lemma

### Statement

Let S index distinct rational squareclasses, including a possible reference class, and let each nonzero difference a+b have its quadratic field and compatible ideal character as in the earlier sparse Gram note. Suppose the ideal characters have been forced to be +1 on every prime ideal of norm r<=Y, and that chi(r)=1 for rational primes r<=Y. Inert prime ideals above such r are generated by r, so they too have character +1. Suppose every rational prime ramifying in one of the fields is <=Y.

For each prime r not dividing the active modulus q and e>=1, let B(r^e) be the matrix of ideal-norm Euler coefficients, with the old artificial diagonal b_0(r^e). Then:

1. B(r^e) is PSD for every r.
2. B(r^e)-J is PSD for r<=Y.
3. Consequently the full Gram inequality holds for all n coprime to q, without excluding the primorial of the radicand basis.

### Proof at a potentially ramified small prime

Use the finite group of local squareclasses at r. The two classes 1 and u corresponding to the trivial and unramified quadratic extensions form a subgroup U of order 2. For odd r the local squareclass group has order 4; at r=2 it has order 8. Explicitly, at an odd r use valuation parity and the Legendre symbol of the unit part. At 2 use valuation parity and the odd unit modulo 8; U is represented by 1 and 5.

Partition S according to cosets of U. Within each coset, let v_0 and v_1 be indicator vectors for its two local classes. Differences in the same class split, differences between its two classes are inert, and differences in different U-cosets ramify. Since all relevant small-prime ideal characters are +1, the local coefficient is e+1 in the split case, 0 or 1 in the inert case according as e is odd or even, and 1 in the ramified case.

For odd e, its contribution to B(r^e)-J on this coset is

\[
\frac{e-1}{2}(v_0+v_1)(v_0+v_1)^T+
\frac{e+1}{2}(v_0-v_1)(v_0-v_1)^T.
\]

For even e it is

\[
e(v_0v_0^T+v_1v_1^T).
\]

The cross-coset entries of B(r^e)-J are zero. Every displayed coefficient is nonnegative. This proves PSD and handles repeated local classes as well as ramification at 2. For r>Y, no required field ramifies and the previous triangle proof applies. Schur products finish the argument.

### Consequence for character-sum assembly

The inequality becomes

\[
\sum_{a\ne b}S_{a+b}^{(q)}(X)
\ge |S|^2\Psi_q(X,Y)-|S|X(1+\log X),
\]

where only rational primes dividing q are excluded. The source's Lemma 6.3(1), summed over ideal classes, already controls the unrestricted ideal sum. Removing the nonselected ideal over the smaller prime factor of q uses the same one-prime correction as before. There is no longer a factor 4^K from removing the entire basis primorial and no need to require its logarithm to be o(log q).

This permits a simpler family. Test primes up to R, use the source's common pivot, and take S consisting of zero and individual nonpivot prime basis vectors. Its cardinality is asymptotic to R/log R. Each difference radicand has absolute value at most R^3, and the triangle biquadratic discriminants are bounded by a fixed power of R. All ramified primes are at most R; take R<=Y. Only triangles of S are needed, so O(|S|^3) composita suffice, rather than overenumerating all pairs of differences.

With log R and log Y of order sqrt(log q log log q), smooth-number entropy and the size of S still balance. Section 7 gives the full L_q[1/2,O(1)] splitter synthesis using the subsequently audited dependencies. The improvement is a simpler and more flexible field family and removal of an inclusion-exclusion loss, not a reduction of the first L-parameter below 1/2. The polynomial degrees in the enumeration cost are not optimized, so no explicit optimized leading L-constant is asserted.

## 4. Why weights or small supports alone do not lower the 1/2 power

This is a limitation of the existing universal diagonal-loss argument, not a factoring lower bound.

Write theta=log X. Suppose a proposed implementation has log-time budget T, enumerates H<=exp(C T) fields/vertices, and tests all integers up to Y<=exp(C T). Permit arbitrary real weights w_a. Its useful effective vertex count is

\[
H_{\rm eff}=\frac{(\sum_a w_a)^2}{\sum_a w_a^2}\le H.
\]

The same PSD comparison with the universal diagonal bound X(1+log X) requires

\[
H_{\rm eff}\Psi(X,Y)>X(1+\log X)
\]

before it even gives a positive lower bound. Weighting cannot improve H_eff beyond H.

For completeness, an elementary Rankin estimate supplies the needed smooth-number upper bound. Put v=log Y and u=theta/v, assume log theta<<v and u tends to infinity polynomially in theta, and take delta=(log u)/(2v). Then

\[
\frac{\Psi(X,Y)}X\le
\exp(-\delta\theta)\prod_{r\le Y}(1-r^{-1+\delta})^{-1}.
\]

Chebyshev's upper bound for the prime-counting function, partial summation, and delta<=1/4 give

\[
\log\prod_{r\le Y}(1-r^{-1+\delta})^{-1}
=O\!\left(\log v+\frac{e^{\delta v}}{\delta v}\right)
=O\!\left(\log v+\frac{\sqrt u}{\log u}\right).
\]

Thus Psi(X,Y)/X <= exp(-(1/2+o(1))u log u). By monotonicity one may replace Y by exp(C T) when its actual value is smaller. The preceding positivity criterion forces

\[
T^2\gg \theta\log(\theta/T).
\]

In particular no budget T=theta^{k+o(1)} with fixed k<1/2 can be justified by this same positivity certificate, and at its optimum T is at least a constant times sqrt(theta log theta). The argument allows nonuniform supports and weights. It does not cover a different positive contribution from nonsmooth integers, a substantially sharper diagonal estimate, a nonenumerative character family, or a new local-relation constructor. Those are substantive escape routes.

## 5. A direct investigation of retained idea N1101

There is a useful, completely explicit connection between supplied exponents and the earlier “short relation in a root algebra” programme. It is a randomized polynomial-cost readout from supplied exponent information, not a new general factoring exponent.

### Inputs and public computation

Let N be any odd integer having distinct prime divisors p and q. Let b be a unit modulo N, with b a square modulo p and a nonsquare modulo q. Other prime divisors and arbitrary prime-power multiplicities are allowed. For the special case N=pq, a unit b of Jacobi symbol -1 guarantees this mixed splitting condition after relabeling. The Jacobi condition alone does not guarantee mixed splitting for general N. Work in

\[
A=(\mathbb Z/N\mathbb Z)[X]/(X^2-b).
\]

Suppose p-1 divides the supplied positive even integer M=2^t u with u odd. The usual input promise that both p-1 and q-1 divide M is sufficient; the proof below needs only the split-prime promise.

Choose a uniform a modulo N. First test gcd(a^2-b,N); a proper gcd is a factor. Otherwise put z_0=(X-a)^u and z_{j+1}=z_j^2 in A for 0<=j<t. At each j, writing z_j=c_j+d_j X, test both

\[
\gcd(N,d_j),\qquad \gcd(N,c_j-1,d_j).
\]

Return any proper gcd. This uses O(log M) quadratic-ring multiplications and gcds, hence polynomial time in bitlen N and bitlen M. Each z_j has a logarithmic-size power-circuit description and only two reduced coefficients. This realizes a concrete N1101 coefficient-content constructor on the stated supplied-exponent inputs.

### Uniform success theorem

The algorithm succeeds for every a with

\[
\left(\frac{a^2-b}{p}\right)=-1,
\]

as well as the two residues a=+/-sqrt(b) modulo p. Therefore its success probability is at least

\[
\frac{p+3}{2p}>\frac12.
\]

To prove it, let r^2=b modulo p and e=v_2(p-1). In the split algebra A modulo p, X-a has the two coordinates r-a and -r-a. If the displayed Legendre symbol is -1, those two coordinates have opposite quadratic characters. Because u is an odd multiple of the odd part of p-1, their 2-primary orders differ: at stage e-1 their values are -1 and +1, and at stage e both are +1. Thus d_{e-1} is nonzero modulo p, while z_e-1 has both coefficients zero modulo p.

Modulo q the algebra is the field F_{q^2}. If z_e is not 1 there, the content gcd of z_e-1 contains p and excludes q. If z_e=1, then z_{e-1} is +1 or -1 in that field, so d_{e-1}=0 modulo q but is nonzero modulo p; its gcd with N contains q and excludes p. Either gcd is a proper factor even when N has additional primes or repeated prime factors. One of two consecutive stages therefore splits N. This proof also handles exponents that annihilate the entire quadratic algebra.

For the success count, sum_a ( (a^2-b)/p )=-1. An elementary proof counts pairs (a,y) with y^2=a^2-b: the equation (a-y)(a+y)=b has p-1 solutions because b is nonzero and 2 is invertible. There are two zeros of a^2-b, hence exactly (p-1)/2 negative-symbol values. Add the two immediate denominator-zero residues.

### Why stripping the exponent matters

For the semiprime specialization, the simpler one-shot relation (X-a)^M-1 has exactly

\[
\gcd(M/(q-1),q+1)-1
\]

zero values as a ranges over F_q, when q-1 divides M. Indeed a maps bijectively to the norm-one subgroup minus 1 by

\[
a\longmapsto\frac{-\sqrt b-a}{\sqrt b-a}=(\sqrt b-a)^{q-1}.
\]

If M is a multiple of lcm(p^2-1,q^2-1), the one-shot relation is blind on every unit input. This does **not** reject the approach: the 2-adic chain above repairs this defect. For N=35, b=2, M=48 the one-shot routine succeeds for only 10 of 35 residues (all from its denominator check), while the full chain succeeds for all 35.

### What remains open for deterministic use

The theorem gives a large set of successful a, but does not locate one in a guaranteed polylogarithmic or sub-L[1/2] deterministic list. That requires an input-conditioned construction or an appropriate short character-sum statement. Randomized factoring from an exponent multiple already has classical polynomial-cost methods, so the new formulation should not be advertised as a previously unknown randomized complexity class. Its value here is that it proves a specific old local-relation programme really interfaces with the supplied exponent, including the previously problematic annihilator-saturation case.

## 6. Reproducible exact checks

Run `python audit/work/verify_ramification_and_relation.py`.

The run performed:

- 960 exact local Gram entry/decomposition checks for local squareclass groups of sizes 4 and 8 and e=1,...,12;
- 224 exact inert-field root-count checks and 224 whole-modulus one-shot success-count checks;
- 224 exact lower-success-probability checks for the full 2-adic chain;
- 14,732 checks that every negative-character witness is found by the chain;
- 21,136 verified one-shot factors and 31,770 verified chain factors.

Known primes are used only by the verification harness. The public algorithms take N,b,M,a and use no factorization. The tests corroborate the finite algebraic identities; they do not verify the uniform analytic inputs or an asymptotic factoring bound.

## 7. Complete sparse parameter synthesis

The enumeration replacement and Burgess audit are now in `enumeration-burgess-audit.md`; the independent order-test and cocycle audit is in `deterministic-splitting-core-audit.md`. Together they remove the earlier conditional-import status of the following ordinary mathematical theorem. No formal proof checker or full implementation has been run.

**Theorem.** Given an odd composite integer N which is not a prime power, and a positive even integer M divisible by p−1 for every prime p dividing N, a deterministic algorithm finds a proper factor in

\[
\exp\!\bigl(O(\sqrt{\log N\log\log N})\bigr)
\operatorname{bitlen}(M)\operatorname{poly}(\log N)
\]

bit operations. The same exponential factor suffices deterministically to construct a quadratic nonresidue modulo a supplied odd prime. Constants are effective. Even inputs, primality, and prime powers can be dealt with by the usual exact preprocessing when using the factoring version.

Here is an explicit alternative to the fixed-weight support in the earlier sparse note. For a dyadic logarithmic scale L=2^m, set

\[
R=2^{\lceil16\sqrt{Lm}\rceil},\qquad K=\pi(R),\qquad
S=\{0,e_1,\ldots,e_K\}\subset\mathbb F_2^K,
\qquad H=K+1.
\]

The ceiling in the exponent can be computed by integer square-root comparisons. Construct the prime basis up to R and only the base stage of Lemma 3.1, not its full 2^K output. Every difference of two points of S has support at most two. The pivot formula therefore gives squarefree radicands of absolute value at most R^3. Each quadratic discriminant is at most 4R^3; the order basis for any required biquadratic compositum gives the uniform bound

\[
D_*=256R^{12}.
\]

Call the biquadratic routine only for triangles of S. All three quadratic edge fields are already in the difference family. There are at most H^2 quadratic calls and H^3 triangle calls; duplicates may be left in place. No information about absent squareclasses is required.

Use the rational test threshold Y_0=R. For each field take an inverse-class norm bound M_F or M_E no larger than the ceiling of the square root of its discriminant. Enforce the field-specific principal-norm thresholds

\[
Z_F=\max(M_F^3,M_FR),\qquad
Z_E=\max\bigl(M_E^3,M_E\max_{F\subset E}M_F^2\bigr).
\]

The integer guard

\[
B=64D_*^4(R+1)
\]

dominates all these thresholds, all field discriminants by the required factor, and R. Under P^−(q)>B, all principal ideals used to enforce the characters are coprime to q, and the enumeration routines meet their input conditions. Every field ramifies only at primes at most R, so the ramification-tolerant PSD lemma in Section 3 applies to every such prime. The Gram average excludes only primes dividing q.

Consider an active prime or semiprime q with L≤log q<2L, and set X=q^{1/3}, V=log R. For the proof only, choose

\[
u=\lceil(\log X)/V\rceil,
\qquad Y=\lfloor X^{1/u}\rfloor\leq R.
\]

For sufficiently large effective L, products of u distinct primes in (Y/2,Y] give

\[
\Psi_q(X,R)\geq\Psi_q(X,Y)
\geq X(25\log X)^{-u}
\geq X e^{-V/8}.
\]

The prime interval contains the required number of primes by the source's effective elementary prime estimate; none divide q because P^−(q)>R. The last inequality follows from u≤2L/(3V)+1 and

\[
V^2\geq256(\log2)L\log L.
\]

Meanwhile H=π(R)+1≥cR/log R gives

\[
\frac{X(1+\log X)}{H-1}\leq Xe^{-3V/4}
\]

for large L. Thus the Gram lower bound forces one quadratic-field coprime ideal sum to be at least \(\frac12Xe^{-V/8}\).

Every field has log D=O(V)=o(log q). The audited Burgess bound, summed over ideal classes and corrected only for the possible nonselected prime above the smaller divisor of q, bounds every same sum by \(Xe^{-(\log q)/8000}\), for sufficiently large effective L. This contradicts the preceding lower bound. Therefore at least one tested modular image has active character −1, and the verified order test must find a proper divisor. For a supplied odd prime p, use M=p−1 in the compatible-root construction, set q=p in this same proof, and test each rational or enumerated image by Euler's criterion. The identical contradiction proves that one of these images is a quadratic nonresidue; the active-character existence lemma is unnecessary in that prime-input case.

To make the argument independent of the unknown active q, run all integer scales 1≤m≤floor(log_2 bitlen(N)). First trial-divide up to the maximum of the corresponding guards, capped at N−1. If no factor is found, every prime divisor exceeds every guard. For all sufficiently large N, the unknown active q supplied by Lemma 3.1 has log q in one of the included scales and that scale exceeds the effective threshold above. Indeed q≥P^−(N)>B_max tends to infinity with N, whereas log q≤log N<bitlen(N). The elementary exhaustive fallback is consequently used only on a finite effective range.

At each scale log B=O(V), H≤R+1, and all enumeration costs are polynomial in B and log N. Prime generation, trial division, constructing sparse roots, and H^3 triangle calls therefore cost exp(O(V)) times the order-test bit cost. Since V=O(sqrt(log N log log N)), this proves the displayed bound. It does not charge the hypothetical full primorial as a numeric discriminant, and never constructs its 2^K character family.

## 8. Current conclusion

The supplied-order splitting theorem now has an assembled ordinary proof with cost exp(O(sqrt(log N log log N))) times the supplied exponent bit length and polynomial log factors. Ramification is incorporated exactly, and the sparse family can be just the origin and the coordinate vectors. A fixed first L-parameter below 1/2 does not follow from merely optimizing supports or weights in the current smooth-positive-mass argument. The explicit quadratic relation/2-adic chain is genuine continued work on N1101, with a complete algebraic success proof; its deterministic successful-parameter construction is still unresolved. The separate file `retained-individual-continuations.md` records additional concrete transfers and limitations for N1505, N1124, N1002, and N1131.
