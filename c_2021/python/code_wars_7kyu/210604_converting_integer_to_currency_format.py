import unittest


def to_currency(price):
    return f"{price:,}"


class TestToCurrency(unittest.TestCase):
    def test_to_currency(self):
        self.assertEqual(to_currency(price=123456), "123,456")
