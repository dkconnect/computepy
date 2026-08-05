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


#---- Precision Helpers ----
def round_nearest(number, multiple):
    """
    Rounds to the nearest multiple.
    """
    if multiple == 0:
        raise ZeroDivisionError("Multiple cannot be zero.")

    quotient = number / multiple
    return round(quotient) * multiple


def round_up_to_multiple(number, multiple):
    """
    Rounds upward to the nearest multiple.
    """
    if multiple == 0:
        raise ZeroDivisionError("Multiple cannot be zero.")

    quotient = number / multiple
    return ceil(quotient) * multiple


def round_down_to_multiple(number, multiple):
    """
    Rounds downward to the nearest multiple.
    """
    if multiple == 0:
        raise ZeroDivisionError("Multiple cannot be zero.")

    quotient = number / multiple
    return floor(quotient) * multiple


#---- Significant Figures ----
def round_significant(number, figures):
    """
    Rounds to the specified number of significant figures.
    """
    if number == 0:
        return 0
    negative = False

    if number < 0:
        negative = True
        number = -number

    exponent = 0
    value = number

    while value >= 10:
        value /= 10
        exponent += 1

    while value < 1:
        value *= 10
        exponent -= 1

    factor = 10 ** (figures - exponent - 1)
    result = round(number * factor) / factor

    if negative:
        return -(result)
    return result


#---- Decimal Checks ----
def has_decimal(number):
    """
    Returns True if the number has a fractional part.
    """
    return number != int(number)


def fractional_part(number):
    """
    Returns only the fractional part.
    """
    return number - truncate(number)


def integer_part(number):
    """
    Returns only the integer part.
    """
    return truncate(number)
