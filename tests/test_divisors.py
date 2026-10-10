"""
test_divisors.py

=============
Divisor Function Tests
=============

Author: Dibyanshu | October 2026
"""

import pytest

from number_theory.divisors import (
    divisors,
    proper_divisors,
    divisor_pairs,
    is_divisor,
    common_divisors,
    divisor_count,
    proper_divisor_count,
    has_exactly_n_divisors,
    divisor_sum,
    proper_divisor_sum,
    divisor_power_sum,
    aliquot_sum,
    is_perfect_number,
    is_abundant_number,
    is_deficient_number,
    classify_number,
    are_amicable_numbers,
    are_betrothed_numbers,
    is_square_free,
    is_highly_composite,
    is_practical_number,
    divisor_table,
    divisor_count_table,
    divisor_sum_table,
    perfect_numbers_up_to,
    abundant_numbers_up_to,
    deficient_numbers_up_to,
)


#---- Basic Divisor Tests ----

def test_divisors():
    assert divisors(1) == [1]
    assert divisors(12) == [1, 2, 3, 4, 6, 12]
    assert divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]


def test_proper_divisors():
    assert proper_divisors(1) == []
    assert proper_divisors(12) == [1, 2, 3, 4, 6]


def test_divisor_pairs():
    assert divisor_pairs(12) == [(1, 12), (2, 6), (3, 4)]
    assert divisor_pairs(36) == [
        (1, 36), (2, 18), (3, 12), (4, 9), (6, 6)
    ]


def test_divisibility():
    assert is_divisor(3, 12)
    assert is_divisor(-3, 12)
    assert not is_divisor(5, 12)

    with pytest.raises(ZeroDivisionError):
        is_divisor(0, 12)


def test_common_divisors():
    assert common_divisors(12, 18) == [1, 2, 3, 6]
    assert common_divisors(0, 12) == [1, 2, 3, 4, 6, 12]

    with pytest.raises(ValueError):
        common_divisors(0, 0)


#---- Divisor Count Tests ----

def test_divisor_counts():
    assert divisor_count(1) == 1
    assert divisor_count(12) == 6
    assert divisor_count(36) == 9
    assert proper_divisor_count(12) == 5
    assert has_exactly_n_divisors(12, 6)


#---- Divisor Sum Tests ----

def test_divisor_sums():
    assert divisor_sum(1) == 1
    assert divisor_sum(12) == 28
    assert proper_divisor_sum(12) == 16
    assert divisor_power_sum(6, 2) == 50
    assert aliquot_sum(28) == 28


#---- Classification Tests ----

def test_number_classification():
    assert is_perfect_number(6)
    assert is_perfect_number(28)
    assert not is_perfect_number(12)

    assert is_abundant_number(12)
    assert is_deficient_number(8)

    assert classify_number(28) == "perfect"
    assert classify_number(12) == "abundant"
    assert classify_number(8) == "deficient"


#---- Special Number Tests ----

def test_special_numbers():
    assert are_amicable_numbers(220, 284)
    assert not are_amicable_numbers(6, 6)

    assert are_betrothed_numbers(48, 75)

    assert is_square_free(30)
    assert not is_square_free(12)

    assert is_highly_composite(12)
    assert not is_highly_composite(5)

    assert is_practical_number(12)
    assert not is_practical_number(7)


#---- Table Tests ----

def test_divisor_tables():
    assert divisor_table(4) == {
        1: [1],
        2: [1, 2],
        3: [1, 3],
        4: [1, 2, 4],
    }

    assert divisor_count_table(5) == [0, 1, 2, 2, 3, 2]
    assert divisor_sum_table(5) == [0, 1, 3, 4, 7, 6]


#---- Generation Tests ----

def test_number_generation():
    assert perfect_numbers_up_to(30) == [6, 28]
    assert abundant_numbers_up_to(20) == [12, 18, 20]
    assert deficient_numbers_up_to(10) == [1, 2, 3, 4, 5, 7, 8, 9, 10]


#---- Validation Tests ----

def test_invalid_inputs():
    with pytest.raises(ValueError):
        divisors(0)

    with pytest.raises(ValueError):
        divisors(-12)

    with pytest.raises(TypeError):
        divisors(12.5)

    with pytest.raises(TypeError):
        divisor_count(True)

    with pytest.raises(ValueError):
        divisor_sum(0)

    with pytest.raises(ValueError):
        divisor_table(-1)

    with pytest.raises(ValueError):
        divisor_power_sum(6, -1)