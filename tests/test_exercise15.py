import pytest

from ppeg.exercise15 import median

@pytest.mark.parametrize("numbers, expected", [
    ([3,7,10,4,1,6,9,2,8], 6),
    ([], None),
    ([1,2,3], 2),
    ([3,7,10,4,1,9,6,5,2,8], 5.5),
])
def test_median(numbers, expected):
    assert median(numbers) == expected


def test_median_after_shuffling():
    import random

    random.seed(42)
    test_data = [3,7,10,4,1,9,6,2,8]
    for i in range(1000):
        random.shuffle(test_data)
        assert median(test_data) == 6