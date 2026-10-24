import unittest

from factory import create_choice
from story import TalentShow


class TestChoiceFactory(unittest.TestCase):
    def test_factory_creates_dance(self):
        dance = create_choice("dance", crew="Blair dancers", minutes=3)
        self.assertEqual(dance.duration(), 3)

    def test_factory_creates_poetry(self):
        poetry = create_choice("poetry", name="Blair's poem")
        self.assertEqual(poetry.name, "Blair's poem")
        self.assertEqual(poetry.duration(), 4)

    def test_factory_creates_audience_wave(self):
        wave = create_choice("audience_wave")
        self.assertEqual(wave.duration(), 1)

    def test_factory_choice_works_with_real_talent_show(self):
        dance = create_choice("dance", crew="Blair dancers", minutes=3)
        show = TalentShow("Blair", 3)

        result = show.book(dance)

        self.assertEqual(show.act_count, 1)
        self.assertEqual(show.clock.remaining, 0)
        self.assertIn("books Blair dancers dance", result)

    def test_refused_booking_keeps_state_unchanged(self):
        poetry = create_choice("poetry", name="Too long")
        show = TalentShow("Blair", 2)

        result = show.book(poetry)

        self.assertIn("No slot", result)
        self.assertEqual(show.act_count, 0)
        self.assertEqual(show.clock.remaining, 2)

    def test_unknown_key_raises_clear_error(self):
        with self.assertRaises(ValueError):
            create_choice("opera")

    def test_factory_creates_separate_instances(self):
        first = create_choice("dance", crew="First", minutes=3)
        second = create_choice("dance", crew="Second", minutes=5)

        self.assertIsNot(first, second)
        self.assertEqual(first.duration(), 3)
        self.assertEqual(second.duration(), 5)


if __name__ == "__main__":
    unittest.main()