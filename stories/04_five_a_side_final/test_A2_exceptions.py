
import unittest

from story import (
    Match,
    StrictMatch,
    Dribble,
    TeamPass,
    WaterBreak,
    MatchChoiceError,
    MatchRequestError,
    MatchResourceError,
)


class NegativeEffortChoice:
    """Test action that requests an invalid amount of energy."""

    name = "Invalid action"

    def effort(self):
        return -10


class TestStrictMatch(unittest.TestCase):

    def setUp(self):
        self.match = StrictMatch("Brian", 15)

    def test_none_choice_raises_choice_error(self):
        with self.assertRaises(MatchChoiceError):
            self.match.safe_play(None)

        self.assertEqual(self.match.energy.remaining, 15)
        self.assertEqual(self.match.completed_actions, 0)
        self.assertIsNone(self.match.action)

    def test_missing_effort_method_raises_choice_error(self):
        with self.assertRaises(MatchChoiceError):
            self.match.safe_play(object())

        self.assertEqual(self.match.energy.remaining, 15)
        self.assertEqual(self.match.completed_actions, 0)

    def test_negative_effort_raises_request_error(self):
        with self.assertRaises(MatchRequestError):
            self.match.safe_play(NegativeEffortChoice())

        self.assertEqual(self.match.energy.remaining, 15)
        self.assertEqual(self.match.completed_actions, 0)
        self.assertIsNone(self.match.action)

    def test_insufficient_energy_raises_resource_error(self):
        with self.assertRaises(MatchResourceError):
            self.match.safe_play(Dribble("Brian"))

        self.assertEqual(self.match.energy.remaining, 15)
        self.assertEqual(self.match.completed_actions, 0)
        self.assertIsNone(self.match.action)

    def test_valid_action_succeeds(self):
        result = self.match.safe_play(TeamPass("Quick team pass"))

        self.assertIn("Done!", result)
        self.assertEqual(self.match.energy.remaining, 5)
        self.assertEqual(self.match.completed_actions, 1)

    def test_zero_effort_action_succeeds(self):
        result = self.match.safe_play(WaterBreak())

        self.assertIn("Done!", result)
        self.assertEqual(self.match.energy.remaining, 15)
        self.assertEqual(self.match.completed_actions, 1)

    def test_failure_preserves_previous_match_state(self):
        previous_action = WaterBreak()
        self.match.safe_play(previous_action)

        energy_before = self.match.energy.remaining
        actions_before = self.match.completed_actions

        with self.assertRaises(MatchResourceError):
            self.match.safe_play(Dribble("Brian"))

        self.assertEqual(self.match.energy.remaining, energy_before)
        self.assertEqual(self.match.completed_actions, actions_before)
        self.assertIs(self.match.action, previous_action)


if __name__ == "__main__":
    unittest.main()
