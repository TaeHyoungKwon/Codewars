import unittest

STEP = 2


def row_weights(array):
    return sum(array[0::STEP]), sum(array[1::STEP])
    
    
class TestRowWeights(unittest.TestCase):
    def test_should_return_all_of_zero_element_when_given_array_ele_is_only_zero(self):
        array = [0]
        actual = row_weights(array)
        self.assertEqual(actual, (0, 0))

    def test_should_return_80_and_0_when_given_array_first_ele_is_80(self):
        array = [80]
        actual = row_weights(array)
        self.assertEqual(actual, (80, 0))

    def test_row_weights_element_count_more_than_two(self):
        array = [100, 51, 50, 100]
        actual = row_weights(array)
        self.assertEqual(actual, (150, 151))
