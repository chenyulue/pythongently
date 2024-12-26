# Exercise #26: Handshakes
"""Write a function named `print_handshakes()` with a list parameter named `people` which will be a list of strings of people's names. The function prints out 'X shakes hands with Y', where X and Y are every possible pair of handshakes between the people in the list. No duplicates are permitted: if “Alice shakes hands with Bob” appears in the output, then “Bob shakes hands with Alice” should not appear.

The `print_handshakes()` function must also return an integer of the number of handshakes.
"""

from collections.abc import Sequence


def print_handshakes(people: Sequence[str]) -> int:
    pairs = [(p1, p2) for i, p1 in enumerate(people) for p2 in people[i + 1 :]]

    for p1, p2 in pairs:
        print(f"{p1} shakes hands with {p2}")

    return len(pairs)
