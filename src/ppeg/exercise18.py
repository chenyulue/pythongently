# Exercise #18: Buy 8 Get 1 Free
"""Write a function named `get_cost_of_coffee()` that has a parameters named `number_of_coffees` and `price_per_coffee`. Given this information, the function returns the total cost of the coffee order. This is not a simple multiplication of cost and quantity, however, because the coffee shop has an offer where you get one free coffee for every eight coffees you buy."""


def get_cost_of_coffee(number_of_coffees: int, price_per_coffee: float) -> float:
    n, r = divmod(number_of_coffees, 9)
    return n * 8 * price_per_coffee + r * price_per_coffee

def run() -> None:
    n = input("Number of coffees: ")
    p = input("Price per coffee: ")
    print(f"Total cost: {get_cost_of_coffee(int(n), float(p))}")
