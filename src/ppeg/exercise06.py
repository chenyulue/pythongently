# Exercise #6: Ordinal Suffix
"""In English, ordinal numerals have suffixes such as the “th” in “30th” or 
“nd” in “2nd”. Write an `ordinal_suffix()` function with an integer parameter 
named `number` and returns a string of the number with its ordinal suffix. 
For example, `ordinal_suffix(42)` should return the string '42nd'.
"""

def ordinal_suffix(number: int) -> str:
    if 11 <= number % 100 <= 13:
        return f"{number}th"
    elif number % 10 == 1:
        return f"{number}st"
    elif number % 10 == 2:
        return f"{number}nd"
    elif number % 10 == 3:
        return f"{number}rd"
    else:
        return f"{number}th"

def run(num: str) -> None:
    print(num, "with ordinal suffix is", ordinal_suffix(int(num)))