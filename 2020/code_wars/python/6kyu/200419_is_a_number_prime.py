import math
import unittest


def is_prime(num):
    if num < 2:
        return False
    for ele in range(2, int(math.sqrt(num)) + 1):
        if num % ele == 0:
            return False
    return True

    
class TestPrime(unittest.TestCase):
    def test_return_false_when_given_num_is_negative(self):
        self.assertEqual(is_prime(-1), False)

    def test_return_false_when_given_num_is_1(self):
        self.assertEqual(is_prime(1), False)

    def test_return_false_when_given_num_is_0(self):
        self.assertEqual(is_prime(0), False)

    def test_return_true_when_given_num_is_73(self):
        self.assertEqual(is_prime(73), True)

    def test_return_true_when_given_num_is_2(self):
        self.assertEqual(is_prime(2), True)
