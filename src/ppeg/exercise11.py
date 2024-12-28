# Exercise #11: Hours, Minutes, Seconds
"""Write a `get_hours_minutes_seconds()` function that has a `total_seconds` parameter. The argument for this parameter will be the number of seconds to be translated into the number of hours, minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don't show it: the function should return '10m' rather than '0h 10m 0s'. The only exception is that `get_hours_minutes_seconds(0)` should return '0s'."""


def get_hours_minutes_seconds(total_seconds: int) -> str:
    if total_seconds < 0:
        raise ValueError("total_seconds cannot be a positive integer")

    time_t = [
        ("d", 24 * 60 * 60),
        ("h", 60 * 60),
        ("m", 60),
        ("s", 1),
    ]

    time_strs: list[str] = []

    for k, v in time_t:
        n, total_seconds = divmod(total_seconds, v)
        if n > 0:
            time_strs.append(f"{n}{k}")
    else:
        if not time_strs:
            time_strs.append(f"{n}s")

    return " ".join(time_strs)

def run(sec: str) -> None:
    print(f"{sec} seconds is {get_hours_minutes_seconds(int(sec))}")
