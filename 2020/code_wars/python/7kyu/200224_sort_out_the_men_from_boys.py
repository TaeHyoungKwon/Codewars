import unittest


def men_from_boys(arr):
    men = sorted(set(ele for ele in arr if ele % 2 == 0))
    boys = sorted(set(ele for ele in arr if ele % 2 == 1), reverse=True)
    return men + boys
    
    
class TestMenFromBoys(unittest.TestCase):
    def test_should_return_sorted_even_from_odd_when_arr_is_mixed(self):
        arr = [7, 3, 14, 17]
        actual = men_from_boys(arr)
        self.assertEqual(actual, [14, 17, 7, 3])

    def test_should_return_sorted_even_from_odd_when_arr_is_mixed_with_duplicated_num(self):
        arr = [2, 15, 17, 15, 2, 10, 10, 17, 1, 1]
        actual = men_from_boys(arr)
        self.assertEqual(actual, [2, 10, 17, 15, 1])

    def test_should_return_sorted_even_from_odd_when_arr_is_mixed_with_negative_num(self):
        arr = [-32, -39, -35, -41]
        actual = men_from_boys(arr)
        self.assertEqual(actual, [-32, -35, -39, -41])
