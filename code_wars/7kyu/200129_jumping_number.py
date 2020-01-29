import unittest

'''
Jumping number is the number that All adjacent digits in it differ by 1.

ex)
1 2 3 4 5  - True
8 9 8 7  - True
9 8 - True
7 9 - False
'''

JUMPING_NUMBER_MSG = 'Jumping!!'
NO_JUMPING_NUMBER_MSG = 'Not!!'


def is_jumping_number(number, idx):
    return abs(int(str(number)[idx]) - int(str(number)[idx - 1])) == 1


def jumping_number(number):
    number_digit = len(str(number))
    idx = number_digit - 1

    for _ in str(number)[::-1]:
        if idx == 0:
            return JUMPING_NUMBER_MSG
        if not is_jumping_number(number, idx):
            return NO_JUMPING_NUMBER_MSG
        idx -= 1

    
class TestJumpingNumber(unittest.TestCase):
    def test_should_return_jumping_message_when_number_digit_count_is_one(self):
        self.assertEqual(jumping_number(1), JUMPING_NUMBER_MSG)

    def test_should_return_jumping_message_when_number_digit_count_is_two_and_number_is_23(self):
        self.assertEqual(jumping_number(23), JUMPING_NUMBER_MSG)

    def test_should_return_not_message_when_number_digit_count_is_two_and_number_is_25(self):
        self.assertEqual(jumping_number(25), NO_JUMPING_NUMBER_MSG)

    def test_should_return_jumping_message_when_number_digit_count_is_more_than_two_and_number_is_8987(self):
        self.assertEqual(jumping_number(8987), JUMPING_NUMBER_MSG)

    def test_should_return_not_message_when_number_digit_count_is_more_than_two_and_number_is_8981(self):
        self.assertEqual(jumping_number(8981), NO_JUMPING_NUMBER_MSG)
        