# Sealed polynomial fibres and short reducible lattice relations

27 November 2026. **Status:** exact unconditional extraction theorem, and a finite public LLL experiment. Finding the required public relation uniformly quickly remains open. This is a separate potential initialization route for [the beyond-one-third program](beyond_one_third_research.md), not a factoring complexity theorem.

This generalizes the sealed-sign reasoning in KeyBreak E.5 and our [multilevel descent accounting](multilevel_descent_accounting.md). Catalogue interfaces N11 (common roots of a public polynomial), N12 (subresultants), O25 (lattice), O27 (resultants), O34 (polynomials over composite rings) are directly relevant.

## 1. Independent CRT permutation fibres

Let N have at least two distinct prime divisors and let \(k\ge2\). Sample \(h_1,\ldots,h_k\) independently uniformly modulo N, with fresh private storage. Check pairwise differences. A proper gcd is success; if a difference is zero modulo N, reject. Otherwise all differences are units. Retain the roots privately and reveal only the monic polynomial
\[
 F(X)=\prod_{i=1}^k(X-h_i)\in(\mathbb Z/N)[X].
\]
The checks and public control schedule can be padded, as for the sealed square sampler, so no successful root ordering is revealed. All later public calculations and stopping decisions must use only F, N and independent public randomness.

For each prime power \(p^a\parallel N\), the local roots \(h_i\bmod p^a\) are distinct modulo p. They are exactly the roots of F modulo \(p^a\): if a product of the linear differences is divisible by \(p^a\), at most one difference is divisible by p, so that one is divisible by \(p^a\). Hence the unordered set of roots in each component is determined by F. Independent permutations of the labels in each component preserve F and the unit-difference guard. CRT combines all permutations into admissible ordered private tuples. The initial sampling law is uniform, and the group acts transitively on the fibre. Conditional on the entire public transcript before first exposure, the component label permutations are independent and uniform. For odd B-rough N and polynomial k, the acceptance probability is \(1-o(1)\) after preprocessing, by the pairwise union bound over primes dividing N; if smaller primes occur the gcd checks or preprocessing handle them. This is an exact symmetry theorem, not an independence assumption about randomly found modular factors.

## 2. Resultant witness

Suppose a public nonzero integer polynomial g (chosen only from the public transcript) satisfies
\[
 \operatorname{Res}(F,g)\equiv0\pmod N,\qquad
 F\nmid g\quad\text{in }(\mathbb Z/N)[X].
 \tag{1}
\]
Use any integer monic lift of F in the resultant. Both conditions are exactly testable in public polynomial bit complexity by a resultant and monic remainder, without factoring N. Compute all \(\gcd(g(h_i),N)\) only after selecting this public g. The probability of a proper factor is at least \(1-1/k\).

Indeed in each prime component let \(I_p\subseteq\{1,\ldots,k\}\) denote the zero set of g modulo p in the private ordering. The resultant identity for monic F makes every such set nonempty. Its cardinality is public-fibre invariant, and the sets are independent uniform subsets conditional on those cardinalities. If some cardinality \(r\) is strictly between 0 and k, compare that component to any other prime component. Different cardinalities force a mismatch; equal cardinalities give coincidence probability \(1/\binom{k}{r}\le1/k\). A mismatch yields a proper gcd (a prime divides one value but another prime does not). If all local cardinalities are k, either at least one evaluation fails to vanish to its full prime-power exponent, giving a proper gcd regardless of the labels, or all evaluations vanish modulo N. The latter implies \(F\mid g\), by monic remainder and the invertible Vandermonde matrix on the k unit-difference roots. It contradicts (1). This proves the claimed probability even for nonsquarefree inputs. A public proper gcd of the resultant with N, if encountered instead, is already success.

There is also a full prime-power separation variant. If every prime component has an intermediate zero-set cardinality, the probability that any pair of components have identical membership signatures on the k labels is at most \(\binom{\omega(N)}2/k\). Saturate each computed gcd to the full prime-power support using \(\gcd(N,g(h_i)^{\operatorname{bitlength}N})\), then split by all signatures. On the separation event this recovers each prime-power block. Thus sufficiently many private labels (still polynomial in the bit length) can give complete factorization once a single such witness is available. The witness-supply condition is the substantive difficulty.

## 3. Reducible public relation suffices

For an integer lift of F, define the explicit polynomial lattice
\[
 \mathcal L_D=\{P\in\mathbb Z[X]:\deg P\le D,\ P=0\bmod(N,F)\},\qquad D\ge k.
\]
It has basis \(NX^i\), \(0\le i<k\), together with \(X^jF\), \(0\le j\le D-k\). This follows by integer monic division, since the remainder coefficients must all be multiples of N. The triangular basis has index \(N^k\) in the coefficient lattice. LLL gives short vectors, with the usual Euclidean norm bound \(2^{D/2}N^{k/(D+1)}\) for its first reduced vector. But shortness alone does not ensure the following additional property.

