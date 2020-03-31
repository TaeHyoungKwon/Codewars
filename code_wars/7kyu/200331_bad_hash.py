import unittest

def string_hash(s):
    return step_d(s)

def step_a(s):
    return sum(ord(ele) for ele in s)

def step_b(s):
    ord_list = [str(ord(ele)) for ele in s]
    return sum(map(lambda x: int(x[1]) - int(x[0]), zip(ord_list, ord_list[1:])))

def step_c(s):
    return (step_a(s) | step_b(s)) & ((~step_a(s)) << 2)

def step_d(s):
    return step_c(s) ^ (32 * (s.count(' ') + 1))


class TestStringHash(unittest.TestCase):
    def test_sum_of_ascii_values_of_input(self):
        s = 'ca'
        actual = step_a(s)
        self.assertEqual(actual, 196)

    def test_sum_of_every_difference_between_consecutive_chars(self):
        s = 'ca'
        actual = step_b(s)
        self.assertEqual(actual, -2)

    def test_step_c(self):
        s = 'ca'
        actual = step_c(s)
        self.assertEqual(actual, -788)

    def test_step_d(self):
        s = 'ca'
        actual = step_d(s)
        self.assertEqual(actual, -820)
