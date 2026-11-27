# Factoring after Google

**Integer factoring, supplied-order splitting, and quadratic nonresidues — research using ChatGPT Astra 6 and 6.2.**

This repository develops and audits improvements to the November 2026 Cogentic factoring manuscripts released by Google Research. It contains readable research manuscripts, explicit algorithm specifications, Lean formalizations of core components, exact finite verification programs, and pinned source material. The aim is to make every claim easy to locate, reconstruct, and challenge.

**Start here:** [results and proof status](docs/proof_status.md) · [manuscripts](manuscripts/README.md) · [Lean proofs](lean/README.md) · [reproduce the checks](docs/reproducibility.md) · [sources and comparisons](docs/comparison_sources.md).

## Results at a glance

All logarithms in the asymptotic expressions are natural. The standard subexponential notation is

```math
L_N[\alpha,c]=\exp\!\bigl((c+o(1))(\log N)^\alpha(\log\log N)^{1-\alpha}\bigr).
```

The table compares like-for-like inputs and computational models. **“Previous” means the bound in the pinned source being improved** (25 November 2026); historical benchmarks appear below. These are research manuscripts, not independently certified world records.

| Problem / manuscript (PDF) | New complexity | Previous bound and source | Proof status |
|:---|:---|:---|:---|
| **[Deterministic factoring](papers/deterministic_factoring.pdf)** | $`\exp(O_\varepsilon((\log N)^{2/3+\varepsilon}))`$ | $`O(\exp(3(\log N)^{3/4}))`$ [D, Thm. 1.1][D] | Written proof; any fixed $`\varepsilon>0`$. [LaTeX](manuscripts/deterministic_factoring/) |
| **[Deterministic supplied-order splitting](papers/order_splitting.pdf)** | $`(\log M)(\log N)^{O(1)}\exp(O(\sqrt{\log N\,\log\log N}))`$ | $`(\log M)(\log N)^2\exp(O(\sqrt{\log N}\,\log\log N))`$ [D, Thm. 1.2][D] | Written proof; supplied exponent. [LaTeX](manuscripts/order_splitting/) |
| **[Deterministic quadratic nonresidues](papers/quadratic_nonresidues.pdf)** | $`\exp(O(\sqrt{\log p\,\log\log p}))`$ | $`\exp(O(\sqrt{\log p}\,\log\log p))`$ [D, Thm. 1.2][D] | Written proof; prime input. [LaTeX](manuscripts/quadratic_nonresidues/) |
| **[Randomized factoring](papers/randomized_factoring.pdf)** — expected time | $`L_N[1/3,91.4]`$ | $`L_N[1/3,105]`$ [R, Thm. 1.1][R] | **Conditional.** [LaTeX](manuscripts/randomized_factoring/) |
| Randomized factoring — workspace | $`L_N[1/3,19]`$ | $`L_N[1/3,40]`$ [R, Thm. 1.1][R] | **Conditional** for the full factorer. |
| **[Quadratic relation chain](papers/quadratic_relations.pdf)** | $`O(\log M)`$ ring multiplications per trial | Auxiliary routine; retained construction [N1101][H] | Single-trial correctness and probability certified in Lean under mixed-sign promise; [code](src/factoring_after_google/quadratic_relations.py). |

### Reading the bounds

- **Deterministic factoring:** the power of the logarithm in the running-time exponent drops from $`3/4`$ to $`2/3+\varepsilon`$ for every fixed $`\varepsilon>0`$. This is a family approaching $`2/3`$, not an endpoint bound of the form $`L_N[2/3,c]`$.
- **Supplied-order splitting and quadratic nonresidues:** the main exponential factor changes from $`\exp(O(\sqrt{\log N}\,\log\log N))`$ to $`\exp(O(\sqrt{\log N\,\log\log N}))`$ (with $`p`$ in place of $`N`$ in the prime-input problem). This saves a factor of $`\sqrt{\log\log N}`$ in the scale of the exponent. The nonresidue bound is $`L_p[1/2,O(1)]`$. The splitting input includes an even positive integer $`M`$ divisible by $`p-1`$ for every prime $`p\mid N`$, with composite $`N`$ not a perfect power. Its bit length is charged; producing it is a separate task.
- **Randomized factoring:** the headline time and deterministic workspace constants change from 105 and 40 to 91.4 and 19, conditional on the widened analytic and square-certification contracts. Google's concluding proof also reports the tighter intermediate constants 104 and 38. Our sparse kernel theorem and recursion budget have written proofs.
- **Quadratic relation chain:** under its mixed-sign promise, each independent uniform trial succeeds with probability at least $`\frac{p+3}{2p}>\frac12`$. This is not a general factoring algorithm without the promised inputs.

