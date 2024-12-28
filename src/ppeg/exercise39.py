# Exercise #39: Collatz Sequence
"""Write a function named `collatz()` with a `starting_number` parameter. The function returns a list of integers of the Collatz sequence that `starting_number` produces. The first integer in this list must be `starting_number` and the last integer must be 1.

Your function should check if `starting_number` is an integer less than 1, and in that case, return an empty list.

The Collatz sequence is defined by four rules:
- begin with a positive, non-zero integer called n;
- if n is 1, the sequence terminates;
- if n is even, the next value of n is n / 2;
- if n is odd, the next value of n is 3 * n + 1.
"""

from collections.abc import Iterator


def is_odd(x: int) -> bool:
    return x % 2 != 0


def collatz(starting_number: int) -> list[int]:
    if starting_number < 1:
        return []

    def collatz_rule(num: int) -> Iterator[int]:
        while num != 1:
            yield num
            if is_odd(num):
                num = 3 * num + 1
            else:
                num //= 2
        yield 1

    return list(collatz_rule(starting_number))


def run(start: str) -> None:
    print(collatz(int(start)))
