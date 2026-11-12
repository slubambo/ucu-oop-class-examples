import unittest

from stage_time import StageTime


class StageTimeTests(unittest.TestCase):
    def test_equal_and_unequal_values(self):
        self.assertEqual(StageTime(3000), StageTime(3000))
        self.assertNotEqual(StageTime(3000), StageTime(4))

    def test_string_and_repr_are_distinct(self):
        duration = StageTime(3000)

        self.assertEqual(str(duration), "3,000 minutes")
        self.assertEqual(repr(duration), "StageTime(3000)")
        self.assertNotEqual(str(duration), repr(duration))

    def test_addition_returns_new_value_without_changing_operands(self):
        first = StageTime(12)
        second = StageTime(8)

        total = first + second

        self.assertEqual(total, StageTime(20))
        self.assertIsNot(total, first)
        self.assertIsNot(total, second)
        self.assertEqual(first.amount, 12)
        self.assertEqual(second.amount, 8)

    def test_zero_is_valid_and_amount_is_read_only(self):
        duration = StageTime(0)

        self.assertEqual(duration.amount, 0)
        with self.assertRaises(AttributeError):
            duration.amount = 2

    def test_negative_fraction_and_boolean_are_rejected(self):
        with self.assertRaises(ValueError):
            StageTime(-1)
        with self.assertRaises(TypeError):
            StageTime(1.5)
        with self.assertRaises(TypeError):
            StageTime(True)

    def test_unsupported_operands_return_not_implemented(self):
        duration = StageTime(3)

        self.assertIs(StageTime.__eq__(duration, 3), NotImplemented)
        self.assertIs(StageTime.__add__(duration, 3), NotImplemented)


if __name__ == "__main__":
    unittest.main()