### Historical benchmarks

Lenstra–Pomerance gives a rigorous randomized $`L_N[1/2,1]`$ bound [LP]. The general number field sieve has heuristic complexity

```math
L_N[1/3,(64/9)^{1/3}]\qquad ((64/9)^{1/3}\approx 1.923).
```

See [NFS]. Our conditional randomized constant improves the explicit constants of Cogentic's rigorous-bound framework, not the heuristic GNFS constant.

The new [monic polynomial-mark construction](docs/monic_polynomial_mark_factorer.md) removes the original common-leading-coefficient barrier and reduces a deterministic # Factoring after Google

**Integer factoring, supplied-order splitting, and quadratic nonresidues — research using ChatGPT Astra 6 and 6.2.**

This repository develops and audits improvements to the November 2026 Cogentic factoring manuscripts released by Google Research. It contains readable research manuscripts, explicit algorithm specifications, Lean formalizations of core components, exact finite verification programs, and pinned source material. The aim is to make every claim easy to locate, reconstruct, and challenge.

**Start here:** [results and proof status](docs/proof_status.md) · [manuscripts](manuscripts/README.md) · [Lean proofs](lean/README.md) · [reproduce the checks](docs/reproducibility.md) · [sources and comparisons](docs/comparison_sources.md).

## Results at a glance

All logarithms in the asymptotic expressions are natural. The standard subexponential notation is

```math
L_N[\alpha,c]=\exp\!\bigl((c+o(1))(\log N)^\alpha(\log\log N)^{1-\alpha}\bigr).
```

The table compares like-for-like inputs and computational models. **“Previous” means the bound in the pinned source being improved** (25 November 2026); historical benchmarks appear below. These are research manuscripts, not independently certified world records.

| Problem / manuscript (PDF) | New complexity | Previous bound and source | Proof status |
|:---|:---|:---|:---|
| **[Deterministic factoring](papers/deterministic_factoring.pdf)** | $`\exp(O_\varepsilon((\log N)^{2/3+\varepsilon}))`$ | $`O(\exp(3(\log N)^{3/4}))`$ [D, Thm. 1.1][D] | Written proof; any fixed $`\varepsilon>0`$. [LaTeX](manuscripts/deterministic_factoring/) |
| **[Deterministic supplied-order splitting](papers/order_splitting.pdf)** | $`(\log M)(\log N)^{O(1)}\exp(O(\sqrt{\log N\,\log\log N}))`$ | $`(\log M)(\log N)^2\exp(O(\sqrt{\log N}\,\log\log N))`$ [D, Thm. 1.2][D] | Written proof; supplied exponent. [LaTeX](manuscripts/order_splitting/) |
| **[Deterministic quadratic nonresidues](papers/quadratic_nonresidues.pdf)** | $`\exp(O(\sqrt{\log p\,\log\log p}))`$ | $`\exp(O(\sqrt{\log p}\,\log\log p))`$ [D, Thm. 1.2][D] | Written proof; prime input. [LaTeX](manuscripts/quadratic_nonresidues/) |
| **[Randomized factoring](papers/randomized_factoring.pdf)** — expected time | $`L_N[1/3,91.4]`$ | $`L_N[1/3,105]`$ [R, Thm. 1.1][R] | **Conditional.** [LaTeX](manuscripts/randomized_factoring/) |
| Randomized factoring — workspace | $`L_N[1/3,19]`$ | $`L_N[1/3,40]`$ [R, Thm. 1.1][R] | **Conditional** for the full factorer. |
| **[Quadratic relation chain](papers/quadratic_relations.pdf)** | $`O(\log M)`$ ring multiplications per trial | Auxiliary routine; retained construction [N1101][H] | Single-trial correctness and probability certified in Lean under mixed-sign promise; [code](src/factoring_after_google/quadratic_relations.py). |

