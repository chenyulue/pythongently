import pytest
from ppeg.exercise06 import ordinal_suffix

@pytest.mark.parametrize("number, expected", [
    (0, "0th"),
    (1, "1st"),
    (2, "2nd"),
    (3, "3rd"),
    (4, "4th"),
    (10, "10th"),
    (11, "11th"),
    (12, "12th"),
    (13, "13th"),
    (14, "14th"),
    (101, "101st"),
])
def test_ordinal_suffix(number, expected):
    assert ordinal_suffix(number) == expected