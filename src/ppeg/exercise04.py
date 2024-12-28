# Exercise #4: Area & Volume
"""You will write four functions for this exercise. The functions `area()` and 
`perimeter()` have `length` and `width` parameters and the functions `volume()` 
and `surface_area()` have `length`, `width`, and `height` parameters. These 
functions return the area, perimeter, volume, and surface area, respectively.
"""

def area(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("length and width cannot be negative.")
    return length * width

def perimeter(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("length and width cannot be negative.")
    return 2*length + 2*width

def volume(length: float, width: float, height: float) -> float:
    if length < 0 or height < 0 or width < 0:
        raise ValueError("length, width and height cannot be negative.")
    return length * height * width

def surface_area(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("length, width and height cannot be negative.")
    return (length*width + length*height + width*height) * 2

def run() -> None:
    length = input("Enter the length: ")
    width = input("Enter the width: ")
    height: str = input("Enter the height: ")
    print(f"Area: {area(float(length), float(width))}")
    print(f"Perimeter: {perimeter(float(length), float(width))}")
    print(f"Volume: {volume(float(length), float(width), float(height))}")
    print(f"Surface Area: {surface_area(float(length), float(width), float(height))}")