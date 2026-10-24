import unittest

from story import Comedy, TalentShow


class TestBlairComedyDuo(unittest.TestCase):
    def test_comedy_duo_duration_is_two_minutes(self):
        comedy = Comedy("Blair and Lawrence")
        self.assertEqual(comedy.duration(), 2)

    def test_comedy_duo_can_fill_two_minute_show(self):
        comedy = Comedy("Blair and Lawrence")
        show = TalentShow("Blair", 2)

        result = show.book(comedy)

        self.assertEqual(result, "MC Blair books Blair and Lawrence.")
        self.assertEqual(show.act_count, 1)
        self.assertEqual(show.clock.remaining, 0)


if __name__ == "__main__":
    unittest.main()