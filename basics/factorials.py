"""
factorials.py

=============
Factorial Functions
=============

Author: Dibyanshu | August 2026
"""

#---- Helpers ----
def _product(start, end, step=1):
    """
    Returns the product of integers from start to end.
    """
    result = 1

    if step > 0:
        current = start
        while current <= end:
            result *= current
            current += step
    else:
        current = start
        while current >= end:
            result *= current
            current += step

    return result


#---- Basic Factorials ----
def factorial(n):
    """
    Returns n!
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    if n == 0 or n == 1:
        return 1

    return _product(2, n)

def double_factorial(n):
    """
    Returns n!!
    """
    if not isinstance(n, int):
        raise TypeError("Double factorial is only defined for integers.")

    if n < -1:
        raise ValueError("Double factorial is undefined.")

    if n == -1 or n == 0:
        return 1

    return _product(n, 1, -2)

def multifactorial(n, step):
    """
    Returns the multifactorial. Example - multifactorial(10, 3) = 10 × 7 × 4 × 1
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(step, int):
        raise TypeError("step must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if step <= 0:
        raise ValueError("step must be positive.")

    return _product(n, 1, -step)


#---- Generalized Factorials ----
def rising_factorial(x, n):
    """
    Returns x(x+1)(x+2)... for n terms.
    """
    if n < 0:
        raise ValueError("n must be non-negative.")
    result = 1

    for i in range(n):
        result *= (x + i)
    return result

def falling_factorial(x, n):
    """
    Returns x(x-1)(x-2)... for n terms.
    """
    if n < 0:
        raise ValueError("n must be non-negative.")
    result = 1

    for i in range(n):
        result *= (x - i)
    return result


#---- Utilities ----
def factorial_ratio(a, b):
    """
    Returns a! / b!
    """
    if a < 0 or b < 0:
        raise ValueError("Arguments must be non-negative.")
    return factorial(a) / factorial(b)

def inverse_factorial(value):
    """
    Returns n if value = n!.
    """
    if value < 1:
        raise ValueError("Value must be positive.")
    current = 1
    n = 1

    while current < value:
        n += 1
        current *= n

    if current != value:
        raise ValueError("Value is not a factorial.")
    return n

def factorial_digits(n):
    """
    Returns the number of digits in n!.
    """
    value = factorial(n)
    digits = 0
    
    while value > 0:
        digits += 1
        value //= 10
    return digits

def trailing_zeros(n):
    """
    Returns the number of trailing zeros in n!.
    """
    if n < 0:
        raise ValueError("n must be non-negative.")

    count = 0
    divisor = 5

    while divisor <= n:
        count += n // divisor
        divisor *= 5
    return count
    

#---- Checks ----
def is_factorial(number):
    """
    Returns True if number is a factorial.
    """
    if number < 1:
        return False
    current = 1
    n = 1

    while current < number:
        n += 1
        current *= n
    return current == number


#---- Tables ----
def factorial_table(n):
    """
    Returns a list of tuples:
    [(0,0!), (1,1!), ...]
    """
    if n < 0:
        raise ValueError("n must be non-negative.")

    table = []
    value = 1
    table.append((0, 1))

    for i in range(1, n + 1):
        value *= i
        table.append((i, value))
