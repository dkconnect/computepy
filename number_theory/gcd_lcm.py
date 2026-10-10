"""
gcd_lcm.py

GCD and LCM

Author: Dibyanshu | October 2026
"""


#---- Validation ----
def _require_int(value, name="value"):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


#---- Greatest Common Divisor ----
def gcd(a, b):
    """Return the greatest common divisor of two integers."""
    _require_int(a, "a")
    _require_int(b, "b")

    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b
    return a


def gcd_many(*numbers):
    """Return the GCD of one or more integers."""
    if not numbers:
        raise ValueError("At least one integer is required")

    result = 0
    for number in numbers:
        _require_int(number)
        result = gcd(result, number)

    return result


#---- Least Common Multiple ----
def lcm(a, b):
    """Return the least common multiple of two integers."""
    _require_int(a, "a")
    _require_int(b, "b")

    if a == 0 or b == 0:
        return 0
    return abs((a // gcd(a, b)) * b)


def lcm_many(*numbers):
    """Return the LCM of one or more integers."""
    if not numbers:
        raise ValueError("At least one integer is required")

    result = 1
    for number in numbers:
        _require_int(number)
        result = lcm(result, number)

    return result


#---- Extended Euclidean Algorithm ----
def extended_gcd(a, b):
    """
    Return (g, x, y) satisfying: a*x + b*y == g
    where g is the nonnegative GCD of a and b.
    """
    _require_int(a, "a")
    _require_int(b, "b")

    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    x = old_s if a >= 0 else -old_s
    y = old_t if b >= 0 else -old_t

    return old_r, x, y


#---- Coprimality ----
def are_coprime(a, b):
    """Return whether two integers have GCD equal to 1."""
    return gcd(a, b) == 1


def pairwise_coprime(*numbers):
    """Return whether every pair of integers is coprime."""
    for number in numbers:
        _require_int(number)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if gcd(numbers[i], numbers[j]) != 1:
                return False

    return True


#---- Bézout Coefficients ----
def bezout_coefficients(a, b):
    """Return coefficients (x, y) such that a*x + b*y = gcd(a, b)."""
    _, x, y = extended_gcd(a, b)
    return x, y


#---- Euclidean Algorithm Steps ----
def euclidean_steps(a, b):
    """Return the division steps used by the Euclidean algorithm."""
    _require_int(a, "a")
    _require_int(b, "b")

    a, b = abs(a), abs(b)
    steps = []

    while b:
        quotient, remainder = divmod(a, b)
        steps.append((a, b, quotient, remainder))
        a, b = b, remainder

    return steps