# Exercise #22: Rock, Paper, Scissors
"""Write a `rps_winner()` function with parameters `player1` and `player2`. These parameters are passed one of the strings 'rock', 'paper', or 'scissors' representing that player's move. If this results in player 1 winning, the function returns 'player one'. If this results in player 2 winning, the function returns 'player two'. Otherwise, the function returns 'tie'."""

from typing import Literal, TypeAlias

RPS: TypeAlias = Literal["rock", "paper", "scissors"]
Winner: TypeAlias = Literal["player one", "player two", "tie"]


def rps_winner(player1: RPS, player2: RPS) -> Winner:
    match (player1, player2):
        case _ if player1 == player2:
            return "tie"
        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            return "player one"
        case _:
            return "player two"


def run(p1, p2) -> None:
    result = rps_winner(p1, p2)
    if result == "tie":
        print("player one and two have a draw.")
    else:
        print(result, "wins.")