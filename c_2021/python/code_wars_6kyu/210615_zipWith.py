import unittest


def zip_with(fn, a1, a2):
    return list(map(fn, a1, a2))
    
    
class TestZipWith(unittest.TestCase):
    def test_zip_with_sum_of_two_list(self):
        self.assertEqual(zip_with(lambda a, b: a + b, [0,1,2,3,4,5],[6,5,4,3,2,1]), [6,6,6,6,6,6])

    def test_zip_with_sum_of_two_list_that_is_not_equal_length_case_1(self):
        self.assertEqual(zip_with(lambda a, b: a + b, [0,1,2,3,4],[6,5,4,3,2,1]), [6,6,6,6,6])

    def test_zip_with_sum_of_two_list_that_is_not_equal_length_case_2(self):
        self.assertEqual(zip_with(lambda a, b: a + b, [0,1,2,3,4,5],[6,5,4,3,2]), [6,6,6,6,6])

    def test_zip_with_max_value_of_two_list(self):
        self.assertEqual(zip_with(lambda a, b:max([a, b]), [1,4,7,1,4,7], [4,7,1,4,7,1]), [4,7,7,4,7,7])


