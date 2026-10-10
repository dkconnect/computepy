"""
ratios.py

Ratio & Proportion Functions

Author: Dibyanshu | August 2026
"""

#---- Internal Helpers ----
def _gcd(a, b):
    """
    Returns the greatest common divisor using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b

    return abs(a)


def _validate_ratio(a, b):
    """
    Validates a ratio consisting of two integer terms.
    """
    if type(a) is not int or type(b) is not int:
        raise TypeError("Ratio terms must be integers.")

    if b == 0:
        raise ZeroDivisionError("Second ratio term cannot be zero.")


def _simplify(a, b):
    """
    Reduces a ratio to its simplest integer form.
    """
    _validate_ratio(a, b)

    if b < 0:
        a = -a
        b = -b

    divisor = _gcd(a, b)
    return a // divisor, b // divisor


#---- Basic Ratios ----
def ratio(a, b):
    """
    Returns the numerical value of a ratio.
    """
    if b == 0:
        raise ZeroDivisionError("Second ratio term cannot be zero.")

    return a / b


def simplify_ratio(a, b):
    """
    Simplifies a ratio to its lowest terms.
    """
    return _simplify(a, b)


def inverse_ratio(a, b):
    """
    Returns the inverse of a ratio.
    """

    _validate_ratio(a, b)

    if a == 0:
        raise ZeroDivisionError("Cannot invert a zero ratio.")

    return _simplify(b, a)


def equivalent_ratio(a, b, multiplier):
    """
    Generates an equivalent ratio.
    """

    _validate_ratio(a, b)
    if multiplier == 0:
        raise ValueError("Multiplier cannot be zero.")

    return a * multiplier, b * multiplier


def ratio_value(a, b):
    """
    Returns the decimal value of a ratio.
    """
    return ratio(a, b)


#---- Ratio Comparison ----
def compare_ratios(a, b, c, d):
    """
    Compares a:b and c:d.
    """
    _validate_ratio(a, b)
    _validate_ratio(c, d)

    a, b = _simplify(a, b)
    c, d = _simplify(c, d)

    left = a * d
    right = c * b

    if left > right:
        return 1

    if left < right:
        return -1

    return 0


def ratios_equal(a, b, c, d):
    """
    Checks whether two ratios are equal.
    """
    return compare_ratios(a, b, c, d) == 0


def is_equivalent_ratio(a, b, c, d):
    """
    Checks whether two ratios are equivalent.
    """
    return ratios_equal(a, b, c, d)


#---- Proportions ----
def proportion(a, b, c):
    """
    Solves a:b = c:x.
    """

    if a == 0:
        raise ZeroDivisionError("First ratio term cannot be zero.")

    return (b * c) / a


def is_proportion(a, b, c, d):
    """
    Checks whether a:b = c:d.
    """
    if b == 0 or d == 0:
        raise ZeroDivisionError("Ratio denominator cannot be zero.")

    return a * d == b * c


def fourth_proportional(a, b, c):
    """
    Finds x such that a:b = c:x.
    """
    return proportion(a, b, c)


def third_proportional(a, b):
    """
    Finds x such that a:b = b:x.
    x = b² / a
    """

    if a == 0:
        raise ZeroDivisionError("First term cannot be zero.")

    return (b * b) / a


def mean_proportional(a, b):
    """
    Finds x such that a:x = x:b.
    x = sqrt(a*b)
    """

    if a < 0 or b < 0:
        raise ValueError("Arguments must be non-negative.")

    number = a * b

    if number == 0:
        return 0

    guess = number if number >= 1 else 1.0

    for _ in range(1000):
        new_guess = (guess + number / guess) / 2

        if abs(new_guess - guess) <= 1e-12 * max(1, abs(new_guess)):
            return new_guess

        guess = new_guess

    return guess


#---- Direct Proportion ----
def direct_proportion(x1, y1, x2):
    """
    Calculates y2 when y is directly proportional to x.

    x1 / y1 = x2 / y2
    """

    if x1 == 0:
        raise ZeroDivisionError("Initial x value cannot be zero.")

    return (y1 * x2) / x1


def direct_proportion_constant(x, y):
    """
    Returns the constant k in y = k*x.
    """
    if x == 0:
        raise ZeroDivisionError("x cannot be zero.")

    return y / x


#---- Inverse Proportion ----
def inverse_proportion(x1, y1, x2):
    """
    Calculates y2 when y is inversely proportional to x.
    """

    if x2 == 0:
        raise ZeroDivisionError("New x value cannot be zero.")

    return (x1 * y1) / x2


def inverse_proportion_constant(x, y):
    """
    Returns the constant k in x*y = k.
    """
    return x * y


#---- Compound Ratios ----
def compound_ratio(*ratios):
    """
    Multiplies multiple ratios.
    """

    numerator = 1
    denominator = 1

    for a, b in ratios:
        _validate_ratio(a, b)

        numerator *= a
        denominator *= b

    return _simplify(numerator, denominator)


def duplicate_ratio(a, b):
    """
    Returns the duplicate ratio a²:b².
    """
    return _simplify(a * a, b * b)


def triplicate_ratio(a, b):
    """
    Returns the triplicate ratio a³:b³.
    """
    return _simplify(a * a * a, b * b * b)


def subduplicate_ratio(a, b):
    """
    Returns the square-root ratio.
    """

    if a < 0 or b <= 0:
        raise ValueError("Ratio must be non-negative with positive denominator.")
    return mean_proportional(a, 1), mean_proportional(b, 1)


#---- Ratio Distribution ----
def divide_in_ratio(total, a, b):
    """
    Divides a total into two parts in ratio a:b.
    """

    if a < 0 or b < 0:
        raise ValueError("Ratio parts must be non-negative.")

    if a + b == 0:
        raise ZeroDivisionError("Sum of ratio terms cannot be zero.")

    first = total * a / (a + b)
    second = total - first

    return first, second


def divide_in_multiple_ratio(total, *parts):
    """
    Divides a total according to multiple ratio terms.
    """

    if len(parts) == 0:
        raise ValueError("At least one ratio term is required.")

    total_parts = 0

    for part in parts:
        if part < 0:
            raise ValueError("Ratio terms must be non-negative.")

        total_parts += part

    if total_parts == 0:
        raise ZeroDivisionError("Sum of ratio terms cannot be zero.")

    result = []
    allocated = 0

    for part in parts[:-1]:
        value = total * part / total_parts
        result.append(value)
        allocated += value

    result.append(total - allocated)
    return tuple(result)


#---- Ratio Transformations ----
def componendo(a, b):
    """
    Returns (a+b):b.
    """
    return _simplify(a + b, b)


def dividendo(a, b):
    """
    Returns (a-b):b.
    """
    return _simplify(a - b, b)


def componendo_dividendo(a, b):
    """
    Returns (a+b):(a-b).
    """
    if a == b:
        raise ZeroDivisionError("a-b cannot be zero.")

    return _simplify(a + b, a - b)


def alternendo(a, b, c, d):
    """
    Rearranges a:b = c:d into a:c = b:d.

    Returns the two resulting ratios.
    """
    if not is_proportion(a, b, c, d):
        raise ValueError("Original ratios are not proportional.")

    if c == 0 or d == 0:
        raise ZeroDivisionError("Alternated ratio denominator cannot be zero.")

    return _simplify(a, c), _simplify(b, d)


def invertendo(a, b):
    """
    Returns b:a.
    """
    return inverse_ratio(a, b)


#---- Ratio Utilities ----
def ratio_to_percentage(a, b):
    """
    Converts a ratio into a percentage.
    """
    return ratio(a, b) * 100


def percentage_to_ratio(percent):
    """
    Converts an integer percentage to a simplified ratio.
    """
    if type(percent) is not int:
        raise TypeError("Percentage must be an integer.")

    return _simplify(percent, 100)


def ratio_difference(a, b, c, d):
    """
    Returns the difference between two ratio values.
    """
    if b == 0 or d == 0:
        raise ZeroDivisionError("Ratio denominator cannot be zero.")

    return (a / b) - (c / d)


def ratio_sum(a, b, c, d):
    """
    Returns the sum of two ratio values.
    """
    if b == 0 or d == 0:
        raise ZeroDivisionError("Ratio denominator cannot be zero.")

    return (a / b) + (c / d)