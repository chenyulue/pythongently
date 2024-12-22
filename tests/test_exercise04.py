import pytest

from ppeg.exercise04 import area, volume, perimeter, surface_area

@pytest.mark.parametrize("length, width, expected", [
    (10, 10, 100),
    (0, 9999, 0),
    (5, 8, 40)
])
def test_area(length, width, expected):
    assert area(length, width) == expected


@pytest.mark.parametrize("length, width, expected", [
    (10, 10, 40),
    (0, 9999, 19998),
    (5, 8, 26),
])
def test_perimeter(length, width, expected):
    assert perimeter(length, width) == expected


@pytest.mark.parametrize("length, width, height, expected", [
    (10, 10, 10, 1000),
    (9999, 0, 9999, 0),
    (5, 8, 10, 400),
])
def test_volume(length, width, height, expected):
    assert volume(length, width, height) == expected


@pytest.mark.parametrize("length, width, height, expected", [
    (10, 10, 10, 600),
    (9999, 0, 9999, 199960002),
    (5, 8, 10, 340),
])
def test_surface_area(length, width, height, expected):
    assert surface_area(length, width, height) == expected


def test_raise_exception_with_negative_number():
    with pytest.raises(ValueError) as exc_info_1:
        area(-4, 5)
    with pytest.raises(ValueError) as exc_info_2:
        perimeter(4, -5)
    with pytest.raises(ValueError) as exc_info_3:
        volume(-5, -6, 3)
    with pytest.raises(ValueError) as exc_info_4:
        surface_area(-7, -5, -3)
    assert "cannot be negative" in str(exc_info_1.value)
    assert "cannot be negative" in str(exc_info_2.value)
    assert "cannot be negative" in str(exc_info_3.value)
    assert "cannot be negative" in str(exc_info_4.value)