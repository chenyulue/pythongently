import pytest

from ppeg.exercise42 import bubble_sort

@pytest.mark.parametrize("numbers, expected", [
    ([2,0,4,1,3],[0,1,2,3,4]),
    ([2,2,2,2], [2,2,2,2])
])
def test_bubble_sort(numbers, expected):
    assert bubble_sort(numbers) == expected