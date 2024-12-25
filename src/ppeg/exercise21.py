# Exercise #21: Validate Date
"""Write an `is_valid_date()` function with parameters `year`, `month`, and `day`. The function should return `True` if the integers provided for these parameters represent a valid date. Otherwise, the function returns `False`. Months are represented by the integers 1 (for January) to 12 (for December) and days are represented by integers 1 up to 28, 29, 30, or 31 depending on the month and year. Your solution should import your leapyear.py program from Exercise #20 for its `is_leap_year()` function, as February 29th is a valid date on leap years.
"""

from .exercise20 import is_leap_year

def is_valid_date(year: int, month: int, day: int) -> bool:
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 1 <= day <= 31
        case 4 | 6 | 9 | 11:
            return 1 <= day <= 30
        case 2 if is_leap_year(year):
            return 1 <= day <= 29
        case 2:
            return 1 <= day <= 28
        case _:
            return False