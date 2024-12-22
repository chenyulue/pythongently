import pytest

from ppeg.exercise09 import get_chess_square_color


@pytest.mark.parametrize(
    "column, row, expected",
    [
        (0, 0, "white"),
        (1, 0, "black"),
        (0, 1, "black"),
        (7, 7, "white"),
        (3, 4, "black"),
        (0, 8, ""),
        (2, 9, ""),
    ],
)
def test_get_chess_square_color(column, row, expected):
    assert get_chess_square_color(column, row) == expected
