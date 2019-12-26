import unittest


def fillable(stock, merch, n):
    return False if not stock.get(merch) else n <= stock[merch]


class TestThinkFul(unittest.TestCase):
    def test_should_return_false_when_given_n_is_bigger_than_stock(self):
        # Given: Set stock, merch, and n
        stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5,
        }
        merch = 'leggos'
        n = 2

        # When: Call fillable
        actual = fillable(stock, merch, n)

        # Then: fillable should return False
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_n_is_less_than_stock(self):
        # Given: Set stock, merch, and n
        stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5,
        }
        merch = 'football'
        n = 3

        # When: Call fillable
        actual = fillable(stock, merch, n)

        # Then: fillable should return False
        self.assertEqual(actual, True)

    def test_should_return_false_when_merch_is_not_belong_to_key_of_stock(self):
        # Given: Set stock, invalid merch, and n
        stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5,
        }
        merch = 'not_belong_to_key_of_stock'
        n = 3

        # When: Call fillable
        actual = fillable(stock, merch, n)

        # Then: fillable should return False
        self.assertEqual(actual, False)