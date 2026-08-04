"""
powers.py

=============
Power Functions
=============

Author: Dibyanshu | August 2026
"""


#---- Basic Powers ----
def power(base, exponent):
    return base ** exponent

def square(x):
    return x * x

def cube(x):
    return x * x * x

def fourth_power(x):
    return x ** 4

def fifth_power(x):
    return x ** 5

def nth_power(base, n):
    return base ** n


#---- Common Exponents ----
def reciprocal_square(x):
    if x == 0:
        raise ZeroDivisionError("Zero cannot be squared and reciprocated.")
    return 1 / (x * x)

def reciprocal_cube(x):
    if x == 0:
        raise ZeroDivisionError("Zero cannot be cubed and reciprocated.")
    return 1 / (x * x * x)

def square_difference(a, b):
    return square(a) - square(b)

def square_sum(a, b):
    return square(a) + square(b)


#---- Power Properties ----
def power_product(base, exponent1, exponent2):
    """
    a^m × a^n = a^(m+n)
    """
    return base ** (exponent1 + exponent2)

def power_quotient(base, exponent1, exponent2):
    """
    a^m ÷ a^n = a^(m-n)
    """
    return base ** (exponent1 - exponent2)

def power_of_power(base, exponent1, exponent2):
    """
    (a^m)^n = a^(mn)
    """
    return base ** (exponent1 * exponent2)


#---- Number Checks ----
