import unittest

from story import Dance, Poetry, TalentShow


class TestDaphineRunningOrder(unittest.TestCase):
    def test_empty_show_running_order(self):
        show = TalentShow("Daphine", 10)

        self.assertEqual(
            show.running_order(),
            "No acts booked. Acts: 0. Minutes left: 10.",
        )

    def test_running_order_lists_booked_acts(self):
        show = TalentShow("Daphine", 10)
        first = Dance("Opening dancers", minutes=3)
        second = Poetry("Spoken word")

        show.book(first)
        show.book(second)

        self.assertEqual(show.act_count, 2)
        self.assertEqual(show.clock.remaining, 3)
        self.assertEqual(
            show.running_order(),
            "Running order: Opening dancers dance, Spoken word. "
            "Acts: 2. Minutes left: 3.",
        )


if __name__ == "__main__":
    unittest.main()