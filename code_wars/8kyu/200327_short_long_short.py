import unittest


def solution(a, b):
    short = min([a, b], key=len)
    long = max([a, b], key=len)
    return '{}{}{}'.format(short, long, short)
    
    
class TestSolution(unittest.TestCase):
    def test_solution(self):
        a, b = '45', '1'
        actual = solution(a, b)
        self.assertEqual(actual, '1451')
