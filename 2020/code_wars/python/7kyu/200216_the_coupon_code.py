import unittest

from dateutil import parser


def parse_string_to_datetime(current_date, expiration_date):
    return parser.parse(current_date), parser.parse(expiration_date)


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date, expiration_date = parse_string_to_datetime(current_date, expiration_date)

    if (entered_code is correct_code) and (current_date <= expiration_date):
        return True
    return False


class TestCheckCoupon(unittest.TestCase):
    def test_should_return_true_when_coupon_is_valid_and_not_expired(self):
        actual = check_coupon(
            entered_code="12345",
            correct_code="12345",
            current_date="September 5, 2014",
            expiration_date="October 1, 2014",
        )
        self.assertEqual(actual, True)

    def test_should_return_false_when_coupon_is_not_valid_but_not_expired(self):
        actual = check_coupon(
            entered_code="",
            correct_code="12345",
            current_date="September 5, 2014",
            expiration_date="October 1, 2014",
        )
        self.assertEqual(actual, False)

    def test_should_return_false_when_coupon_is_valid_but_expired(self):
        actual = check_coupon(
            entered_code="12345",
            correct_code="12345",
            current_date="October 2, 2015",
            expiration_date="October 1, 2014",
        )
        self.assertEqual(actual, False)

    def test_should_return_false_when_coupon_is_not_valid_and_expired(self):
        actual = check_coupon(
            entered_code="",
            correct_code="12345",
            current_date="October 2, 2015",
            expiration_date="October 1, 2014",
        )
        self.assertEqual(actual, False)

    def test_should_return_false_when_coupon_is_not_valid_by_0_and_false(self):
        actual = check_coupon(
            entered_code=0,
            correct_code=False,
            current_date="September 5, 2014",
            expiration_date="September 25, 2014",
        )
        self.assertEqual(actual, False)
