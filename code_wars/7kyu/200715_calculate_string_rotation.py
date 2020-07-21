import unittest
from collections import deque


def shifted_diff(first, second):
    if first == second:
        return 0

    temp = deque(first)
    cnt = 0
    for _ in first:
        cnt += 1
        temp.appendleft(temp.pop())
        if ''.join(temp) == second:
            return cnt
    return -1


class TestShiftedDiff(unittest.TestCase):
    def test_should_return_0_when_fist_and_second_are_same(self):
        first, second = "Msom", "Msom"
        actual = shifted_diff(first, second)
        self.assertEqual(actual, 0)

    def test_should_return_negative_one_when_second_is_invalid(self):
        first, second = "Msom", "msom"
        actual = shifted_diff(first, second)
        self.assertEqual(actual, -1)

    def test_shifted_diff(self):
        first, second = "eecoff", "coffee"
        actual = shifted_diff(first, second)
        self.assertEqual(actual, 4)
