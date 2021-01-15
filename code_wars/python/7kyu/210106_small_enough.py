import unittest


def small_enough(array, limit):
    return all(ele <= limit for ele in array)


class TestSmallEnough(unittest.TestCase):
    def test_small_enough(self):
        self.assertTrue(small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
