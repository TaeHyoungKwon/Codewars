import unittest


def check_even_number_when_digit_is_one(n):
    return len(str(n)) == 1 and n % 2 == 0


def is_very_even_number(n):
    digits = len(str(n))
    if digits > 1:
        while True:
            if digits == 1:
                break
            if digits > 1:
                n = sum(list(map(int, str(n))))
                digits = len(str(n))
    return check_even_number_when_digit_is_one(n)


class Test(unittest.TestCase):
    def test_should_return_true_when_given_n_is_one_digit_and_even_number(self):
        n = 0
        actual = is_very_even_number(n)
        self.assertEqual(actual, True)

    def test_should_return_false_when_given_n_is_one_digit_and_odd_number(self):
        n = 1
        actual = is_very_even_number(n)
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_n_is_22_that_is_more_than_two_digit(self):
        n = 22
        actual = is_very_even_number(n)
        self.assertEqual(actual, True)

    def test_should_return_false_when_given_n_is_4554_that_is_more_than_two_digit(self):
        n = 4554
        actual = is_very_even_number(n)
        self.assertEqual(actual, False)
        