import unittest

from story import (
    ShowChoiceError,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
    TalentShow,
)


class FixedDurationChoice:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    def duration(self):
        return self.minutes


class StrictTalentShowTests(unittest.TestCase):
    def setUp(self):
        self.show = StrictTalentShow("Test MC", 2)

    def assert_booking_state(self, minutes, act_count):
        self.assertEqual(self.show.clock.remaining, minutes)
        self.assertEqual(self.show.act_count, act_count)

    def test_missing_choice_raises_without_mutation(self):
        before = (self.show.clock.remaining, self.show.act_count)
        self.assertEqual(before, (2, 0))

        with self.assertRaises(ShowChoiceError):
            self.show.safe_book(None)

        self.assertEqual((self.show.clock.remaining, self.show.act_count), before)

    def test_negative_duration_raises_without_mutation(self):
        choice = FixedDurationChoice("negative act", -1)
        before = (self.show.clock.remaining, self.show.act_count)
        self.assertEqual(before, (2, 0))

        with self.assertRaises(ShowRequestError):
            self.show.safe_book(choice)

        self.assertEqual((self.show.clock.remaining, self.show.act_count), before)

    def test_unaffordable_choice_raises_without_mutation(self):
        choice = FixedDurationChoice("too-long act", 3)
        before = (self.show.clock.remaining, self.show.act_count)
        self.assertEqual(before, (2, 0))

        with self.assertRaises(ShowResourceError):
            self.show.safe_book(choice)

        self.assertEqual((self.show.clock.remaining, self.show.act_count), before)

    def test_affordable_choice_books_and_spends_time(self):
        choice = FixedDurationChoice("one-minute act", 1)

        result = self.show.safe_book(choice)

        self.assertEqual(result, "MC Test MC books one-minute act.")
        self.assert_booking_state(1, 1)

    def test_zero_duration_choice_is_valid_and_recorded(self):
        choice = FixedDurationChoice("zero-minute act", 0)

        result = self.show.safe_book(choice)

        self.assertEqual(result, "MC Test MC books zero-minute act.")
        self.assert_booking_state(2, 1)

    def test_baseline_zero_duration_behavior_remains_unchanged(self):
        show = TalentShow("Baseline MC", 2)
        choice = FixedDurationChoice("zero-minute act", 0)

        result = show.book(choice)

        self.assertEqual(
            result,
            "No slot for zero-minute act. The timetable has entered the chat.",
        )
        self.assertEqual(show.clock.remaining, 2)
        self.assertEqual(show.act_count, 0)


if __name__ == "__main__":
    unittest.main()
