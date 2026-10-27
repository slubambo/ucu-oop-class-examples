import unittest

from stories.rolex_rescue.story import LunchMoney


class LunchMoneyTests(unittest.TestCase):
    def test_equal_and_unequal_amounts(self):
        self.assertEqual(LunchMoney(3000), LunchMoney(3000))
        self.assertNotEqual(LunchMoney(3000), LunchMoney(2000))

    def test_display_and_developer_representation(self):
        money = LunchMoney(3000)
        self.assertEqual(str(money), "UGX 3,000")
        self.assertEqual(repr(money), "LunchMoney(3000)")

    def test_addition_returns_new_total_without_changing_inputs(self):
        first = LunchMoney(1200)
        second = LunchMoney(800)

        total = first + second

        self.assertEqual(total, LunchMoney(2000))
        self.assertIsNot(total, first)
        self.assertEqual(first.amount, 1200)
        self.assertEqual(second.amount, 800)

    def test_zero_is_allowed_and_amount_is_read_only(self):
        money = LunchMoney(0)
        self.assertEqual(money.amount, 0)

        with self.assertRaises(AttributeError):
            money.amount = 10

    def test_invalid_amounts_are_refused(self):
        for invalid_amount in (-1, 1.5, True):
            with self.subTest(amount=invalid_amount):
                with self.assertRaises(ValueError):
                    LunchMoney(invalid_amount)


if __name__ == "__main__":
    unittest.main()