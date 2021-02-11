import unittest


def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


class TestSumDigits(unittest.TestCase):
    def test_sum_digits_when_number_is_positive(self):
        number = 10
        actual = sum_digits(number)
        self.assertEqual(actual, 1)

    def test_sum_digits_when_number_is_negative(self):
        number = -32
        actual = sum_digits(number)
        self.assertEqual(actual, 5)
