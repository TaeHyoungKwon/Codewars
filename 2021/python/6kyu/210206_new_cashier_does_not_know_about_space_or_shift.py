import unittest

MENU_ITEMS = (
    "Burger",
    "Fries",
    "Chicken",
    "Pizza",
    "Sandwich",
    "Onionrings",
    "Milkshake",
    "Coke",
)


def get_order(order):
    return ' '.join(item for item in MENU_ITEMS for _ in range(order.count(item.lower())))


class TestGetOrder(unittest.TestCase):
    def test_get_order(self):
        order = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
        actual = get_order(order)
        self.assertEqual(actual, "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke")
