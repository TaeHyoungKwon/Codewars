import unittest


def next_id(arr):
    for i in range(len(arr) + 1):
        if i not in arr:
            return i


class TestNextId(unittest.TestCase):
    def test_next_id(self):
        self.assertEqual(next_id(arr=[]), 0)
        self.assertEqual(next_id(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
        self.assertEqual(next_id(arr=[5, 4, 3, 2, 1]), 0)
        self.assertEqual(next_id(arr=[0, 1, 2, 3, 5]), 4)
        self.assertEqual(next_id(arr=[0, 0, 0, 0, 0, 0]), 1)
        self.assertEqual(next_id(arr=[0, 0, 1, 1, 2, 2]), 3)
