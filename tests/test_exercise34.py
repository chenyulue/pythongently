import pytest

from ppeg.exercise34 import get_uppercase



@pytest.mark.parametrize("text, expected", [
    ("Hello", "HELLO"),
    ("hello", "HELLO"),
    ("HELLO", "HELLO"),
    ("Hello, world!", "HELLO, WORLD!"),
    ("goodbye 123!", "GOODBYE 123!"),
    ("12345", "12345"),
    ("", ""),
])
def test_get_uppercase(text, expected):
    assert get_uppercase(text) == expected