**Sufficient condition.** Find a nonzero \(P\in\mathcal L_D\) whose integer content is coprime to N and whose factorization over \(\mathbb Q\) has **no individual irreducible factor in \(\mathcal L_D\)**. Rational polynomial factorization is deterministic polynomial time by Lenstra–Lenstra–Lovász (1982), independently of integer factoring. Compute it publicly. For each primitive integer factor g test the public gcd of its resultant with F against N. If a proper factor occurs, stop. Otherwise these gcds are 1 or N. They cannot all be 1: the resultant of P with F vanishes modulo N, and the resultant is multiplicative in P. Select one having gcd N; by the sufficient condition it is not divisible by F modulo N. It satisfies (1). Apply the extraction theorem. This makes precise which reducible relations are useful, including repeated irreducible factors. A reducible P containing a factor already divisible by F does not automatically give a new witness, though its other factors may independently pass (1).

This is a smoothness-free alternative certificate, with short polynomial relation search entirely public and rational factorization over characteristic zero. It does not claim that a shortest polynomial in this lattice is reducible or that a reducible vector is nontrivial in the required sense. Neither follows from LLL. In particular supplying the secret h_i as a factorization aid before selecting g would invalidate the fibre theorem.

For comparison, a fixed g independent of F, nonzero modulo both balanced prime factors and degree at most D, has probability at most \(k^2D^2/(p_1p_2)\) of vanishing at some private root in each component (the conditioning on distinct roots does not change the uniform single-root marginal; use a union bound and independent components). Thus enumerating a fixed small set of polynomials does not give a subexponential supply theorem. The public lattice depends on F and is not subject to that fixed-family argument.

## 4. Exact finite experiment

Script: [verification/research/verify_sealed_polynomial.py](../verification/research/verify_sealed_polynomial.py), Python 3.13.5, SymPy 1.14.0. Tested and committed Git blob 671e0d2d69d10db5dbf9a5e966f420f1edbf78c7, SHA-256 0a797339071a0ccee20c4c7eae43ef5d9a8703041829d6234bef5031e9bea50f. The first 144 exhaustive tests manufacture local CRT coverage patterns using known factors **only to test the extraction theorem**, including prime powers; check the predicted \(1/\binom{k}{r}\) failure count and exact public resultant/remainder predicates. Also check the all-mod-p-zero but nonzero modulo a prime power branch.

In the search experiment, the sampler chooses private tuples using N alone and publishes F. To isolate the experiment it discards immediate nonunit-difference exits. The lattice and reduction use only N and F. For each fixture, examine the LLL basis and all pairwise sums/differences of its basis vectors; factor the candidates over the integers and check the exact product and monic remainder identities. Select the publicly sufficient class in §3 before computing private gcds. Every reported factor is verified by division.

Fixed seed 271828; \(k=2,3\) and \(D=k+2,k+4,k+6\), one fresh sampled F per pair of parameters per N. Results:

| N | k | Candidates | Reducible | Sufficient public certificates | Certificate splits | Fixtures with a split / 3 |
|---:|---:|---:|---:|---:|---:|---:|
| 3127 | 2 | 155 | 81 | 76 | 74 | 2 |
| 3127 | 3 | 200 | 15 | 6 | 6 | 2 |
| 10403 | 2 | 155 | 14 | 0 | 0 | 0 |
| 10403 | 3 | 200 | 22 | 5 | 5 | 1 |
| 1022117 | 2 | 155 | 10 | 0 | 0 | 0 |
| 1022117 | 3 | 200 | 0 | 0 | 0 | 0 |
| 100160063 | 2 | 155 | 37 | 36 | 36 | 1 |
| 100160063 | 3 | 200 | 0 | 0 | 0 | 0 |
| 1000036000099 | 2 | 155 | 0 | 0 | 0 | 0 |
| 1000036000099 | 3 | 200 | 0 | 0 | 0 | 0 |

Totals 1,775 lattice candidates, 179 reducible, 56 trivial multiples, 123 sufficient certificates, 121 certificate splits. The verified factors on successful fixtures are 53,59; 101,103; and 10007,10009. Six of thirty distinct sampled fixtures split. Within a fixture candidates are highly correlated; the 121/123 statistic is **not** an estimate of independent success probability or asymptotic witness supply. Most tested larger fixtures yield no sufficient relation. The test uses finite integer and rational operations, not a numerically guessed factor or hidden prime-dependent choice of LLL basis.

## 5. Next step

This route establishes exact extraction and a publicly testable generation objective, but the cheap short-vector heuristic is not uniformly successful. The challenge is to generate a lattice element whose rational factorization splits the modular root constraints nontrivially, or directly a short nonzero-resultant-mod-N witness (1), with a provable sub-one-third time bound. Approaches based on common resultants or rank-compressed polynomial products should be measured against that explicit target, rather than assuming generic reducibility of LLL outputs. The independent [probe-free S-unit certificate](exact_descent_unit_certificate.md) is currently the stronger continuation of the number-field route because it removes a specific proven degree-dependent cost, whereas this polynomial route has an unresolved relation-supply theorem from its first step.
