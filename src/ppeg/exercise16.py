# Exercise #16: Mode
"""Write a `mode()` function that has a `numbers` parameter. This function returns the mode, or most frequently appearing number, of the list of integer and floating-point numbers passed to the function.

If the numbers parameter is an empty list, the function should return None. You should put the code that checks this at the start of the function.
"""

from collections.abc import Sequence


def mode(numbers: Sequence[float]) -> float | None:
    if not numbers:
        return None

    counts: dict[float, int] = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts.keys(), key=lambda k: counts[k])


def run(*args: str) -> None:
    ns = list(map(float, args))
    print("The mode is:", mode(ns))