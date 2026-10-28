import unittest

from fair_running_order import FairRunningOrderPlanner, PerformerAct


class SamplePerformance:
    def __init__(self, minutes):
        self.minutes = minutes

    def duration(self):
        return self.minutes


class FairRunningOrderTests(unittest.TestCase):
    def setUp(self):
        self.planner = FairRunningOrderPlanner()

    def make_act(self, performer_id, minutes):
        return PerformerAct(performer_id, SamplePerformance(minutes))

    def test_avoids_consecutive_performers_and_respects_available_time(self):
        acts = [
            self.make_act("P-101", 5),
            self.make_act("P-101", 4),
            self.make_act("P-202", 3),
            self.make_act("P-303", 4),
        ]

        plan = self.planner.plan(acts, 12)

        self.assertEqual(
            [act.performer_id for act in plan.scheduled],
            ["P-101", "P-202", "P-101"],
        )
        self.assertEqual([act.performer_id for act in plan.skipped], ["P-303"])
        self.assertEqual(plan.scheduled_minutes, 12)
        self.assertEqual(plan.remaining_minutes, 0)

    def test_submission_order_breaks_ties(self):
        acts = [
            self.make_act("P-101", 2),
            self.make_act("P-101", 2),
            self.make_act("P-202", 2),
            self.make_act("P-303", 2),
        ]

        plan = self.planner.plan(acts, 6)

        self.assertEqual(
            [act.performer_id for act in plan.scheduled],
            ["P-101", "P-202", "P-101"],
        )

    def test_repeats_performer_when_no_other_waiting_act_fits(self):
        acts = [
            self.make_act("P-101", 2),
            self.make_act("P-101", 2),
            self.make_act("P-202", 3),
        ]

        plan = self.planner.plan(acts, 4)

        self.assertEqual(
            [act.performer_id for act in plan.scheduled], ["P-101", "P-101"]
        )
        self.assertEqual([act.performer_id for act in plan.skipped], ["P-202"])

    def test_no_fitting_act_is_reported_as_skipped_without_mutating_input(self):
        acts = [self.make_act("P-101", 3), self.make_act("P-202", 4)]
        original_acts = list(acts)

        plan = self.planner.plan(acts, 2)

        self.assertEqual(plan.scheduled, ())
        self.assertEqual(plan.skipped, tuple(original_acts))
        self.assertEqual(plan.remaining_minutes, 2)
        self.assertEqual(acts, original_acts)

    def test_empty_list_and_zero_time_are_valid_boundary_cases(self):
        plan = self.planner.plan([], 0)

        self.assertEqual(plan.scheduled, ())
        self.assertEqual(plan.skipped, ())
        self.assertEqual(plan.remaining_minutes, 0)

    def test_invalid_time_and_duration_are_rejected(self):
        with self.assertRaises(ValueError):
            self.planner.plan([], -1)
        with self.assertRaises(TypeError):
            self.planner.plan([], True)
        with self.assertRaises(ValueError):
            self.planner.plan([self.make_act("P-101", 0)], 5)


if __name__ == "__main__":
    unittest.main()