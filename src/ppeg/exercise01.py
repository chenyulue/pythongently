# Exersise #1: Hello, World!
"""Write a program that, when run, greets the user by printing "Hello, World!" 
on the screen. Then it prints a message on the screen asking the user to enter 
their name. The program greets the user by name by printing the "Hello," followed 
by the user's name.
"""

def greet() -> None:
    print("Hello, world!\nWhat is your name?")
    name = input()
    print(f"Hello, {name}")


def run() -> None:
    greet()