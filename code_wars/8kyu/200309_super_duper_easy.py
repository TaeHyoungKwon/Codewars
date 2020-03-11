import unittest

ERROR_MSG = 'Error'


def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return ERROR_MSG
    
    
class TestProblem(unittest.TestCase):
    def test_should_return_error_text_when_given_a_is_str(self):
        self.assertEqual(problem("String"), ERROR_MSG)

    def test_should_return_56_when_given_a_is_1(self):
        self.assertEqual(problem(1), 56)
