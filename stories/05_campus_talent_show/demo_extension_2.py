"""Demo for Extension 2: The MC gets extra time."""
from story import ShowClock


def main():
    clock = ShowClock(5)

    print("Normal case: extend(3) ->", clock.extend(3), "Remaining:", clock.remaining)
    print("Boundary case: extend(0) ->", clock.extend(0), "Remaining:", clock.remaining)
    print("Refused case: extend(-2) ->", clock.extend(-2), "Remaining:", clock.remaining)


if __name__ == "__main__":
    main()
