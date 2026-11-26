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
audit reports fail the build. A fresh successful run has not been observed
in the current session; the external comparator evidence is distinct from
this project's own integration evidence.

No unconditional general polynomial-time factoring theorem is claimed.
