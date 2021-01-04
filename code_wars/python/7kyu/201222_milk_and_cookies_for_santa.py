import unittest
from datetime import date


def time_for_milk_and_cookies(dt):
    return dt.month == 12 and dt.day == 24
    
    
class TestTimeForMilkAndCookies(unittest.TestCase):
    def test_time_for_milk_and_cookies_should_true_when_date_is_christmas_eve(self):
        self.assertTrue(time_for_milk_and_cookies(date(2013, 12, 24)))

    def test_time_for_milk_and_cookies_should_false_when_date_is_not_christmas_eve(self):
        self.assertFalse(time_for_milk_and_cookies(date(2013, 10, 24)))
