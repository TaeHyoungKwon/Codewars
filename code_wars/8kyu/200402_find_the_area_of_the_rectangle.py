import unittest
import math

NOT_RECTANGLE_MESSAGE = 'Not a rectangle'


def area(d, l):
    if l >= d:
        return NOT_RECTANGLE_MESSAGE
    unknown_quantity = math.sqrt((d ** 2) - (l ** 2))
    return round(unknown_quantity * l, 2)


class TestArea(unittest.TestCase):
    def test_should_return_not_rectangle_msg_when_given_l_is_greater_than_given_d(self):
        d, l = 3, 5
        actual = area(d, l)
        self.assertEqual(actual, "Not a rectangle")

    def test_should_return_not_rectangle_msg_when_given_l_is_equals_given_d(self):
        d, l = 5, 5
        actual = area(d, l)
        self.assertEqual(actual, "Not a rectangle")

    def test_area_return_no_decimal_num(self):
        d, l = 5, 4
        actual = area(d, l)
        self.assertEqual(actual, 12)

    def test_area_return_decimal_num(self):
        d, l = 12, 5
        actual = area(d, l)
        self.assertEqual(actual, 54.54)
