import pytest

from ppeg.exercise36 import reverse_string


@pytest.mark.parametrize("text, expected", [
    ("Hello", "olleH"),
    ("", ""),
    ("aaazzz", "zzzaaa"),
    ("xxxx", "xxxx")
])
def test_reverse_string(text: str, expected: str):
    assert reverse_string(text) == expected