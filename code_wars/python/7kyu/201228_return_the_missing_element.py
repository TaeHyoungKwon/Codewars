import unittest


def get_missing_element(seq):
    return list(i for i in range(10) if i not in seq)[0]


class TestGetMissingElement(unittest.TestCase):
    def test_get_missing_element(self):
        self.assertEqual(get_missing_element([0, 5, 1, 3, 2, 9, 7, 6, 4]), 8)

    def test_get_missing_element_second_case(self):
        self.assertEqual(get_missing_element([8, 6, 2, 7, 5, 0, 1, 4, 3]), 9)
