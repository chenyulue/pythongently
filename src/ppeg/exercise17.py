# Exercise #17: Dice Roll
"""Write a `roll_dice()` function with a `number_of_dice` parameter that represents the number of six-sided dice. The function returns the sum of all of the dice rolls. For this exercise you must import Python's random module to call its `random.randint()` function for this exercise."""

import random

def roll_dice(number_of_dice: int) -> int:
    return sum(random.randint(1, 6) for _ in range(number_of_dice))