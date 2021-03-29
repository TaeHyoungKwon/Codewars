import unittest


def divisors(n):
    return sum(1 for ele in range(1, n // 2 + 1) if n % ele == 0) + 1
    
    
class TestDivisor(unittest.TestCase):
    def test_should_return_3_when_given_n_is_4(self):
        n = 4
        result = divisors(n)
        self.assertEqual(result, 3)

    def test_should_return_2_when_given_n_is_5(self):
        n = 5
        result = divisors(n)
        self.assertEqual(result, 2)

    def test_should_return_8_when_given_n_is_30(self):
        n = 30
        result = divisors(n)
        self.assertEqual(result, 8)

    def test_should_return_13_when_given_n_is_4096(self):
        n = 4096
        result = divisors(n)
        self.assertEqual(result, 13)
