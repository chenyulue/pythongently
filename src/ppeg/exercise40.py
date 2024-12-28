# Exercise #40: Merging Two Sorted Lists
"""Write a `merge_two_lists()` function with two parameters `list1` and `list2`. The lists of numbers passed for these parameters are already in sorted order from smallest to largest number. The function returns a single sorted list of all numbers from these two lists.

Don't use the `sorted()` function or `sort()` method as part of your solution.
"""

from collections.abc import Iterator
from typing import TypeVar, Protocol, Any

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...

T = TypeVar("T", bound=Comparable)
    
def merge_two_lists(list1: list[T], list2: list[T]) -> list[T]:

    def _merge_next(list1: list[T], list2: list[T]) -> Iterator[T]:
        i, j = 0, 0
        while i < len(list1) or j < len(list2):
            if i == len(list1):
                yield list2[j]
                j += 1
            elif j == len(list2):
                yield list1[i]
                i += 1
            elif list1[i] < list2[j]:
                yield list1[i]
                i += 1
            else:
                yield list2[j]
                j += 1

    return list(_merge_next(list1, list2))


def run() -> None:
    list1 = input("Sorted list of integers separated by space: ")
    list2 = input("Another sorsted list of integers separated by space: ")

    list1 = list(map(int, list1.split()))
    list2 = list(map(int, list2.split()))

    print("Merged list:\n", merge_two_lists(list1, list2)) # type: ignore

    