import unittest


def solution(full_text, search_text):
    return full_text.count(search_text)
    
    
class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('abbc', 'bb'), 1)
