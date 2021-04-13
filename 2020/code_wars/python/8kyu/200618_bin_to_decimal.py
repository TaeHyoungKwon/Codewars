import unittest


def bin_to_decimal(inp):
    return sum((2 ** index) * 1 for index, ele in enumerate(inp[::-1]) if ele == '1')


class TestBinToDecimal(unittest.TestCase):
    def test_should_return_0_when_given_inp_is_0(self):
        inp = '0'
        actual = bin_to_decimal(inp)
        self.assertEqual(actual, 0)

    def test_should_return_3_when_given_inp_is_11(self):
        inp = '11'
        actual = bin_to_decimal(inp)
        self.assertEqual(actual, 3)
