import unittest


def find_all(array, n):
    return [idx for idx, ele in enumerate(array) if ele == n]
    
    
class TestFindAll(unittest.TestCase):

    @staticmethod
    def _call_find_all(array, n):
        # When: call find_all
        actual = find_all(array, n)
        return actual

    def test_should_return_empty_list_when_given_n_is_not_in_array(self):
        actual = self._call_find_all([1, 2, 3, 4, 5], 6)

        # Then: should return empty list
        self.assertEqual(actual, [])

    def test_should_return_empty_list_when_given_n_is_empty(self):
        actual = self._call_find_all([], 3)

        # Then: should return empty list
        self.assertEqual(actual, [])

    def test_should_return_index_position_when_given_n_is_contained_in_array(self):
        actual = self._call_find_all([1, 2, 3, 3, 5], 3)

        # Then: should return [2, 3] - 2 and 3 is index of '3' in array
        self.assertEqual(actual, [2, 3])
