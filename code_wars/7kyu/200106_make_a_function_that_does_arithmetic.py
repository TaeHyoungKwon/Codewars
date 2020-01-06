import unittest


def arithmetic(a, b, operator):
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a / b
    
    
class TestArithmetic(unittest.TestCase):
    def test_should_return_3_when_given_a_is_1_b_is_2_and_operator_is_add(self):
        a, b, operator = 1, 2, 'add'
        actual = arithmetic(a, b, operator)
        self.assertEqual(actual, 3)

    def test_should_return_5_when_given_a_is_10_b_is_5_and_operator_is_subtract(self):
        a, b, operator = 10, 5, 'subtract'
        actual = arithmetic(a, b, operator)
        self.assertEqual(actual, 5)

    def test_should_return_50_when_given_a_is_10_b_is_5_and_operator_is_multiply(self):
        a, b, operator = 10, 5, 'multiply'
        actual = arithmetic(a, b, operator)
        self.assertEqual(actual, 50)

    def test_should_return_2_when_given_a_is_10_b_is_5_and_operator_is_divide(self):
        a, b, operator = 10, 5, 'divide'
        actual = arithmetic(a, b, operator)
        self.assertEqual(actual, 2)
        