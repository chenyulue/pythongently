import pytest

from ppeg.exercise18 import get_cost_of_coffee


@pytest.mark.parametrize(
    "number,price,expected",
    [(7, 2.50, 17.50), (8, 2.50, 20), (9, 2.50, 20), (10, 2.50, 22.5)],
)
def test_get_cost_of_coffee(number, price, expected):
    assert get_cost_of_coffee(number, price) == expected


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 0),
        (8, 8),
        (9, 8),
        (18, 16),
        (19, 17),
        (30, 27),
    ],
)
def test_get_cost_of_coffee_with_different_price(n, m):
    for i in range(1, 4):
        assert get_cost_of_coffee(n, i) == m * i
