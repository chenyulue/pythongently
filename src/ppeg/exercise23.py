# Exercise #23: 99 Bottles of Beer
"""Write a program that displays the lyrics to “99 Bottles of Beer.”"""


def stanza(number: int) -> str:
    if number < 1:
        raise ValueError("number must be positive")

    def bottles(n: int) -> str:
        match n:
            case 0:
                return "No more bottles"
            case 1:
                return "1 bottle"
            case _:
                return f"{n} bottles"

    return (
        f"{bottles(number)} of beer on the wall,\n"
        f"{bottles(number)} of beer,\n"
        "Take one down,\n"
        "Pass it around,\n"
        f"{bottles(number-1)} of beer on the wall{'!' if number == 1 else ','}\n"
    )


def print_lyrics() -> None:
    lyrics = (stanza(n) for n in range(99, 0, -1))
    print("\n".join(lyrics), end="")


def run() -> None:
    print_lyrics()