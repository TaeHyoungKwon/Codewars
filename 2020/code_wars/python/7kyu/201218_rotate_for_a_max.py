import unittest
from collections import deque


def max_rot(n):
    result = [n]
    temp = []
    list_n = list(str(n))
    queue_ = deque(list_n)

    for i in range(len(list_n) - 1):
        queue_.append(queue_.popleft())
        result.append(''.join(temp + list(queue_)))
        temp.append(queue_.popleft())
    return max(map(int, result))


class TestMaxRot(unittest.TestCase):
    def test_max_rot(self):
        self.assertEqual(max_rot(56789), 68957)
