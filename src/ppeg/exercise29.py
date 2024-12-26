# Exercise #29: Pyramid Drawing
"""Write a `draw_pyramid()` function with a `height` parameter. The top of the pyramid has one centered hashtag character, and the subsequent rows have two more hashtags than the previous row. The number of rows matches the `height` integer. There are no Python assert statements to check the correctness of your program. Instead, you can visually inspect the output yourself."""


def draw_pyramid(height: int) -> None:
    if height < 1:
        return

    for i in range(height):
        hashtag_num = 2 * i + 1
        row_len = height + i
        print(("#" * hashtag_num).rjust(row_len))


def run(h: str) -> None:
    draw_pyramid(int(h))
