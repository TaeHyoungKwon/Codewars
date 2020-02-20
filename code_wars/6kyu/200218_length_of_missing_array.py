import unittest


def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays or None in array_of_arrays or [] in array_of_arrays:
        return 0
    origin_set = set(map(len, array_of_arrays))
    return next(ele for ele in set(range(min(origin_set), max(origin_set) + 1)) - origin_set)


class TestLengthOfMissingArray(unittest.TestCase):
    def test_should_return_0_when_array_in_the_array_is_empty(self):
        actual = get_length_of_missing_array(array_of_arrays=[[], []])
        self.assertEqual(actual, 0)

    def test_should_return_0_when_an_array_in_the_array_is_empty(self):
        actual = get_length_of_missing_array(array_of_arrays=[[], [1], [1, 2], [1, 2, 3, 4]])
        self.assertEqual(actual, 0)

    def test_missing_array(self):
        actual = get_length_of_missing_array(array_of_arrays=[[1], [1, 2], [1, 2, 3, 4]])
        self.assertEqual(actual, 3)

    def test_missing_array_with_none(self):
        actual = get_length_of_missing_array(array_of_arrays=[[None], [None, None, None]])
        self.assertEqual(actual, 2)

    def test_missing_array_with_empty_array(self):
        actual = get_length_of_missing_array(array_of_arrays=[])
        self.assertEqual(actual, 0)
