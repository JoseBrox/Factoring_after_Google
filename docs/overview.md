# Mathematical overview

## Three problems that should be kept separate

**General factoring** begins with an integer $N$ and asks for its prime factors. No information about the hidden factors is supplied. A deterministic algorithm must succeed without random choices; a Las Vegas algorithm may use random choices, but it checks its output and is never allowed to return an incorrect factorization.

**Supplied-order splitting** begins with a composite $N$ and an additional even integer $M$ known to be divisible by $p-1$ for every prime divisor $p$ of $N$. Multiplicative groups modulo those hidden primes therefore satisfy useful exponent identities. The task is to exploit those identities to separate some of the prime factors. Perfect powers are handled separately. Finding a suitable $M$ from $N$ is part of the general factoring problem, not part of this promised-input subproblem.

**Quadratic nonresidue construction** begins with an odd prime $p$ and asks for a number $z$ that is not a square modulo $p$. A proposed output is checked by Euler's criterion, $z^{(p-1)/2}\equiv-1\pmod p$. Finding the output deterministically is the issue; checking it is cheap.

## The deterministic general algorithm

The algorithm constructs polynomial pairs with a shared root modulo $N$ and prescribed behavior modulo many small primes. Relations from smooth values of those polynomials live in two number fields. Matching their ideal valuations and cancelling their unit logarithms produces exact modular exponent certificates. A saturation argument combines these into an even multiple of every hidden $p-1$. The supplied-order splitter then returns a factor.

The improvement changes the size parameters of this construction. This requires revisiting the analytic estimates at their new ranges: smooth values in progressions, conditioned Gaussian moments, exceptional conductors, adaptive deletion of bad rows, and the spectral gap used by exact extraction. The manuscript provides this transfer and an explicit parameter schedule. Its final exponent is $2/3+\varepsilon$ for any fixed positive $\varepsilon$; the constants may depend on that choice.

The use of probability in the proof does not make the algorithm randomized. A probability argument proves that a finite box contains a successful object. The deterministic algorithm visits that box in a specified order and verifies the required certificates.

## Why a sparse Gram family helps splitting

A Gram matrix packages many local character identities into one positive semidefinite matrix. Positivity says that certain contributions cannot cancel arbitrarily. Smooth integers supply a lower bound. A character-sum estimate gives an upper bound if all candidate tests fail. Contradiction forces a useful splitting witness.

The new construction uses a small family of coordinate choices instead of the full product family. The matrix dimension falls sharply. The proof also deals with ramified primes, where simply treating every local character as unramified would be incorrect. Combining the sparse family with uniform character estimates gives the $\exp(O(\sqrt{L\log L}))$ scale. The prime-input specialization yields a nonresidue algorithm.

The technical appendix supplies the exact arithmetic needed to turn this argument into an algorithm: quadratic characters, compatible roots, fixed-dimensional lattice enumeration, and the uniform short character-sum bound used in the comparison.

## What changes in the randomized framework

The starting framework collects algebraic relations through a recursive tree of smaller factoring problems. Its running time is sensitive to the cost of those recursive calls and to the memory used to find a relation dependency.

The new sparse-kernel construction replaces a dense dependency calculation with repeated sparse matrix-vector operations and a verified reconstruction. A revised recursion schedule then lowers the proposed explicit time and workspace constants. Exact rational inequalities certify that the revised budget closes; they also exhibit why an earlier, more aggressive choice fails.

The complete factorer needs analytic distribution and square-certification estimates at a wider range than the pinned source proves with its fixed parameters. Those statements are explicit assumptions in the randomized manuscript. Consequently, $91.4/19$ is a conditional theorem. The linear-algebra theorem and the conditional recurrence calculation have their own complete proofs.

## A concrete retained construction

The quadratic relation chain works in $(\mathbb Z/N\mathbb Z)[X]/(X^2-b)$. Repeated squaring of $X-a$ produces pairs of coefficients. Their gcds with $N$ can reveal a factor when $b$ is a square modulo one hidden prime and a nonresidue modulo another. Checking every stage of the squaring chain preserves information that can disappear at the final exponent.

This routine is fully implemented here. The promise is substantive: the repository does not give a new general method for finding the needed mixed-sign $b$ and supplied exponent at the same cost. The implementation and its small exhaustive checks make the local theorem independently reproducible.

## The remaining barriers

The deterministic smooth-progression argument has a large-modulus term whose size is not negligible in the desired range. A formally smaller exponent schedule cannot erase that term. The general deterministic $1/2$ objective therefore needs a new uniform estimate or a different construction.

In the present randomized balance, three competing contributions have exponents $a$, $b$, and $1-a-b$. Their maximum is at least $1/3$. This is a limitation of that balance, not a lower bound for all factoring algorithms. A first $L$-parameter below $1/3$ would require a new mechanism beyond the optimization performed here.

For exact theorem statements and citations, use the [manuscripts](../manuscripts/README.md). For the evidential status of each step, use the [proof-status register](proof_status.md).
