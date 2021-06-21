import unittest

# 1:21:54 초


def custom_sum(v):
    """1 ~ n 까지의"""
    accumulator = 0
    for i in range(1, v + 1):
        accumulator += i
    return accumulator


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(custom_sum(10), 55)


def custom_sum_recursive(v):
    return v + custom_sum_recursive(v - 1) if v > 1 else 1


class TestSolutionRecursive(unittest.TestCase):
    def test_custom_sum_recursive(self):
        self.assertEqual(custom_sum_recursive(10), 55)


def custom_sum_recursive_with_tail(v, acc=0):
    return custom_sum_recursive_with_tail(v - 1, acc + v) if v > 1 else v + acc


class TestSolutionRecursiveWithTail(unittest.TestCase):
    def test_custom_sum_recursive_with_tail(self):
        self.assertEqual(custom_sum_recursive_with_tail(10), 55)
