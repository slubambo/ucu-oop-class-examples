import unittest

from choice_factory import create_choice
from story import TalentShow


class ChoiceFactoryTests(unittest.TestCase):
    def test_factory_dance_books_through_talent_show(self):
        show = TalentShow("Joel", 8)
        dance = create_choice("dance", crew="Mukono Movers", minutes=6)

        result = show.book(dance)

        self.assertEqual(result, "MC Joel books Mukono Movers dance.")
        self.assertEqual(show.clock.remaining, 2)
        self.assertEqual(show.act_count, 1)

    def test_factory_poetry_books_through_talent_show(self):
        show = TalentShow("Joel", 4)
        poetry = create_choice("poetry", name="Achen's spoken word")

        result = show.book(poetry)

        self.assertEqual(result, "MC Joel books Achen's spoken word.")
        self.assertEqual(show.clock.remaining, 0)
        self.assertEqual(show.act_count, 1)

    def test_factory_audience_wave_works_by_shared_interface(self):
        show = TalentShow("Joel", 1)
        wave = create_choice("audience_wave")

        result = show.book(wave)

        self.assertEqual(result, "MC Joel books Audience wave.")
        self.assertEqual(show.clock.remaining, 0)
        self.assertEqual(show.act_count, 1)

    def test_refused_factory_choice_does_not_change_show_state(self):
        show = TalentShow("Joel", 5)
        dance = create_choice("dance", crew="Mukono Movers", minutes=6)

        result = show.book(dance)

        self.assertIn("No slot", result)
        self.assertEqual(show.clock.remaining, 5)
        self.assertEqual(show.act_count, 0)

    def test_unknown_key_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, "Unknown choice key"):
            create_choice("karaoke")

    def test_shows_have_independent_clock_and_booking_state(self):
        first = TalentShow("Joel", 8)
        second = TalentShow("Faith", 4)
        first.book(create_choice("dance", crew="Mukono Movers", minutes=6))

        self.assertEqual(first.clock.remaining, 2)
        self.assertEqual(first.act_count, 1)
        self.assertEqual(second.clock.remaining, 4)
        self.assertEqual(second.act_count, 0)

    def test_dance_requires_crew_setting(self):
        with self.assertRaisesRegex(TypeError, "requires the 'crew' setting"):
            create_choice("dance")

    def test_factory_rejects_unexpected_settings(self):
        with self.assertRaisesRegex(TypeError, "Unexpected dance setting"):
            create_choice("dance", crew="Mukono Movers", venue="Main Hall")


if __name__ == "__main__":
    unittest.main()
