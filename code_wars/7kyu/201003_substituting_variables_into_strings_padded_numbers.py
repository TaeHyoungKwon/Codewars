import unittest

FORMATTED_STRING = 'Value is {:05d}'


def solution(value):
    return FORMATTED_STRING.format(value)
    
    
class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(value=0), 'Value is 00000')
