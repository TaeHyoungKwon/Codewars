import unittest


def is_monotone(heights):
    return all(front <= back for front, back in zip(heights, heights[1:]))


class TestMonotone(unittest.TestCase):
    def test_is_monotone_should_true_when_heights_is_empty_list(self):
        self.assertTrue(is_monotone(heights=[]))

    def test_is_monotone_should_true_when_heights_length_is_1(self):
        self.assertTrue(is_monotone(heights=[1]))

    def test_is_monotone_should_true_when_all_element_is_same(self):
        self.assertTrue(is_monotone(heights=[5, 5, 5, 5, 5, 5]))

    def test_is_monotone_should_true_when_element_is_ascending(self):
        self.assertTrue(is_monotone(heights=[1, 2, 3, 4]))

    def test_is_monotone_should_true_when_element_is_descending(self):
        self.assertFalse(is_monotone(heights=[4, 3, 2, 1]))
