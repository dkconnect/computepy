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
