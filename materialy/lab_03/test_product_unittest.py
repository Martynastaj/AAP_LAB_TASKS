# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-1)

    def test_remove_stock_positive(self):
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_stock_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(11)

    def test_remove_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-1)

    def test_is_available_when_in_stock(self):
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        product = Product("Mysz", 99.99, 0)
        self.assertFalse(product.is_available())

    def test_total_value(self):
        self.assertEqual(self.product.total_value(), 29999.9)

    def test_constructor_negative_price_raises(self):
        with self.assertRaises(ValueError):
            Product("Laptop", -1, 10)

    def test_constructor_negative_quantity_raises(self):
        with self.assertRaises(ValueError):
            Product("Laptop", 1000, -1)

    def test_remove_all_stock(self):
        self.product.remove_stock(10)
        self.assertEqual(self.product.quantity, 0)
        self.assertFalse(self.product.is_available())


if __name__ == "__main__":
    unittest.main()
