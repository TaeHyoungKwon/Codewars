import unittest


def tribonacci(signature, n):
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]
    else:
        result = signature
        signature_length = len(signature)
        while n - signature_length > 0:
            temp = result[-1] + result[-2] + result[-3]
            result.append(temp)
            n -= 1
    return result

    
class TestTribonacci(unittest.TestCase):
    def test_should_return_empty_list_when_given_n_is_0(self):
        signature, n = [300, 200, 100], 0
        actual = tribonacci(signature, n)
        self.assertEqual(actual, [])

    def test_tribonacci_when_given_n_is_less_equal_than_3(self):
        signature, n = [1, 1, 1], 1
        actual = tribonacci(signature, n)
        self.assertEqual(actual, [1])

    def test_tribonacci_when_given_n_is_greater_equal_than_3(self):
        signature, n = [1, 1, 1], 10
        actual = tribonacci(signature, n)
        self.assertEqual(actual, [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
