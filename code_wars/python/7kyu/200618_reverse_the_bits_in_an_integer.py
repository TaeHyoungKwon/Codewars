import unittest


def reverse_bits(n):
    return int(bin(n)[2:][::-1], 2)
    
    
class TestReverseBits(unittest.TestCase):
    def test_reverse_bits_should_return_0_when_n_is_0(self):
        n = 0
        actual = reverse_bits(n)
        self.assertEqual(actual, 0)

    def test_reverse_bits_when_n_is_not_0(self):
        n = 417
        actual = reverse_bits(n)
        self.assertEqual(actual, 267)
