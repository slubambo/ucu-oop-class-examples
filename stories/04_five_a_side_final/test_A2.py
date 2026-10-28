
import unittest

from story import (
    StrictMatch,
    Dribble,
    TeamPass,
    InvalidEnergyError,
    InvalidEffortError,
    InsufficientEnergyError,
)


class TestA2Exceptions(unittest.TestCase):

    def test_invalid_energy(self):
        with self.assertRaises(InvalidEnergyError):
            StrictMatch("Brian", 120)

    def test_energy_unchanged_after_invalid_assignment(self):
        match = StrictMatch("Brian", 50)

        with self.assertRaises(InvalidEnergyError):
            match.energy.remaining = 120

        self.assertEqual(match.energy.remaining, 50)

    def test_insufficient_energy(self):
        match = StrictMatch("Brian", 15)

        with self.assertRaises(InsufficientEnergyError):
            match.play(Dribble("Brian"))

        self.assertEqual(match.energy.remaining, 15)
        self.assertEqual(match.completed_actions, 0)
        self.assertIsNone(match.action)

    def test_successful_attack(self):
        match = StrictMatch("Brian", 15)

        result = match.play(TeamPass("Team pass"))

        self.assertIn("Done!", result)
        self.assertEqual(match.energy.remaining, 5)
        self.assertEqual(match.completed_actions, 1)

    def test_negative_effort(self):
        class BadAttack:
            name = "Bad attack"

            def effort(self):
                return -5

        match = StrictMatch("Brian", 50)

        with self.assertRaises(InvalidEffortError):
            match.play(BadAttack())

        self.assertEqual(match.energy.remaining, 50)
        self.assertEqual(match.completed_actions, 0)
        self.assertIsNone(match.action)


if __name__ == "__main__":
    unittest.main()
