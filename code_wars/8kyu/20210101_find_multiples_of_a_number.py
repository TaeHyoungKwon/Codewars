import unittest


def find_multiples(integer, limit):
    return [integer * index for index in range(1, limit // integer + 1)]


class TestFindMultiples(unittest.TestCase):
    def test_find_multiples(self):
        self.assertEqual(find_multiples(5, 25), [5, 10, 15, 20, 25])
