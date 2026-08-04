"""
utilities.py

=============
Basic Mathematical Utilities
=============

Author: Dibyanshu | August 2026
"""

def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

#---- Returns Ratio & Proportions ----
def ratio(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def proportion(a, b, c):
    if a == 0:
        raise ZeroDivisionError
    return (b * c) / a

#---- Spatial & Summary Helpers ----
def mean(*numbers):
    return average(*numbers)

def distance(a, b):
    return absolute_difference(a, b)

def midpoint(a, b):
    return (a + b) / 2

#---- Interpolation & Range Mapping ----
def scale(value, factor):
    return value * factor

def linear_interpolation(start, end, t):
    return start + (end - start) * t

def inverse_linear_interpolation(start, end, value):
    if start == end:
        raise ZeroDivisionError
    return (value - start) / (end - start)

def normalize(value, minimum, maximum):
    return inverse_linear_interpolation(minimum, maximum, value)

def denormalize(value, minimum, maximum):
    return linear_interpolation(minimum, maximum, value)

def map_range(value, input_min, input_max, output_min, output_max):
    normalized = normalize(value, input_min, input_max)
    return denormalize(normalized, output_min, output_max)

def safe_divide(a, b, default=None):
    if b == 0:
        return default
    return a / b

#---- Modular & Cyclic Math ----
def cyclic_wrap(value, minimum, maximum):
    width = maximum - minimum
    return ((value - minimum) % width) + minimum

def modular_distance(a, b, modulus):
    diff = abs(a - b)
    return min(diff, modulus - diff)
  
#---- Multiples & Grid Alignment ----
def nearest_multiple(value, multiple):
    if multiple == 0:
        raise ZeroDivisionError
    lower = (value // multiple) * multiple
    upper = lower + multiple
  
    if value - lower <= upper - value:
        return lower
    return upper

def next_multiple(value, multiple):
    if multiple == 0:
        raise ZeroDivisionError
    return ((value + multiple - 1) // multiple) * multiple

def previous_multiple(value, multiple):
    if multiple == 0:
        raise ZeroDivisionError
    return (value // multiple) * multiple
