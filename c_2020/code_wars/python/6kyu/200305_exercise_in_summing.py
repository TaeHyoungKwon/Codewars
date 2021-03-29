import unittest


def minimum_sum(values, n):
    return sum(sorted(values)[:n])


def maximum_sum(values, n):
    return sum(sorted(values, reverse=True)[:n])
    
    
class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [5, 4, 3, 2, 1]

    def test_max_sum(self):
        actual = maximum_sum(self.values, 3)
        self.assertEqual(actual, 12)

    def test_min_sum(self):
        actual = minimum_sum(self.values, 2)
        self.assertEqual(actual, 3)
