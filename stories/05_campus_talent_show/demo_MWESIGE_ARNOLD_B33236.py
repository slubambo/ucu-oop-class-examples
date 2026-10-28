from story import (
    Dance,
    HeadlineDance,
    ShowChoiceError,
    ShowClock,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
)


# extend() accepts positive minutes and leaves the clock unchanged otherwise.
print("=== MC GETS EXTRA TIME: NORMAL CASE ===")
normal_clock = ShowClock(8)
expected = "True; 11 minutes remaining"
actual = f"{normal_clock.extend(3)}; {normal_clock.remaining} minutes remaining"
print(f"Expected: {expected}")
print(f"Actual:   {actual}")


class NegativeRequirement:
    name = "Impossible encore"

    def duration(self):
        return -1


def attempt_booking(show, choice):
    try:
        result = show.safe_book(choice)
    except ShowChoiceError as error:
        print(f"Please choose an act: {error}")
    except ShowRequestError as error:
        print(f"That booking request is invalid: {error}")
    except ShowResourceError as error:
        print(f"That act will not fit: {error}")
    else:
        print(result)
    finally:
        print("Booking attempt complete.\n")


print("\n=== STRICT BOOKING ===")
show = StrictTalentShow("Joel", 5)
attempt_booking(show, None)
attempt_booking(show, NegativeRequirement())
attempt_booking(show, Dance("Mukono Movers"))
attempt_booking(show, HeadlineDance("Mukono Movers: short set"))
print(f"Minutes left: {show.clock.remaining}; successful bookings: {show.act_count}")

print("\n=== MC GETS EXTRA TIME: ZERO-MINUTE BOUNDARY ===")
zero_clock = ShowClock(8)
expected = "False; 8 minutes remaining"
actual = f"{zero_clock.extend(0)}; {zero_clock.remaining} minutes remaining"
print(f"Expected: {expected}")
print(f"Actual:   {actual}")

print("\n=== MC GETS EXTRA TIME: NEGATIVE INPUT ===")
negative_clock = ShowClock(8)
expected = "False; 8 minutes remaining"
actual = f"{negative_clock.extend(-2)}; {negative_clock.remaining} minutes remaining"
print(f"Expected: {expected}")
print(f"Actual:   {actual}")
