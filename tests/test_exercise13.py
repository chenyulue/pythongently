import pytest
from ppeg.exercise13 import calculate_product, calculate_sum

@pytest.mark.parametrize("numbers, expected", [
    ([2,4,6,8,10], 30),
    ([], 0),
])
def test_calculate_sum(numbers, expected):
    assert calculate_sum(numbers) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([2,4,6,8,10], 3840),
    ([], 1),
])
def test_calculate_product(numbers, expected):
    assert calculate_product(numbers) == expected