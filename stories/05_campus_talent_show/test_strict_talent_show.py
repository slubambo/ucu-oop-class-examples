import unittest

from story import (
    Dance,
    ShowChoiceError,
    ShowRequestError,
    ShowResourceError,
    StrictTalentShow,
)


class NegativeRequirement:
    name = "Impossible encore"

    def duration(self):
        return -1


class StrictTalentShowTests(unittest.TestCase):
    def assert_failed_without_booking(self, show, error, choice):
        remaining = show.clock.remaining
        successful_bookings = show.act_count

        with self.assertRaises(error):
            show.safe_book(choice)

        self.assertEqual(show.clock.remaining, remaining)
        self.assertEqual(show.act_count, successful_bookings)

    def test_missing_choice_raises_choice_error_without_booking(self):
        show = StrictTalentShow("Joel", 5)

        self.assert_failed_without_booking(show, ShowChoiceError, None)

    def test_negative_requirement_raises_request_error_without_booking(self):
        show = StrictTalentShow("Joel", 5)

        self.assert_failed_without_booking(
            show, ShowRequestError, NegativeRequirement()
        )

    def test_unaffordable_choice_raises_resource_error_without_booking(self):
        show = StrictTalentShow("Joel", 5)

        self.assert_failed_without_booking(show, ShowResourceError, Dance("Movers"))

    def test_valid_choice_books_and_spends_minutes(self):
        show = StrictTalentShow("Joel", 7)

        result = show.safe_book(Dance("Movers"))

        self.assertEqual(result, "MC Joel books Movers dance.")
        self.assertEqual(show.clock.remaining, 1)
        self.assertEqual(show.act_count, 1)

    def test_zero_cost_choice_is_not_treated_as_missing(self):
        class ZeroMinuteChoice:
            name = "Silent pose"

            def duration(self):
                return 0

        show = StrictTalentShow("Joel", 5)

        result = show.safe_book(ZeroMinuteChoice())

        self.assertEqual(result, "MC Joel books Silent pose.")
        self.assertEqual(show.clock.remaining, 5)
        self.assertEqual(show.act_count, 1)


if __name__ == "__main__":
    unittest.main()
