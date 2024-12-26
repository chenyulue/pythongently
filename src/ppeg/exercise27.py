# Exercise #27: Rectangle Drawing
"""Write a `draw_rectangle()` function with two integer parameters: `width` and `height`. The function doesn't return any values but rather prints a rectangle with the given number of hashtags in the horizontal and vertical directions.
"""

def draw_rectangle(width: int, height: int) -> None:
    if width < 1 or height < 1:
        return
    
    for i in range(height):
        for j in range(width):
            print("#", end="")
        print()

def run(width: str, height: str) -> None:
    draw_rectangle(int(width), int(height))