import unittest


def number_of_occurrences(element, sample):
    return sample.count(element)


class TestNumberOfOccurrences(unittest.TestCase):
    def test_should_return_1_when_given_element_is_0(self):
        self.assertEqual(number_of_occurrences(
            element=0,
            sample=[0, 1, 2, 2, 3]), 1
        )
