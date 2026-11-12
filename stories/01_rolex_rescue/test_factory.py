import unittest

from story import LunchBreak, create_choice


class ChoiceFactoryTests(unittest.TestCase):
    def test_rolex_created_by_factory_is_bought_through_coordinator(self):
        lunch_break = LunchBreak("Sarah", 5000)
        rolex = create_choice("rolex")

        result = lunch_break.buy(rolex)

        self.assertIn("Sarah gets Rolex", result)
        self.assertEqual(lunch_break.wallet.balance, 2000)
        self.assertEqual(lunch_break.order_count, 1)
        self.assertIn("Rolex", lunch_break.receipt())

    def test_kikomando_created_by_factory_is_bought_through_coordinator(self):
        lunch_break = LunchBreak("Joel", 3000)

        result = lunch_break.buy(create_choice("kikomando"))

        self.assertIn("Joel gets Kikomando", result)
        self.assertEqual(lunch_break.wallet.balance, 500)
        self.assertEqual(lunch_break.order_count, 1)

    def test_home_packed_lunch_is_free_but_is_recorded_as_an_order(self):
        lunch_break = LunchBreak("Amina", 1200)

        result = lunch_break.buy(create_choice("home_packed_lunch"))

        self.assertIn("Amina gets Home-packed lunch", result)
        self.assertEqual(lunch_break.wallet.balance, 1200)
        self.assertEqual(lunch_break.order_count, 1)

    def test_refused_purchase_changes_neither_balance_nor_order_count(self):
        lunch_break = LunchBreak("Eric", 2500)
        too_expensive = create_choice("rolex", eggs=3)
        before = (lunch_break.wallet.balance, lunch_break.order_count)

        result = lunch_break.buy(too_expensive)

        self.assertIn("over budget", result)
        self.assertEqual((lunch_break.wallet.balance, lunch_break.order_count), before)
        self.assertEqual(lunch_break.receipt(),
                         "Receipt for Eric: 0 order(s) (nothing yet); balance left UGX 2,500.")

    def test_unknown_key_raises_clear_error(self):
        with self.assertRaisesRegex(ValueError, "Unknown choice key 'pizza'"):
            create_choice("pizza")

    def test_rolex_eggs_setting_changes_price_used_by_real_caller(self):
        lunch_break = LunchBreak("Nadia", 2000)
        rolex = create_choice("rolex", eggs=1)

        result = lunch_break.buy(rolex)

        self.assertIn("Nadia gets Rolex", result)
        self.assertEqual(lunch_break.wallet.balance, 0)
        self.assertEqual(lunch_break.order_count, 1)

    def test_each_coordinator_keeps_separate_wallet_and_order_state(self):
        first = LunchBreak("First", 5000)
        second = LunchBreak("Second", 3000)

        second.buy(create_choice("kikomando"))

        self.assertEqual(first.wallet.balance, 5000)
        self.assertEqual(first.order_count, 0)
        self.assertEqual(second.wallet.balance, 500)
        self.assertEqual(second.order_count, 1)

    def test_choices_are_separate_instances(self):
        first = create_choice("rolex", eggs=1)
        second = create_choice("rolex", eggs=3)

        self.assertEqual(first.price(), 2000)
        self.assertEqual(second.price(), 4000)
        self.assertNotEqual(first, second)


if __name__ == "__main__":
    unittest.main()