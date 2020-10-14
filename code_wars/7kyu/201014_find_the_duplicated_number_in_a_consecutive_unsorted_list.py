import unittest


def find_dup(arr):
    return next(ele for ele in arr if arr.count(ele) == 2)
    
    
class TestFindDup(unittest.TestCase):
    def test_find_dup(self):
        arr = [5, 4, 3, 2, 1, 1]
        actual = find_dup(arr)
        self.assertEqual(actual, 1)
