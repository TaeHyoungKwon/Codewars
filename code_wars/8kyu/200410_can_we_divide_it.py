import unittest


def is_divide_by(number, a, b):
    def _check_divide_by_num(unknown_number):
        return number % unknown_number == 0
    return _check_divide_by_num(a) and _check_divide_by_num(b)
    
    
class TestIsDivideBy(unittest.TestCase):
    def test_should_return_true_when_a_and_b_is_able_to_be_divide_by_number(self):
        number, a, b = -12, 2, -6
        actual = is_divide_by(number, a, b)
        self.assertEqual(actual, True)

    def test_should_return_false_when_a_and_b_is_not_able_to_be_divide_by_number(self):
        number, a, b = -12, 5, 7
        actual = is_divide_by(number, a, b)
        self.assertEqual(actual, False)

    def test_should_return_false_when_one_of_a_and_b_is_not_able_to_be_divide_by_number(self):
        number, a, b = -12, 5, 3
        actual = is_divide_by(number, a, b)
        self.assertEqual(actual, False)
