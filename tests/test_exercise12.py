import pytest

from ppeg.exercise12 import get_biggest, get_smallest

@pytest.mark.parametrize('numbers, expected', [
    ([1,2,3], 1), 
    ([3,2,1], 1),
    ([28, 25, 42, 2, 28], 2),
    ([1], 1),
    ([], None),
])
def test_get_smallest(numbers, expected):
    assert get_smallest(numbers) == expected


@pytest.mark.parametrize('numbers, expected', [
    ([1,2,3], 3), 
    ([3,2,1], 3),
    ([28, 25, 42, 2, 28], 42),
    ([1], 1),
    ([], None),
])
def test_get_biggest(numbers, expected):
    assert get_biggest(numbers) == expected