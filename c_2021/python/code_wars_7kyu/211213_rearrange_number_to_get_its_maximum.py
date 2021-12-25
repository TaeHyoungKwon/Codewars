from itertools import permutations
import unittest


def max_redigit(num):
    is_valid = len(str(num)) == 3 and isinstance(num, int) and num > 0
    if not is_valid:
        return None
    return max(int("".join(ele)) for ele in permutations(str(num), 3))


class TestMaxRedigit(unittest.TestCase):
    def test_max_redigit_should_return_minus_1_on_invalid_num(self):
        self.assertIsNone(max_redigit(num="abc"))
        self.assertIsNone(max_redigit(num="1"))
        self.assertIsNone(max_redigit(num=1))
        self.assertIsNone(max_redigit(num=-32))

    def test_max_redigit_on_valid_num(self):
        self.assertEqual(max_redigit(num=123), 321)
