import unittest


def sum_dig_pow(a, b):
    def _generate_digit_pow(index):
        for digit_index, digit in enumerate(str(index)):
            yield int(digit) ** (digit_index + 1)

    def _is_eureka(index):
        return sum(_generate_digit_pow(index)) == index

    return [index_ for index_ in range(a, b + 1) if _is_eureka(index_)]
    
    
class TestSumDigPow(unittest.TestCase):
    def test_sum_dig_pow(self):
        a, b = 1, 10
        actual = sum_dig_pow(a, b)
        self.assertEqual(actual, [1, 2, 3, 4, 5, 6, 7, 8, 9])
