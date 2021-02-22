import unittest


def solve(a, b):
    def get_unique_string_by_string(first_string, second_string):
        return [char for char in first_string if char not in second_string]
    first = get_unique_string_by_string(a, b)
    second = get_unique_string_by_string(b, a)
    return ''.join(first + second)
    
    
class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(a="xyab", b="xzca"), 'ybzc')
