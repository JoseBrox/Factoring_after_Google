"""Exact finite checks of the 2026-11-27 research lemmas, not asymptotic proofs."""
from collections import Counter
from fractions import Fraction as Q
from math import gcd, isqrt
from random import Random


def mul(a, b, modulus, k):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a >> k:
            a ^= modulus
    return out


def graph_checks():
    rng = Random(20261127)
    eigen_checks = walk_checks = 0
    for n, k, modulus in [(4, 3, 0b1011), (6, 4, 0b10011)]:
        q, size = 1 << k, 1 << n
        edges = Counter()
        roots = [0] * size
        for a in range(q):
            powers = [1]
            for _ in range(n - 1):
                powers.append(mul(powers[-1], a, modulus, k))
            for w in range(size):
                p = 0
                for i, ai in enumerate(powers):
                    if w >> i & 1:
                        p ^= ai
                roots[w] += p == 0
            for z in range(q):
                v = sum((mul(z, ai, modulus, k) & 1) << i
                        for i, ai in enumerate(powers))
                edges[v] += 1
        for w in range(size):
            eig = Q(sum(c * (-1 if (w & v).bit_count() & 1 else 1)
                        for v, c in edges.items()), q * q)
            assert eig == Q(roots[w], q)
            if w:
                assert 0 <= eig <= Q(n - 1, q)
            eigen_checks += 1
        for _ in range(40):
            bad = set(rng.sample(range(size), rng.randrange(1, size)))
            beta = Q(len(bad), size)
            counts = {x: 1 for x in bad}
            for r in range(1, 7):
                probability = Q(sum(counts.values()), size * q ** (2 * (r - 1)))
                assert probability <= beta * (beta + Q(n - 1, q)) ** (r - 1)
                counts = {y: sum(counts[x] * edges[x ^ y] for x in bad)
                          for y in bad}
                walk_checks += 1
    print("exact small-bias eigenvalues:", eigen_checks,
          "walk survival bounds:", walk_checks)


def incidence_checks():
    mu = [Q(1, 2), Q(1, 3), Q(1, 6)]
    rows = [Q(1, 10), Q(2, 5), Q(1, 20)]
    factors = [Q(1, 20), Q(0), Q(1, 4)]
    p = sum(w * (s + f) for w, s, f in zip(mu, rows, factors))
    selected = [w * s / p for w, s in zip(mu, rows)]
    assert sum(selected) + sum(w * f for w, f in zip(mu, factors)) / p == 1
    # Each accepted row has an explicit conditional expected bad-child count.
    means = [Q(2, 7), Q(3, 5), Q(7, 4)]
    incidence = [s * z for s, z in zip(rows, means)]
    assert sum(w * z for w, z in zip(selected, means)) == sum(
        w * z for w, z in zip(mu, incidence)) / p
    costs = [Q(7), Q(11), Q(13)]
    assert sum(w * c / s for w, c, s in zip(selected, costs, rows)) == sum(
        w * c for w, c in zip(mu, costs)) / p
    # An explicit subprobability law of good selected rows and completion costs.
    law = [(Q(1, 5), 3), (Q(1, 10), 40), (Q(1, 4), 6)]
    good_mass = sum(w for w, _ in law)
    immediate_factor_mass = Q(1, 10)
    gamma = good_mass + immediate_factor_mass
    work = sum(w * c for w, c in law)
    cap = (2 * work / gamma).__ceil__()
    actual_success = immediate_factor_mass + sum(w for w, c in law if c <= cap)
    assert actual_success >= gamma - work / cap >= gamma / 2
    print("exact incidence, cost cancellation and capped-restart identities: 4")


def smooth(x, primes):
    for p in primes:
        while x % p == 0:
            x //= p
    return x == 1


def height_checks():
    checks = 0
    for N in (15, 21, 35, 77, 101):
        units = [a for a in range(1, N) if gcd(a, N) == 1]
        shifts = units[:3]
        for primes in [(2,), (2, 3), (2, 3, 5, 7)]:
            # Exact rational upper approximation to Z_B(1/2).
            scale = 10000
            Z = Q(1)
            for p in primes:
                reciprocal_upper = Q(scale, isqrt(p * scale * scale))
                Z /= 1 - reciprocal_upper
            for M in (15, 40, 100, 200):
                pairs = [(x, y) for x in range(1, M + 1) if smooth(x, primes)
                         for y in range(1, M // x + 1) if smooth(y, primes)]
                assert len(pairs) <= (isqrt(M) + 1) * Z ** 2
                support = set()
                reduced = set()
                for x, y in pairs:
                    if gcd(x * y, N) != 1:
                        continue
                    g = gcd(x, y)
                    X, Y = x // g, y // g
                    assert X * Y <= M and smooth(X, primes) and smooth(Y, primes)
                    for a in shifts:
                        for sign in (-1, 1):
                            support.add(a * sign * y * pow(x, -1, N) % N)
                            reduced.add(a * sign * Y * pow(X, -1, N) % N)
                assert support == reduced
                assert len(support) <= min(len(units), 2 * len(shifts) * len(pairs))
                checks += 1
    print("exact finite height/support checks:", checks)


if __name__ == "__main__":
    graph_checks()
    incidence_checks()
    height_checks()
