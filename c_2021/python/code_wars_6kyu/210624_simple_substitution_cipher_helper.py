import re
import unittest
from typing import Callable


class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, s):
        return self.generate_string(to=self.map2, from_=self.map1, s=s)

    def decode(self, s):
        return self.generate_string(to=self.map1, from_=self.map2, s=s)

    @staticmethod
    def generate_string(to: str, from_: Callable, s: str) -> str:
        return "".join(to[from_.index(ele)] if ele.isalpha() else ele for ele in s)


class TestCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = Cipher(map1="abcdefghijklmnopqrstuvwxyz", map2="etaoinshrdlucmfwypvbgkjqxz")

    def test_cipher_with_encode(self):
        self.assertEqual(self.cipher.encode(s="abc"), "eta")

    def test_cipher_with_decode(self):
        self.assertEqual(self.cipher.decode(s="eta"), "abc")

    def test_cipher_with_special_char(self):
        self.assertEqual(self.cipher.encode(s="a_bc&*83"), "e_ta&*83")
