# Exercise #37: Change Maker
"""Write a `make_change()` function with an amount parameter. The amount parameter contains an integer of the number of cents to make change for. For example, 30 would represent 30 cents and 125 would represent $1.25. This function should return a dictionary with keys 'quarters', 'dimes', 'nickels', and 'pennies', where the value for a key is an integer of the number of this type of coin.

The value for a coin's key should never be 0. Instead, the key should not be present in the dictionary. For example, `make_change(5)` should return `{'nickels': 1}` and not `{'quarters': 0, 'dimes': 0, 'nickels': 1, 'pennies': 0}`.

For example, `make_change(30)` would returns the dictionary `{'quarters': 1, 'nickels': 5}` to represent the coins used for 30 cents change. The function should use the minimal number of coins. For example, `make_change(10)` should return `{'dimes': 1} and not {'nickels': 2}`, even though they both add up to 10 cents.

Note: A quarter is 25 cents, a dime is 10 cents, a nickel is 5 cents, and a penny is 1 cent.
"""

from typing import Literal, TypeAlias

Coin: TypeAlias = Literal['quarters', 'dimes', 'nickels', 'pennies']

def make_change(amount: int) -> dict[Coin, int]:
    COINS: list[Coin] = ["quarters", "dimes", "nickels", "pennies"]
    VALUES: list[int] = [25, 10, 5, 1]

    coins = {}
    for n, coin in zip(VALUES, COINS):
        num, amount = divmod(amount, n)
        if num:
            coins[coin] = num

    return coins


def run(amount: str) -> None:
    print(make_change(int(amount)))
