# Progression, norm and readiness checkpoint — 26 November 2026

## Confirmed builds

- [Run 45837943265](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45837943265), source `f4421258972a5d8bf0b8f46b172076a7def2cf86`: strict individual compilation of RationalRecovery (three named roots) and SaddleDecay (four).
- [Run 45842191300](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45842191300), source `454feef23c74a5728c51b3802aa144356a82beba`: after promotion, full aggregate audit passed (682 logical declarations, including 526 kernel theorem objects).
- [Run 45843433818](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45843433818), source `fa144d1049d3e1aaab33e56293b881e187b9bbd1`: strict independent candidate compilation, including NumberFieldNorm and PrefixBounds.
- [Run 45843906600](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45843906600), source `f40c29b418f4cd8b4dea7a8785286ffdfcc11092`: aggregate build and axiom audit passed with pinned dependencies, warnings as errors, 706 logical declarations including 548 kernel theorem objects. The core contains **266 explicitly named source theorems in 37 modules**. Kernel object counts include generated and private objects and are not the named source theorem count.

NumberFieldNorm certifies the actual power-basis norm formula for a linear factor, its nonmonic leading-coefficient correction, and the scaled monic integral-root construction. PrefixBounds certifies the injective unit-residue count, normalized two-prefix Cauchy–Schwarz bound and terminal Euler-product bound. RationalRecovery and SaddleDecay are also in the core. These are components, not end-to-end algorithm theorems.

IdealCancellation and PrimitiveFibre remain staged at this checkpoint; earlier candidate attempts failed, and the repair at `a9d86e1751cf4913465c1fcdc25712c91c767d13` is being checked by [run 45844337004](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45844337004). They are not included in the above theorem count.

## New written arguments

- [Deterministic squarefree progressions from quasi-RH](../../docs/qrh_deterministic_progressions.md): conditional uniform progression and principal windowed-saddle argument using a fixed zero-free strip, two-prefix decomposition, and a compact smooth cutoff.
- [Enlarged rational-root smoothing](../../docs/randomized_rational_root_smoothing.md): written conditional root distribution and slope-bin estimate under the stated weighted AP and lattice inputs.
- [Setup sampler and global readiness assembly](../../docs/randomized_setup_readiness.md): written conditional C1 argument connecting the coefficient sampler, moment bounds and valid-history backward inequalities. The actual machine, sampler and complete formal transfer remain unverified. C2–C5 remain separate obligations.

The exact modern QRH dependency build is still pending after the pinned upstream compatibility patch ([run 45836288815](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836288815), [run 45837815223](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45837815223)). No passing project QRH build is claimed here. The earlier independently checked comparator endpoints do not substitute for this integration.

No additional whole milestone is counted yet. See the [fixed completion register](../../docs/lean_completion.md).

## Confirmed subsequent checks

Both patched QRH builds (45836288815 and 45837815223) passed and all seven roots were audited. Candidate run 45844337004 also passed, including IdealCancellation and PrimitiveFibre. Their exact sources were promoted at 25b4191; the current named source theorem count is 277 in 39 modules, with the new aggregate receipt pending. The fixed milestone count is now 17/36; see the [comparison](../../docs/int_fac_comparison.md).

### Subsequent full build

Run [45851754483](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45851754483) passed pinned dependencies, warning-free compilation and compiled axiom audit after the two additional modules were promoted. The log records 728 declarations, including 566 theorems. All 277 explicitly named source theorems in 39 modules are thus covered by the aggregate build. The new polynomial-mark construction is separate written research and is not counted as a Lean milestone.
