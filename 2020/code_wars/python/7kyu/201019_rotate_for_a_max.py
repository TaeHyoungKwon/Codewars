import unittest
from collections import deque


def max_rot(number):
    # WIP 아직 푸는 중
    deque_ = deque(list(str(number)))
    max_value = number
    for _ in range(len(deque_)):
        deque_.append(deque_.popleft())
        if int(''.join(map(str, deque_))) > max_value:
            max_value = int(''.join(map(str, deque_)))
    return max_value


class TestMaxRot(unittest.TestCase):
    def test_max_rot(self):
        self.assertEqual(max_rot(number=1234), 4321)
