"""Independent exact verification of the selected bundle-section formula.

The transition polynomial is expanded by integer binomial coefficients.
The proposed section is instead built by recursive geometric sums with
sparse polynomial multiplication.  Equality is checked coefficientwise,
not only by evaluation at a few points.  Known primes are used only by
this finite verification harness, not by a claimed transition-only solver.
"""

from math import comb, gcd, isqrt
import json


def clean(poly, n):
    return {e: c % n for e, c in poly.items() if c % n}


def add(left, right, n):
    out = dict(left)
    for e, c in right.items():
        out[e] = (out.get(e, 0) + c) % n
    return clean(out, n)


def multiply(left, right, n):
    out = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i+j] = (out.get(i+j, 0) + a*b) % n
    return clean(out, n)


def scale_shift(poly, scalar, shift, n):
    assert shift >= 0
    return clean({e+shift: scalar*c for e, c in poly.items()}, n)


def geometric_power(base, k, n):
    """Return base**k, sum(base**j, j<k), and arithmetic-gate count."""
    if k == 0:
        return {0: 1}, {}, 0
    power, series, gates = geometric_power(base, k//2, n)
    even_power = multiply(power, power, n)
    even_series = multiply(series, add({0: 1}, power, n), n)
    gates += 3
    if k % 2:
        return (multiply(even_power, base, n),
                add(even_series, even_power, n), gates+2)
    return even_power, even_series, gates


def checks():
    counts = {
        "semiprime_instances": 0,
        "prefix_gcd_checks": 0,
        "selected_value_candidates": 0,
        "nonzero_sections_checked": 0,
        "chart_coefficient_comparisons": 0,
        "geometric_power_comparisons": 0,
        "maximum_geometric_recursion_gates": 0,
    }
    primes = (3, 5, 7, 11, 13, 17, 19, 23)
    for i, p in enumerate(primes):
        for q in primes[i+1:]:
            n = p*q
            m = isqrt(n)//2 + 1
            h = 2*m-1
            assert p <= isqrt(n) <= h < q

            # Direct integer expansion of the input transition.
            transition = clean({j: comb(n, j) for j in range(1, n+1)}, n)
            prefix = [comb(n, j) % n for j in range(1, h+1)]
            prefix_gcd = n
            for c in prefix:
                prefix_gcd = gcd(prefix_gcd, c)
            assert prefix_gcd == q
            counts["prefix_gcd_checks"] += 1

            base = {0: 1, q: 1}
            power, series, gates = geometric_power(base, p, n)
            assert power == clean({q*j: comb(p, j) for j in range(p+1)}, n)
            assert gates <= 5*p.bit_length()
            counts["geometric_power_comparisons"] += 1
            counts["maximum_geometric_recursion_gates"] = max(
                counts["maximum_geometric_recursion_gates"], gates)

            for selected in range(n):
                admissible = all(selected*c % n == 0 for c in prefix)
                assert admissible == (selected % p == 0)
                counts["selected_value_candidates"] += 1
                if not admissible or selected == 0:
                    continue

                finite_first = scale_shift(series, selected, q-2*m, n)
                glued_first = scale_shift(finite_first, 1, 2*m, n)
                required_first = scale_shift(transition, selected, 0, n)
                for e in range(n+1):
                    assert glued_first.get(e, 0) == required_first.get(e, 0)
                    counts["chart_coefficient_comparisons"] += 1
                assert gcd(selected, n) == p
                counts["nonzero_sections_checked"] += 1

            counts["semiprime_instances"] += 1

    return {
        "checks": counts,
        "scope": "Finite exact prefix-annihilator and full polynomial chart-gluing verification; not a transition-only section constructor",
    }


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2, sort_keys=True))
