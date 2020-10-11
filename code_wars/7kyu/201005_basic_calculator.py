import unittest

SPECIFIED_OPERATION = {
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
}


def calculate(num1, operation, num2):
    def is_edge_case():
        return operation == '/' and num2 == 0 or operation not in SPECIFIED_OPERATION

    return SPECIFIED_OPERATION[operation](num1, num2) if not is_edge_case() else None


class TestCalculate(unittest.TestCase):
    def test_calculate_should_return_none_when_given_num2_is_0_and_operation_is_division(self):
        self.assertEqual(calculate(num1=-3, operation='/', num2=0), None)

    def test_calculate_should_return_none_when_given_operation_is_not_specified(self):
        self.assertEqual(calculate(num1=-3, operation='w', num2=1), None)

    def test_calculate_common_case_with_plus(self):
        self.assertEqual(calculate(num1=3, operation='+', num2=1), 4)

    def test_calculate_common_case_with_minus(self):
        self.assertEqual(calculate(num1=3, operation='-', num2=1), 2)

    def test_calculate_common_case_with_multiply(self):
        self.assertEqual(calculate(num1=3, operation='*', num2=1), 3)

    def test_calculate_common_case_with_division(self):
        self.assertEqual(calculate(num1=3, operation='/', num2=1), 3)