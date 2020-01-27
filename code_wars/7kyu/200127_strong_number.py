import math
import unittest

STRONG_NUMBER = 'STRONG!!!!'
NOT_STRONG_NUMBER = 'Not Strong !!'


def strong_num(number):
    is_strong_num = sum(math.factorial(int(ele)) for ele in str(number)) == number
    return STRONG_NUMBER if is_strong_num else NOT_STRONG_NUMBER
    
    
class TestStrongNumber(unittest.TestCase):
    def test_should_return_strong_number_is_true_message_when_given_number_is_145(self):
        # 145 is strong number
        self.assertEqual(strong_num(145), STRONG_NUMBER)

    def test_should_return_strong_number_is_true_message_when_given_number_is_1(self):
        # 1 is strong number
        self.assertEqual(strong_num(1), STRONG_NUMBER)

    def test_should_return_strong_number_is_false_message_when_given_number_is_7(self):
        # 7 is not strong number
        self.assertEqual(strong_num(7), NOT_STRONG_NUMBER)


        