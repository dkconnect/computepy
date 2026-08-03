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
