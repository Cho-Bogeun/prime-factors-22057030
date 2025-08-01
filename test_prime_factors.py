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

def test_prime_factors_of_4():
    prime_factors = PrimeFactors()
    assert prime_factors.of(4) == [2,2]

def test_prime_factors_of_6():
    prime_factors = PrimeFactors()
    assert prime_factors.of(6) == [2,3]

def test_prime_factors_of_9():
    prime_factors = PrimeFactors()
    assert prime_factors.of(9) == [3,3]

def test_prime_factors_of_12():
    prime_factors = PrimeFactors()
    assert prime_factors.of(12) == [2, 2, 3]