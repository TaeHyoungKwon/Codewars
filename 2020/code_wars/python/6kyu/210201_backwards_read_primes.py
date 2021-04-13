import math
import unittest


def is_prime(num):
    if num < 2:
        return False
    for ele in range(2, int(math.sqrt(num)) + 1):
        if num % ele == 0:
            return False
    return True


def backwards_prime(start, stop):
    result = []
    for num in range(start, stop + 1):
        if is_prime(num):
            reversed_num = int(str(num)[::-1])
            if num != reversed_num and is_prime(reversed_num):
                result.append(num)
    return result


class TestBackwardsPrime(unittest.TestCase):
    def test_backwards_prime(self):
        self.assertEqual(backwards_prime(start=2, stop=100), [13, 17, 31, 37, 71, 73, 79, 97])
