import unittest


def isLeapYear(year):
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True
    return False


class TestIsLeapYear(unittest.TestCase):
    def test_should_return_true_when_year_is_divisible_by_4(self):
        year = 1984
        actual = isLeapYear(year)
        self.assertEqual(actual, True)

    def test_should_return_false_when_year_is_divisible_by_4_and_divisible_by_100(self):
        year = 1100
        actual = isLeapYear(year)
        self.assertEqual(actual, False)

    def test_should_return_true_when_year_is_2000(self):
        year = 2000
        actual = isLeapYear(year)
        self.assertEqual(actual, True)

    def test_should_return_false_when_year_is_1234(self):
        year = 1234
        actual = isLeapYear(year)
        self.assertEqual(actual, False)

