"""Exact checks for ramification-tolerant Gram factors and an N1101 bridge.

Run: python verification/verify_ramification_and_relation.py
Known primes are used only to verify the local counting theorem.
"""

from math import gcd, lcm
import json


def qmul(x, y, b, modulus):
    return ((x[0] * y[0] + b * x[1] * y[1]) % modulus,
            (x[0] * y[1] + x[1] * y[0]) % modulus)


def qpow(x, exponent, b, modulus):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = qmul(result, x, b, modulus)
        x = qmul(x, x, b, modulus)
        exponent //= 2
    return result


def relation_factor(n, b, exponent, a):
    denominator_factor = gcd(a * a - b, n)
    if 1 < denominator_factor < n:
        return denominator_factor
    if denominator_factor == n:
        return None
    z = qpow((-a % n, 1), exponent, b, n)
    g = gcd(n, gcd((z[0] - 1) % n, z[1]))
    return g if 1 < g < n else None


def relation_chain_factor(n, b, exponent, a):
    denominator_factor = gcd(a * a - b, n)
    if 1 < denominator_factor < n:
        return denominator_factor
    if denominator_factor == n:
        return None
    t, odd = 0, exponent
    while odd % 2 == 0:
        t, odd = t+1, odd//2
    z = qpow((-a % n, 1), odd, b, n)
    for _ in range(t+1):
        for g in (gcd(n, z[1]), gcd(n, gcd((z[0]-1) % n, z[1]))):
            if 1 < g < n:
                return g
        z = qmul(z, z, b, n)
    return None


def checks():
    counters = {"ramified_gram_entries": 0, "inert_zero_counts": 0,
                "global_success_counts": 0, "verified_factors": 0,
                "chain_success_bounds": 0, "chain_witnesses": 0,
                "chain_verified_factors": 0}
    # F_2^2 at odd primes, F_2^3 at 2; u=1 denotes the unramified class.
    # Each pair {2c, 2c+1} is one coset of {0,u}.
    for local_group_size in (4, 8):
        for e in range(1, 13):
            for x in range(local_group_size):
                for y in range(local_group_size):
                    difference = x ^ y
                    local_euler = (e + 1 if difference == 0 else
                                   (0 if e % 2 else 1) if difference == 1 else 1)
                    decomposition = 0
                    for c in range(local_group_size // 2):
                        v0x, v0y = int(x == 2*c), int(y == 2*c)
                        v1x, v1y = int(x == 2*c+1), int(y == 2*c+1)
                        if e % 2:
                            decomposition += ((e-1)//2 * (v0x+v1x)*(v0y+v1y)
                                              + (e+1)//2 * (v0x-v1x)*(v0y-v1y))
                        else:
                            decomposition += e * (v0x*v0y + v1x*v1y)
                    assert local_euler - 1 == decomposition
                    counters["ramified_gram_entries"] += 1

    primes = (3, 5, 7, 11, 13, 17, 19, 23)
    for p in primes:
        for q in primes:
            if p == q:
                continue
            nonresidue = next(b for b in range(2, q) if pow(b, (q-1)//2, q) == q-1)
            # b=1 mod p and b=nonresidue mod q. Known factorization: test only.
            b = (1 + p * (((nonresidue - 1) * pow(p, -1, q)) % q)) % (p*q)
            n = p*q
            base = lcm(p-1, q-1)
            exponents = sorted({base, 2*base, 3*base, lcm(p*p-1, q*q-1)})
            for exponent in exponents:
                divisor = gcd(exponent//(q-1), q+1)
                zeros = sum(qpow((-a % q, 1), exponent, b, q) == (1, 0)
                            for a in range(q))
                assert zeros == divisor - 1
                counters["inert_zero_counts"] += 1
                successes = 0
                for a in range(n):
                    factor = relation_factor(n, b, exponent, a)
                    if factor is not None:
                        assert n % factor == 0 and 1 < factor < n
                        successes += 1
                        counters["verified_factors"] += 1
                assert successes == n - (p-2)*(divisor-1)
                counters["global_success_counts"] += 1
                chain_successes = 0
                for a in range(n):
                    factor = relation_chain_factor(n, b, exponent, a)
                    if factor is not None:
                        assert n % factor == 0 and 1 < factor < n
                        chain_successes += 1
                        counters["chain_verified_factors"] += 1
                    if pow((a*a-b) % p, (p-1)//2, p) == p-1:
                        assert factor is not None
                        counters["chain_witnesses"] += 1
                assert chain_successes >= (p+3)*q//2
                counters["chain_success_bounds"] += 1

    # Inert at q=5, split at p=7: a fully saturated exponent loses the relation.
    saturated = {"N": 35, "b": 2, "M": 48,
                 "successful_a": [a for a in range(35) if relation_factor(35, 2, 48, a)]}
    assert saturated["successful_a"] == [3, 4, 10, 11, 17, 18, 24, 25, 31, 32]
    saturated["chain_successful_a"] = [a for a in range(35)
                                        if relation_chain_factor(35, 2, 48, a)]
    return {"checks": counters, "saturated_example": saturated,
            "scope": "Finite exact verification of identities and counts; no analytic runtime verification."}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
