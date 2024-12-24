# Exercise #19: Password Generator
"""Write a `generate_password()` function that has a `length` parameter. The `length` parameter is an integer of how many characters the generated password should have. For security reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway. The password string returned by the function must have at least one lowercase letter, one uppercase letter, one number, and one special character. The special characters for this exercise are ~!@#$%^&*()_+."""

import random


def generate_password(length: int) -> str:
    """Generate a password with the given length. If the length is less than 12,
    it will be set to 12.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password.
    """
    if length < 12:
        length = 12

    lower_cases = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    upper_cases = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    numbers = [str(i) for i in range(10)]
    special_characters = "~!@#$%^&*()_+"

    passwords: list[str] = []
    for i, chars in enumerate([lower_cases, upper_cases, numbers, special_characters]):
        pre_length = len(passwords)
        n = (
            random.randint(1, length - pre_length - 3 + i)
            if i < 3
            else length - pre_length
        )
        selected_chars = random.choices(chars, k=n)
        passwords.extend(selected_chars)

    random.shuffle(passwords)
    return "".join(passwords)

def run(n: str) -> None:
    print("Generated pass words:", generate_password(int(n)))
