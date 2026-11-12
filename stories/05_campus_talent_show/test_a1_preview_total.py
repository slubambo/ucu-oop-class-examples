import unittest

from stage_time import StageTime
from story import AudienceWave, Dance, Poetry, TalentShow


class PreviewTotalTests(unittest.TestCase):
    def test_preview_sums_different_choice_types_without_changing_show(self):
        show = TalentShow("Joel", 15)
        show.book(AudienceWave())
        remaining_before = show.clock.remaining
        count_before = show.act_count
        lineup_before = list(show._lineup)

        choices = [
            Dance("Apex", minutes=6),
            Poetry("Mirembe's poem"),
            AudienceWave(),
        ]

        self.assertEqual(show.preview_total(choices), StageTime(11))
        self.assertEqual(show.clock.remaining, remaining_before)
        self.assertEqual(show.act_count, count_before)
        self.assertEqual(show._lineup, lineup_before)

    def test_empty_preview_returns_zero_without_changing_show(self):
        show = TalentShow("Joel", 15)

        total = show.preview_total([])

        self.assertEqual(total, StageTime(0))
        self.assertEqual(show.clock.remaining, 15)
        self.assertEqual(show.act_count, 0)

    def test_invalid_duration_is_refused_without_changing_show(self):
        class NegativeDurationChoice:
            def duration(self):
                return -1

        show = TalentShow("Joel", 15)

        with self.assertRaises(ValueError):
            show.preview_total([NegativeDurationChoice()])

        self.assertEqual(show.clock.remaining, 15)
        self.assertEqual(show.act_count, 0)


if __name__ == "__main__":
    unittest.main()