import unittest
from unittest.mock import patch, Mock


def input_():
    return [int(ele) for ele in input().split()]


def solution():
    def reverse_(num):
        return str(num)[::-1]
    x, y = input_()
    return max(int(reverse_(x)), int(reverse_(y)))


if __name__ == '__main__':
    print(solution())


class TestSolution(unittest.TestCase):
    @patch('200503_2908.input_', Mock(return_value=[734, 893]))
    def test_solution(self):
        actual = solution()
        self.assertEqual(actual, 437)
