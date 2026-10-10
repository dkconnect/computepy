"""
divisors.py

Divisor & Number Classification Functions

Author: Dibyanshu | October 2026
"""


#---- Internal Helpers ----
def _validate_integer(n):
    """
    Validates that n is an integer, excluding booleans.
    """
    if type(n) is not int:
        raise TypeError("Expected an integer.")


def _validate_positive(n):
    """
    Validates that n is a positive integer.
    """
    _validate_integer(n)

    if n <= 0:
        raise ValueError("Expected a positive integer.")


def _integer_sqrt(n):
    """
    Returns floor(sqrt(n)) using integer binary search.
    """
    if n < 0:
        raise ValueError("Square root requires a non-negative integer.")

    if n < 2:
        return n

    left = 1
    right = n
    result = 1

    while left <= right:
        middle = (left + right) // 2

        if middle <= n // middle:
            result = middle
            left = middle + 1
        else:
            right = middle - 1

    return result


def _prime_factorization(n):
    """
    Returns the prime factorization of n as a dictionary.
    """

    factors = {}
    divisor = 2

    while divisor <= n // divisor:

        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor

        if divisor == 2:
            divisor = 3
        else:
            divisor += 2

    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _proper_divisor_sum(n):
    """
    Returns the sum of positive divisors excluding n.
    """
    if n == 1:
        return 0

    return divisor_sum(n) - n


#---- Basic Divisors ----
def divisors(n):
    """
    Returns all positive divisors of n in ascending order.
    """

    _validate_positive(n)

    lower = []
    upper = []

    limit = _integer_sqrt(n)

    for divisor in range(1, limit + 1):

        if n % divisor == 0:
            lower.append(divisor)

            partner = n // divisor

            if partner != divisor:
                upper.append(partner)
    upper.reverse()

    return lower + upper


def proper_divisors(n):
    """
    Returns all positive divisors excluding n.
    """

    _validate_positive(n)
    return divisors(n)[:-1]


