import unittest


class Solution(object):
    def __init__(self):
        self.hello_world = "Hello World!"

    def main(self):
        return self.hello_world


class TestSolution(unittest.TestCase):
    def test_main_should_return_none_with_print_hello_world(self):
        solution = Solution()
        self.assertEqual(solution.main(), "Hello World!")
