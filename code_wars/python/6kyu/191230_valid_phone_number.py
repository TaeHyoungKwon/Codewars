import unittest


def validPhoneNumber(phoneNumber):
    splited_phone_number = phoneNumber.split()
    return (len(splited_phone_number[0]) == 5 and
            len(splited_phone_number[1]) == 8 and
            splited_phone_number[0][0] == '(' and
            splited_phone_number[0][4] == ')' and
            splited_phone_number[1][3] == '-')


class TestValidPhoneNumber(unittest.TestCase):
    def test_should_false_when_given_phone_number_has_left_parenthesis_at_first_index(self):
        # Given: Set phoneNumbe(123) 456-7890r
        phoneNumber = "123) 456-7890"
        # When: Call validPhoneNumber
        actual = validPhoneNumber(phoneNumber)
        # Then: validPhoneNumber should return false
        self.assertEqual(actual, False)

    def test_should_false_when_given_phone_number_has_empty_space_is_two(self):
        # Given: Set phoneNumbe(123) 456-7890r
        phoneNumber = "(123) 456 7890"
        # When: Call validPhoneNumber
        actual = validPhoneNumber(phoneNumber)
        # Then: validPhoneNumber should return false
        self.assertEqual(actual, False)

    def test_should_false_when_given_phone_number_without_hyphen_and_not_proper_empty_space_position(self):
        # Given: Set phoneNumbe(123) 456-7890r
        phoneNumber = "(123)456 7890"
        # When: Call validPhoneNumber
        actual = validPhoneNumber(phoneNumber)
        # Then: validPhoneNumber should return false
        self.assertEqual(actual, False)

    def test_should_true_when_given_phone_number_with_three_length_of_first_part_and_second_element_has_hyphen(self):
        # Given: Set phoneNumbe(123) 456-7890r
        phoneNumber = "(123) 456-7890"
        # When: Call validPhoneNumber
        actual = validPhoneNumber(phoneNumber)
        # Then: validPhoneNumber should return false
        self.assertEqual(actual, True)

