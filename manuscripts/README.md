# Manuscripts

Author: **Jose Brox**. Version 0.1.0, 25 November 2026. CC BY 4.0.

| Manuscript | Read | Scope |
|---|---|---|
| *Deterministic Integer Factoring with Exponent $2/3+\varepsilon$* | [PDF](../papers/deterministic_factoring.pdf) · [source](deterministic_factoring/main.tex) | The general deterministic construction, changed analytic estimates, exact extraction, and the remaining large-modulus barrier |
| *Sparse Gram Methods for Deterministic Supplied-Order Splitting* | [PDF](../papers/order_splitting.pdf) · [source](order_splitting/main.tex) | The supplied-exponent problem, sparse Gram contradiction, exact arithmetic, and character estimates |
| *Deterministic Quadratic Nonresidue Construction* | [PDF](../papers/quadratic_nonresidues.pdf) · [source](quadratic_nonresidues/main.tex) | The prime-input specialization, construction, certificate, and complexity |
| *Sparse Kernels and a Repaired Recursion Budget for Integer Factoring* | [PDF](../papers/randomized_factoring.pdf) · [source](randomized_factoring/main.tex) | Proved sparse-kernel machinery and a **conditional** improved general randomized factorer |
| *Quadratic Relation Chains for Integer Splitting* | [PDF](../papers/quadratic_relations.pdf) · [source](quadratic_relations/main.tex) | A retained auxiliary construction, complete local theorem, exact implementation, and examples |

Each PDF has its own introduction, theorem statements, proof, and bibliography. The splitter and nonresidue PDFs each include the complete [shared quadratic appendix](shared/quadratic_package.tex). Sharing its source keeps corrections synchronized without requiring readers to switch between PDFs for the technical argument.

The manuscripts build from the **repository root**, not their individual directories:

```sh
python3 scripts/build_manuscripts.py
```

Each `main.tex` supplies the title and bibliography and includes its `body.tex`. The common [preamble](shared/preamble.tex) controls typography. References are maintained in [one BibTeX database](shared/references.bib). See [reproducibility](../docs/reproducibility.md) for dependencies and build evidence.

For citation, give the manuscript title, author, version date, and repository commit. These are research manuscripts with explicitly stated dependencies, not claims of completed external review or formal verification. The [proof-status register](../docs/proof_status.md) is the guide to those distinctions.
