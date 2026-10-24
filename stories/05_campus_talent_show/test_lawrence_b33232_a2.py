import unittest

from story import (
    ShowChoiceError,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
)


class FixedChoice:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    def duration(self):
        return self.minutes


class TestLawrenceA2Exceptions(unittest.TestCase):
    def test_missing_choice_raises_show_choice_error_without_changing_state(self):
        show = StrictTalentShow("Lawrence", 10)

        with self.assertRaises(ShowChoiceError):
            show.safe_book(None)

        self.assertEqual(show.clock.remaining, 10)
        self.assertEqual(show.act_count, 0)

    def test_negative_duration_raises_show_request_error(self):
        show = StrictTalentShow("Lawrence", 10)
        invalid_choice = FixedChoice("Negative act", -2)

        with self.assertRaises(ShowRequestError):
            show.safe_book(invalid_choice)

        self.assertEqual(show.clock.remaining, 10)
        self.assertEqual(show.act_count, 0)

    def test_too_long_choice_raises_show_resource_error(self):
        show = StrictTalentShow("Lawrence", 3)
        long_choice = FixedChoice("Too long", 4)

        with self.assertRaises(ShowResourceError):
            show.safe_book(long_choice)

        self.assertEqual(show.clock.remaining, 3)
        self.assertEqual(show.act_count, 0)

    def test_valid_choice_succeeds_and_updates_state(self):
        show = StrictTalentShow("Lawrence", 5)
        choice = FixedChoice("Lawrence's act", 2)

        result = show.safe_book(choice)

        self.assertIn("Lawrence's act", result)
        self.assertEqual(show.clock.remaining, 3)
        self.assertEqual(show.act_count, 1)

    def test_failed_booking_does_not_change_state_after_success(self):
        show = StrictTalentShow("Lawrence", 5)
        valid_choice = FixedChoice("Opening act", 2)
        long_choice = FixedChoice("Later act", 10)

        show.safe_book(valid_choice)
        minutes_before = show.clock.remaining
        acts_before = show.act_count

        with self.assertRaises(ShowResourceError):
            show.safe_book(long_choice)

        self.assertEqual(show.clock.remaining, minutes_before)
        self.assertEqual(show.act_count, acts_before)

    def test_choice_without_name_raises_show_choice_error(self):
        show = StrictTalentShow("Lawrence", 10)

        class NamelessChoice:
            def duration(self):
                return 2

        with self.assertRaises(ShowChoiceError):
            show.safe_book(NamelessChoice())

        self.assertEqual(show.clock.remaining, 10)
        self.assertEqual(show.act_count, 0)


if __name__ == "__main__":
    unittest.main()