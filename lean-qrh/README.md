# Pinned quasi-RH integration (pending fresh verification)

This standalone target imports the actual OpenAI/math proof of Dirichlet
and zeta nonvanishing in Re(s)>7/8. It pins OpenAI/math at
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, Lean 4.34.1 and the matching
mathlib revision. It is separate from the established Lean 4.19 project
and the PNT+ target; no migration of their verified results is implied.

See [the source and comparator audit](../docs/quasi_rh_audit.md) and
[the mathematical application to small witnesses](../docs/quasi_rh_witnesses.md).
The [CI workflow](../.github/workflows/lean-qrh.yml) retrieves the source,
builds the selected dependency closure, compiles the adapters and checks
the transitive axioms at the named roots. Unsupported imports or missing
audit reports fail the build. The [source build](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45832742669) passed closure discovery and installation but failed in three RellichKondrachov modules. The workflow now verifies and applies the exact upstream compatibility patch before compilation, with full build logs preserved. The [patched rebuild](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45836288815) was still running when this checkpoint was recorded. No fresh successful build is claimed; external comparator evidence is distinct from this project's own integration evidence.

No unconditional general polynomial-time factoring theorem is claimed.
