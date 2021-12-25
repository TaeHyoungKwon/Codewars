import unittest


def explode(s):
    return "".join(digit * int(digit) for digit in s)
    
    
class TestExplode(unittest.TestCase):
    def test_explode_on_success(self):
        self.assertEqual(explode(s="312"), "333122")

    def test_explode_on_s_includes_0(self):
        self.assertEqual(explode(s="0"), "")
