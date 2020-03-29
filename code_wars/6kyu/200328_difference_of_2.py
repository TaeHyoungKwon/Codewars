import unittest

DIFFERENCE = 2


def twos_difference(lst):
    return [(ele, ele + DIFFERENCE) for ele in sorted(lst) if ele + DIFFERENCE in lst]

    
class Test(unittest.TestCase):
    def test_should_empty_list_when_given_lst_is_empty_list(self):
        lst = []
        actual = twos_difference(lst)
        self.assertEqual(actual, [])

    def test_should_empty_list_when_given_lst_has_not_difference_2_elements(self):
        lst = [1, 4, 7, 10]
        actual = twos_difference(lst)
        self.assertEqual(actual, [])

    def test_twos_difference(self):
        lst = [6, 3, 4, 1, 5]
        actual = twos_difference(lst)
        self.assertEqual(actual, [(1, 3), (3, 5), (4, 6)])
