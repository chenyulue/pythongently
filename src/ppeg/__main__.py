import argparse
import importlib


def get_args() -> argparse.Namespace:
    # Parse the command arguments
    parser = argparse.ArgumentParser(
        prog="ppeg",
        description="Run the solution for Python Proramming Exercises, Gently Explained.",
        epilog="Thanks for Al Sweigart's work",
    )
    parser.add_argument("number", type=int, help="Number of exercise")
    return parser.parse_args()


def main() -> None:
    args = get_args()
    module = importlib.import_module(f"ppeg.exercise{args.number:02d}")
    getattr(module, "run")()
