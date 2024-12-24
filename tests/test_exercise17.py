import pytest

from ppeg.exercise17 import roll_dice

def test_roll_dice_zero_times():
    assert roll_dice(0) == 0

def test_roll_dice_randomly():
    assert roll_dice(1000) != roll_dice(1000)

@pytest.mark.parametrize("low, high, number_of_dice", [
    (1, 6, 1),
    (2, 12, 2),
    (3, 18, 3),
    (100, 600, 100),
])
def test_roll_dice_within_range(low, high, number_of_dice):
    for _ in range(1000):
        assert low <= roll_dice(number_of_dice) <= high