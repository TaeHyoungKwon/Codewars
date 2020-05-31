import unittest
from collections import deque


def solution(args):
    deque_ = deque(args)
    temp_stack = []
    result = []

    def _generate_result_using_temp_stack():
        if len(temp_stack) == 1 or len(temp_stack) == 2:
            result.extend(temp_stack)
        else:
            result.append(f'{temp_stack[0]}-{temp_stack[-1]}')
        temp_stack.clear()

    while deque_:
        temp_stack.append(deque_.popleft())
        if not deque_:
            _generate_result_using_temp_stack()
        elif temp_stack[-1] + 1 != deque_[0]:
            _generate_result_using_temp_stack()
    return ','.join(map(str, result))


class TestSolution(unittest.TestCase):
    def test_solution(self):
        args = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
        actual = solution(args)
        self.assertEqual(actual, '-6,-3-1,3-5,7-11,14,15,17-20')
