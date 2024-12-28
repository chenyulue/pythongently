# Exercise #42: Bubble Sort
"""Write a `bubble_sort()` function with a list parameter named `numbers`. The function rearranges the values in this list in-place. The function also returns the now-sorted list. There are many sorting algorithms, but this exercise asks you to implement the bubble sort algorithm.

The objective of this exercise is to write a sorting algorithm, so avoid using Python's `sort()` method or `sorted()` function as that would defeat the purpose of the exercise.
"""


def bubble_sort(numbers: list[int]) -> list[int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


def run(*numbers: str) -> None:
    n = list(map(int, numbers))
    print("Sorted list:", bubble_sort(n))