import unittest
import itertools


def flatten(lst):
    if len(lst) == 1:
        return lst
    return list(itertools.chain(*lst))

    
    
class TestFlatten(unittest.TestCase):
    def test_should_return_empty_list_when_lst_is_empty_list(self):
        lst = []
        actual = flatten(lst)
        self.assertEqual(actual, [])

    def test_should_return_origin_lst_when_given_lst_length_is_1(self):
        lst = [[1, 2, 3]]
        actual = flatten(lst)
        self.assertEqual(actual, [[1, 2, 3]])

    def test_flatten(self):
        lst = [[1, 2, 3],["a", "b", "c"],[1, 2, 3]]
        actual = flatten(lst)
        self.assertEqual(actual, [1,2,3,"a","b","c",1,2,3])
