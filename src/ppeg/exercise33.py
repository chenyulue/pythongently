# Exercise #33: Comma-Formatted Numbers
"""Write a `comma_format()` function with a `number` parameter. The argument for this parameter can be an integer or floating-point number. Your function returns a string of this number with proper US/UK comma formatting. There is a comma after every third digit in the whole number part. There are no commas at all in the fractional part: The proper comma formatting of 1234.5678 is 1,234.5678 and not 1,234.567,8.
"""

from itertools import pairwise, count

def comma_format(number: float | int) -> str:
    whole, *fract = str(number).split(".")
    if whole.startswith("-"):
        sign = "-"
        whole = whole[1:]
    else:
        sign = ""

    if len(whole) <= 3:
        return str(number)

    grouped = []
    grouped.append(whole[-3:])

    indexs = pairwise(count(-3, -3))
    for end, start in indexs:
        selected = whole[start:end]
        if selected:
            grouped.append(selected)
            
        if len(selected) < 3:
            break

    whole_part = ','.join(grouped[::-1])
    dot = '.' if fract else ''
    fractional_part = ''.join(fract)
    return f"{sign}{whole_part}{dot}{fractional_part}"


def run(num: str) -> None:
    if '.' in num:
        n = float(num)
    else:
        n = int(num)
    print("Comma formatted:", comma_format(n))
        
    