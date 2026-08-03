"""
percentages.py

=============
Percentage operations.
=============

Author: Dibyanshu | July 2026
"""

def percentage(value, percent):
    return value * percent / 100

def percentage_change(old, new):
    if old == 0:
        raise ZeroDivisionError("Old value cannot be zero.")

    return ((new - old) / old) * 100

def percentage_difference(a, b):
    average = (a + b) / 2
    if average == 0:
        raise ZeroDivisionError("Average is zero.")

    return absolute_difference(a, b) / average * 100
