# Exercise #9: Chess Square Color
"""Write a `get_chess_square_color()` function that has parameters `column` and 
`row`. The function either returns 'black' or 'white' depending on the color at 
the specified column and row. Chess boards are 8 x 8 spaces in size, and the 
columns and rows in this program begin at 0 and end at 7 like in Figure 9-1. 
If the arguments for column or row are outside the 0 to 7 range, the function 
returns a blank string.

Note that chess boards always have a white square in the top left corner.
"""

from .exercise03 import is_even

def get_chess_square_color(column: int, row: int) -> str:
    if column < 0 or column > 7 or row < 0 or row > 7:
        return ""
    
    if is_even(column) ^ is_even(row):
        return "black"
    else:
        return "white"