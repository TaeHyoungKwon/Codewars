import unittest


def odd_row(n: int) -> int:

    count = (n * (n - 1)) // 2
    last_element = 2 * count - 1
    a = last_element + 2
    d = 2
    return [d * i + a - d for i in range(1, n + 1)]
    
    
class TestOddRow(unittest.TestCase):
    def test_odd_row_when_n_is_1(self):
        self.assertEqual(odd_row(n=1), [1])

    def test_odd_row_when_n_is_2(self):
        self.assertEqual(odd_row(n=2), [3, 5])

    def test_odd_row_when_n_is_3(self):
        self.assertEqual(odd_row(n=3), [7, 9, 11])
