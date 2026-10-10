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
def is_square(n):
    if n < 0:
        return False

    i = 0
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

def is_cube(n):
    if n < 0:
        n = -n

    i = 0
    while i * i * i <= n:
        if i * i * i == n:
            return True
        i += 1
    return False


#---- Powers of Ten ----
def power_of_ten(exponent):
    return 10 ** exponent

def is_power_of_ten(n):
    if n <= 0:
        return False

    while n > 1:
        if n % 10 != 0:
            return False
        n //= 10
    return True


#---- Powers of Two ----
def power_of_two(exponent):
    return 2 ** exponent

def is_power_of_two(n):
    if n <= 0:
        return False
        
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


#---- Powers of Three ----
def power_of_three(exponent):
    return 3 ** exponent

def is_power_of_three(n):
    if n <= 0:
        return False

    while n > 1:
        if n % 3 != 0:
            return False
        n //= 3
    return True


#---- Miscellaneous ----
def exponent(base, value):
    """
    Alias for power().
    """
    return power(base, value)

def square_distance(a, b):
    diff = a - b
    return diff * diff

def cube_distance(a, b):
    diff = a - b
    return diff * diff * diff
