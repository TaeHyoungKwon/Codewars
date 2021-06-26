from itertools import chain, groupby
import unittest


def solve(arr):
    def count_in_arr(num):
        return arr.count(num)

    return list(
        chain.from_iterable(
            sorted(g) for _, g in groupby(sorted(arr, key=count_in_arr, reverse=True), key=count_in_arr)
        )
    )


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(arr=[5, 9, 6, 9, 6, 5, 9, 9, 4, 4]), [9, 9, 9, 9, 4, 4, 5, 5, 6, 6])

    def test_solve_case_2(self):
        self.assertEqual(solve(arr=[2, 3, 5, 3, 7, 9, 5, 3, 7]), [3, 3, 3, 5, 5, 7, 7, 2, 9])
