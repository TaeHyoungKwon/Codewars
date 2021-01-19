import unittest


def _get_alphabet(char, start_char, end_char):
    alpha = ord(char) + 13
    if alpha > ord(end_char):
        alpha = ord(start_char) + (alpha - ord(end_char)) - 1
    return alpha


def rot13(message):
    rot13 = ""
    for char in message:
        if not char.isalpha():
            rot13 += char
        elif char.islower():
            rot13 += chr(_get_alphabet(char, "a", "z"))
        elif char.isupper():
            rot13 += chr(_get_alphabet(char, "A", "Z"))
    return rot13


class TestRot13(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual(rot13(message="TEST"), "GRFG")

    def test_rot13(self):
        self.assertEqual(rot13(message="test"), "grfg")
