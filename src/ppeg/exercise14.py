# Exercise #14: Average
"""Write an `average()` function that has a `numbers` parameter. This function returns the statistical average of the list of integer and floating-point numbers passed to the function. While Python's built-in sum() function can help you solve this exercise, try writing the solution without using it.

Passing an empty list to `average()` should cause it to return None.
"""

from typing import Sequence


def average(numbers: Sequence[float]) -> float | None:
    count = len(numbers)
    if count == 0:
        return None

    total = 0
    for number in numbers:
        total += number

    return total / count
