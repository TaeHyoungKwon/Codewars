import unittest


def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]


class TestNthSmallest(unittest.TestCase):
    def test_nth_smallest(self):
        self.assertEqual(nth_smallest(arr=[3, 1, 2], pos=2), 2)
