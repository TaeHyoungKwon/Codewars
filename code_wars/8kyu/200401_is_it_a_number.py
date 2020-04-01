import unittest


def isDigit(string):
    string_without_empty_space = string.replace(' ', '')
    if string_without_empty_space.isdigit() and len(string_without_empty_space) > 1:
        return False
    try:
        if isinstance(float(string_without_empty_space), float):
            return True
    except ValueError:
        pass
    return len(string_without_empty_space) == 1
    
    
class TestIsDigit(unittest.TestCase):
    def test_should_return_false_when_given_string_is_mixed_between_numeric_and_string(self):
        string = "s2324"
        actual = isDigit(string)
        self.assertEqual(actual, False)

    def test_should_return_false_when_given_string_is_not_single_digit(self):
        string = "2324"
        actual = isDigit(string)
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_string_is_float(self):
        string = "-232.4"
        actual = isDigit(string)
        self.assertEqual(actual, True)

    def test_should_return_True_when_given_string_is_single_digit(self):
        string = "2"
        actual = isDigit(string)
        self.assertEqual(actual, True)
