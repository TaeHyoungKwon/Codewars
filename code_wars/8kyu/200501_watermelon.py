import unittest


def divide(weight):
    if weight == 2:
        return False
    if weight % 2 == 0:
        return True
    return False
    
    
class TestDivide(unittest.TestCase):
    def test_should_return_false_when_given_weight_is_2(self):
        weight = 2
        actual = divide(weight)
        self.assertEqual(actual, False)

    def test_should_return_false_when_given_weight_is_odd(self):
        weight = 3
        actual = divide(weight)
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_weight_is_even(self):
        weight = 4
        actual = divide(weight)
        self.assertEqual(actual, True)
