import unittest

from later_topics import LunchMoney
from story import LunchBreak, Rolex, Kikomando


class TestLunchMoney(unittest.TestCase):

    def test_display_and_representation(self):
        money = LunchMoney(3000)

        self.assertEqual(str(money), "UGX 3,000")
        self.assertEqual(repr(money), "LunchMoney(3000)")

    def test_equal_and_unequal_values(self):
        self.assertEqual(LunchMoney(3000), LunchMoney(3000))
        self.assertNotEqual(LunchMoney(3000), LunchMoney(2000))

    def test_addition_does_not_change_originals(self):
        first = LunchMoney(1000)
        second = LunchMoney(2000)

        result = first + second

        self.assertEqual(result, LunchMoney(3000))
        self.assertEqual(first.amount, 1000)
        self.assertEqual(second.amount, 2000)
        self.assertIsNot(result, first)

    def test_invalid_amounts_are_rejected(self):
        for value in [-1, 1.5, True]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    LunchMoney(value)

    def test_amount_is_read_only(self):
        money = LunchMoney(500)

        with self.assertRaises(AttributeError):
            money.amount = 1000

    def test_preview_does_not_spend_or_record_orders(self):
        lunch = LunchBreak("Sarah", 10000)
        balance = lunch.wallet.balance
        order_count = lunch.order_count

        result = lunch.preview_total([Rolex(), Kikomando()])

        self.assertIsInstance(result, LunchMoney)
        self.assertGreaterEqual(result.amount, 0)
        self.assertEqual(lunch.wallet.balance, balance)
        self.assertEqual(lunch.order_count, order_count)

    def test_empty_preview_returns_zero(self):
        lunch = LunchBreak("Sarah", 10000)

        self.assertEqual(lunch.preview_total([]), LunchMoney(0))


if __name__ == "__main__":
    unittest.main()
    