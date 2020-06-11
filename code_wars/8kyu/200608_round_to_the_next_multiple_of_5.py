import unittest


def round_to_next5(n):
    if n % 5 == 0:
        return n

    last_digit = int(str(n)[-1])
    result = n

    if n > 0:
        if n > 5:
            result = 10 - last_digit + n
        else:
            result = 5 - last_digit + n
    else:
        if n < -5:
            result = -5 + last_digit + n
        else:
            result = 0 + last_digit + n
    return result


class TestRoundToNext5(unittest.TestCase):
    def test_should_return_0_when_given_n_is_0(self):
        n = 0
        actual = round_to_next5(n)
        self.assertEqual(actual, 0)

    def test_multiple_of_5_with_positive_n(self):
        n = 5
        actual = round_to_next5(n)
        self.assertEqual(actual, 5)

    def test_multiple_of_5_with_negative_n(self):
        n = -10
        actual = round_to_next5(n)
        self.assertEqual(actual, -10)

    def test_no_multiple_of_5_with_positive_n(self):
        n = 6
        actual = round_to_next5(n)
        self.assertEqual(actual, 10)

    def test_no_multiple_of_5_with_positive_n_is_less_than_5(self):
        n = 3
        actual = round_to_next5(n)
        self.assertEqual(actual, 5)

    def test_no_multiple_of_5_with_negative_n(self):
        n = -7
        actual = round_to_next5(n)
        self.assertEqual(actual, -5)

    def test_no_multiple_of_5_with_positive_n_is_less_than_negative_5(self):
        n = -1
        actual = round_to_next5(n)
        self.assertEqual(actual, 0)
