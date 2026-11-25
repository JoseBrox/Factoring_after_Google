"""Exact small checks for enumeration-burgess-audit.md; no external packages."""

from fractions import Fraction
from math import isqrt
import json


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    assert z in (1, p - 1)
    return 1 if z == 1 else -1


def main():
    p = 5
    values = [(x**3 + 2*x) % p for x in range(p)]
    roots = [x for x, y in enumerate(values) if y == 0]
    character_sum = sum(legendre(y, p) for y in values)
    assert roots == [0]
    assert character_sum == -4
    # A cubic cannot be a constant times a polynomial square.
    assert len(roots) - 1 == 0

    terms = [
        Fraction(1, 3200), Fraction(1, 16000), -Fraction(3, 80),
        Fraction(1, 32000), -Fraction(15, 256), Fraction(3, 32),
        Fraction(3, 8000),
    ]
    exponent = sum(terms)
    assert exponent == -Fraction(1, 640)
    assert exponent < -Fraction(1, 4000)

    # Safe rational bounds for the reduced-basis coordinate argument.
    # sqrt(2) < 10/7, sqrt(8) < 20/7; rounding up enlarges the box.
    ratio = Fraction(101, 100)
    gs_bounds = [ratio, ratio * Fraction(10, 7), 2*ratio,
                 ratio * Fraction(20, 7)]
    coefficient_bounds = [0] * 4
    for i in range(3, -1, -1):
        b = gs_bounds[i] + Fraction(sum(coefficient_bounds[i+1:]), 2)
        coefficient_bounds[i] = b.numerator // b.denominator
    assert max(coefficient_bounds) <= 8

    print(json.dumps({
        "finite_field_counterexample": {"p": p, "roots": roots, "values": values,
                                        "character_sum": character_sum},
        "burgess_exponent": str(exponent),
        "lll_safe_coordinate_bounds": coefficient_bounds,
        "scope": "Exact finite counterexample and rational exponent/coordinate arithmetic"
    }, indent=2))


if __name__ == "__main__":
    main()
