import unittest


def array_madness(a, b):
    return sum(ele ** 2 for ele in a) > sum(ele ** 3 for ele in b)
    
    
class TestArrayMadness(unittest.TestCase):
    def test_should_return_true_when_sum_of_the_squares_of_each_element_in_a_is_greater_than_the_sum_of_the_cubes_of_each_element_in_b(self):
        a, b = [4, 5, 6], [1, 2, 3]
        actual = array_madness(a, b)
        self.assertEqual(actual, True)

    def test_should_return_false_when_sum_of_the_squares_of_each_element_in_a_is_not_greater_than_the_sum_of_the_cubes_of_each_element_in_b(self):
        a, b = [1, 2, 3],[4, 5, 6]
        actual = array_madness(a, b)
        self.assertEqual(actual, False)
