import unittest


def max_product(lst, n_largest_elements):
    result = 1
    for number in sorted(lst, reverse=True)[:n_largest_elements]:
        result *= number
    return result
    
    
class TestMaxProudct(unittest.TestCase):
    def test_max_product_with_lst_has_only_zero(self):
        self.assertEqual(max_product(lst=[0] * 10, n_largest_elements=5), 0)

    def test_max_product(self):
        self.assertEqual(max_product(lst=[4, 3, 5], n_largest_elements=2), 20)
