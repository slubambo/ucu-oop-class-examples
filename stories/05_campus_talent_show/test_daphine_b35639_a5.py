import unittest
from fair_planner import FairRunningOrder


class TestFairRunningOrder(unittest.TestCase):
    def test_normal_planning(self):
        planner = FairRunningOrder(10)
        acts = [("A1", "Dance", 3), ("B2", "Poetry", 4)]
        result = planner.plan(acts)
        self.assertEqual(len(result), 2)

    def test_fairness_rule_skips_back_to_back(self):
        planner = FairRunningOrder(10)
        # A1 is waiting, but A1 just performed. B2 should get the slot.
        acts = [("A1", "Dance 1", 2), ("A1", "Dance 2", 2), ("B2", "Poetry", 4)]
        result = planner.plan(acts)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[1]["performer"], "B2")

    def test_time_limit(self):
        planner = FairRunningOrder(5)
        acts = [("A1", "Dance", 3), ("B2", "Poetry", 4)]
        result = planner.plan(acts)
        self.assertEqual(len(result), 1)

    def test_empty_list(self):
        planner = FairRunningOrder(10)
        self.assertEqual(planner.plan([]), [])


if __name__ == "__main__":
    unittest.main()