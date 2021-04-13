import unittest


def solve(arr_):
    return [ele for ele in arr_ if ele * -1 not in arr_][0]


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(arr_=[1, -1, 2, -2, 3]), 3)

    def test_solve_common_case_2(self):
        self.assertEqual(solve(arr_=[-3, 1, 2, 3, -1, -4, -2]), -4)

    def test_solve_common_case_with_number_greater_than_others(self):
        self.assertEqual(solve(arr_=[-110, 110, -38, -38, -62, 62, -38, -38, -38]), -38)
