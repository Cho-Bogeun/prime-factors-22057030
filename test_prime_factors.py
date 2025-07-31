from prime_factors import PrimeFactors


def test_prime_factors():
    prime_factors = PrimeFactors()
    assert prime_factors.of(1) == []