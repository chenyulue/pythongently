import pytest
from decimal import Decimal

from ppeg.exercise02 import convert_to_celsius, convert_to_fahrenheit

@pytest.mark.parametrize("degree, expected", [
    (0, Decimal("-17.78")),
    (180, Decimal("82.22")),
])
def test_convert_to_celsius(degree, expected):
    result = convert_to_celsius(degree)
    assert result == expected

@pytest.mark.parametrize("degree, expected", [
    (0, Decimal("32")),
    (100, Decimal("212")),
])
def test_convert_to_fahrenheit(degree, expected):
    result = convert_to_fahrenheit(degree)
    assert result == expected

@pytest.mark.parametrize("degree", [
    15, 7.45, 9.54, 69, 5.73
])
def test_convert_back_and_forth(degree):
    assert convert_to_celsius(convert_to_fahrenheit(degree)) == Decimal(str(degree))