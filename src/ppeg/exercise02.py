# Exercise #2: Temperature Conversion
"""Write a `convert_to_fahrenheit` function with a `degree_celsius` parameter. This
function returns the number of this temperature in degrees Fahrenheit. Then write a
function named `convert_to_celsius` with a `degree_fahrenheit` parameter and returns
a number of this temperature in degrees Celsius.
"""

from decimal import Decimal


def convert_to_fahrenheit(degree_celsius: Decimal | float, ndigits: int = 2) -> Decimal:
    if not isinstance(degree_celsius, Decimal):
        degree_celsius = Decimal(degree_celsius)
    result = degree_celsius * 9 / 5 + 32
    return round(result, 2)


def convert_to_celsius(degree_fahrenheit: Decimal | float, ndigits: int = 2) -> Decimal:
    if not isinstance(degree_fahrenheit, Decimal):
        degree_fahrenheit = Decimal(degree_fahrenheit)
    result = (degree_fahrenheit - 32) * 5 / 9
    return round(result, 2)