import unittest


def count_letters_and_digits(s):
    return sum(ele.isalnum() for ele in s)
    
    
class TestCountLettersAndDigits(unittest.TestCase):

    @staticmethod
    def _set_s_and_call_count_letters_and_digits(s):
        return count_letters_and_digits(s)

    def test_should_return_0_given_s_is_empty_space(self):
        actual = self._set_s_and_call_count_letters_and_digits('')
        self.assertEqual(actual, 0)

    def test_should_return_3_given_s_is_only_alphabet_that_is_abc(self):
        actual = self._set_s_and_call_count_letters_and_digits('abc')
        self.assertEqual(actual, 3)

    def test_should_return_3_given_s_is_only_num_that_is_123(self):
        actual = self._set_s_and_call_count_letters_and_digits('123')
        self.assertEqual(actual, 3)

    def test_s_is_only_alphanumeric(self):
        actual = self._set_s_and_call_count_letters_and_digits('!@#$')
        self.assertEqual(actual, 0)

    def test_given_s_is_mixed_num_alphabet_and_non_alphanumeric(self):
        actual = self._set_s_and_call_count_letters_and_digits('!@#$1a')
        self.assertEqual(actual, 2)

        