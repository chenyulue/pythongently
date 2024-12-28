import pytest

from ppeg.exercise37 import make_change

@pytest.mark.parametrize("amount, expected", [
    (30, {"quarters": 1, "nickels": 1}),
    (10, {"dimes": 1}),
    (57, {"quarters":2, "nickels": 1, "pennies": 2}),
    (100, {"quarters": 4}),
    (0, {}),
    (125, {"quarters": 5})
])
def test_make_change(amount, expected):
    assert make_change(amount) == expected