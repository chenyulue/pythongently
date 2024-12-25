import pytest

from ppeg.exercise22 import rps_winner


@pytest.mark.parametrize("p1, p2, expected", [
    ("rock", "paper", "player two"),
    ("rock", "scissors", "player one"),
    ("paper", "scissors", "player two"),
    ("paper", "rock", "player one"),
    ("scissors", "rock", "player two"),
    ("scissors", "paper", "player one"),
    ("rock", "rock", "tie"),
    ("paper", "paper", "tie"),
    ("scissors", "scissors", "tie")
])
def test_rps_winner(p1, p2, expected) -> None:
    assert rps_winner(p1, p2) == expected