"""Stage-time value object and a read-only talent-show preview extension.

Run from the repository root with:
    py -3 stories/05_campus_talent_show/A1.py
"""

from story import AudienceWave, Poetry, TalentShow as StoryTalentShow


class StageTime:
    """A non-negative whole number of minutes."""

    def __init__(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("StageTime amount must be a non-negative whole number.")
        self._amount = amount

    @property
    def amount(self):
        """Return the number of minutes; callers cannot assign this property."""
        return self._amount

    def __str__(self):
        return f"{self.amount:,} minutes"

    def __repr__(self):
        return f"StageTime({self.amount})"

    def __eq__(self, other):
        if not isinstance(other, StageTime):
            return NotImplemented
        return self.amount == other.amount

    def __add__(self, other):
        if not isinstance(other, StageTime):
            return NotImplemented
        return StageTime(self.amount + other.amount)


class TalentShow(StoryTalentShow):
    """The original show with a preview that never books or spends time."""

    def preview_total(self, choices):
        total = StageTime(0)
        for choice in choices:
            total = total + StageTime(choice.duration())
        return total


class ZeroDurationChoice:
    """A tiny example choice for the zero-minute boundary check."""

    def duration(self):
        return 0


class InvalidDurationChoice:
    """An example of a choice that returns a refused, fractional duration."""

    def duration(self):
        return 1.5


def run_checks():
    print("StageTime represents minutes and addition creates a new value.")

    # Normal case: display, representation, equality, addition and immutability.
    first = StageTime(3000)
    same = StageTime(3000)
    different = StageTime(3001)
    second = StageTime(25)
    combined = first + second
    assert str(first) == "3,000 minutes"
    assert repr(first) == "StageTime(3000)"
    assert first == same
    assert first != different
    assert combined == StageTime(3025)
    assert first.amount == 3000 and second.amount == 25
    assert combined is not first and combined is not second
    print(f"Normal case: {first!s} + {second!s} = {combined!s}")
    print(f"Equal: {first == same}; unequal: {first == different}")
    print(f"Developer representation: {first!r}")

    # Boundary case: zero is allowed, and amount is a read-only property.
    zero = StageTime(0)
    assert zero.amount == 0
    try:
        zero.amount = 2
    except AttributeError:
        pass
    else:
        raise AssertionError("amount should be read-only")
    assert zero.amount == 0
    print(f"Boundary case: {zero!s}; amount remains read-only")

    # Refused case: negatives, fractions and Booleans are not whole-minute values.
    for invalid_amount in (-1, 1.5, True):
        try:
            StageTime(invalid_amount)
        except ValueError:
            pass
        else:
            raise AssertionError(f"StageTime accepted {invalid_amount!r}")
    assert StageTime.__eq__(first, 3000) is NotImplemented
    assert StageTime.__add__(first, 3000) is NotImplemented
    print("Refused case: negative, fractional and Boolean amounts; unsupported operands")

    # Normal case: distinct choice types contribute duration without booking.
    show = TalentShow("Joel", 8)
    choices = [Poetry("Spoken word"), AudienceWave()]
    state_before_preview = (show.clock.remaining, show.act_count)
    preview = show.preview_total(choices)
    assert preview == StageTime(5)
    assert (show.clock.remaining, show.act_count) == state_before_preview
    print(f"Preview of Poetry and AudienceWave: {preview!s}")

    # Boundary case: an empty list and a zero-minute choice both total zero.
    assert show.preview_total([]) == StageTime(0)
    assert show.preview_total([ZeroDurationChoice()]) == StageTime(0)
    print(f"Boundary case: empty preview = {show.preview_total([])!s}")

    # Refused case: preview applies StageTime validation to each choice duration.
    try:
        show.preview_total([InvalidDurationChoice()])
    except ValueError:
        pass
    else:
        raise AssertionError("preview accepted a fractional choice duration")
    assert (show.clock.remaining, show.act_count) == state_before_preview
    print("Refused case: fractional choice duration; show state stays unchanged")


if __name__ == "__main__":
    run_checks()


