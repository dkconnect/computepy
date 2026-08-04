"""
=============
arithmetic.py
=============

Basic arithmetic operations.

This module provides fundamental arithmetic functions for real and integer numbers with consistent error handling.

Author: Dibyanshu | July 2026
"""

'''
Starting with basics operation, even they are part of arithmetic operations.
'''

# ------------------
# BASIC OPERATIONS
# ------------------
def add(a, b):
    return a + b
  
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is undefined.")
    return a % b

def remainder(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a % b

def quotient(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a // b

# ------------------
# UNARY OPERATIONS
# ------------------
def negate(x):
    return -x

def reciprocal(x):
    if x == 0:
        raise ZeroDivisionError("Zero has no reciprocal.")
    return 1 / x

def increment(x):
    return x + 1

def decrement(x):
    return x - 1
  
# -----------------=-----
# COLLECTION OPERATIONS
# -----------------------
def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def product(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def average(*numbers):
    if len(numbers) == 0:
        raise ValueError("At least one number is required.")
    return sum_numbers(*numbers) / len(numbers)

def weighted_average(values, weights):
    if len(values) != len(weights):
        raise ValueError("Values and weights must have equal length.")

    total_weight = sum_numbers(*weights)

    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")
    weighted_sum = 0

    for value, weight in zip(values, weights):
        weighted_sum += value * weight
    return weighted_sum / total_weight


# -------------
# DIFFERENCES
# -------------
def difference(a, b):
    return a - b

def absolute_difference(a, b):
    if a >= b:
        return a - b
    return b - a
