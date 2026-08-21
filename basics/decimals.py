"""
decimals.py

=============
Decimal Functions
=============

Author: Dibyanshu | August 2026
"""

#---- Internal Helpers ----
def _absolute(number):
    if number < 0:
        return -number
    return number

def _power_of_ten(exponent):
    result = 1

    if exponent >= 0:
        for _ in range(exponent):
            result *= 10
    else:
        for _ in range(-exponent):
            result /= 10
    return result


#---- Decimal Places ----
def count_decimal_places(number):
    """
    Returns the number of decimal places in a number.
    Example: count_decimal_places(12.345) -> 3
    """
    number = _absolute(number)

    if number == int(number):
        return 0
    count = 0
    value = number

    while value != int(value) and count < 15:
        value *= 10
        count += 1
    return count

def decimal_part(number):
    """
    Returns only the decimal part of a number.
    Example: decimal_part(12.345) -> 0.345
    """
    integer = int(number)
    return number - integer

def integer_part(number):
    """
    Returns only the integer part of a number.
    """
    return int(number)
