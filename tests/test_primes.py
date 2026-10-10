"""
test_primes.py

=============
Prime Number Tests
=============

Author: Dibyanshu | October 2026
"""

import pytest

from number_theory.primes import (
    is_prime,
    is_composite,
    primes_up_to,
    primes_between,
    first_n_primes,
    nth_prime,
    next_prime,
    previous_prime,
    prime_factors,
    prime_factorization,
    distinct_prime_factors,
    prime_factor_count,
    prime_count,
    prime_sum,
    are_twin_primes,
    is_mersenne_prime,
    is_coprime,
)


def test_primality():
    assert is_prime(2)
    assert is_prime(97)
    assert not is_prime(1)
    assert not is_prime(-7)
    assert not is_prime(100)
    assert is_composite(12)
    assert not is_composite(1)


def test_invalid_input():
    with pytest.raises(TypeError):
        is_prime(3.5)

    with pytest.raises(TypeError):
        is_prime(True)


def test_prime_generation():
    assert primes_up_to(10) == [2, 3, 5, 7]
    assert primes_between(10, 20) == [11, 13, 17, 19]
    assert first_n_primes(5) == [2, 3, 5, 7, 11]
    assert first_n_primes(0) == []
    assert nth_prime(6) == 13
    assert next_prime(11) == 13
    assert previous_prime(11) == 7

def test_factorization():
    assert prime_factors(60) == [2, 2, 3, 5]
    assert prime_factors(-12) == [2, 2, 3]
    assert prime_factors(1) == []
    assert prime_factorization(360) == {2: 3, 3: 2, 5: 1}
    assert distinct_prime_factors(60) == [2, 3, 5]
    assert prime_factor_count(60) == 4

    with pytest.raises(ValueError):
        prime_factors(0)


def test_prime_utilities():
    assert prime_count(10) == 4
    assert prime_sum(10) == 17
    assert are_twin_primes(11, 13)
    assert not are_twin_primes(7, 13)
    assert is_mersenne_prime(3)
    assert not is_mersenne_prime(11)
    assert is_coprime(14, 25)
    assert not is_coprime(12, 18)