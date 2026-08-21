"""
fractions.py

=============
Fraction Functions
=============

Author: Dibyanshu | August 2026
"""

#---- Internal Helpers ----
def _gcd(a, b):
    """
    Returns the greatest common divisor using Euclid's algorithm.
    """
    if a < 0:
        a = -a

    if b < 0:
        b = -b

    while b != 0:
        a, b = b, a % b
    return a

def _normalize(numerator, denominator):
    """
    Normalizes the sign of a fraction.
    """
    if denominator == 0:
        raise ZeroDivisionError("Fraction denominator cannot be zero.")

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator
    return numerator, denominator


def _simplify(numerator, denominator):
    """
    Reduces a fraction to lowest terms.
    """
    numerator, denominator = _normalize(numerator, denominator)
    divisor = _gcd(numerator, denominator)

    if divisor == 0:
        return 0, 1
    return numerator // divisor, denominator // divisor


#---- Fraction Creation ----
def fraction(numerator, denominator=1):
    """
    Creates a normalized fraction.

    Example:
        fraction(3, 4) -> (3, 4)
        fraction(6, -8) -> (-6, 8)
    """
    return _normalize(numerator, denominator)

def simplify_fraction(numerator, denominator):
    """
    Reduces a fraction to its simplest form.

    Example:
        simplify_fraction(6, 8) -> (3, 4)
    """
    return _simplify(numerator, denominator)


#---- Fraction Arithmetic ----
def add_fraction(a, b, c, d):
    """
    Returns: a/b + c/d
    """
    numerator = (a * d) + (c * b)
    denominator = b * d
    return _simplify(numerator, denominator)

def subtract_fraction(a, b, c, d):
    """
    Returns: a/b - c/d
    """
    numerator = (a * d) - (c * b)
    denominator = b * d
    return _simplify(numerator, denominator)

def multiply_fraction(a, b, c, d):
    """
    Returns: a/b × c/d
    """
    numerator = a * c
    denominator = b * d
    return _simplify(numerator, denominator)

def divide_fraction(a, b, c, d):
    """
    Returns: a/b ÷ c/d
    """
    if c == 0:
        raise ZeroDivisionError("Cannot divide by a zero fraction.")

    numerator = a * d
    denominator = b * c
    return _simplify(numerator, denominator)
