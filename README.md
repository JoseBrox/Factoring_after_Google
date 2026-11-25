# Factoring after Google

**Integer factoring, supplied-order splitting, and quadratic nonresidues — research by Jose Brox using ChatGPT Astra 6 and 6.2.**

This repository develops and audits improvements to the November 2026 Cogentic factoring manuscripts released by Google Research. It contains readable research manuscripts, explicit algorithm specifications, exact finite verification programs, and pinned source material. The aim is to make every claim easy to locate, reconstruct, and challenge.

**Start here:** [results and proof status](docs/proof_status.md) · [manuscripts](manuscripts/README.md) · [reproduce the checks](docs/reproducibility.md) · [sources and comparisons](docs/comparison_sources.md).

## Results at a glance

Put $L=\log N$, and use the standard convention

$$L_N[\alpha,c]=\exp\!\left((c+o(1))(\log N)^\alpha(\log\log N)^{1-\alpha}\right).$$

The table compares like-for-like inputs and computational models. **“Previous” refers to the bound in the pinned source being improved**, with established historical benchmarks listed immediately below. The newly posted Google manuscripts and the new manuscripts here are research claims open to independent scrutiny; this table is not a certification of world-record status. Comparisons are dated **25 November 2026**.

| Algorithm | Complexity developed here | Previously best-known comparison bound / cited predecessor | Status and manuscript |
|---|---|---|---|
| **Deterministic general integer factoring** | $\exp(O_\varepsilon(L^{2/3+\varepsilon}))$ for each fixed $\varepsilon>0$ | $O(\exp(3L^{3/4}))$, Cogentic, Theorem 1.1 [D] | Written proof of the replacement schedule and analytic transfer; [PDF](papers/deterministic_factoring.pdf) · [LaTeX](manuscripts/deterministic_factoring/) |
| **Deterministic supplied-order splitting** | $\exp(O(\sqrt{L\log L}))\,\operatorname{len}(M)\,L^{O(1)}$ | $\exp(O(\sqrt L\log L))\,(\log M)L^2$, Cogentic, Theorem 1.2 [D] | Sparse Gram construction, with the promise described below; [PDF](papers/order_splitting.pdf) · [LaTeX](manuscripts/order_splitting/) |
| **Deterministic quadratic nonresidue construction** | $\exp(O(\sqrt{\log p\,\log\log p}))=L_p[1/2,O(1)]$ | $\exp(O(\sqrt{\log p}\,\log\log p))$, Cogentic, Theorem 1.2 [D] | Prime input $p$; [PDF](papers/quadratic_nonresidues.pdf) · [LaTeX](manuscripts/quadratic_nonresidues/) |
| **Randomized general integer factoring** | **Conditional** expected time $L_N[1/3,91.4]$, deterministic workspace $L_N[1/3,19]$ | Source headline: time $L_N[1/3,105]$, workspace $L_N[1/3,40]$, Cogentic, Theorem 1.1 [R]. Its proof also gives the tighter intermediate accounting $104/38$ | Sparse kernel theorem and recursion budget proved; widened analytic and square-certification contracts remain assumptions. [PDF](papers/randomized_factoring.pdf) · [LaTeX](manuscripts/randomized_factoring/) |
| **Quadratic relation chain** (auxiliary promised-input routine) | $O(\log M)$ quadratic-ring multiplications per random trial; success probability at least $(p+3)/(2p)>1/2$ under the mixed-sign promise | No claim of a new general factoring record; develops the retained quadratic-algebra construction N1101 [H] | Proved local theorem, executable implementation, exhaustive small-instance checks; [PDF](papers/quadratic_relations.pdf) · [code](src/factoring_after_google/quadratic_relations.py) |

**Established benchmarks, with a different evidential status.** Lenstra–Pomerance gives a rigorous randomized $L_N[1/2,1]$ bound [LP]. The general number field sieve has heuristic complexity $L_N[1/3,(64/9)^{1/3}]$, with constant about $1.923$ [NFS]. The conditional $91.4$ result is an improvement to the explicit constants in the new Cogentic framework; it is not an improvement to the heuristic GNFS constant.

**What the splitting promise means.** The input includes an even positive integer $M$ divisible by $p-1$ for every prime $p\mid N$, and $N$ is composite and not a perfect power. The algorithm uses that supplied information to find a proper factor, without randomness. Producing a suitable $M$ is a separate task. Its bit length is charged in the running time; it is not a free oracle.

