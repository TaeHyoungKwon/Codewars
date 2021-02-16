import unittest


def max_diff(lst):
    if not lst or len(lst) == 1:
        return 0
    return max(lst) - min(lst)
    
    
class TestMaxDiff(unittest.TestCase):
    def test_max_diff_should_return_0_when_lst_is_empty(self):
        self.assertEqual(max_diff(lst=[]), 0)

    def test_max_diff_should_return_0_when_lst_has_element_only_one(self):
        self.assertEqual(max_diff(lst=[16]), 0)

    def test_max_diff(self):
        self.assertEqual(max_diff(lst=[0, 1, 2, 3, 4, 5, 16]), 16)
