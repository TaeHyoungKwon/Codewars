import unittest


def index(array, n):
    if n not in array:
        return -1
    return array[n] ** n
    
    
class TestNthPower(unittest.TestCase):
    def test_should_return_negative_one_when_given_n_is_not_in_array(self):
        actual = index([1, 3, 5], 2)
        self.assertEqual(actual, -1)

    def test_should_return_1000000_when_given_n_is_3_array_has_element_1_3_10_100(self):
        actual = index([1, 3, 10, 100], 3)
        self.assertEqual(actual, 1000000)
