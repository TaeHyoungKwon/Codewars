import unittest


def solution(st, limit):
    return f"{st[:limit]}..." if len(st) > limit else st
    
    
class TestSolution(unittest.TestCase):
    def test_limit_string_length_with_result_is_shorter_than_the_original(self):
        self.assertEqual(solution('Testing String', 3), 'Tes...')

    def test_limit_string_length_with_result_is_equal_longer_than_the_original(self):
        self.assertEqual(solution('Test', 8), 'Test')
