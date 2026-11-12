import unittest

from factory import create_choice
from story import AudienceWave, Dance, Poetry, TalentShow


class FactoryAndTalentShowTests(unittest.TestCase):
    def test_factory_creates_dance_with_settings(self):
        choice = create_choice("dance", crew="Apex", minutes=5)

        self.assertIsInstance(choice, Dance)
        self.assertEqual(choice.name, "Apex dance")
        self.assertEqual(choice.duration(), 5)

    def test_factory_creates_poetry(self):
        choice = create_choice("poetry", name="Mirembe's poem")

        self.assertIsInstance(choice, Poetry)
        self.assertEqual(choice.duration(), 4)
        self.assertIn("Mirembe's poem", choice.describe())

    def test_factory_creates_audience_wave_without_settings(self):
        choice = create_choice("audience_wave")

        self.assertIsInstance(choice, AudienceWave)
        self.assertEqual(choice.duration(), 1)

    def test_factory_choice_works_through_real_caller(self):
        show = TalentShow("Joel", 5)
        choice = create_choice("dance", crew="Apex", minutes=3)

        result = show.book(choice)

        self.assertIn("books Apex dance", result)
        self.assertEqual(show.clock.remaining, 2)
        self.assertEqual(show.act_count, 1)

    def test_refused_booking_preserves_state(self):
        show = TalentShow("Joel", 2)
        choice = create_choice("dance", crew="Apex", minutes=3)

        result = show.book(choice)

        self.assertIn("No slot", result)
        self.assertEqual(show.clock.remaining, 2)
        self.assertEqual(show.act_count, 0)

    def test_unknown_factory_key_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown choice key"):
            create_choice("fireworks")

    def test_separate_shows_keep_independent_state(self):
        first_show = TalentShow("Joel", 4)
        second_show = TalentShow("Faith", 4)
        choice = create_choice("poetry", name="Achen's poem")

        first_show.book(choice)

        self.assertEqual(first_show.clock.remaining, 0)
        self.assertEqual(second_show.clock.remaining, 4)
        self.assertEqual(first_show.act_count, 1)
        self.assertEqual(second_show.act_count, 0)


if __name__ == "__main__":
    unittest.main()
