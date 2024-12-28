import pytest

from ppeg.exercise39 import collatz

@pytest.mark.parametrize("start, expected", [
    (0, []),
    (10, [10, 5, 16, 8, 4, 2, 1]),
    (11, [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
    (12, [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]),
])
def test_collatz_results(start, expected):
    assert collatz(start) == expected


@pytest.mark.parametrize("start, expected", [
    (256, 9),
    (257, 123),
])
def test_collatz_length(start, expected):
    assert len(collatz(start)) == expected

def test_collatz_randomly():
    import random
    random.seed(42)
    for i in range(1000):
        starting_num = random.randint(1, 100000)
        seq = collatz(starting_num)
        assert seq[0] == starting_num
        assert seq[-1] == 1