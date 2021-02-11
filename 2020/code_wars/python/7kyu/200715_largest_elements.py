import unittest


def solve(s):
    lower_case = []
    upper_case = []
    for char in s:
        if char.isupper():
            upper_case.append(char)
        else:
            lower_case.append(char)
    return s.lower() if len(lower_case) >= len(upper_case) else s.upper()
    
    
class TestSolve(unittest.TestCase):
    def test_solve_should_return_lower_case_when_lowercase_count_is_greater_than_upper_case(self):
        s = 'coDe'
        actual = solve(s)
        self.assertEqual(actual, 'code')

    def test_solve_should_return_upper_case_when_lowercase_count_is_lower_than_upper_case(self):
        s = 'CODe'
        actual = solve(s)
        self.assertEqual(actual, 'CODE')

    def test_solve_should_return_lower_case_on_having_same_count_between_lower_case_and_upper_case(self):
        s = 'cODe'
        actual = solve(s)
        self.assertEqual(actual, 'code')
