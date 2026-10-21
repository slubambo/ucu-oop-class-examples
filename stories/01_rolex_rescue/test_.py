import unittest

from story import LunchBreak, Rolex, Kikomando, HomePackedLunch, Juice
from LatertopicsA2 import (
    StrictLunchBreak, LunchChoiceError, LunchRequestError,
    LunchResourceError
)

class NegativeQuote:
    name = "Negative quote"

    def price(self):
        return -10


class FractionalQuote:
    name = "Fractional quote"

    def price(self):
        return 10.5

class TestA2StrictErrors(unittest.TestCase):
    def assert_failure_unchanged(self, choice, error_type, balance=1000):
        lunch = LunchBreak("Joel", balance)
        service = StrictLunchBreak(lunch)
        before_balance, before_count = lunch.wallet.balance, lunch.order_count
        with self.assertRaises(error_type):
            service.safe_buy(choice)
        self.assertEqual(lunch.wallet.balance, before_balance)
        self.assertEqual(lunch.order_count, before_count)

    def test_missing_choice_refused_without_state_change(self):
        self.assert_failure_unchanged(None, LunchChoiceError)

    def test_negative_quote_refused_without_state_change(self):
        self.assert_failure_unchanged(NegativeQuote(), LunchRequestError)

    def test_fractional_quote_refused_without_state_change(self):
        self.assert_failure_unchanged(FractionalQuote(), LunchRequestError)

    def test_insufficient_money_refused_without_state_change(self):
        self.assert_failure_unchanged(Rolex(eggs=2), LunchResourceError)

    def test_affordable_choice_succeeds(self):
        lunch = LunchBreak("Sarah", 3500)
        result = StrictLunchBreak(lunch).safe_buy(Kikomando("Kikomando"))
        self.assertIn("Sarah gets Kikomando", result)
        self.assertEqual(lunch.wallet.balance, 1000)
        self.assertEqual(lunch.order_count, 1)

    def test_zero_cost_home_packed_lunch_is_valid(self):
        lunch = LunchBreak("Sarah", 0)
        result = StrictLunchBreak(lunch).safe_buy(HomePackedLunch())
        self.assertIn("Lunch is saved", result)
        self.assertEqual(lunch.wallet.balance, 0)
        self.assertEqual(lunch.order_count, 1)
   
if __name__ == "__main__":
    unittest.main()