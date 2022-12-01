"""euler_19.py Problem 19
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""


from datetime import date


def main() -> None:
    _sunday = 6
    _first = 1
    sundays: int = 0

    for _, year in enumerate(range(1901, 2001, 1)):
        for _, month in enumerate(range(1, 13, 1)):
            if date(year, month, _first).weekday() == _sunday:
                sundays += 1

    print(f"{sundays} Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)")


if __name__ == "__main__":
    main()
