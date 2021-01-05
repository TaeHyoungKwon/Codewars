import unittest


def sum_str(a, b):
    if not a and not b:
        return "0"
    if not a:
        return b
    if not b:
        return a
    return str(int(a) + int(b))
    
    
class TestSumStr(unittest.TestCase):
    def test_sum_str(self):
        self.assertEqual(sum_str("4", "5"), "9")

    def test_sum_str_with_one_empty(self):
        self.assertEqual(sum_str("4", ""), "4")

    def test_sum_str_with_all_empty(self):
        self.assertEqual(sum_str("", ""), "0")
