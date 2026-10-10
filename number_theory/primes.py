"""
primes.py

Prime Number Functions

Author: Dibyanshu | October 2026
"""


#---- Internal Helpers ----
def _validate_integer(n):
    if type(n) is not int:
        raise TypeError("Expected an integer.")


def _integer_sqrt(n):
    """
    Returns floor(sqrt(n)) using integer binary search.
    """
    if n < 0:
        raise ValueError("Cannot calculate the square root of a negative integer.")

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


#---- Primality ----
def is_prime(n):
    """
    Returns True if n is prime.
    """
    _validate_integer(n)

    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    while divisor <= n // divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False

        divisor += 6

    return True


def is_composite(n):
    """
    Returns True if n is composite.
    """
    _validate_integer(n)
    return n > 1 and not is_prime(n)


#---- Prime Generation ----
def primes_up_to(limit):
    """
    Returns all primes less than or equal to limit. Uses the Sieve of Eratosthenes.
    """
    _validate_integer(limit)

    if limit < 2:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = 0
    sieve[1] = 0
    p = 2

    while p <= limit // p:
        if sieve[p]:
            start = p * p
            sieve[start:limit + 1:p] = (
                b"\x00" * (((limit - start) // p) + 1)
            )
        p += 1

    return [n for n in range(2, limit + 1) if sieve[n]]


def primes_between(start, end):
    """
    Returns primes in the inclusive interval [start, end].
    """
    _validate_integer(start)
    _validate_integer(end)

    if start > end:
        raise ValueError("Start cannot exceed end.")

    if end < 2:
        return []

    return [p for p in primes_up_to(end) if p >= start]


def first_n_primes(count):
    """
    Returns the first count prime numbers.
    """
    _validate_integer(count)
    if count < 0:
        raise ValueError("Count cannot be negative.")

    result = []
    candidate = 2

    while len(result) < count:
        if is_prime(candidate):
            result.append(candidate)

        candidate = 3 if candidate == 2 else candidate + 2
    return result


def nth_prime(n):
    """
    Returns the nth prime, using 1-based indexing.
    """
    _validate_integer(n)

    if n < 1:
        raise ValueError("n must be positive.")

    return first_n_primes(n)[-1]


def next_prime(n):
    """
    Returns the smallest prime strictly greater than n.
    """
    _validate_integer(n)

    candidate = n + 1

    if candidate <= 2:
        return 2

    if candidate % 2 == 0:
        candidate += 1

    while not is_prime(candidate):
        candidate += 2

    return candidate


def previous_prime(n):
    """
    Returns the largest prime strictly less than n.
    """
    _validate_integer(n)

    if n <= 2:
        raise ValueError("No prime exists below the given number.")

    candidate = n - 1

    if candidate == 2:
        return 2

    if candidate % 2 == 0:
        candidate -= 1

    while candidate >= 3:
        if is_prime(candidate):
            return candidate

        candidate -= 2

    return 2


#---- Prime Factorization ----

def prime_factors(n):
    """
    Returns the prime factors of n, including multiplicities.

    Example:
        prime_factors(60) -> [2, 2, 3, 5]
    """
    _validate_integer(n)

    if n == 0:
        raise ValueError("Zero has no finite prime factorization.")

    n = abs(n)
    factors = []

    while n % 2 == 0 and n > 1:
        factors.append(2)
        n //= 2

    divisor = 3

    while divisor <= n // divisor:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

        divisor += 2

    if n > 1:
        factors.append(n)

    return factors


def prime_factorization(n):
    """
    Returns prime factors and their exponents.

    Example:
        prime_factorization(360) -> {2: 3, 3: 2, 5: 1}
    """
    factors = {}

    for prime in prime_factors(n):
        factors[prime] = factors.get(prime, 0) + 1

    return factors


def distinct_prime_factors(n):
    """
    Returns unique prime factors in ascending order.
    """
    return list(prime_factorization(n))


def prime_factor_count(n):
    """
    Returns the number of prime factors with multiplicity.
    """
    return len(prime_factors(n))


#---- Prime Utilities ----

def prime_count(limit):
    """
    Counts primes less than or equal to limit.
    """
    return len(primes_up_to(limit))


def prime_sum(limit):
    """
    Returns the sum of primes less than or equal to limit.
    """
    return sum(primes_up_to(limit))


def are_twin_primes(a, b):
    """
    Returns True if a and b form a twin-prime pair.
    """
    _validate_integer(a)
    _validate_integer(b)

    return abs(a - b) == 2 and is_prime(a) and is_prime(b)


def is_mersenne_prime(exponent):
    """
    Returns True if 2^exponent - 1 is prime.

    Intended for moderate exponents.
    """
    _validate_integer(exponent)

    if exponent < 2:
        return False

    if not is_prime(exponent):
        return False

    return is_prime((1 << exponent) - 1)


def is_coprime(a, b):
    """
    Returns True if gcd(a, b) = 1.
    """
    _validate_integer(a)
    _validate_integer(b)

    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b

    return a == 1