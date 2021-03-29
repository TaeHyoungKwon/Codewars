import datetime
import unittest

FRIDAY = 5


def unlucky_days(year: int) -> int:
    return sum(datetime.date(year, month, 13).isoweekday() == FRIDAY for month in range(1, 13))


class TestUnluckyDays(unittest.TestCase):
    def test_unlucky_days(self):
        self.assertEqual(unlucky_days(2015), 3)
        self.assertEqual(unlucky_days(1986), 1)
