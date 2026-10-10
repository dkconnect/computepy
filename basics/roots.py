"""
roots.py

=============
Root Functions
=============

-- I am trying to implement roots using the Newton-Raphson (Babylonian) method, with no math.sqrt() or ** --

Author: Dibyanshu | August 2026
"""

#---- Square Root ----
def sqrt(number, tolerance=1e-10, max_iterations=1000):
    """
    Returns the square root using the Newton-Raphson method.
    """
  
    # -- The Newton-Raphson method is a fast way to find the roots (where f(x) = 0) of a function. --
    # -- It uses an initial guess, a derivative, and an iterative formula to get closer to the true answer. --
  
    if number < 0:
        raise ValueError("Cannot find the square root of a negative number.")
    if number == 0:
        return 0
    guess = number

    for _ in range(max_iterations):
        new_guess = (guess + number / guess) / 2

        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
      
    return guess


#---- Cube Root ----
def cbrt(number, tolerance=1e-10, max_iterations=1000):
    """
    Returns the cube root using Newton-Raphson.
    """

    if number == 0:
        return 0
    negative = False

    if number < 0:
        negative = True
        number = -(number)
    guess = number

    for _ in range(max_iterations):
        new_guess = (2 * guess + number / (guess * guess)) / 3

        if abs(new_guess - guess) < tolerance:
            if negative:
                return -(new_guess)
            return new_guess
        guess = new_guess

    if negative:
        return -(guess)
    return guess
    

#---- Nth Root ----
def nth_root(number, n, tolerance=1e-10, max_iterations=1000):
    """
    Returns the nth root using Newton-Raphson.
    """

    if n <= 0:
        raise ValueError("Root must be greater than zero.")
    if number == 0:
        return 0
    if number < 0 and n % 2 == 0:
        raise ValueError("Even root of a negative number is undefined.")
    negative = False

    if number < 0:
        negative = True
        number = -(number)
    guess = number

    for _ in range(max_iterations):
        numerator = ((n - 1) * guess) + (number / (guess ** (n - 1)))
        new_guess = numerator / n

        if abs(new_guess - guess) < tolerance:
            if negative:
                return -(new_guess)
            return new_guess
        guess = new_guess

    if negative:
        return -(guess)
    return guess


#---- Perfect Root Checks ----
def _integer_root_floor(number, power):
    """Exact integer root by binary search, without floating-point arithmetic."""
    if type(number) is not int or type(power) is not int:
        raise TypeError("Number and power must be integers.")
    if power <= 0:
        raise ValueError("Power must be positive.")
    if number < 0:
        raise ValueError("Number must be non-negative.")
    low, high = 0, number + 1
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** power <= number:
            low = mid
        else:
            high = mid
    return low

def is_perfect_square(number):
    if type(number) is not int:
        raise TypeError("Number must be an integer.")
    if number < 0:
        return False
    root = _integer_root_floor(number, 2)
    return root * root == number

def is_perfect_cube(number):
    if type(number) is not int:
        raise TypeError("Number must be an integer.")
    root = _integer_root_floor(abs(number), 3)
    return root * root * root == abs(number)

def is_perfect_power(number, power):
    if type(number) is not int or type(power) is not int:
        raise TypeError("Number and power must be integers.")
    if power <= 0:
        raise ValueError("Power must be positive.")
    if number < 0 and power % 2 == 0:
        return False
    root = _integer_root_floor(abs(number), power)
    return root ** power == abs(number)


#---- Root Utilities ----
def reciprocal_root(number):
    """
    Returns 1 / sqrt(number).
    """
    
    if number <= 0:
        raise ValueError("Number must be positive.")
    return 1 / sqrt(number)

def root_difference(a, b):
    """
    Difference between square roots.
    """
    return sqrt(a) - sqrt(b)

def root_sum(a, b):
    """
    Sum of square roots.
    """
    return sqrt(a) + sqrt(b)
