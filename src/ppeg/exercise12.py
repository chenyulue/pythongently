# Exercise #12: Smallest & Biggest
"""Write a `get_smallest()` function that has a `numbers` parameter. The numbers parameter will be a list of integer and floating-point number values. The function returns the smallest value in the list. If the list is empty, the function should return None. Since this function replicates Python's min() function, your solution shouldn't use it.

Similarly, write a `get_biggest()` function which returns the biggest number instead of the smallest number.
"""
from typing import Sequence
from functools import reduce

def get_smallest(numbers: Sequence[float]) -> float | None:
    if not numbers:
        return None

    return reduce(lambda x, y: x if x < y else y, numbers)

def get_biggest(numbers: Sequence[float]) -> float | None:
    if not numbers:
        return None

    return reduce(lambda x, y: x if x > y else y, numbers)