import unittest


def even_numbers(arr, n):
    return [x for x in arr if x % 2 == 0][-n:]
    
    
class TestEvenNumbers(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(even_numbers(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9], n=3), [4, 6, 8])
