import re
import unittest


def change(st):
    alphabet_map = ["0"] * 26
    all_alphabet = re.findall(r"[a-zA-Z]", st)
    for alphabet in map(str.lower, all_alphabet):
        alphabet_map[ord(alphabet) - 97] = "1"
    return ''.join(alphabet_map)


class TestChange(unittest.TestCase):
    def test_change(self):
        self.assertEqual(change("a **&  bZ"), "11000000000000000000000001")