### Reading the bounds

- **Deterministic factoring:** the power of the logarithm in the running-time exponent drops from $`3/4`$ to $`2/3+\varepsilon`$ for every fixed $`\varepsilon>0`$. This is a family approaching $`2/3`$, not an endpoint bound of the form $`L_N[2/3,c]`$.
- **Supplied-order splitting and quadratic nonresidues:** the main exponential factor changes from $`\exp(O(\sqrt{\log N}\,\log\log N))`$ to $`\exp(O(\sqrt{\log N\,\log\log N}))`$ (with $`p`$ in place of $`N`$ in the prime-input problem). This saves a factor of $`\sqrt{\log\log N}`$ in the scale of the exponent. The nonresidue bound is $`L_p[1/2,O(1)]`$. The splitting input includes an even positive integer $`M`$ divisible by $`p-1`$ for every prime $`p\mid N`$, with composite $`N`$ not a perfect power. Its bit length is charged; producing it is a separate task.
- **Randomized factoring:** the headline time and deterministic workspace constants change from 105 and 40 to 91.4 and 19, conditional on the widened analytic and square-certification contracts. Google's concluding proof also reports the tighter intermediate constants 104 and 38. Our sparse kernel theorem and recursion budget have written proofs.
- **Quadratic relation chain:** under its mixed-sign promise, each independent uniform trial succeeds with probability at least $`\frac{p+3}{2p}>\frac12`$. This is not a general factoring algorithm without the promised inputs.

### Historical benchmarks

Lenstra–Pomerance gives a rigorous randomized $`L_N[1/2,1]`$ bound [LP]. The general number field sieve has heuristic complexity

```math
L_N[1/3,(64/9)^{1/3}]\qquad ((64/9)^{1/3}\approx 1.923).
```

See [NFS]. Our conditional randomized constant improves the explicit constants of Cogentic's rigorous-bound framework, not the heuristic GNFS constant.

