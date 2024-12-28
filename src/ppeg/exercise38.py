# Exercise #38: Random Shuffle
"""Write a `shuffle()` function with a `values` parameter set to a list of values. The function doesn't return anything, but rather it sets each value in the list to a random index. The resulting shuffled list must contain the same values as before but in random order.

This exercise asks you to implement a function identical to Python's `random.shuffle()` function. As such, avoid using this function in your solution as it'd defeat the purpose of the exercise.
"""

from typing import Any
import random

def shuffle(values: list[Any]) -> None:
    for i, value in enumerate(values):
        swap_index = random.randint(0, len(values) - 1)
        values[i], values[swap_index] = values[swap_index], values[i]

def run(*values: str) -> None:
    vs = list(values)
    shuffle(vs)
    print(vs)