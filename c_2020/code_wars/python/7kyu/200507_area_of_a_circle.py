import unittest
import math


def circleArea(r):
    if isinstance(r, str) or r < 0:
        return False
    return round(math.pi * (r ** 2), 2)


class TestCircleArea(unittest.TestCase):
    def test_should_return_false_when_given_r_is_str(self):
        r = "number"
        actual = circleArea(r)
        self.assertFalse(actual)

    def test_should_return_false_when_given_r_is_negative(self):
        r = -1485
        actual = circleArea(r)
        self.assertFalse(actual)

    def test_should_return_false_when_given_r_is_zero(self):
        r = 0
        actual = circleArea(r)
        self.assertFalse(actual)

    def test_circle_area_on_success(self):
        r = 68
        actual = circleArea(r)
        self.assertEqual(actual, 14526.72)
