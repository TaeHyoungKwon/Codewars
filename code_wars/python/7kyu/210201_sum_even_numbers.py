import unittest


def sum_even_numbers(seq):
    return sum(ele for ele in seq if ele % 2 == 0)
    
    
class TestSumEvenNumbers(unittest.TestCase):
    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_nubers(seq=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
