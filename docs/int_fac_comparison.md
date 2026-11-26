# Audit of gldanoob/int-fac and reuse opportunities

Inspected 26 November 2026 at commit
[d77c21fc89ce983e917282b5b6ba165292a8b0d4](https://github.com/gldanoob/int-fac/tree/d77c21fc89ce983e917282b5b6ba165292a8b0d4).
This is a source/statement and evidence audit, **not a new local build of
the external factoring proof**. The repository is public; its GitHub
metadata reports no license and the recursive tree has no license file.
No external proof source has been copied into this project.

## What is actually claimed and checked

- [CogenticWithGRH.lean](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/formal/cogentic/CogenticWithGRH.lean)
  imports Main and Cogentic. Its parameter-free theorem
  `Cogentic.binary_factorization_two_thirds` has type
  `Cogentic.Companion.LocalFactorizationBound`.
  The proof applies the exact Dirichlet critical-line theorem
  `LFunction_eq_zero_re`, and a run_cmd audit rejects every
  transitive axiom other than propext, Classical.choice, Quot.sound.
- [TwoThirdsFactorization.lean](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/formal/cogentic/Cogentic/TwoThirdsFactorization.lean)
  expands LocalFactorizationBound: there are fixed natural generator
  cutoffs s,k, a proof of generation for every modulus, and a positive
  absolute C such that one algorithm emits prime-factor bit lists with
  correct product and multiplicity on every N>=2; for every epsilon>0,
  on all sufficiently large inputs its specified bit charge is at most
  exp((C+epsilon)(log N)^(2/3)(log log N)^(1/3)).
  The explicit constant available in the proof is
  max(6528665845,C1+12A+131117), with C1,A splitter bounds.
  The paper's smaller constant 400000 is not the constant of the
  verified exhaustive-minor implementation.
- [BinaryFactorization.lean](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/formal/cogentic/Cogentic/BinaryFactorization.lean)
  defines the output and charge from the same recursion tree, rather
  than a theorem about the existence of an arbitrary factorization
  with a supplied per-node charge. SearchTraceCost identifies the
  metered search's result with the actual collector, and DriverBitCost
  accounts for fallback/guards. The intended machine interpretation
  still merits checking: metered bit-cell operations, encoding and
  simulation overhead are not a theorem about wall-clock Lean runtime
  or automatically a standard Turing-machine complexity theorem.
  Existential fixed cutoff constants suffice for the theoretical
  asymptotic claim, not for an optimized turnkey factorer.
- [MissRank.lean](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/formal/cogentic/Cogentic/MissRank.lean)
  has the all-large-input, every-target rank theorem
  eventual_box_has_rank, from the critical-line proposition.
  Thus the headline theorem is materially stronger than a
  conditional extraction certificate or a supplied rank witness.
- The [external verification report](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/research/cogentic-worst-case-verification.md)
  reports a successful combined build on 26 November (10,210 Lake jobs),
  with the three standard axioms only. It uses the readable GRH
  cache and 31 selected, hashed and ported original analytic modules.
  No Actions workflows or runs were present in this repo at inspection.
  We inspected the main endpoint, cost definition, critical-line
  statement, rank theorem, selected analytic modules and build scripts;
  we did not independently replay all 319 Cogentic submodules.
  The claimed proof is credible, but a fresh sandboxed source build
  and independent exported-statement/kernel comparison would increase
  confidence in the factoring result itself.

## Full Dirichlet GRH is now a verified stronger dependency

Andrew Sutherland's independent reports
[original GRH](https://math.mit.edu/~drew/grh/) and
[short GRH](https://math.mit.edu/~drew/shortgrh/) record successful
source builds, statement matching and multiple kernel checks for
the ordinary RH and Dirichlet GRH statements (not general Hecke or
Dedekind GRH). The shorter readable and compact editions use Lean
4.35.0 and mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679.
The readable source/cache is pinned at
[leanprover-community/riemann-hypothesis@2d39be8e0f21c2e58b067f6e70e6d21dc63a4c99](https://github.com/leanprover-community/riemann-hypothesis/tree/2d39be8e0f21c2e58b067f6e70e6d21dc63a4c99),
which carries Apache-2.0. Its Statements.lean blob is identical to
the original archive at 3091d9fb6eab9943787c5d19d0b7848bf364eac2.
The theorem LFunction_ne_zero_of_half_lt_re directly implies the
Dirichlet seven-eighths zero-free theorem at the same mathlib revision.
The short-GRH release itself has stronger independent verification
evidence than the downstream factoring proof. Our QRH target is now
also independently built by our own CI (see below); it is useful as
a separate weaker-hypothesis result but need not be the primary
analytic dependency when full Dirichlet GRH suffices.

## Comparison

| Problem | Our current result | External result |
|---|---|---|
| Worst-case deterministic factoring | exp(O_epsilon((log N)^(2/3+epsilon))), written using classical inputs; component Lean proofs | L_N[2/3,O(1)], parameter-free Lean endpoint, reported combined build; strictly stronger scale |
| Supplied-order splitting / prime nonresidues | Subexponential written bounds; QRH polylog witness argument; partial formalization | Checked polynomial-size generating bases under full GRH and concrete local supplied-exponent splitter; polylog-time prime nonresidue follows by scanning Euler signs |
| Randomized worst-case expected time | L_N[1/3,91.4], conditional; deterministic space L_N[1/3,19] | Written L_N[1/3,(32/3)^(2/3)] (~4.84565), using randomized deterministic-extractor variants; not part of the checked endpoint, no matching audited space bound |
| Deterministic mean time | No comparable complete-input mean theorem established here | Written L_X[1/3,O(1)] arithmetic mean over X<N<=2X; not a worst-case bound |
| Quadratic mixed-sign relation chain | Separate verified finite theorem and arithmetic budgets | No equivalent result identified in the inspected headline proofs |

The external randomized coefficient is a different extraction algorithm,
not a verification of our enlarged recursive tree. Its optimized
parameter and randomized elimination/extraction arguments must be
audited separately. Source:
[research/cogentic-randomized-relation-time.md](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/research/cogentic-randomized-relation-time.md).
The mean-time result is not comparable to a per-input guarantee:
[universal-score sampler](https://github.com/gldanoob/int-fac/blob/d77c21fc89ce983e917282b5b6ba165292a8b0d4/research/cogentic-universal-score-sampler.md).
The external fixed schedule and the two-thirds logarithmic scale
are the same broad Cogentic construction as ours; their full-GRH
contour method provides stronger uniformity and their fixed-schedule
constants and actual executable extractor are different.

## Recommended integration

1. Independently build the pinned external theorem in a separate
   Lean 4.35 workspace with read-only credentials, verify the
   exact expanded endpoint and its dependency axioms; export
   it for Comparator or independent kernel checking. Do not
   try to import 4.35 olean files into the 4.19 or 4.34 project.
   The external short-GRH preparation script and manifest document
   which analytic declarations are required.
2. Pin the Apache-licensed readable GRH upstream directly in a new
   project target. Import the exact Main endpoints, not an axiom
   alias or a textually similar cross-version declaration. Reuse
   its allowed analytic ingredients subject to their licenses.
3. Seek a license or explicit permission for the external factoring
   proof files before vendoring them. Public visibility alone does not
   grant permission to redistribute them. A read-only independent
   build and mathematical rederivation remain possible. If permission
   is obtained, first reuse the exact dependency closure for the
   deterministic endpoint, then the character estimate/small generator,
   smooth windows and conditional Gaussian/covariance, rank/deletion,
   field/valuation and reconstruction, and metered driver modules.
   Preserve authorship, pinned revision and licenses.
4. Adopt the stronger full-GRH deterministic endpoint as a comparison
   baseline, not as a new result attributable to this repository.
   Build explicit adapters to our actual statements; fixed-schedule
   endpoints do not imply the more general parameter-uniform
   propositions automatically. Use the shared analytic estimates
   to shorten our randomized proof, then audit the promising 4.84565
   randomized coefficient and its memory cost. Keep our QRH route,
   independent algorithms and quantitative space goal as separate
   contributions.

## Our current verification status

The new successful QRH builds
[45836288815](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836288815)
and [45837815223](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45837815223)
both compiled the pinned OpenAI proof/adapter and audited all seven roots.
This completes milestone 17. Independently, the previously staged
IdealCancellation and PrimitiveFibre passed strict compilation in
[45844337004](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45844337004)
and were promoted in 25b4191. The existing deterministic and randomized
full endpoint milestones remain open. No external factoring result
has been counted toward our project's completion metric.
