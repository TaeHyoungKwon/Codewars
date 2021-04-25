import re
import unittest


def eight_bit_number(n: str) -> bool:
    return bool(re.fullmatch(r"\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]", n))
    
    
class TestEightBitNumber(unittest.TestCase):
    def test_eight_bit_number_with_n_is_55(self):
        self.assertTrue(eight_bit_number("55"))

    def test_eight_bit_number_with_n_is_00(self):
        self.assertFalse(eight_bit_number("00"))
