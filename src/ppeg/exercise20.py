# Exercise #20: Leap Year
"""Write a `is_leap_year()` function with an integer `year` parameter. If year is a leap year, the function returns `True`. Otherwise, the function returns `False`.
"""

def is_leap_year(year: int) -> bool:
    if year % 4:
        return False
    elif year % 100:
        return True
    else:
        return year % 400 == 0