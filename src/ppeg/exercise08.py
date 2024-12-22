# Exercise #8: Read Write File
"""You will write three functions for this exercise. First, write a `write_to_file()`
function with two parameters for the `filename` of the file and the `text` to write
into the file. Second, write an `append_to_file()` function, which is identical to
`write_to_file()` except that the file opens in append mode instead of write mode.
Finally, write a `read_from_file()` function with one parameter for the `filename`
to open. This function returns the full text contents of the file as a string.
"""

from pathlib import Path


def write_to_file(filename: str | Path, text: str, encoding: str = "utf-8") -> None:
    if not isinstance(filename, Path):
        filename = Path(filename)
    filename.write_text(text, encoding=encoding)


def append_to_file(filename: str | Path, text: str, encoding: str = "utf-8") -> None:
    if not isinstance(filename, Path):
        filename = Path(filename)
    with filename.open("a", encoding=encoding) as fh:
        fh.write(text)


def read_from_file(filename: str | Path, encoding: str = "utf-8") -> str:
    if not isinstance(filename, Path):
        filename = Path(filename)
    return filename.read_text(encoding=encoding)
