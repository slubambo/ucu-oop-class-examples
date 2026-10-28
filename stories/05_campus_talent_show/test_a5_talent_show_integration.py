import unittest

from fair_running_order import PerformerAct
from story import AudienceWave, Dance, TalentShow


class NegativeDuration:
    def duration(self):
        return -1


class TalentShowRunningOrderTests(unittest.TestCase):
    def test_plan_books_fair_order_and_respects_existing_booking(self):
        show = TalentShow("Joel", 11)
        show.book(AudienceWave())
        acts = [
            PerformerAct("P-101", Dance("River Crew", minutes=4)),
            PerformerAct("P-101", Dance("River Crew short", minutes=2)),
            PerformerAct("P-202", Dance("Skyline Crew", minutes=4)),
            PerformerAct("P-303", Dance("Hilltop Crew", minutes=1)),
        ]

        plan = show.plan_and_book(acts)

        self.assertEqual(
            [act.performer_id for act in plan.scheduled],
            ["P-101", "P-202", "P-101"],
        )
        self.assertEqual([act.performer_id for act in plan.skipped], ["P-303"])
        self.assertEqual(show.clock.remaining, 0)
        self.assertEqual(show.act_count, 4)

    def test_no_fitting_act_leaves_show_unchanged(self):
        show = TalentShow("Joel", 2)
        acts = [
            PerformerAct("P-101", Dance("River Crew", minutes=3)),
            PerformerAct("P-202", Dance("Skyline Crew", minutes=4)),
        ]

        plan = show.plan_and_book(acts)

        self.assertEqual(plan.scheduled, ())
        self.assertEqual(len(plan.skipped), 2)
        self.assertEqual(show.clock.remaining, 2)
        self.assertEqual(show.act_count, 0)

    def test_invalid_duration_leaves_existing_show_unchanged(self):
        show = TalentShow("Joel", 8)
        show.book(AudienceWave())
        lineup_before = list(show._lineup)
        minutes_before = show.clock.remaining

        with self.assertRaises(ValueError):
            show.plan_and_book(
                [PerformerAct("P-404", NegativeDuration())]
            )

        self.assertEqual(show._lineup, lineup_before)
        self.assertEqual(show.clock.remaining, minutes_before)
        self.assertEqual(show.act_count, 1)

    def test_empty_plan_does_not_change_show(self):
        show = TalentShow("Joel", 5)

        plan = show.plan_and_book([])

        self.assertEqual(plan.scheduled, ())
        self.assertEqual(plan.skipped, ())
        self.assertEqual(show.clock.remaining, 5)
        self.assertEqual(show.act_count, 0)


if __name__ == "__main__":
    unittest.main()