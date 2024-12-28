# Exercise #32: Convert Strings to Integers
"""Write a `convert_str_to_int()` function with a `string_num` parameter. This function returns an integer form of the parameter just like the `int()` function. For example, `convert_str_to_int('42')` should return the integer 42. The function doesn't have to work for floating-point numbers with a decimal point, but it should work for negative number values.

Avoid using `int()` in your code, as that would do the conversion for you and defeat the purpose of this exercise.
"""

from functools import reduce


def str_to_digit(digit: str) -> int:
    codepoint = ord(digit)
    if codepoint < ord("0") or codepoint > ord("9"):
        raise ValueError(f"Invalid digit char: {digit}")

    return codepoint - ord("0")


def convert_str_to_int(string_num: str) -> int:
    if string_num.startswith("-"):
        sign = -1
        string_num = string_num[1:]
    else:
        sign = 1

    return sign * reduce(lambda x, y: 10 * x + y, map(str_to_digit, string_num))

def run(num: str) -> None:
    print(f'"{num}"', "=>", convert_str_to_int(num))
