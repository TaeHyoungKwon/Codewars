import unittest
from itertools import groupby, zip_longest


def sum_consecutives(s):
    result = []
    temp = 0
    for first, second in zip_longest(s, s[1:]):
        if first == second:
            temp += first
        else:
            result.append(temp + first)
            temp = 0
    return result


# def sum_consecutives(s):
#     return [sum(grp) for _, grp in groupby(s)]


class TestSumConsecutives(unittest.TestCase):
    def test_sum_consecutives_case_1(self):
        self.assertEqual(sum_consecutives([3, 3, 3, 3, 1]), [12, 1])

    def test_sum_consecutives_case_2(self):
        self.assertEqual(sum_consecutives([1, 1, 7, 7, 3]), [2, 14, 3])

    def test_sum_consecutives_edge_case(self):
        self.assertEqual(sum_consecutives([0, 1, 1, 2, 2]), [0, 2, 4])

    def test_sum_consecutives_edge_case_2(self):
        self.assertEqual(sum_consecutives([-5, -5, 7, 7, 12, 0]), [-10, 14, 12, 0])
