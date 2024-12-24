import pytest

from ppeg.exercise16 import mode

@pytest.mark.parametrize("numbers, expected", [
    ([1,1,2,3,4], 1),
    ([], None),
    ([1,2,3,4,4], 4),
])
def test_mode(numbers, expected):
    assert mode(numbers) == expected


def test_mode_after_shuffling():
    import random

    test_data = [1,2,3,4,4]
    for i in range(1000):
        random.shuffle(test_data)
        assert mode(test_data) == 4