"""
constants.py

Mathematical Constants

Author: Dibyanshu | October 2026
"""


#---- Internal Helpers ----
def _validate_precision(precision):
    """
    Validates the requested number of decimal places.
    """
    if type(precision) is not int:
        raise TypeError("Precision must be an integer.")

    if precision < 0:
        raise ValueError("Precision cannot be negative.")

    if precision > 15:
        raise ValueError(
            "Precision cannot exceed 15 decimal places when using Python floats."
        )


def _absolute(number):
    """
    Returns the absolute value of a number.
    """
    if number < 0:
        return -number

    return number


def _sqrt(number):
    """
    Computes the square root using Newton's method.
    """
    if number < 0:
        raise ValueError("Square root of a negative number is undefined.")

    if number == 0:
        return 0.0

    guess = number if number >= 1 else 1.0

    for _ in range(1000):
        new_guess = (guess + number / guess) / 2

        if new_guess == guess:
            break
        guess = new_guess

    return guess


def _arctan_inverse(value, precision=15):
    """
    Computes arctan(1/value) using its Taylor series.
    """
    if value <= 1:
        raise ValueError("Value must be greater than 1.")

    _validate_precision(precision)

    x = 1.0 / value
    x_squared = x * x

    term = x
    result = x

    tolerance = 10.0 ** -(precision + 2)

    for n in range(1, 10000):
        term *= -x_squared

        addition = term / (2 * n + 1)
        result += addition

        if _absolute(addition) < tolerance:
            break

    return result


def _round_constant(value, precision):
    """
    Rounds a constant to the requested decimal places.
    """
    _validate_precision(precision)
    return round(value, precision)


#---- PI Constants ----

def calculate_pi(precision=15):
    """
    Calculates pi using Machin's formula
    """

    _validate_precision(precision)

    value = (
        16 * _arctan_inverse(5, precision)
        - 4 * _arctan_inverse(239, precision)
    )

    return _round_constant(value, precision)

PI = calculate_pi()


#---- Euler's Number ----
def calculate_e(precision=15):
    """
    Calculates Euler's number using
    """
    _validate_precision(precision)

    result = 1.0
    term = 1.0

    tolerance = 10.0 ** -(precision + 2)

    for n in range(1, 1000):
        term /= n
        result += term

        if term < tolerance:
            break

    return _round_constant(result, precision)

E = calculate_e()


#---- Golden Ratio ----
def calculate_golden_ratio(precision=15):
    """
    Calculates the golden ratio
    """
    _validate_precision(precision)
    value = (1 + _sqrt(5)) / 2

    return _round_constant(value, precision)

PHI = calculate_golden_ratio()


#---- Square Root Constants ----
SQRT_2 = _sqrt(2)
SQRT_3 = _sqrt(3)
SQRT_5 = _sqrt(5)
SQRT_1_2 = 1 / SQRT_2


#---- Pi Derived Constants ---
TAU = 2 * PI
HALF_PI = PI / 2
QUARTER_PI = PI / 4
TWO_PI = 2 * PI
THREE_PI = 3 * PI
FOUR_PI = 4 * PI
PI_SQUARED = PI * PI
INV_PI = 1 / PI
INV_TWO_PI = 1 / (2 * PI)
DEG_TO_RAD = PI / 180
RAD_TO_DEG = 180 / PI


#---- Euler Derived Constants ----
E_SQUARED = E * E
INV_E = 1 / E


#---- Golden Ratio Derived Constants ----
INV_PHI = 1 / PHI
PHI_SQUARED = PHI * PHI


#---- Logarithmic Constants ----
def _ln_atanh(value):
    """
    Computes the natural logarithm using:

        ln(x) = 2 * (
            z + z^3/3 + z^5/5 + ...
        )

    where:
        z = (x - 1)/(x + 1)

    Intended for values near 1.
    """

    if value <= 0:
        raise ValueError("Logarithm requires a positive number.")

    z = (value - 1) / (value + 1)
    z_squared = z * z

    term = z
    result = 0.0

    for n in range(1, 10000, 2):
        addition = term / n
        result += addition

        if _absolute(addition) < 1e-18:
            break

        term *= z_squared
    return 2 * result


