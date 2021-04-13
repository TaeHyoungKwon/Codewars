import unittest


def head(x):
    return x[0]


def tail(x):
    return x[1:]


def init(x):
    return x[:-1]


def last(x):
    return x[-1]


def solution(func, list_):
    return func(list_)


class TestSolution(unittest.TestCase):
    def test_solution_with_head(self):
        self.assertEqual(solution(head, [5, 1]), 5)

    def test_solution_with_tail(self):
        self.assertEqual(solution(tail, [1]), [])

    def test_solution_with_init(self):
        self.assertEqual(solution(init, [1, 5, 7, 9]), [1, 5, 7])

    def test_solution_with_last(self):
        self.assertEqual(solution(last, [7, 2]), 2)
