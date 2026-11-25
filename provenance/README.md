# Research provenance

The public manuscripts consolidate work from `JoseBrox/factoring-algorithms`, frozen at commit **94d84cf90cc958aebde8853a1ecfcda304f60500**. The files in `notes/` are preserved working notes, not the recommended entry point for the current theorems. Their source paths and SHA-256 hashes are recorded in [manifest.json](manifest.json).

## Main lines of development

| Line | Working notes | Current presentation |
|---|---|---|
| Deterministic parameter schedule | [parameter compression](notes/deterministic-parameter-compression.md), [analytic audit](notes/deterministic-analytic-audit.md), [algebraic completion](notes/deterministic-algebraic-completion.md) | Deterministic factoring manuscript |
| Supplied-order and nonresidue improvement | [sparse Gram construction](notes/sparse-gram-order-splitting.md), [splitting core audit](notes/deterministic-splitting-core-audit.md), [enumeration and Burgess audit](notes/enumeration-burgess-audit.md) | Splitter and nonresidue manuscripts with shared appendix |
| Randomized costs | [sparse factorer](notes/sparse-randomized-factorer.md), [recursion audit](notes/randomized-recursion-audit.md) | Conditional randomized manuscript |
| Retained constructions | [provenance audit](notes/splitting-provenance-audit.md), [individual continuations](notes/retained-individual-continuations.md) | Quadratic relation manuscript and explicitly scoped open directions |

## Retained construction map

**N1101, quadratic algebras.** This supplies the executable relation chain. The mixed-sign promise, scalarization stage, success probability, and prime-power cases are treated in the new manuscript.

**N1505, a selected section.** The verified continuation constructs a section after the factors are available. It does not provide a new efficient general factoring method or eliminate the missing section-construction step.

**N1124, trace and rank.** A rank-one nilpotent matrix gives the decisive trace-only counterexample. The finite check is retained because it prevents reusing the rejected inference.

**N1002, quotient coefficients.** Computing a fixed quotient coefficient does not establish the full prefix bound needed by the proposed shortcut. The note identifies that distinction and an obstructing polynomial.

**N1131, projective lattice relations.** A short relation common to the local components need not split the integer. An independent separator argument remains necessary.

The old catalogue identifiers are research labels, not published algorithm names. The current manuscripts introduce every object they use rather than requiring readers to know the catalogue.

Some historical notes contain source URLs that moved or exploratory citations superseded by the manuscript bibliography. Their text is preserved for attribution and audit history; current comparisons and proof status are governed by `docs/` and `manuscripts/`.
