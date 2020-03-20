import unittest
from collections import deque


def is_keith_number(n):
    queue = deque()
    initial_list = [int(ele) for ele in str(n)]
    queue.extend(initial_list)

    result = sum(initial_list)
    cnt = 1

    if len(str(n)) == 1:
        return False

    while result <= n:
        queue.append(result)
        if result == n:
            return cnt
        cnt += 1
        result = result * 2 - queue.popleft()

    return False


class TestKeithNumber(unittest.TestCase):
    def test_should_return_3_when_given_n_is_14(self):
        n = 14
        actual = is_keith_number(n)
        self.assertEqual(actual, 3)

    def test_should_return_false_when_sum_of_n_is_less_than_10(self):
        n = 4
        actual = is_keith_number(n)
        self.assertEqual(actual, False)