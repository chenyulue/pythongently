import pytest

from ppeg.exercise03 import is_odd, is_even

@pytest.mark.parametrize("number, expected", [
    (42, False),
    (9999, True),
    (-10, False),
    (-11, True),
    (3.1415, False)
])
def test_is_odd(number, expected):
    assert is_odd(number) == expected


@pytest.mark.parametrize("number, expected", [
    (42, True),
    (9999, False),
    (-10, True),
    (-11, False),
    (3.1415, False)
])
def test_is_even(number, expected):
    assert is_even(number) == expected