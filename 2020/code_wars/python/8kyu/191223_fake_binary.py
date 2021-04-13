import unittest


def fake_bin(x):
    return ''.join('0' if int(ele) < 5 else '1' for ele in x)


class TestFakeBinary(unittest.TestCase):
    def test_should_return_all_of_0_when_given_x_is_below_5(self):
        x = '44444'
        result = fake_bin(x)
        self.assertEqual(result, '00000')

    def test_should_return_all_of_1_when_given_x_is_above_5(self):
        x = '44444'
        result = fake_bin(x)
        self.assertEqual(result, '00000')

    def test_should_return_value_is_mixed_0_or_1_when_given_x_is_below_5_or_above_5(self):
        x = '366058562030849490134388085'
        result = fake_bin(x)
        self.assertEqual(result, '011011110000101010000011011')