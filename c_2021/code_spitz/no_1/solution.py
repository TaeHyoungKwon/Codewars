import unittest


def sum_arr(num_list):
    return sum(num_list)


def sum_arr_with_loop(num_list):
    acc = 0
    for i in range(1, len(num_list) + 1):
        acc += i
    return acc


def sum_arr_with_recursive(l, n):
    return n + sum_arr_with_recursive(l[:n], n - 1) if n > 0 else 0


def sum_arr_with_recursive(l):
    if len(l) == 0:
        return 0
    return sum_arr_with_recursive() if len(l) > 0 else 0



def sum_arr_with_tail_recursive(l, n, acc=0):
    return sum_arr_with_tail_recursive(l[:n], n - 1, acc + n) if n > 0 else acc + n


class TestSumArr(unittest.TestCase):
    def test_sum_arr(self):
        self.assertEqual(sum_arr(num_list=[1, 2, 3, 4, 5]), 15)

    def test_sum_arr_with_loop(self):
        self.assertEqual(sum_arr_with_loop(num_list=[1, 2, 3, 4, 5]), 15)

    def test_sum_arr_with_recursive(self):
        self.assertEqual(sum_arr_with_recursive(l=[1, 2, 3, 4, 5]), 15)

    def test_sum_arr_with_tail_recursive(self):
        self.assertEqual(sum_arr_with_tail_recursive(l=[1, 2, 3, 4, 5], n=5), 15)
