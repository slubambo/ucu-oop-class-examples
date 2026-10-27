import unittest

from story import (
    DataAmount,
    MovieNight,
    MovieResourceError,
    StrictMovieNight,
    StorytellingCircle,
    StreamedMovie,
    MusicSession,
    create_choice,
)


# Later-topic contribution — Brian Joshua:
# A4 unittest coverage for factory behavior, callers and state changes.
class LaterTopicTests(unittest.TestCase):
    def test_data_amount_addition_does_not_change_operands(self):
        left = DataAmount(100)
        right = DataAmount(50)
        self.assertEqual(left + right, DataAmount(150))
        self.assertEqual(left.amount, 100)
        self.assertEqual(right.amount, 50)

    def test_preview_total_does_not_change_movie_night(self):
        night = MovieNight("Test", 500)
        choices = [StreamedMovie("Movie", 200), MusicSession("Music")]
        self.assertEqual(night.preview_total(choices), DataAmount(300))
        self.assertEqual(night.bundle.remaining, 500)
        self.assertEqual(night.activities, 0)

    def test_strict_movie_night_refuses_expensive_choice_without_state_change(self):
        night = StrictMovieNight("Test", 100)
        with self.assertRaises(MovieResourceError):
            night.safe_enjoy(StreamedMovie("Large", 200))
        self.assertEqual(night.bundle.remaining, 100)
        self.assertEqual(night.activities, 0)

    def test_factory_creates_movie_for_real_caller(self):
        night = MovieNight("Test", 300)
        movie = create_choice("movie", title="Factory movie", megabytes=200)
        self.assertIn("Factory movie", night.enjoy(movie))
        self.assertEqual(night.bundle.remaining, 100)

    def test_factory_creates_music_for_real_caller(self):
        night = MovieNight("Test", 100)
        music = create_choice("music", title="Factory music")
        self.assertIn("Factory music", night.enjoy(music))
        self.assertEqual(night.activities, 1)

    def test_factory_creates_offline_story_for_real_caller(self):
        night = MovieNight("Test", 0)
        story = create_choice("story")
        self.assertIn("Hostel storytelling circle", night.enjoy(story))
        self.assertEqual(night.activities, 1)

    def test_factory_rejects_unknown_key(self):
        with self.assertRaises(ValueError):
            create_choice("unknown")

    def test_factory_instances_have_independent_settings(self):
        first = create_choice("movie", title="First", megabytes=100)
        second = create_choice("movie", title="Second", megabytes=200)
        self.assertNotEqual(first.title, second.title)
        self.assertNotEqual(first.data_cost(), second.data_cost())


if __name__ == "__main__":
    unittest.main()
