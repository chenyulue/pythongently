import pytest

from ppeg.exercise20 import is_leap_year

@pytest.mark.parametrize("year, expected", [
    (1999, False),
    (2000, True),
    (2001, False),
    (2004, True),
    (2100, False),
    (2400, True),
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected