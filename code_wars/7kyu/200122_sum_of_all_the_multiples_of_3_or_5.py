import unittest


def find(n):
    multiple_of_3 = list(range(3, n + 1, 3))
    multiple_of_5 = list(range(5, n + 1, 5))
    return sum(set(multiple_of_3 + multiple_of_5))
    
    
class TestFind(unittest.TestCase):
    def test_should_return_8_when_given_n_is_5(self):
        n = 5
        result = find(n)
        self.assertEqual(result, 8)

    def test_should_return_33_when_given_n_is_10(self):
        n = 10
        result = find(n)
        self.assertEqual(result, 33)

    def test_should_return_2418_when_given_n_is_100(self):
        n = 100
        result = find(n)
        self.assertEqual(result, 2418)
        