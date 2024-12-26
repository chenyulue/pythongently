# Exercise #24: Every 15 Minutes
"""Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm. Your solution should produce the following output:

12:00 am

12:15 am

12:30 am

12:45 am

1:00 am

1:15 am

--cut--

11:30 pm

11:45 pm"""


def print_every_15_minutes() -> None:
    for hour in range(0, 24):
        hour_n = h if (h := hour % 12) else 12
        meridiem = "am" if hour < 12 else "pm"
        for minute in range(0, 60, 15):
            print(f"{hour_n}:{minute:02d} {meridiem}")


def run() -> None:
    print_every_15_minutes()