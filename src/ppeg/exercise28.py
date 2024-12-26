# Exercise #28: Border Drawing
"""Write a `draw_border()` function with parameters `width` and `height`. The function draws the border of a rectangle with the given integer sizes. There are no Python assert statements to check the correctness of your program. Instead, you can visually inspect the output yourself. For example, calling drawBorder(16, 4) would output the following:
+--------------+
|              |
|              |
+--------------+
The interior of the rectangle requires printing spaces. The sizes given include the space required for the corners. If the width or height parameter is less than 2, the function should print nothing.
"""

def draw_border(width: int, height: int) -> None:
    if width < 2 or height < 2:
        return

    for i in range(height):
        corner = "+" if i == 0 or i == height - 1 else "|"
        pad = "-" if i == 0 or i == height - 1 else " "
        print(corner, end="")
        print(corner.rjust(width-2, pad))


def run(w: str, h: str) -> None:
    draw_border(int(w), int(h))