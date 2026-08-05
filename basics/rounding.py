"""
rounding.py

=============
Rounding Functions
=============

Author: Dibyanshu | August 2026
"""

#---- Basic Rounding ----
def floor(number):
    """
    Returns the greatest integer less than or equal to the number.
    """
    integer = int(number)
    if number >= 0 or number == integer:
        return integer
        
    return integer - 1
  

def ceil(number):
    """
    Returns the smallest integer greater than or equal to the number.
    """
    integer = int(number)
    if number == integer:
        return integer

    if number > 0:
        return integer + 1
    return integer


def truncate(number):
    """
    Removes the decimal part.
    """
    return int(number)

def round(number):
    """
    Rounds to the nearest integer.
    Half values are rounded away from zero.
    """
    if number >= 0:
        return floor(number + 0.5)

    return ceil(number - 0.5)


#---- Decimal Place Rounding ----
def round_to(number, digits):
    """
    Rounds a number to the specified decimal places.
    """
    factor = 10 ** digits
    return round(number * factor) / factor


def round_up(number, digits=0):
    """
    Always rounds upward.
    """
    factor = 10 ** digits
    return ceil(number * factor) / factor


def round_down(number, digits=0):
    """
    Always rounds downward.
    """
    factor = 10 ** digits
    return floor(number * factor) / factor
