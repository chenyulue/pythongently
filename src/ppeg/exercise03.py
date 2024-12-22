# Exercise #3: Odd & Even
"""Write two functions, `is_odd` and `is_even`, with a single numeric parameter 
named number. The `i_odd` function returns True if number is odd and False if 
number is even. The `is_even` function returns the True if number is even and 
False if number is odd. Both functions return False for numbers with fractional 
parts, such as 3.14 or -4.5. Zero is considered an even number.
"""
from typing import TypeAlias

Number: TypeAlias = float | int

def is_odd(number: Number) -> bool:
    match number:
        case float():
            return False
        case _:
            return number % 2 == 1

def is_even(number: Number) -> bool:
    match number:
        case float():
            return False
        case _:
            return number % 2 == 0