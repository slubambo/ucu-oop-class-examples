"""Demonstrate Extension 4: cancel the most recently booked act.

PR checks: the normal case restores minutes and reduces the lineup; the empty
case returns False without changing the clock or act count. Get review comments
from every group member before merging the pull request.
"""
from story import Dance, Poetry, TalentShow


# Book two acts into a 10-minute show; Poetry is the most recent booking.
show = TalentShow("Arnold", 10)
show.book(Dance("Mukono Movers"))
show.book(Poetry("Achen's spoken word"))

# Save the starting state so the demo can show what cancellation changed.
minutes_before_cancel = show.clock.remaining
acts_before_cancel = show.act_count
# Cancelling Poetry should return its 4 minutes and leave Dance booked.
expected_result = True
expected_minutes = 4
expected_acts = 1
actual_result = show.cancel_last()
print("Normal case:")
print(
	f"Expected: result={expected_result}, minutes={expected_minutes}, "
	f"acts={expected_acts}"
)
print(
	f"Actual:   result={actual_result}, minutes={show.clock.remaining}, "
	f"acts={show.act_count}"
)
print(
	f"Check: restored {show.clock.remaining - minutes_before_cancel} minutes; "
	f"removed {acts_before_cancel - show.act_count} act(s)."
)

# A separate, empty show checks that cancellation refuses without changing state.
empty_show = TalentShow("Arnold", 10)
expected_result = False
expected_minutes = empty_show.clock.remaining
expected_acts = empty_show.act_count
actual_result = empty_show.cancel_last()
print("\nEmpty case:")
print(
	f"Expected: result={expected_result}, minutes={expected_minutes}, "
	f"acts={expected_acts}"
)
print(
	f"Actual:   result={actual_result}, minutes={empty_show.clock.remaining}, "
	f"acts={empty_show.act_count}"
)

