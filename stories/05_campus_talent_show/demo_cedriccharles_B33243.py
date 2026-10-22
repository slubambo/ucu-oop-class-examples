"""Demo for the Campus Talent Show running-order extension."""
from story import Dance, Poetry, TalentShow


def check_running_order(label, show, expected):
    # Snapshot state to verify the report is read-only.
    resource_before = show.clock.remaining
    history_before = tuple(show._lineup)

    actual = show.running_order()
    resource_unchanged = show.clock.remaining == resource_before
    history_unchanged = tuple(show._lineup) == history_before

    print(label)
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("Expected resource/history unchanged: True")
    print(f"Actual resource unchanged: {resource_unchanged}")
    print(f"Actual history unchanged: {history_unchanged}")

    assert actual == expected
    assert resource_unchanged
    assert history_unchanged


# Two acts make the booking order visible in the report.
booked_show = TalentShow("Cedric", 12)
booked_show.book(Dance("Mukono Movers"))
booked_show.book(Poetry("Achen's spoken word"))
check_running_order(
    "Normal case: two booked acts",
    booked_show,
    {
        "names": ["Mukono Movers dance", "Achen's spoken word"],
        "count": 2,
        "minutes_left": 2,
        "message": None,
    },
)

# A separate show checks the empty-lineup response.
empty_show = TalentShow("Cedric", 8)
check_running_order(
    "Empty case: no acts booked",
    empty_show,
    {
        "names": [],
        "count": 0,
        "minutes_left": 8,
        "message": "No acts booked.",
    },
)
