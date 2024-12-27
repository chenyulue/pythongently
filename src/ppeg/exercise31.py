# Exercise #31: Convert Integers to Strings
"""Write a `convert_int_to_str()` function with an `integer_num` parameter. This function operates similarly to the `str()` function in that it returns a string form of the parameter. For example, `convert_int_to_str(42)` should return the string '42'. The function doesn't have to work for floating-point numbers with a decimal point, but it should work for negative integer values.

Avoid using Python's `str()` function in your code, as that would do the conversion for you and defeat the purpose of this exercise.
"""

from collections.abc import Iterator
import math


def digit_to_str(digit: int) -> str:
    if digit < 0 or digit > 9:
        raise ValueError(f"Invalid digit: {digit}")

    return chr(ord("0") + digit)


def integer_to_digits(integer_num: int) -> Iterator[int]:
    if integer_num == 0:
        yield 0
        return

    ndigits = int(math.log10(integer_num))

    for i in range(ndigits, -1, -1):
        q, v = divmod(integer_num, 10**i)
        yield q
        integer_num = v


def convert_int_to_str(integer_num: int) -> str:
    sign = "-" if integer_num < 0 else ""
    digits = map(digit_to_str, integer_to_digits(abs(integer_num)))

    return f"{sign}{''.join(digits)}"


def run(num: str) -> None:
    print(int(num))
    print(convert_int_to_str(int(num)))
