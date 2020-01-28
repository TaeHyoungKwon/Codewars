import unittest

BALANCED = 'Balanced'
NOT_BALANCED = 'Not Balanced'


def is_balanced(number):
    length_of_number = len(str(number))
    middle = length_of_number // 2

    if length_of_number <= 2:
        return BALANCED
    if length_of_number % 2 == 1:
        return sum(map(int, str(number)[:middle + 1])) == sum(map(int, str(number)[middle:]))
    else:
        return sum(map(int, str(number)[:middle - 1])) == sum(map(int, str(number)[middle + 1:]))


def check_balanced_num(number):
    return BALANCED if is_balanced(number) else NOT_BALANCED


def balanced_num(number):
    return check_balanced_num(number)
    
    
class TestBalancedNum(unittest.TestCase):
    def test_balanced_number_not_balanced_case_when_given_number_digit_is_odd(self):
        self.assertEqual(balanced_num(92645), 'Not Balanced')

    def test_balanced_number_balanced_case_when_given_number_digit_is_odd(self):
        self.assertEqual(balanced_num(12621), 'Balanced')

    def test_balanced_number_not_balanced_case_when_given_number_digit_is_even(self):
        self.assertEqual(balanced_num(133012), 'Not Balanced')

    def test_balanced_number_balanced_case_when_given_number_digit_is_even(self):
        self.assertEqual(balanced_num(123012), 'Balanced')

    def test_balanced_number_balanced_case_two_when_given_number_digit_is_even(self):
        self.assertEqual(balanced_num(13), 'Balanced')

    def test_balanced_number_balanced_case_three_when_given_number_digit_is_even_and_large_number(self):
        self.assertEqual(balanced_num(56239814), 'Balanced')
