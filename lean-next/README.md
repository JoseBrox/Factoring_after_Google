# Staged proofs and independent checks

BitArithmetic, EulerDecay, LatticeClearing, ModularBits and CharacterMoments have been strictly compiled and individually audited and promoted into the core. The copies here retain their explicit audit roots for CI. See [the receipt](../verification/lean/qrh-continuation.md). DeterminantHeight and ModularPower remain staged until fresh warning-free compilation and audit succeed.

The separate [QRH target](../lean-qrh/) imports the exact modern endpoints. The mathematical [weighted AP proof](../docs/qrh_weighted_progressions.md) and [rough/bad-child continuation](../docs/weighted_rough_bad_child.md) require formalization of their analytic arguments. The [completion register](../docs/lean_completion.md) gives a fixed metric.

The CI workflow independently checks every file against the pinned Lean 4.19 core and records the actual compiler exit code and transitive axiom roots. It rejects any failure, warning, missing report or nonstandard axiom.
