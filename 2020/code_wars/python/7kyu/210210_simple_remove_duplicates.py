import unittest


def solve(arr):
    return [num for index, num in enumerate(arr) if arr[index + 1:].count(num) == 0]


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(arr=[3, 4, 4, 3, 6, 3]), [4, 6, 3])
