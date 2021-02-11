import unittest


def no_odds(values):
    return [ele for ele in values if ele % 2 == 0]
    
    
class TestNoOdds(unittest.TestCase):
    def test_should_empty_list_when_given_values_is_empty_list(self):
        values = []
        actual = no_odds(values)
        self.assertEqual(actual, [])

    def test_no_odds_with_all_of_negative_num(self):
        values = [-1, -3, -5, -7, -9]
        actual = no_odds(values)
        self.assertEqual(actual, [])

    def test_no_odds(self):
        values = [0, 1, 2, 3]
        actual = no_odds(values)
        self.assertEqual(actual, [0, 2])
