"""Exact quadratic relation splitting over (Z/nZ)[X]/(X^2-b).

Copyright 2026 Jose Brox. CC BY 4.0; see LICENSE.

Each returned integer is a proper divisor, regardless of the unverified
mixed-sign promise. Under the manuscript's promise (distinct p,q dividing odd
n, b a unit and square modulo p but nonsquare modulo q, even m divisible by
p-1), uniform a modulo n gives chain_split success probability at least
(p+3)/(2*p). Finding a suitable b and m is outside this routine.

The representation (u,v) denotes u+v*X. Only integer arithmetic is used.
"""

from math import gcd


def _multiply(x, y, b, n):
    return ((x[0] * y[0] + b * x[1] * y[1]) % n,
            (x[0] * y[1] + x[1] * y[0]) % n)


def quadratic_power(x, exponent, b, n):
    """Return x**exponent in the quadratic ring, by binary exponentiation."""
    if n < 2 or exponent < 0:
        raise ValueError("Require n >= 2 and a nonnegative exponent")
    result, base = (1, 0), (x[0] % n, x[1] % n)
    b %= n
    while exponent:
        if exponent & 1:
            result = _multiply(result, base, b, n)
        exponent >>= 1
        if exponent:
            base = _multiply(base, base, b, n)
    return result


def _validate(n, m):
    if n < 3 or n % 2 == 0:
        raise ValueError("The quadratic relation routine requires odd n >= 3")
    if m < 2 or m % 2:
        raise ValueError("The supplied exponent m must be positive and even")


def _proper(g, n):
    return g if 1 < g < n else None


def one_shot_split(n, b, m, a):
    """Try the denominator gcd and the final exponent relation only.

    This is included for comparison. Its success can be lost when the final
    exponent saturates both local groups; use chain_split for the theorem.
    """
    _validate(n, m)
    b, a = b % n, a % n
    denominator = gcd(a * a - b, n)
    if denominator != 1:
        return _proper(denominator, n)
    u, v = quadratic_power((-a, 1), m, b, n)
    return _proper(gcd(n, gcd(u - 1, v)), n)


def chain_split(n, b, m, a):
    """Try one parameter a; return a verified proper factor or None.

    Write m=2**t*s with s odd. At each exponent 2**j*s, for 0<=j<=t,
    test both the linear-coefficient gcd and the identity-relation gcd.
    The cost is O(log m) quadratic-ring multiplications and gcd tests.
    This function performs no random sampling; callers choose a explicitly.
    """
    _validate(n, m)
    b, a = b % n, a % n
    denominator = gcd(a * a - b, n)
    if denominator != 1:
        return _proper(denominator, n)
    t, odd = 0, m
    while odd % 2 == 0:
        t, odd = t + 1, odd // 2
    z = quadratic_power((-a, 1), odd, b, n)
    for j in range(t + 1):
        for candidate in (gcd(n, z[1]), gcd(n, gcd(z[0] - 1, z[1]))):
            if 1 < candidate < n:
                assert n % candidate == 0
                return candidate
        if j < t:
            z = _multiply(z, z, b, n)
    return None
