from prime_factors import PrimeFactors


def test_prime_factors():
    prime_factors = PrimeFactors()
    assert prime_factors.of(1) == []

def test_prime_factors_of_2():
    prime_factors = PrimeFactors()
    assert prime_factors.of(2) == [2]

def test_prime_factors_of_3():
    prime_factors = PrimeFactors()
    assert prime_factors.of(3) == [3]