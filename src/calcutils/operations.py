"""
Core arithmetic and statistical helper functions for calcutils.
"""

from typing import List


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def average(numbers: List[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)
