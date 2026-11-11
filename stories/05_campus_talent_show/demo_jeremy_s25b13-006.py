"""Demonstrate StageTime values and a non-mutating mixed-choice preview."""
from story import AudienceWave, Dance, Poetry, StageTime, TalentShow


first = StageTime(3)
same_value = StageTime(3)
other_value = StageTime(4)
combined = first + other_value

assert first == same_value
assert first != other_value
assert combined == StageTime(7)
assert first.amount == 3 and other_value.amount == 4
assert str(first) == "3 minutes"
assert repr(first) == "StageTime(3)"

for invalid_amount in (-1, 1.5, True):
    try:
        StageTime(invalid_amount)
    except ValueError:
        pass
    else:
        raise AssertionError(f"StageTime accepted invalid amount: {invalid_amount!r}")

show = TalentShow("Joel", 12)
choices = [Dance("Mukono Movers"), Poetry("Achen's spoken word"), AudienceWave()]
minutes_before = show.clock.remaining
acts_before = show.act_count
preview = show.preview_total(choices)

assert preview == StageTime(11)
assert show.preview_total([]) == StageTime(0)
assert show.clock.remaining == minutes_before
assert show.act_count == acts_before

print("StageTime addition:", repr(combined))
print("Mixed-choice preview:", preview)
print("Empty preview:", show.preview_total([]))
print("Show unchanged:", show.clock.remaining == minutes_before and show.act_count == acts_before)