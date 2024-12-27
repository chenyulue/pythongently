# Exercise #33: Comma-Formatted Numbers
"""Write a `comma_format()` function with a `number` parameter. The argument for this parameter can be an integer or floating-point number. Your function returns a string of this number with proper US/UK comma formatting. There is a comma after every third digit in the whole number part. There are no commas at all in the fractional part: The proper comma formatting of 1234.5678 is 1,234.5678 and not 1,234.567,8."""


def comma_format(number: float | int) -> str:
    whole, *fract = str(number).split(".")

    grouped = []
