import unittest


def distinct(sequence):
    result = []
    for ele in sequence:
        if ele not in result:
            result.append(ele)

    return result

    
class TestDistinct(unittest.TestCase):
    def test_distinct_with_one_element(self):
        seq = [1]
        actual = distinct(seq)
        self.assertEqual(actual, [1])

    def test_distinct_with_over_two_elements_has_distinct_element(self):
        seq = [1, 2]
        actual = distinct(seq)
        self.assertEqual(actual, [1, 2])

    def test_distinct_with_over_two_elements_has_duplicated_element(self):
        seq = [1, 1, 2]
        actual = distinct(seq)
        self.assertEqual(actual, [1, 2])
