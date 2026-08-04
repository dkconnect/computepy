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


    return sqrt(a) + sqrt(b)
