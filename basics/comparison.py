"""
comparison.py

=============
Comparison Mathematical operations.
=============

Author: Dibyanshu | July 2026
"""

def minimum(*numbers):
    if len(numbers) == 0:
        raise ValueError("No numbers given.")

    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

''' August 2026 '''

def minimum(*numbers):
    if len(numbers) == 0:
        raise ValueError("No numbers given.")

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def maximum(*numbers):
    if len(numbers) == 0:
        raise ValueError("No numbers given.")

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def minmax(*numbers):
    return minimum(*numbers), maximum(*numbers)

def between(value, minimum, maximum):
    return minimum <= value <= maximum

def compare(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0

def is_positive(x):
    return x > 0

def is_negative(x):
    return x < 0

def is_zero(x):
    return x == 0

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_multiple(a, b):
    if b == 0:
        return False
    return a % b == 0

def is_divisible(a, b):
    return is_multiple(a, b)