def divisor_pairs(n):
    """
    Returns all positive factor pairs of n.
    """

    _validate_positive(n)

    result = []
    limit = _integer_sqrt(n)

    for divisor in range(1, limit + 1):

        if n % divisor == 0:
            result.append((divisor, n // divisor))

    return result


def is_divisor(divisor, number):
    """
    Returns True if divisor divides number exactly.
    """

    _validate_integer(divisor)
    _validate_integer(number)

    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")

    return number % divisor == 0


def common_divisors(a, b):
    """
    Returns all positive common divisors of a and b.
    """
    _validate_integer(a)
    _validate_integer(b)

    a = abs(a)
    b = abs(b)

    if a == 0 and b == 0:
        raise ValueError(
            "The pair (0, 0) has infinitely many common divisors."
        )

    while b:
        a, b = b, a % b

    return divisors(a)


#---- Divisor Counting ----
def divisor_count(n):
    """
    Returns the number of positive divisors of n.
    """

    _validate_positive(n)
    factors = _prime_factorization(n)
    result = 1

    for exponent in factors.values():
        result *= exponent + 1

    return result


def proper_divisor_count(n):
    """
    Returns the number of proper positive divisors.
    """
    _validate_positive(n)
    return divisor_count(n) - 1


def has_exactly_n_divisors(number, count):
    """
    Returns True if number has exactly count positive divisors.
    """
    _validate_positive(number)
    _validate_integer(count)

    if count < 0:
        raise ValueError("Count cannot be negative.")

    return divisor_count(number) == count


#---- Divisor Sums ----
def divisor_sum(n):
    """
    Returns the sum of all positive divisors of n.
    """
    _validate_positive(n)

    factors = _prime_factorization(n)
    result = 1

    for prime, exponent in factors.items():
        term = 1
        power = 1

        for _ in range(exponent):
            power *= prime
            term += power

        result *= term
    return result


def proper_divisor_sum(n):
    """
    Returns the sum of proper positive divisors.
    """
    _validate_positive(n)
    return _proper_divisor_sum(n)


def divisor_power_sum(n, power):
    """
    Returns the sum of each positive divisor raised to power.
    """
    _validate_positive(n)
    _validate_integer(power)

    if power < 0:
        raise ValueError("Power must be non-negative.")

    total = 0

    for divisor in divisors(n):
        total += divisor ** power

    return total


def aliquot_sum(n):
    """
    Returns the aliquot sum of n. The aliquot sum is the sum of proper divisors.
    """
    return proper_divisor_sum(n)


#---- Number Classification ----
def is_perfect_number(n):
    """
    Returns True if n equals the sum of its proper divisors.
    """
    _validate_positive(n)
    return _proper_divisor_sum(n) == n


def is_abundant_number(n):
    """
    Returns True if the sum of proper divisors exceeds n.
    """
    _validate_positive(n)
    return _proper_divisor_sum(n) > n


def is_deficient_number(n):
    """
    Returns True if the sum of proper divisors is less than n.
    """
    _validate_positive(n)
    return _proper_divisor_sum(n) < n


def classify_number(n):
    """
    Classifies a positive integer as:
        "perfect"
        "abundant"
        "deficient"
    """
    _validate_positive(n)
    total = _proper_divisor_sum(n)

    if total == n:
        return "perfect"

    if total > n:
        return "abundant"

    return "deficient"


#---- Special Number Relationships ----
def are_amicable_numbers(a, b):
    """
    Returns True if a and b are distinct amicable numbers.
    """
    _validate_positive(a)
    _validate_positive(b)

    if a == b:
        return False

    return (
        _proper_divisor_sum(a) == b
        and _proper_divisor_sum(b) == a
    )


def are_betrothed_numbers(a, b):
    """
    Returns True if a and b form a betrothed pair.
    For betrothed numbers:
        s(a) = b + 1
        s(b) = a + 1
    """
    _validate_positive(a)
    _validate_positive(b)

    if a == b:
        return False

    return (
        _proper_divisor_sum(a) == b + 1
        and _proper_divisor_sum(b) == a + 1
    )


#---- Special Divisor Properties ----
def is_square_free(n):
    """
    Returns True if no prime square divides n.
    """
    _validate_positive(n)
    factors = _prime_factorization(n)

    for exponent in factors.values():

        if exponent > 1:
            return False
    return True


def is_highly_composite(n):
    """
    Returns True if n has more divisors than every positive integer smaller than n.
    """
    _validate_positive(n)
    target = divisor_count(n)

    for number in range(1, n):
        if divisor_count(number) >= target:
            return False

    return True


def is_practical_number(n):
    """
    Returns True if every integer from 1 to n can be expressed as a sum of distinct divisors of n.
    """
    _validate_positive(n)

    if n == 1:
        return True

    factors = _prime_factorization(n)
    items = list(factors.items())

    if items[0][0] != 2:
        return False
    sigma = 1

    for prime, exponent in items:
        if prime > sigma + 1:
            return False

        term = 1
        power = 1

        for _ in range(exponent):
            power *= prime
            term += power

        sigma *= term
    return True


#---- Divisor Tables ----
def divisor_table(limit):
    """
    Returns a dictionary mapping every positive integer up to limit to its positive divisors.
    """
    _validate_integer(limit)

    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    table = {
        number: []
        for number in range(1, limit + 1)
    }

    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            table[multiple].append(divisor)

    return table


def divisor_count_table(limit):
    """
    Returns a list of divisor counts for 0 through limit.
    """
    _validate_integer(limit)
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    counts = [0] * (limit + 1)
    for divisor in range(1, limit + 1):

        for multiple in range(divisor, limit + 1, divisor):
            counts[multiple] += 1

    return counts


def divisor_sum_table(limit):
    """
    Returns a list of positive divisor sums for integers from 0 through limit.
    """
    _validate_integer(limit)
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    sums = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            sums[multiple] += divisor

    return sums


#---- Number Generation ----
def perfect_numbers_up_to(limit):
    """
    Returns all perfect numbers up to limit.
    """
    _validate_integer(limit)

    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    sums = divisor_sum_table(limit)
    return [
        n for n in range(2, limit + 1)
        if sums[n] - n == n
    ]


def abundant_numbers_up_to(limit):
    """
    Returns all abundant numbers up to limit.
    """
    _validate_integer(limit)
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    sums = divisor_sum_table(limit)
    return [
        n for n in range(1, limit + 1)
        if sums[n] - n > n
    ]


def deficient_numbers_up_to(limit):
    """
    Returns all deficient numbers up to limit.
    """
    _validate_integer(limit)
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    sums = divisor_sum_table(limit)

    return [
        n for n in range(1, limit + 1)
        if sums[n] - n < n
    ]