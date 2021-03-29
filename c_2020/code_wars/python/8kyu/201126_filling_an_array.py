import unittest


def arr(n=0):
    return list(range(n))
    
    
class TestArr(unittest.TestCase):
    def test_arr_should_return_n_is_empty_list_when_n_is_0(self):
        self.assertEqual(arr(0), [])

    def test_arr_should_return_n_is_empty_list_when_n_is_none(self):
        self.assertEqual(arr(0), [])

    def test_arr_should_return_list_with_number_under_n_when_n_is_over_0(self):
        self.assertEqual(arr(4), [0, 1, 2, 3])