1/2+\varepsilon`$ exponent to an explicit **open** one-mark covariance estimate for two smooth resultants. The [paired-unit construction](docs/paired_unit_construction.md) provides nearly # Factoring after Google

**Integer factoring, supplied-order splitting, and quadratic nonresidues — research using ChatGPT Astra 6 and 6.2.**

This repository develops and audits improvements to the November 2026 Cogentic factoring manuscripts released by Google Research. It contains readable research manuscripts, explicit algorithm specifications, Lean formalizations of core components, exact finite verification programs, and pinned source material. The aim is to make every claim easy to locate, reconstruct, and challenge.

**Start here:** [results and proof status](docs/proof_status.md) · [manuscripts](manuscripts/README.md) · [Lean proofs](lean/README.md) · [reproduce the checks](docs/reproducibility.md) · [sources and comparisons](docs/comparison_sources.md).

## Results at a glance

All logarithms in the asymptotic expressions are natural. The standard subexponential notation is

```math
L_N[\alpha,c]=\exp\!\bigl((c+o(1))(\log N)^\alpha(\log\log N)^{1-\alpha}\bigr).
```

The table compares like-for-like inputs and computational models. **“Previous” means the bound in the pinned source being improved** (25 November 2026); historical benchmarks appear below. These are research manuscripts, not independently certified world records.

| Problem / manuscript (PDF) | New complexity | Previous bound and source | Proof status |
|:---|:---|:---|:---|
| **[Deterministic factoring](papers/deterministic_factoring.pdf)** | $`\exp(O_\varepsilon((\log N)^{2/3+\varepsilon}))`$ | $`O(\exp(3(\log N)^{3/4}))`$ [D, Thm. 1.1][D] | Written proof; any fixed $`\varepsilon>0`$. [LaTeX](manuscripts/deterministic_factoring/) |
| **[Deterministic supplied-order splitting](papers/order_splitting.pdf)** | $`(\log M)(\log N)^{O(1)}\exp(O(\sqrt{\log N\,\log\log N}))`$ | $`(\log M)(\log N)^2\exp(O(\sqrt{\log N}\,\log\log N))`$ [D, Thm. 1.2][D] | Written proof; supplied exponent. [LaTeX](manuscripts/order_splitting/) |
| **[Deterministic quadratic nonresidues](papers/quadratic_nonresidues.pdf)** | $`\exp(O(\sqrt{\log p\,\log\log p}))`$ | $`\exp(O(\sqrt{\log p}\,\log\log p))`$ [D, Thm. 1.2][D] | Written proof; prime input. [LaTeX](manuscripts/quadratic_nonresidues/) |
| **[Randomized factoring](papers/randomized_factoring.pdf)** — expected time | $`L_N[1/3,91.4]`$ | $`L_N[1/3,105]`$ [R, Thm. 1.1][R] | **Conditional.** [LaTeX](manuscripts/randomized_factoring/) |
| Randomized factoring — workspace | $`L_N[1/3,19]`$ | $`L_N[1/3,40]`$ [R, Thm. 1.1][R] | **Conditional** for the full factorer. |
| **[Quadratic relation chain](papers/quadratic_relations.pdf)** | $`O(\log M)`$ ring multiplications per trial | Auxiliary routine; retained construction [N1101][H] | Single-trial correctness and probability certified in Lean under mixed-sign promise; [code](src/factoring_after_google/quadratic_relations.py). |

### Reading the bounds

- **Deterministic factoring:** the power of the logarithm in the running-time exponent drops from $`3/4`$ to $`2/3+\varepsilon`$ for every fixed $`\varepsilon>0`$. This is a family approaching $`2/3`$, not an endpoint bound of the form $`L_N[2/3,c]`$.
- **Supplied-order splitting and quadratic nonresidues:** the main exponential factor changes from $`\exp(O(\sqrt{\log N}\,\log\log N))`$ to $`\exp(O(\sqrt{\log N\,\log\log N}))`$ (with $`p`$ in place of $`N`$ in the prime-input problem). This saves a factor of $`\sqrt{\log\log N}`$ in the scale of the exponent. The nonresidue bound is $`L_p[1/2,O(1)]`$. The splitting input includes an even positive integer $`M`$ divisible by $`p-1`$ for every prime $`p\mid N`$, with composite $`N`$ not a perfect power. Its bit length is charged; producing it is a separate task.
- **Randomized factoring:** the headline time and deterministic workspace constants change from 105 and 40 to 91.4 and 19, conditional on the widened analytic and square-certification contracts. Google's concluding proof also reports the tighter intermediate constants 104 and 38. Our sparse kernel theorem and recursion budget have written proofs.
- **Quadratic relation chain:** under its mixed-sign promise, each independent uniform trial succeeds with probability at least $`\frac{p+3}{2p}>\frac12`$. This is not a general factoring algorithm without the promised inputs.

### Historical benchmarks

Lenstra–Pomerance gives a rigorous randomized $`L_N[1/2,1]`$ bound [LP]. The general number field sieve has heuristic complexity

```math
L_N[1/3,(64/9)^{1/3}]\qquad ((64/9)^{1/3}\approx 1.923).
```

See [NFS]. Our conditional randomized constant improves the explicit constants of Cogentic's rigorous-bound framework, not the heuristic GNFS constant.

d`$ independent shared unit relations without smoothness assumptions. Neither is an unconditional improvement to the worst-case factoring bound. **No general classical algorithm below first L-parameter 1/3 is claimed here.**

## How to read the repository

