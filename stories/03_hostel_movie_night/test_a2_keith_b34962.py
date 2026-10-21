import unittest

from story import (
    MusicSession,
    MovieNight,
    StorytellingCircle,
    StreamedMovie,
)
from strict_movie import (
    MovieChoiceError,
    MovieRequestError,
    MovieResourceError,
    StrictMovieNight,
)


class BadChoice:
    title = "Bad choice"

    def data_cost(self):
        return -5


class ZeroCostChoice:
    title = "Zero-cost choice"

    def data_cost(self):
        return 0


class StrictMovieNightTests(unittest.TestCase):
    def test_none_raises_choice_error_without_changing_state(self):
        night = StrictMovieNight("Faith", 500)

        with self.assertRaises(MovieChoiceError):
            night.safe_enjoy(None)

        self.assertEqual(night.bundle.remaining, 500)
        self.assertEqual(night.activities, 0)

    def test_negative_requirement_raises_request_error_without_changing_state(self):
        night = StrictMovieNight("Faith", 500)

        with self.assertRaises(MovieRequestError):
            night.safe_enjoy(BadChoice())

        self.assertEqual(night.bundle.remaining, 500)
        self.assertEqual(night.activities, 0)

    def test_insufficient_resource_raises_without_changing_state(self):
        night = StrictMovieNight("Faith", 500)

        with self.assertRaises(MovieResourceError):
            night.safe_enjoy(StreamedMovie("Big movie"))

        self.assertEqual(night.bundle.remaining, 500)
        self.assertEqual(night.activities, 0)
        self.assertIsNone(night.entertainment)

    def test_valid_music_session_succeeds(self):
        night = StrictMovieNight("Faith", 500)

        night.safe_enjoy(MusicSession("Beats"))

        self.assertEqual(night.bundle.remaining, 400)
        self.assertEqual(night.activities, 1)

    def test_exact_fit_succeeds(self):
        night = StrictMovieNight("Faith", 100)

        night.safe_enjoy(MusicSession("Beats"))

        self.assertEqual(night.bundle.remaining, 0)
        self.assertEqual(night.activities, 1)

    def test_zero_cost_choice_is_valid(self):
        night = StrictMovieNight("Faith", 500)

        night.safe_enjoy(StorytellingCircle())

        self.assertEqual(night.bundle.remaining, 500)
        self.assertEqual(night.activities, 1)

    def test_plain_movie_night_behavior_is_unchanged(self):
        night = MovieNight("Faith", 500)

        message = night.enjoy(StreamedMovie("Big movie"))

        self.assertIn("needs too much data", message)
        self.assertEqual(night.bundle.remaining, 500)
        self.assertEqual(night.activities, 0)


if __name__ == "__main__":
    unittest.main()
