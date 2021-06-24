import unittest


def sum_arr(l):
    return sum(l)


def sum_arr_with_recursive(l, n):
    return n + sum_arr_with_recursive(l[:n], n - 1) if n > 0 else 0

def test_sum_arr_with_tail_recursive(l, n):
    return


class TestSumArr(unittest.TestCase):
    def test_sum_arr(self):
        self.assertEqual(sum_arr(l=[1, 2, 3, 4, 5]), 15)

    def test_sum_arr_with_recursive(self):
        self.assertEqual(sum_arr_with_recursive(l=[1, 2, 3, 4, 5], n=5), 15)

    def test_sum_arr_with_tail_recursive(self):
        self.assertEqual(test_sum_arr_with_tail_recursive(l=[1, 2, 3, 4, 5], n=5), 15)
