import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_fractional_weight_rates(self):
        for weight, local, regional in [(0.1, 5.15, 8.15), (1.234, 6.85, 9.85)]:
            with self.subTest(weight=weight, zone="local"):
                self.assertEqual(shipping_quote(weight, "local"), local)
            with self.subTest(weight=weight, zone="regional"):
                self.assertEqual(shipping_quote(weight, "regional"), regional)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
