import unittest


def take(arr, n):
    return arr[:n]


class TestTake(unittest.TestCase):
    def test_take(self):
        self.assertEqual(take([0, 1, 2, 3, 4, 5, 8, 13], 3), [0, 1, 2])
