import math
import unittest


def is_prime(num):
    if num < 2:
        return False
    for ele in range(2, int(math.sqrt(num)) + 1):
        if num % ele == 0:
            return False
    return True


def is_last_digit_is_7_or_9(num):
    if str(num)[-1] == '7' or str(num)[-1] == '9':
        return True
    return False


def solution(num):
    result = []
    for index in range(1, num + 1):
        if is_prime(index) and is_last_digit_is_7_or_9(index):
            result.append(index)
    return sum(result)
    
    
class TestSolution(unittest.TestCase):
    def test_solution(self):
        num = 100000
        actual = solution(num)
        self.assertEqual(actual, 227715037)
