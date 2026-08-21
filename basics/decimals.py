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


#---- Decimal Checks ----
def is_integer(number):
    """
    Returns True if the number has no fractional part.
    """
    return number == int(number)

def has_decimal(number):
    """
    Returns True if the number contains a fractional part.
    """
    return not is_integer(number)


#---- Trailing Zeros ----
def remove_trailing_zeros(number):
    """
    Removes unnecessary trailing zeros from a decimal.

    Example: remove_trailing_zeros(12.3400) -> 12.34
    """

    if number == int(number):
        return int(number)
    return number


#---- Decimal Digits ----
def decimal_digit(number, position):
    """
    Returns a decimal digit at a given position.
    position=1 -> tenths
    position=2 -> hundredths
    position=3 -> thousandths
    """
    if position <= 0:
        raise ValueError("Position must be positive.")

    number = _absolute(number)
    scaled = number * _power_of_ten(position)
    integer_value = int(scaled)
    return integer_value % 10

def decimal_digits(number, count=None):
    """
    Returns decimal digits as a list.

    Example: decimal_digits(12.345) -> [3, 4, 5]
    """
    number = _absolute(number)
    fraction = number - int(number)
    digits = []

    if count is None:
        count = count_decimal_places(number)

    for _ in range(count):
        fraction *= 10
        digit = int(fraction)
        digits.append(digit)
        fraction -= digit

    return digits


#---- Decimal Construction ----
def from_decimal_digits(integer, digits):
    """
    Constructs a decimal number from an integer and decimal digits.
    Example: from_decimal_digits(12, [3, 4, 5]) -> 12.345
    """
    if len(digits) == 0:
        return integer

    value = integer
    divisor = 10

    for digit in digits:
        if digit < 0 or digit > 9:
            raise ValueError("Each digit must be between 0 and 9.")
        value += digit / divisor
        divisor *= 10
    return value


#---- Decimal Shifting ----
def shift_decimal(number, places):
    """
    Moves the decimal point by a number of places.
    Positive places move it right.
    Negative places move it left.

    Example: shift_decimal(12.34, 2) -> 1234.0
    """
    return number * _power_of_ten(places)

def decimal_to_integer(number, places):
    """
    Converts a decimal portion into an integer representation.

    Example: decimal_to_integer(12.345, 3) -> 12345
    """
    if places < 0:
        raise ValueError("places must be non-negative.")
    return int(number * _power_of_ten(places))


#---- Decimal Comparison ----
def compare_decimals(a, b):
    """
    Compares two decimal values.

    Returns:
        1  if a > b
        0  if a == b
       -1  if a < b
    """
    if a > b:
        return 1

    if a < b:
        return -1
    return 0

def decimals_equal(a, b):
    """
    Returns True if two decimals are equal.
    """
    return a == b
    

#---- Decimal Operations ----
def decimal_sum(*numbers):
    """
    Returns the sum of decimal numbers.
    """
    total = 0

    for number in numbers:
        total += number
    return total

def decimal_product(*numbers):
    """
    Returns the product of decimal numbers.
    """
    result = 1

    for number in numbers:
        result *= number
    return result

def decimal_average(*numbers):
    """
    Returns the arithmetic mean of decimal numbers.
    """
    if len(numbers) == 0:
        raise ValueError("At least one number is required.")

    return decimal_sum(*numbers) / len(numbers)
