import unittest


NO = 'No'
NORMAL = 'normal'


def get_neck(x, y):
    return x / y


def divide(x, y, mode):
    def _get_normal(x, y):
        return NO if y == 0 else get_neck(x, y)

    def _get_abnormal(x, y):
        rest = x % y
        return NO if y == 0 else [get_neck(x, y), rest]

    return _get_normal(x, y) if mode == NORMAL else _get_abnormal(x, y)


class TestCalculator(unittest.TestCase):
    def test_calculator_on_divide(self):
        self.assertEqual(divide(x=4, y=4, mode=NORMAL), 1)

    def test_calculator_on_divide_when_y_is_0(self):
        self.assertEqual(divide(x=4, y=0, mode=NORMAL), NO)

    def test_calculator_on_divide_when_x_is_0(self):
        self.assertEqual(divide(x=0, y=4, mode=NORMAL), 0)

    def test_calculator_on_divide_when_x_is_negative_2_and_y_is_4(self):
        self.assertEqual(divide(x=-2, y=4, mode=NORMAL), -0.5)
