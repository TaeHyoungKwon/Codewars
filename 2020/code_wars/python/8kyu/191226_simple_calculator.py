import unittest


def calculator(x, y, op):
    if not (str(x).isdigit() and str(y).isdigit()):
        return "unknown value"
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "unknown value"


class TestCalculator(unittest.TestCase):
    def test_should_return_8_when_x_is_6_y_is_2_op_is_plus(self):
        # Given: Set x, y, op
        x, y, op = 6, 2, '+'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: 6 + 2 is 8
        self.assertEqual(actual, 8)

    def test_should_return_1_when_x_is_4_y_is_3_op_is_minus(self):
        # Given: Set x, y, op
        x, y, op = 4, 3, '-'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: 4 - 3 is 1
        self.assertEqual(actual, 1)

    def test_should_return_25_when_x_is_5_y_is_5_op_is_multiple(self):
        # Given: Set x, y, op
        x, y, op = 5, 5, '*'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: 5 * 5 is 25
        self.assertEqual(actual, 25)

    def test_should_return_1_point_25_when_x_is_5_y_is_4_op_is_multiple(self):
        # Given: Set x, y, op
        x, y, op = 5, 4, '/'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: 5 / 4 is 1.25
        self.assertEqual(actual, 1.25)

    def test_should_return_unknown_value_point_when_x_is_6_y_is_2_op_is_unknown_operator(self):
        # Given: Set x, y, op
        x, y, op = 6, 2, '$'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: return unknown value
        self.assertEqual(actual, 'unknown value')

    def test_should_return_unknown_value_point_when_x_or_y_is_not_integer(self):
        # Given: Set x, y, op
        x, y, op = 'abcde', 2, '*'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: return unknown value
        self.assertEqual(actual, 'unknown value')

    def test_should_return_unknown_value_point_when_x_is_int_y_is_str(self):
        # Given: Set x, y, op
        x, y, op = 1, 'abcde', '*'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: return unknown value
        self.assertEqual(actual, 'unknown value')

    def test_should_return_unknown_value_point_when_x_is_int_y_is_special_char(self):
        # Given: Set x, y, op
        x, y, op = 1, '$', '*'

        # When: Call calculator
        actual = calculator(x, y, op)

        # Then: return unknown value
        self.assertEqual(actual, 'unknown value')