The deterministic general bound is a **family approaching power $2/3$**, not an endpoint $L_N[2/3,c]$ bound. The large-modulus obstruction toward $1/2$ remains open. **No general classical algorithm with first $L$-parameter below $1/3$ is claimed here.**

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

The mathematical checks use **Python's standard library and Node.js**, with no third-party Python packages. They are deterministic and offline. The runner compares each result with the committed expected output and fails on a discrepancy. See [reproducibility](docs/reproducibility.md) for versions, individual checks, manuscript builds, and source hashes.

To rebuild the PDFs with a normal TeX Live installation containing `latexmk`, the AMS packages, `lmodern`, `microtype`, `xurl`, and `cleveref`:

```sh
python3 scripts/build_manuscripts.py
```

The GitHub Actions workflows run the checks and compile all manuscripts. Finite computations verify the listed identities and examples; they do not prove asymptotic analytic estimates or certify an entire formal proof.

## What is reused, and what changes

The deterministic work retains Cogentic's exponent-annihilation architecture and develops a new parameter schedule with its analytic justification. The splitting and nonresidue improvements replace a large auxiliary family with a sparse Gram family and use exact enumeration in fixed-dimensional quadratic arithmetic. The randomized work retains the relation-tree architecture, uses sparse black-box linear algebra, and repairs the recursive budget.

The retained construction N1101 contributes the quadratic relation chain. Other retained ideas have their own continuation notes: N1505 yields a section once factors are known, N1124 has a trace-based rank counterexample, N1002 does not justify a full coefficient-prefix shortcut, and N1131 does not by itself turn a common lattice relation into a separator. See [provenance](provenance/README.md). These are kept as individually assessed research directions.

## Open work

- Prove the widened arithmetic-progression, fibre, local-moment, and square-certification estimates required by the randomized $91.4/19$ theorem.
- Overcome the large-modulus equidistribution obstruction in the deterministic construction; reducing exponents on a spreadsheet alone does not remove it.
- Implement and benchmark the complete theoretical factorers, including the exact algebraic subroutines and explicit finite thresholds.
- Obtain independent mathematical review and, separately, a complete machine-checked development. The source's announced Lean artifacts are not treated here as checked evidence.
- Find a new mechanism that can beat the $1/3$ balance in the present randomized architecture. This is an open research objective.

Contributions are welcome: a precise counterexample or a corrected lemma is as useful as a faster algorithm. See [CONTRIBUTING.md](CONTRIBUTING.md).

## References

- **[D]** Cogentic / Google Research, *Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction* (2026), [pinned manuscript](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf), especially Theorems 1.1–1.2.
- **[R]** Cogentic / Google Research, *Unconditional Integer Factorization in Time $L_N[1/3,O(1)]$* (2026), [pinned manuscript](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf), Theorem 1.1 and its concluding cost analysis.
- **[LP]** H. W. Lenstra, Jr. and C. Pomerance, *A rigorous time bound for factoring integers*, J. Amer. Math. Soc. **5** (1992), 483–516, [doi:10.1090/S0894-0347-1992-1137100-0](https://doi.org/10.1090/S0894-0347-1992-1137100-0).
- **[NFS]** A. K. Lenstra and H. W. Lenstra, Jr., eds., *The Development of the Number Field Sieve*, LNM **1554**, Springer (1993), [doi:10.1007/BFb0091539](https://doi.org/10.1007/BFb0091539).
- **[H]** Jose Brox, [prior research snapshot](https://github.com/JoseBrox/factoring-algorithms/tree/94d84cf90cc958aebde8853a1ecfcda304f60500/research/2026-11-25-cogentic), including the retained-construction audit notes.

The [comparison source register](docs/comparison_sources.md) records the exact claims and a source L-notation discrepancy. Full references appear in each manuscript.

## Author, citation, and license

**Jose Brox.** Cite a specific manuscript and a commit identifier so that the version of the result is unambiguous. [CITATION.cff](CITATION.cff) and [CITATION.bib](CITATION.bib) provide repository-level citation metadata.

Original material in this repository is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**; see [LICENSE](LICENSE). Upstream material retains its own attribution; see [NOTICE](NOTICE). This is an independent research repository, with no claim of Google endorsement. The mathematical investigations and preparation of this collection used AI assistance; authorship, provenance, and the status of each result are stated explicitly.
