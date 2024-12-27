# Exercise #30: 3D Box Drawing
"""Write a `draw_box()` function with a `size` parameter. The size parameter contains an integer for the width, length, and height of the box. The horizontal lines are drawn with - dash characters, the vertical lines with | pipe characters, and the diagonal lines with / forward slash characters. The corners of the box are drawn with + plus signs.

If the argument for `size` is less than 1, the function prints nothing.
"""


def make_line(size: int, line: int) -> list[str]:
    match line:
        case 1:
            return ["+".rjust(size + 2), "+".rjust(2 * size + 1, "-")]
        case 2:
            return ["/".rjust(i) for i in range(size + 1, 1, -1)]
        case 3:
            return ["/".rjust(2 * size + 1) for _ in range(size + 1, 1, -1)]
        case 4:
            return ["|".rjust(i) for i in range(1, size + 1)]
        case 5:
            return ["+", "+".rjust(2 * size + 1, "-"), "+".rjust(size + 1)]
        case 6:
            return ["|"] * size
        case 7:
            return ["|".rjust(2 * size + 1) for _ in range(size)]
        case 8:
            return ["/".rjust(i) for i in range(size, 0, -1)]
        case 9:
            return ["+", "+".rjust(2 * size + 1, "-")]
        case _:
            return []


def draw_box(size: int) -> None:
    if size < 1:
        return

    line_1 = "".join(make_line(size, 1))
    line_234 = "\n".join(
        "".join([a, b, c])
        for a, b, c in zip(make_line(size, 2), make_line(size, 3), make_line(size, 4))
    )
    line_5 = "".join(make_line(size, 5))
    line_678 = "\n".join(
        "".join([a, b, c])
        for a, b, c in zip(make_line(size, 6), make_line(size, 7), make_line(size, 8))
    )
    line_9 = "".join(make_line(size, 9))

    for line in [line_1, line_234, line_5, line_678, line_9]:
        print(line)


def run(size: str) -> None:
    draw_box(int(size))
