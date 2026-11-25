"""Compare public ring code to an independent 2x2 matrix representation.

The legacy finite-count checker is separately retained for provenance. This
test uses a different ring representation for powering, then compares public
splitting outputs to the independently retained finite-count implementation.
"""

from pathlib import Path
from math import gcd
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from factoring_after_google import chain_split, one_shot_split, quadratic_power
from verify_ramification_and_relation import relation_factor, relation_chain_factor


def matrix_mul(a, b, n):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) % n
             for j in range(2)] for i in range(2)]


def matrix_power(u, v, b, exponent, n):
    base = [[u % n, (b * v) % n], [v % n, u % n]]
    z = [[1, 0], [0, 1]]
    # Deliberately use direct multiplication; small exact comparison cases.
    for _ in range(exponent):
        z = matrix_mul(z, base, n)
    return z[0][0], z[1][0]


def checks():
    powers = split_cases = factors = invalid = 0
    for n in (3, 9, 15, 25, 35, 45, 63, 105):
        for b in range(1, min(n, 9)):
            for u in range(4):
                for v in range(3):
                    for e in (0, 1, 2, 3, 8, 13):
                        assert quadratic_power((u, v), e, b, n) == matrix_power(u, v, b, e, n)
                        powers += 1
            for m in (2, 4, 6, 12, 24, 48):
                for a in range(n):
                    got = chain_split(n, b, m, a)
                    assert got == relation_chain_factor(n, b, m, a)
                    assert one_shot_split(n, b, m, a) == relation_factor(n, b, m, a)
                    if got is not None:
                        assert 1 < got < n and n % got == 0
                        factors += 1
                    split_cases += 1
    for args in ((2, 1, 2, 0), (35, 2, 0, 0), (35, 2, 3, 0), (35, 2, -2, 0)):
        try:
            chain_split(*args)
        except ValueError:
            invalid += 1
        else:
            raise AssertionError("Invalid input was accepted")
    assert [a for a in range(35) if chain_split(35, 2, 48, a)] == list(range(35))
    return {"matrix_power_comparisons": powers, "splitting_comparisons": split_cases,
            "proper_factors_checked": factors, "invalid_inputs_rejected": invalid,
            "scope": "Finite exact public-implementation verification"}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
