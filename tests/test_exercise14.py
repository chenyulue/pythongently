import pytest

from ppeg.exercise14 import average


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], None),
        ([1], 1),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 2.5),
        ([1, 2, 3, 1, 2, 3, 1, 2, 3], 2),
        ([12, 20, 37], 23),
        ([0, 0, 0, 0, 0], 0),
    ],
)
def test_average(numbers, expected):
    assert average(numbers) == expected


def test_average_after_shuffling():
    import random

    random.seed(42)
    test_data = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    for i in range(1000):
        random.shuffle(test_data)
        assert average(test_data) == 2
