import unittest

VOID_MSG = 'Void!'


def explode(arr):
    new_arr = [0 if str(ele).isalpha() else ele for ele in arr]
    if sum(new_arr) == 0:
        return VOID_MSG
    return [arr for _ in range(sum(new_arr))]
    
    
class TestExplode(unittest.TestCase):
    def test_explode_with_only_numerics(self):
        arr = [9, 3]
        actual = explode(arr)
        self.assertEqual(actual, [[9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3]])

    def test_explode_with_numeric_and_alphabet(self):
        arr = [6, 'c']
        actual = explode(arr)
        self.assertEqual(actual, [[6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c']])

    def test_explode_with_only_alphabet(self):
        arr = ['a', 'c']
        actual = explode(arr)
        self.assertEqual(actual, 'Void!')