def calculate_ln2(precision=15):
    """
    Calculates the natural logarithm of 2.
    """
    _validate_precision(precision)
    return _round_constant(_ln_atanh(2), precision)


def calculate_ln10(precision=15):
    """
    Calculates the natural logarithm of 10.
    """

    _validate_precision(precision)
    value = (
        3 * _ln_atanh(2)
        + _ln_atanh(1.25)
    )

    return _round_constant(value, precision)


LN_2 = calculate_ln2()
LN_10 = calculate_ln10()
LOG10_E = 1 / LN_10
LOG2_E = 1 / LN_2


#---- Euler-Mascheroni Constant ----
def calculate_euler_gamma(terms=100000):
    """
    Approximates the Euler-Mascheroni constant.

    Uses the harmonic-number asymptotic expansion:

        gamma ≈ H_n - ln(n)
                - 1/(2n)
                + 1/(12n²)
                - 1/(120n⁴)

    A fixed internal logarithm calculation is used.
    """

    if type(terms) is not int:
        raise TypeError("Terms must be an integer.")

    if terms <= 0:
        raise ValueError("Terms must be positive.")

    harmonic = 0.0

    for n in range(1, terms + 1):
        harmonic += 1 / n

    reduced = float(terms)
    exponent = 0

    while reduced >= 2:
        reduced /= 2
        exponent += 1

    while reduced < 1:
        reduced *= 2
        exponent -= 1

    logarithm = (
        exponent * LN_2
        + _ln_atanh(reduced)
    )

    n = float(terms)

    correction = (
        -1 / (2 * n)
        + 1 / (12 * n * n)
        - 1 / (120 * n * n * n * n)
    )

    return harmonic - logarithm + correction

EULER_GAMMA = calculate_euler_gamma(10000)


#---- Integer Constants ----
ZERO = 0
ONE = 1
TWO = 2
TEN = 10
HUNDRED = 100
THOUSAND = 1000
MILLION = 1000000
BILLION = 1000000000
TRILLION = 1000000000000


#---- Number System Constants ----
BINARY_BASE = 2
OCTAL_BASE = 8
DECIMAL_BASE = 10
HEXADECIMAL_BASE = 16


#---- Mathematical Limits ----
INFINITY = float("inf")
NEGATIVE_INFINITY = float("-inf")
NAN = float("nan")
FLOAT_EPSILON = 2.220446049250313e-16
FLOAT_MAX = 1.7976931348623157e308
FLOAT_MIN_NORMAL = 2.2250738585072014e-308


#---- Constant Utilities ----
def get_constant(name):
    """
    Returns a mathematical constant by name.
    """

    if not isinstance(name, str):
        raise TypeError("Constant name must be a string.")

    constants = {
        "PI": PI,
        "E": E,
        "PHI": PHI,
        "GOLDEN_RATIO": PHI,
        "TAU": TAU,
        "SQRT_2": SQRT_2,
        "SQRT_3": SQRT_3,
        "SQRT_5": SQRT_5,
        "LN_2": LN_2,
        "LN_10": LN_10,
        "EULER_GAMMA": EULER_GAMMA,
        "INFINITY": INFINITY,
        "NEGATIVE_INFINITY": NEGATIVE_INFINITY,
        "NAN": NAN,
    }

    key = name.upper()

    if key not in constants:
        raise ValueError("Unknown mathematical constant.")
    return constants[key]


def list_constants():
    """
    Returns the names of available mathematical constants.
    """
    return (
        "PI",
        "E",
        "PHI",
        "GOLDEN_RATIO",
        "TAU",
        "SQRT_2",
        "SQRT_3",
        "SQRT_5",
        "LN_2",
        "LN_10",
        "EULER_GAMMA",
        "INFINITY",
        "NEGATIVE_INFINITY",
        "NAN",
    )


def is_infinite(number):
    """
    Returns True for positive or negative infinity.
    """
    return number == INFINITY or number == NEGATIVE_INFINITY


def is_nan(number):
    """
    Returns True if the number is NaN.
    """
    return number != number


def is_finite(number):
    """
    Returns True for finite real numbers.
    """
    return not is_infinite(number) and not is_nan(number)
