import unittest
from unittest.mock import patch, Mock

LESS_THAN_SYMBOL = "<"
GREATER_THAN_SYMBOL = ">"
EQUAL_SYMBOL = "=="


def input_():
    return [int(ele) for ele in input().split()]


def solution():
    x, y = input_()

    if x < y:
        return LESS_THAN_SYMBOL
    elif x > y:
        return GREATER_THAN_SYMBOL
    else:
        return EQUAL_SYMBOL


if __name__ == "__main__":
    print(solution())


class TestSolution(unittest.TestCase):
    @patch("200503_backjoon_test.input_", Mock(return_value=[1, 2]))
    def test_return_less_than_symbol_when_left_is_less_than_right(self):
        self.assertEqual(solution(), LESS_THAN_SYMBOL)

    @patch("200503_backjoon_test.input_", Mock(return_value=[10, 2]))
    def test_return_greater_than_symbol_when_left_is_greater_than_right(self):
        self.assertEqual(solution(), GREATER_THAN_SYMBOL)

    @patch("200503_backjoon_test.input_", Mock(return_value=[5, 5]))
    def test_return_equal_symbol_when_left_and_greater_is_equal(self):
        self.assertEqual(solution(), EQUAL_SYMBOL)
