import pytest

from ppeg.exercise01 import greet

PROMPT = "Hello, world!\nWhat is your name?\n"

@pytest.mark.parametrize("input_value, expected_value", [
    ("Alice", PROMPT + "Hello, Alice\n"),
    ("Bob", PROMPT + "Hello, Bob\n"),
])
def test_greet(monkeypatch, capsys, input_value, expected_value):
    # Use monkeypatch to replace the readline method of sys.stdin
    monkeypatch.setattr("builtins.input", lambda: input_value)
    # Call the tested function.
    greet()
    # Capture the standard output
    captured = capsys.readouterr()

    assert captured.out == expected_value