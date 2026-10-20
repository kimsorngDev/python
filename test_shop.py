import unittest
from io import StringIO
import sys

from models.product import Product
from models.food import Food
from models.electronics import Electronics
from models.shop import Shop
from exceptions import OutOfStockError, ProductNotFoundError, ProductAlreadyExistsError, InvalidQuantityError


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Generic Item", "P001", 50.0, 10)

    def test_init_and_get_quantity(self):
        self.assertEqual(self.product.name, "Generic Item")
        self.assertEqual(self.product.product_id, "P001")
        self.assertEqual(self.product.price, 50.0)
        self.assertEqual(self.product.get_quantity(), 10)
        self.assertEqual(self.product.get__quantity(), 10)

    def test_restock_success(self):
        self.product.restock(5)
        self.assertEqual(self.product.get_quantity(), 15)

    def test_restock_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.product.restock(0)
        with self.assertRaises(ValueError):
            self.product.restock(-5)

    def test_sell_success(self):
        self.product.sell(4)
        self.assertEqual(self.product.get_quantity(), 6)

    def test_sell_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.product.sell(0)
        with self.assertRaises(ValueError):
            self.product.sell(-2)

    def test_sell_out_of_stock(self):
        with self.assertRaises(Exception):
            self.product.sell(11)

    def test_get_total_price(self):
        total = self.product.get_total_price(3)
        self.assertEqual(total, 150.0)

    def test_display_info(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.product.display_info()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Generic Item", output)
        self.assertIn("P001", output)
        self.assertIn("50", output)
        self.assertIn("10", output)


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Apple", "F001", 10.0, 20, "2026-12-31")

    def test_food_attributes(self):
        self.assertEqual(self.food.name, "Apple")
        self.assertEqual(self.food.expiry_date, "2026-12-31")
        self.assertEqual(self.food.get_quantity(), 20)

    def test_food_total_price_calculation(self):
        # Base: 10.0 * 2 = 20.0, with 10% fee: 20.0 + 2.0 = 22.0
        total = self.food.get_total_price(2)
        self.assertAlmostEqual(total, 22.0, places=2)

    def test_food_display_info(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.food.display_info()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Expiry date: 2026-12-31", output)


class TestElectronics(unittest.TestCase):
    def setUp(self):
        self.electronics = Electronics("Headphones", "E001", 100.0, 5, 24)

    def test_electronics_attributes(self):
        self.assertEqual(self.electronics.name, "Headphones")
        self.assertEqual(self.electronics.warranty_months, 24)
        self.assertEqual(self.electronics.get_quantity(), 5)

    def test_electronics_total_price_calculation(self):
        # Base: 100.0 * 2 = 200.0, with 5% fee: 200.0 * 1.05 = 210.0
        total = self.electronics.get_total_price(2)
        self.assertAlmostEqual(total, 210.0, places=2)

    def test_electronics_display_info(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.electronics.display_info()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Warranty months: 24", output)


class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()
        self.food = Food("Bread", "F01", 5.0, 15, "2026-10-30")
        self.electronics = Electronics("Mouse", "E01", 20.0, 3, 12)

    def test_add_and_find_product(self):
        self.shop.add_product(self.food)
        found = self.shop.find_product("F01")
        self.assertEqual(found, self.food)

    def test_add_duplicate_product_raises(self):
        self.shop.add_product(self.food)
        with self.assertRaises(ValueError):
            self.shop.add_product(self.food)

    def test_remove_product(self):
        self.shop.add_product(self.food)
        self.shop.remove_product("F01")
        self.assertIsNone(self.shop.find_product("F01"))

    def test_remove_nonexistent_product_raises(self):
        with self.assertRaises(ValueError):
            self.shop.remove_product("NONEXISTENT")

    def test_sell_product_and_sales_history(self):
        self.shop.add_product(self.food)
        # 5.0 * 2 = 10.0 + 10% = 11.0
        total_price = self.shop.sell_product("F01", 2)
        self.assertAlmostEqual(total_price, 11.0, places=2)
        self.assertEqual(self.food.get_quantity(), 13)
        self.assertEqual(len(self.shop.sales_history), 1)
        self.assertAlmostEqual(self.shop.total_sales(), 11.0, places=2)

    def test_sell_product_not_found(self):
        with self.assertRaises(ValueError):
            self.shop.sell_product("INVALID", 1)

    def test_get_low_stock(self):
        self.shop.add_product(self.food)         # quantity 15
        self.shop.add_product(self.electronics)  # quantity 3

        low_stock = self.shop.get_low_stock(5)
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0].product_id, "E01")

        all_products = self.shop.get_low_stock(20)
        self.assertEqual(len(all_products), 2)


if __name__ == "__main__":
    unittest.main()
