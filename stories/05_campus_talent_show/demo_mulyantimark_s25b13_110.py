from story import (
    ShowChoiceError,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
)


class TimedChoice:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    def duration(self):
        return self.minutes


def main():
    print("=== STRICT BOOKING DEMO ===")
    strict_show = StrictTalentShow("Mulyanti", 1)

    def attempt(label, choice, expected_error=None):
        before = (strict_show.clock.remaining, strict_show.act_count)
        print(f"Attempt: {label}")
        try:
            result = strict_show.safe_book(choice)
        except ShowChoiceError as error:
            assert expected_error is ShowChoiceError
            print(f"Choice error: {error}")
            assert (strict_show.clock.remaining, strict_show.act_count) == before
        except ShowRequestError as error:
            assert expected_error is ShowRequestError
            print(f"Request error: {error}")
            assert (strict_show.clock.remaining, strict_show.act_count) == before
        except ShowResourceError as error:
            assert expected_error is ShowResourceError
            print(f"Resource error: {error}")
            assert (strict_show.clock.remaining, strict_show.act_count) == before
        else:
            assert expected_error is None
            print(f"Booking result: {result}")
        finally:
            print(
                f"Minutes left: {strict_show.clock.remaining}; "
                f"booked acts: {strict_show.act_count}"
            )

    attempt("missing choice", None, ShowChoiceError)
    attempt("negative duration", TimedChoice("invalid act", -1), ShowRequestError)
    attempt(
        "unaffordable comedy",
        TimedChoice("overtime act", 2),
        ShowResourceError,
    )
    attempt("zero-duration choice", TimedChoice("zero-duration act", 0))
    attempt("affordable choice", TimedChoice("one-minute act", 1))


if __name__ == "__main__":
    main()
