# Candidate next modules (not part of the verified core yet)

These are proof candidates committed for fresh strict CI, without changing the already verified aggregate module or theorem count. The current editing runtime has no Lean installation or outbound git access. No compilation result is claimed until the workflow and dependency audit pass.

- BitArithmetic: executable little-endian binary addition and schoolbook multiplication, decoding correctness, representation size and counted cell operations. A bit-machine model still needs to charge input length scans, counters, division, modular reduction, gcd, sampling and exponentiation. The cost here counts a full-adder cell or final carry, and one shift per multiplication recursion, rather than wall time or the Lean compiler's Nat operations.
- EulerDecay: local and finite product squared-norm decay for factors 1+z, with radius at most one. It avoids taking complex logarithms of possibly zero factors. To obtain clean smooth progression estimates, still prove the actual uniform prime sums, the Mellin inversion and saddle approximation, and prefix summation with the relevant ranges.

The separate [QRH target](../lean-qrh/) contains the exact modern imported endpoints. The [written QRH witness argument](../docs/quasi_rh_witnesses.md) provides a new route toward polynomial-time promised-input splitting and nonresidue construction, pending formalization.

The CI workflow compiles against the pinned Lean 4.19 core, rejects warnings and nonstandard axioms at the explicit roots, and preserves logs. Successful compilation is required before moving candidates into the core and running its full declaration audit.
