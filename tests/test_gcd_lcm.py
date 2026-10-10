"""
test_gcd_lcm.py

=============
GCD and LCM Tests
=============

Author: Dibyanshu | October 2026
"""

import pytest

from number_theory.gcd_lcm import (
    gcd,
    gcd_many,
    lcm,
    lcm_many,
    extended_gcd,
    are_coprime,
    pairwise_coprime,
    bezout_coefficients,
    euclidean_steps,
)


#---- GCD Tests ----
def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(-48, 18) == 6
    assert gcd(0, 15) == 15
    assert gcd(0, 0) == 0


def test_gcd_many():
    assert gcd_many(48, 72, 120) == 24
    assert gcd_many(7) == 7
    assert gcd_many(-8, 12) == 4

    with pytest.raises(ValueError):
        gcd_many()


#---- LCM Tests ----
def test_lcm():
    assert lcm(12, 18) == 36
    assert lcm(-12, 18) == 36
    assert lcm(0, 18) == 0
    assert lcm(0, 0) == 0


def test_lcm_many():
    assert lcm_many(4, 6, 10) == 60
    assert lcm_many(7) == 7
    assert lcm_many(4, 0, 6) == 0

    with pytest.raises(ValueError):
        lcm_many()


#---- Extended GCD Tests ----
def test_extended_gcd():
    for a, b in [
        (240, 46),
        (-240, 46),
        (240, -46),
        (-240, -46),
        (0, 0),
        (0, 7),
    ]:
        g, x, y = extended_gcd(a, b)

        assert g == gcd(a, b)
        assert a * x + b * y == g


#---- Coprimality Tests ----
def test_coprime():
    assert are_coprime(14, 15)
    assert not are_coprime(12, 18)

    assert pairwise_coprime(5, 7, 9)
    assert not pairwise_coprime(6, 10, 15)


#---- Bézout Tests ----
def test_bezout():
    x, y = bezout_coefficients(30, 18)
    assert 30 * x + 18 * y == 6


#---- Euclidean Steps Tests ----
def test_euclidean_steps():
    assert euclidean_steps(48, 18) == [
        (48, 18, 2, 12),
        (18, 12, 1, 6),
        (12, 6, 2, 0),
    ]


#---- Validation Tests ----
def test_invalid_inputs():
    with pytest.raises(TypeError):
        gcd(4.5, 2)

    with pytest.raises(TypeError):
        lcm(True, 5)

    with pytest.raises(TypeError):
        extended_gcd("12", 6)