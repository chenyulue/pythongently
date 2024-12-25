import pytest
import datetime

from ppeg.exercise21 import is_valid_date

@pytest.mark.parametrize("year, month, day, expected", [
    (1999, 12, 31, True),
    (2000, 2, 29, True),
    (2001, 2, 29, False),
    (2029, 2, 29, False),
    (1000000, 1, 1, True),
    (2015, 4, 31, False),
    (1970, 5, 99, False),
    (1981, 0, 3, False),
    (1666, 4, 0, False)
])
def test_is_valid_date(year, month, day, expected):
    assert is_valid_date(year, month, day) == expected


def test_is_valid_date_with_datetime():
    d = datetime.date(1970, 1, 1)
    one_day = datetime.timedelta(days=1)
    for i in range(1000000):
        assert is_valid_date(d.year, d.month, d.day) is True
        d += one_day