For a quick mathematical orientation, read [the overview](docs/overview.md), then the introduction and main theorem of the relevant manuscript. Each manuscript explains the input promise, the algorithm, the proof, the cost model, and its limitations before the longer technical development.

For a proof audit, use the [claim and dependency register](docs/proof_status.md). The supplied-order and nonresidue manuscripts each include the shared quadratic arithmetic appendix in their compiled PDF. The deterministic factoring manuscript states its imported source contracts and proves the changed analytic transfer. The randomized manuscript separates its proved linear-algebra and recurrence results from the unproved transfer obligations.

For experiments, start with the [quadratic relation example](examples/quadratic_relation_example.py) and the [verification guide](verification/README.md). The full asymptotic factorers are mathematical specifications; this repository does not present them as completed production implementations.

| Directory | Contents |
|---|---|
| [`manuscripts/`](manuscripts/) | Five editable LaTeX manuscripts, shared technical appendix, bibliography |
| [`papers/`](papers/) | Compiled, searchable PDFs of the manuscripts |
| [`src/`](src/) | Implemented quadratic-ring relation and chain routines |
| [`examples/`](examples/) | A small reproducible worked example |
| [`lean/`](lean/) | Compiled component proofs, pinned Lean/mathlib dependencies, and an axiom audit |
| [`verification/`](verification/) | Exact rational inequalities, finite-field identities, counterexamples, exhaustive small-input tests, fixed expected outputs |
| [`references/`](references/) | Immutable upstream identifiers, source attribution, extracted source text, retrieval instructions |
| [`provenance/`](provenance/) | Frozen working notes explaining where the constructions and corrections came from |
| [`docs/`](docs/) | Overview, notation, proof status, comparisons, errata, reproducibility |
| [`scripts/`](scripts/) | Source retrieval, manuscript compilation, repository integrity checks |

## Reproduce the verification

Clone the repository and run from its root:

```sh
python3 verification/run_all.py
python3 scripts/verify_repository.py
```

For byte-level verification of the initial published snapshot, check out [commit `af09583`](https://github.com/JoseBrox/Factoring_after_Google/tree/af09583053f45e910e865bb6594b2ba0f8706bc2) and run `python3 scripts/verify_release.py`. The release manifest records that snapshot, not subsequent editorial changes.

The main verification runner uses **Python's standard library and Node.js**, with no third-party Python packages. The separate [polynomial-mark research experiment](verification/research/polynomial_marks.py) requires SymPy and mpmath. They are deterministic and offline. The runner compares each result with the committed expected output and fails on a discrepancy. See [reproducibility](docs/reproducibility.md) for versions, individual checks, manuscript builds, and source hashes.

To rebuild the PDFs with a normal TeX Live installation containing `latexmk`, the AMS packages, `lmodern`, `microtype`, `xurl`, and `cleveref`:

```sh
python3 scripts/build_manuscripts.py
```

The GitHub Actions workflows run the exact checks, compile all manuscripts, and compile and audit the Lean proofs. Finite computations verify the listed identities and examples; they do not prove asymptotic analytic estimates or certify an entire formal proof.

## Lean formalizations

The [Lean guide](lean/README.md) gives the theorem names, assumptions, and reproduction commands. The formalization follows this priority order:

| Priority | Formalized component | Coverage |
|---|---|---|
| 1 | Deterministic parameter schedule | All parameter inequalities; rational schedules; exact exponent-saturation construction from the successful-prime density and verified modular powers; finite adaptive peeling invariant; conditional exponential cost transfer. |
| 2 | Sparse Gram argument | Explicit ramification-sensitive local coefficient matrices, PSD domination, triangle-sign rank-one representation, Schur products, and finite sparse averaging. |
| 3 | Randomized recursion | Path maxima for all depths; exact margins; finite-threshold recurrence bounds with time/workspace coefficients 91.4 and 19; exact subexponential scale contraction and uniform fibres of a kernel projection and verified Krylov correction. |
| 4 | Quadratic relation chain | Executable supplied-M splitter, proper-divisor soundness, exact mixed-prime success probability ≥ (p+3)/(2p) > 1/2 (including repeated prime powers), and arithmetic-operation budgets. |
| 5 | Square-root extraction | A nontrivial square congruence yields a proper gcd factor, including even moduli and noninvertible roots. |

The core contains **277 explicitly named source theorems in 39 modules**; all passed aggregate compilation and complete axiom audit in run 45851754483 ([build evidence](verification/lean/progression-readiness.md)). The quadratic chain's main finite single-trial correctness and probability theorem is now certified. The remaining results are compiled component theorems. The full analytic complexity bounds in the results table are not yet end-to-end Lean proofs. The remaining analytic, arithmetic, probability, and implementation bridges are listed in the [proof-status register](docs/proof_status.md).

The library-reuse checkpoint additionally certifies the unit-lattice torsion argument, localized polynomial evaluation and two-field modular cancellation, exact character orthogonality for injective prefixes, the coprime smooth-product count, the affine quadratic-character sum identity, and executable scalar supplied-order splitting from a certified Euler-sign discrepancy. See [library reuse and remaining dependencies](docs/lean_library_reuse.md).

The separate [analytic target](lean-analytic/README.md) rebuilds PNT+ on Lean 4.36.0 and verifies five bridge theorems, including the strong Chebyshev theta estimate and the eventual dyadic prime density. It remains separate from the Lean 4.19.0 core.

The arithmetic project pins Lean 4.19.0 and every mathlib dependency revision. Builds treat warnings as errors. The audit inspects compiled logical declarations, including private and generated proofs, and permits only Lean's standard axioms `propext`, `Classical.choice`, and `Quot.sound`. Project proofs contain no `sorry` or `native_decide`.

## What is reused, and what changes

The deterministic work retains Cogentic's exponent-annihilation architecture and develops a new parameter schedule with its analytic justification. The splitting and nonresidue improvements replace a large auxiliary family with a sparse Gram family and use exact enumeration in fixed-dimensional quadratic arithmetic. The randomized work retains the relation-tree architecture, uses sparse black-box linear algebra, and repairs the recursive budget.

The retained construction N1101 contributes the quadratic relation chain. Other retained ideas have their own continuation notes: N1505 yields a section once factors are known, N1124 has a trace-based rank counterexample, N1002 does not justify a full coefficient-prefix shortcut, and N1131 does not by itself turn a common lattice relation into a separator. See [provenance](provenance/README.md). These are kept as individually assessed research directions.

## Open work

- Formalize and independently audit the written conditional widened arithmetic-progression, fibre, local-moment and C1 readiness arguments; establish C2–C5, including square certification, for the randomized 91.4/19 theorem.
- Overcome the large-modulus equidistribution obstruction in the deterministic construction; reducing exponents on a spreadsheet alone does not remove it.
- Implement and benchmark the complete theoretical factorers, including the exact algebraic subroutines and explicit finite thresholds.
- Obtain independent mathematical review and extend the compiled Lean component proofs to the complete algorithms and analytic complexity bounds. The source's announced Lean artifacts are not treated here as checked evidence.
- Find a new mechanism that can beat the 1/3 balance in the present randomized architecture. This is an open research objective.

Contributions are welcome: a precise counterexample or a corrected lemma is as useful as a faster algorithm. See [CONTRIBUTING.md](CONTRIBUTING.md).

## References

- **[D]** Cogentic / Google Research, *Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction* (2026), [pinned manuscript](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf), especially Theorems 1.1–1.2.
- **[R]** Cogentic / Google Research, *Unconditional Integer Factorization in Time* $`L_N[1/3,O(1)]`$ (2026), [pinned manuscript](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf), Theorem 1.1 and its concluding cost analysis.
- **[LP]** H. W. Lenstra, Jr. and C. Pomerance, *A rigorous time bound for factoring integers*, J. Amer. Math. Soc. **5** (1992), 483–516, [doi:10.1090/S0894-0347-1992-1137100-0](https://doi.org/10.1090/S0894-0347-1992-1137100-0).
- **[NFS]** A. K. Lenstra and H. W. Lenstra, Jr., eds., *The Development of the Number Field Sieve*, LNM **1554**, Springer (1993), [doi:10.1007/BFb0091539](https://doi.org/10.1007/BFb0091539).
- **[H]** Jose Brox, [prior research snapshot](https://github.com/JoseBrox/factoring-algorithms/tree/94d84cf90cc958aebde8853a1ecfcda304f60500/research/2026-11-25-cogentic), including the retained-construction audit notes.

The [comparison source register](docs/comparison_sources.md) records the exact claims and a source L-notation discrepancy. Full references appear in each manuscript.

## Author, citation, and license

**Jose Brox.** Cite a specific manuscript and a commit identifier so that the version of the result is unambiguous. [CITATION.cff](CITATION.cff) and [CITATION.bib](CITATION.bib) provide repository-level citation metadata.

Original material in this repository is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**; see [LICENSE](LICENSE). Upstream material retains its own attribution; see [NOTICE](NOTICE). This is an independent research repository, with no claim of Google endorsement. The mathematical investigations and preparation of this collection used AI assistance; authorship, provenance, and the status of each result are stated explicitly.

[D]: https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf
[R]: https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf
[LP]: https://doi.org/10.1090/S0894-0347-1992-1137100-0
[NFS]: https://doi.org/10.1007/BFb0091539
[H]: https://github.com/JoseBrox/factoring-algorithms/tree/94d84cf90cc958aebde8853a1ecfcda304f60500/research/2026-11-25-cogentic

The [full Lean completion register](docs/lean_completion.md) tracks checked proof packages. The [QRH-based weighted progression proof](docs/qrh_weighted_progressions.md) and [rough/bad-child continuation](docs/weighted_rough_bad_child.md) are written mathematical results, not checked analytic Lean endpoints. The [squarefree saddle expansion](docs/deterministic_saddle_proof.md), [effective reconstruction](docs/effective_number_field_recovery.md), [enlarged fibre coupling](docs/randomized_fibre_coupling.md), and [conditional local moment transfer](docs/randomized_local_moments.md) develop further parts of the remaining mathematical contracts.

The [QRH-based deterministic squarefree progression proof](docs/qrh_deterministic_progressions.md), [rational-root smoothing](docs/randomized_rational_root_smoothing.md) and [setup/readiness assembly](docs/randomized_setup_readiness.md) extend the written conditional arguments. Their complete analytic and algorithmic Lean verification remains open.

The [external int-fac audit](docs/int_fac_comparison.md) records a stronger deterministic two-thirds endpoint from the independently verified full Dirichlet GRH, its reported build evidence, and reuse/licensing considerations. Our own pinned quasi-RH integration now passes its source build and axiom audit.

**Current deterministic research priority:** [exact targeted half-scale search](docs/targeted_half_scale_search.md) and [prescribed ramified targets](docs/ramified_target_construction.md). The initial ideal target is now constructed without smoothness, and the exact certificate search fits the half-scale budget. Uniform paired-unit target coverage remains open; the new results do not change the proved general worst-case bound.

The latest [half-scale necessary rank and unit-height bounds](docs/half_scale_unit_rank_obstruction.md) rule out ordinary short-unit completion on most balanced inputs. The [full-degree factor-refinement search](docs/full_degree_factor_refinement.md) eliminates norm-factorization and bad-prime restrictions in the exact relation decision. Uniform target coverage, not the decision's cost, is still open.

The [scalar-free coverage audit](docs/scalar_free_target_coverage.md) removes diagonal rational rank, proves a private-prime obstruction to rank-only arguments, and identifies the exact target coset order in the common-order unit quotient. Uniform coverage of the half-scale family remains unproved.

The [one-field rank-one continuation](docs/one_field_rank_one_coverage.md) explicitly constructs a full unit-log basis with prescribed modular images and all but one independent congruence-unit direction. Its exact finite extraction succeeds with certified logarithm intervals. Uniform existence of the final transverse relation remains open.

The [exact 2-adic rank-one extractor](docs/padic_rank_one_extraction.md) replaces real-log reconstruction by integer lifting in the quadratic branch, and gives a first-jet sufficient criterion and sharp linear-mark norm restrictions. The [adversarial parameter theorem](docs/adversarial_rank_one_parameter.md) constructs valid field parameters that force all unit relations in any predetermined bounded polynomial family to be trivial. It rules out coverage based solely on the field construction guards, not coverage for the specific least-C construction. The uniform half-scale existence theorem is still open.

The [positive smooth-relation coverage theorem](docs/positive_smooth_relation_coverage.md) proves full-rank rational relation existence using prime-character moments, without any new smoothness conjecture. It gives uniform randomized and nonuniform deterministic half-scale algorithms. A uniform deterministic dense-product hitting algorithm remains open.

The [recent derandomization audit](docs/prime_word_derandomization_audit.md) gives a precise low-space verifier target using the L=RL=BPL probability-approximation theorem, identifies the streaming residue obstruction and the one-third entropy barrier, and records deterministic Miller primality testing from the verified Dirichlet inputs. Uniform half-scale search remains open.

The [common-anchor continuation](docs/common_anchor_derandomization.md) replaces the adaptive positive-relation search by a single dense residue search, proves nonsingularity of the signed translation matrix and polynomial-size nonuniform advice, and isolates the read-once versus reusable-randomness barrier in its exact low-workspace verifier. Uniform deterministic half-scale factoring remains open.

The [narrow-band streaming construction](docs/narrow_band_streaming_atoms.md) replaces the smoothness verifier by exact one-pass modular atoms and provides a half-scale conditional-count oracle for bounded-degree combinations. Uniformly hitting their full Boolean composition remains open.

The [shared AP/lattice counting continuation](docs/ap_lattice_conditional_counting.md) gives exact arbitrary-degree conjunction counts using CRT and Euclidean floor sums, and a deterministic construction of partial multiplicative relations with prescribed prime factors. Aggregating over unspecified prime choices or guaranteeing smooth residual cofactors remains open.

[Primitive-ratio lattice aggregation](docs/primitive_ratio_lattice_aggregation.md) now gives exact compressed enumeration of smooth suffix pairs in determinant-scale boxes and a factor-free graph method for cancelling large residual cofactors. Dense short-ratio coverage is proved, but uniform deterministic selection at the required target powers remains open.

[Dyadic balancing and pooled cofactor relations](docs/power_shift_pooled_relations.md) removes collinear target-lattice obstructions by admissible smooth shifts, and permits exact global cancellation across distinct target primes. Uniform successful rank increase within the half-scale budget is still open.

[Adaptive rank-or-residual theorem](docs/adaptive_rank_or_residual.md) makes every residual dependence yield strict base-rank progress by exact exponent separation. Uniform control of new independent residual directions remains open; finite negative experiments are included.

The [support-budget and 2-saturation continuation](docs/support_budget_and_two_saturation.md) gives exact factor-free residual-span membership, support-growth accounting and complete 2-primary readout from the full pooled relation lattice. A factor can now be recovered even with zero pure rank. Uniform support-budget control and uniform deterministic half-scale factoring remain open.

[Primary pooling and batch-affine separation](docs/primary_pool_extraction.md) extends the exact readout beyond square roots of unity, gives a half-scale LLL exit from a sufficiently large certified common order, and makes signed affine residual dependencies rank-increasing. Uniform success remains open.

[Factor-free squareclass pooling](docs/squareclass_ratio_pool.md) permits exact first-level square congruence extraction without rational cofactor cancellation, and succeeds on two previously difficult test inputs using longer parity dependencies. Uniform coverage remains open.

[Character-lift ratio coverage](docs/character_lift_ratio_coverage.md) supplies a bounded constraint-progress mechanism using Jacobi-labelled torsion and proves uniform density of differently labelled short ratios for eligible inputs. Exact lattice queries and modular linear algebra are deterministic; the uniform selection of successful queries remains open.
