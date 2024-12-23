# Exercise #15: Median
"""Write a `median()` function that has a `numbers` parameter. This function returns the statistical median of the numbers list. The median of an odd-length list is the number in the middlemost number when the list is in sorted order. If the list has an even length, the median is the average of the two middlemost numbers when the list is in sorted order. Feel free to use Python's built-in sort() method to sort the numbers list.

Passing an empty list to `median()` should cause it to return None.
"""

from collections.abc import Sequence


def median(numbers: Sequence[float]) -> float | None:
    count = len(numbers)
    if count == 0:
        return None

    numbers = sorted(numbers)

    if count % 2:
        return numbers[count // 2]
    else:
        return (numbers[count // 2] + numbers[count // 2 - 1]) / 2
