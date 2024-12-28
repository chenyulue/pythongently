import pytest

from ppeg.exercise33 import comma_format


@pytest.mark.parametrize("number, expected", [
    (1, '1'),
    (10, '10'),
    (100, '100'),
    (1000, '1,000'),
    (10000, '10,000'),
    (100000, '100,000'),
    (1000000, '1,000,000'),
    (10000000, '10,000,000'),
    (1234567890, '1,234,567,890'),
    (1000.123456, '1,000.123456'),
    (-100000, '-100,000'),
    (-1000.123456, '-1,000.123456'),
    (-100000000, '-100,000,000'),
])
def test_comma_format(number, expected):
    assert comma_format(number) == expected