import pytest

from ppeg.exercise41 import rot13

@pytest.mark.parametrize("text, expected", [
    ('Hello, world!','Uryyb, jbeyq!'),
    ('Uryyb, jbeyq!','Hello, world!'),
    ('abcdefghijklmnopqrstuvwxyz','nopqrstuvwxyzabcdefghijklm'),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ','NOPQRSTUVWXYZABCDEFGHIJKLM'),
])
def test_rot13(text, expected):
    assert rot13(text) == expected


def test_rot13_decryption():
    assert rot13(rot13('Hello, world!')) == 'Hello, world!'