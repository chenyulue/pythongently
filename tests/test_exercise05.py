import pytest

from ppeg.exercise05 import fizz_buzz

@pytest.mark.parametrize("number, expected", [
    (5, "1 2 Fizz 4 Buzz"),
    (35, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz"),
])
def test_fizz_buzz(number, expected, capsys):
    fizz_buzz(number)
    captured = capsys.readouterr()
    assert captured.out == expected + "\n"