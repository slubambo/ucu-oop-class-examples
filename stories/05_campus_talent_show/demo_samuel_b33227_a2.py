"""A2 demo for strict Campus Talent Show booking."""

from story import (
    Comedy,
    Poetry,
    ShowChoiceError,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
)


class NegativeDurationAct:
    """A fake act used to demonstrate an invalid request."""

    name = "Negative duration act"

    def duration(self):
        return -1


def attempt(label, action, show):
    """Run one attempt and report whether failed state stayed unchanged."""
    minutes_before = show.clock.remaining
    acts_before = show.act_count
    lineup_before = tuple(act.name for act in show._lineup)

    try:
        result = action()
    except ShowChoiceError as error:
        print(f"{label}: ShowChoiceError: {error}")
    except ShowRequestError as error:
        print(f"{label}: ShowRequestError: {error}")
    except ShowResourceError as error:
        print(f"{label}: ShowResourceError: {error}")
    else:
        print(f"{label}: booking succeeded: {result}")
    finally:
        state_unchanged = (
            show.clock.remaining == minutes_before
            and show.act_count == acts_before
            and tuple(act.name for act in show._lineup) == lineup_before
        )
        print(f"{label}: state unchanged = {state_unchanged}")
        print(f"{label}: attempt complete")


def main():
    show = StrictTalentShow("Samuel", 6)

    print("=== SAMUEL A2 STRICT BOOKING DEMO ===")

    print(show.safe_book(Poetry("Samuel's poetry")))
    print(
        f"After valid booking: {show.clock.remaining} minutes left, "
        f"{show.act_count} acts"
    )

    print(show.safe_book(Comedy("Samuel's comedy")))
    print(
        f"After exact-fit booking: {show.clock.remaining} minutes left, "
        f"{show.act_count} acts"
    )

    attempt(
        "Insufficient time",
        lambda: show.safe_book(Comedy("Another comedy")),
        show,
    )

    attempt(
        "None choice",
        lambda: show.safe_book(None),
        show,
    )

    attempt(
        "Negative duration",
        lambda: show.safe_book(NegativeDurationAct()),
        show,
    )

    print(
        f"Final state: {show.clock.remaining} minutes left, "
        f"{show.act_count} acts"
    )


if __name__ == "__main__":
    main()