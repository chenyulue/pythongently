# Exercise #7: ASCII Table
"""Write a `print_ascii_table()` function that displays the ASCII number and its
corresponding text character, from 32 to 126.  (These are called the printable
ASCII characters.)"""


def print_ascii_table() -> None:
    code_points = range(32, 127)
    chars = (chr(i) for i in code_points)
    strings = (f"{code_point} {char}" for code_point, char in zip(code_points, chars))
    print("\n".join(strings))
