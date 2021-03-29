import unittest

DEFAULT_PRICE = 100


def sale_hotdogs(n):
    if n < 5:
        return n * DEFAULT_PRICE
    elif 5 <= n < 10:
        return n * DEFAULT_PRICE * 0.95
    return n * DEFAULT_PRICE * 0.9
    
    
class TestSaleHotDogs(unittest.TestCase):
    def test_sale_hotdogs_should_return_0_when_given_n_is_0(self):
        n = 0
        actual = sale_hotdogs(n)
        self.assertEqual(actual, 0)

    def test_sale_hotdogs_with_n_is_less_than_5(self):
        n = 4
        actual = sale_hotdogs(n)
        self.assertEqual(actual, 400)

    def test_sale_hotdogs_with_n_is_less_than_10_and_equal_more_than_5(self):
        n = 5
        actual = sale_hotdogs(n)
        self.assertEqual(actual, 475)

    def test_sale_hotdogs_with_n_is_equal_more_than_10(self):
        n = 10
        actual = sale_hotdogs(n)
        self.assertEqual(actual, 900)
