import unittest


def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))


class TestPipeFix(unittest.TestCase):
    def test_pipe_fix(self):
        self.assertEqual(pipe_fix([1, 2, 3, 5, 6, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
