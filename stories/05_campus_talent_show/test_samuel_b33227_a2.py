"""Automated A2 checks for strict talent-show booking."""

import sys
import unittest
from pathlib import Path


STORY_DIRECTORY = Path(__file__).resolve().parent
sys.path.insert(0, str(STORY_DIRECTORY))

from story import (  # noqa: E402
    Comedy,
    Poetry,
    ShowChoiceError,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
    TalentShow,
)


class NegativeDurationAct:
    """Fake act used to test an invalid negative duration."""

    name = "Negative duration act"

    def duration(self):
        return -1


class TestStrictTalentShow(unittest.TestCase):
    """Tests for the strict A2 booking path."""

    @staticmethod
    def snapshot(show):
        """Capture the state that failed bookings must preserve."""
        return (
            show.clock.remaining,
            show.act_count,
            tuple(act.name for act in show._lineup),
        )

    def test_valid_booking_succeeds_and_updates_state(self):
        show = StrictTalentShow("Samuel", 6)

        result = show.safe_book(Poetry("Samuel's poetry"))

        self.assertEqual(result, "MC Samuel books Samuel's poetry.")
        self.assertEqual(show.clock.remaining, 2)
        self.assertEqual(show.act_count, 1)
        self.assertEqual(
            [act.name for act in show._lineup],
            ["Samuel's poetry"],
        )

    def test_exact_fit_booking_succeeds(self):
        show = StrictTalentShow("Samuel", 6)
        show.safe_book(Poetry("Samuel's poetry"))

        result = show.safe_book(Comedy("Samuel's comedy"))

        self.assertEqual(result, "MC Samuel books Samuel's comedy.")
        self.assertEqual(show.clock.remaining, 0)
        self.assertEqual(show.act_count, 2)

    def test_insufficient_time_raises_and_preserves_state(self):
        show = StrictTalentShow("Samuel", 6)
        show.safe_book(Poetry("Samuel's poetry"))
        show.safe_book(Comedy("Samuel's comedy"))
        before = self.snapshot(show)

        with self.assertRaises(ShowResourceError):
            show.safe_book(Comedy("Another comedy"))

        self.assertEqual(self.snapshot(show), before)

    def test_none_choice_raises_and_preserves_state(self):
        show = StrictTalentShow("Samuel", 6)
        before = self.snapshot(show)

        with self.assertRaises(ShowChoiceError):
            show.safe_book(None)

        self.assertEqual(self.snapshot(show), before)

    def test_negative_duration_raises_and_preserves_state(self):
        show = StrictTalentShow("Samuel", 6)
        before = self.snapshot(show)

        with self.assertRaises(ShowRequestError):
            show.safe_book(NegativeDurationAct())

        self.assertEqual(self.snapshot(show), before)

    def test_original_book_behavior_still_works(self):
        show = TalentShow("Samuel", 4)

        result = show.book(Poetry("Samuel's poetry"))

        self.assertEqual(result, "MC Samuel books Samuel's poetry.")
        self.assertEqual(show.clock.remaining, 0)
        self.assertEqual(show.act_count, 1)


if __name__ == "__main__":
    unittest.main()