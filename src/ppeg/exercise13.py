# Exercise #13: Sum & Product
"""Write two functions named `calculate_sum()` and `calculate_product()`. They both have a parameter named `numbers`, which will be a list of integer or floating-point values. The `calculate_sum()` function adds these numbers and returns the sum while the `calculate_product()` function multiplies these numbers and returns the product. If the list passed to `calculate_sum()` is empty, the function returns 0. If the list passed to `calculate_product()` is empty, the function returns 1. Since this function replicates Python's `sum()` function, your solution shouldn't call."""

from typing import Sequence


def calculate_sum(numbers: Sequence[float]) -> float:
    total = 0
    for number in numbers:
        total += number

    return total


def calculate_product(numbers: Sequence[float]) -> float:
    total = 1
    for number in numbers:
        total *= number

    return total
