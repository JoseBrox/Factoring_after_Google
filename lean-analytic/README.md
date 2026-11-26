# Verified strong PNT bridge

This separate Lean target imports the actual `StrongPNT` theorem from [PNT+](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/tree/e9906138410f8f76ca66b9bc252d0993f3ee348c) at commit `e9906138410f8f76ca66b9bc252d0993f3ee348c`, with Lean 4.36.0 and upstream mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`. It does not replace the existing Lean 4.19.0 arithmetic project. The imported theorem and all five adapter theorems were checked for their complete axiom dependencies: only `propext`, `Classical.choice`, and `Quot.sound` occur.

| Theorem | Verified statement |
|---|---|
| `sqrt_error_scale` | The square-root prime-power correction fits the strong PNT error scale for each positive decay constant. |
| `theta_strongPNT` | The actual Chebyshev theta function has the strong PNT asymptotic. |
| `theta_relative_error` | Eventual relative error at most any positive epsilon. |
| `dyadic_density_of_theta` | Two explicit relative error bounds imply at least x/(6 log x) primes in the dyadic interval. |
| `dyadic_density` | That prime count holds eventually, without the two finite error hypotheses. |

This discharges a classical analytic input to the manuscripts. It does not discharge growing-modulus equidistribution, the smooth-number saddle-point estimates, or effectiveness of a numerical threshold.

## Reproduce

Use Lean 4.36.0, Git, Bash, and Python 3. From the repository root:

```sh
root="$PWD"
git clone https://github.com/AlexKontorovich/PrimeNumberTheoremAnd.git /tmp/pnt-factoring
cd /tmp/pnt-factoring
git checkout --detach e9906138410f8f76ca66b9bc252d0993f3ee348c
mapfile -t imports < <(python3 "$root/lean-analytic/cache_roots.py" PrimeNumberTheoremAnd/StrongPNT.lean "$root/lean-analytic/FactoringAnalytic.lean")
lake exe cache get "${imports[@]}"
lake build PrimeNumberTheoremAnd.StrongPNT
cp "$root/lean-analytic/FactoringAnalytic.lean" .
set -o pipefail
lake env lean -DwarningAsError=true FactoringAnalytic.lean | tee axioms.txt
python3 "$root/lean-analytic/audit.py" axioms.txt
```

[Successful source build and axiom audit](https://github.com/JoseBrox/Factoring_after_Google/actions/runs/45825262779); [build receipt](../verification/lean/library-reuse.md). The GitHub Actions workflow pins the Lean release archive's SHA-256 as well as the upstream source commit.
