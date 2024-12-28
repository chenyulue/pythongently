import pytest

from ppeg.exercise35 import get_title_case

@pytest.mark.parametrize("text, expected", [
    ("Hello, world!", "Hello, World!"),
    ("HELLO", "Hello"),
    ("hello", "Hello"),
    ("hElLo", "Hello"),
    ("", ""),
    ("abc123xyz", "Abc123Xyz"),
    ("cat dog RAT", "Cat Dog Rat"),
    ("cat,dog,RAT", "Cat,Dog,Rat")
])
def test_get_title_case(text: str, expected: str) -> None:
    assert get_title_case(text) == expected