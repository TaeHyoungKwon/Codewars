import unittest


def sum_arr(num_list):
    return sum(num_list)


def sum_arr_with_recursive(l, n):
    return n + sum_arr_with_recursive(l[:n], n - 1) if n > 0 else 0


def sum_arr_with_tail_recursive(array, i, acc):
    return sum_arr_with_tail_recursive(array, i - 1, array[i] + acc) if i > -1 else acc


def sum_arr_with_loop(num_list):
    acc = 0
    for i in reversed(range(len(num_list))):
        acc = num_list[i] + acc
    return acc


def sum_arr_with_while(num_list):
    i = len(num_list) - 1
    acc = 0
    while i > -1:
        acc = acc + num_list[i]
        i = i - 1
    return acc


class TestSumArr(unittest.TestCase):
    def test_sum_arr(self):
        self.assertEqual(sum_arr(num_list=[1, 2, 3, 4, 5]), 15)

    def test_sum_arr_with_loop(self):
        self.assertEqual(sum_arr_with_loop(num_list=[1, 2, 3, 4, 5]), 15)

    def test_sum_arr_with_recursive(self):
        self.assertEqual(sum_arr_with_recursive(l=[1, 2, 3, 4, 5], n=5), 15)

    def test_sum_arr_with_tail_recursive(self):
        l = [1, 2, 3, 4, 5]
        self.assertEqual(sum_arr_with_tail_recursive(array=l, i=len(l) - 1, acc=0), 15)

    def test_sum_arr_with_while(self):
        l = [1, 2, 3, 4, 5]
        self.assertEqual(sum_arr_with_while(num_list=l), 15)
