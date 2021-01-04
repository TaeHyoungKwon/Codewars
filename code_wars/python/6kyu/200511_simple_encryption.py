import unittest
from itertools import zip_longest


def encrypt(encrypted_text, n):
    if encrypted_text is None and n == 0:
        return None

    if not encrypted_text:
        return ''

    while n > 0:
        n -= 1
        encrypted_text = (''.join(ele for idx, ele in enumerate(encrypted_text, 1) if idx % 2 == 0)
                          + ''.join(ele for idx, ele in enumerate(encrypted_text, 1) if idx % 2 == 1))
    return encrypted_text


def decrypt(text, n):
    if text is None and n == 0:
        return None

    if not text:
        return ''

    while n > 0:
        n -= 1
        result = ''
        for ele in list(zip_longest(text[len(text) // 2:], text[:len(text) // 2], fillvalue='')):
            result += ''.join(ele)
        text = result
    return text


class TestEncryptedDecrypted(unittest.TestCase):
    def test_should_return_origin_text_when_n_is_0(self):
        encrypted_text, n = "This is a test!", 0
        actual = encrypt(encrypted_text, n)
        self.assertEqual(actual, "This is a test!")

    def test_should_return_empty_string_when_n_is_0_and_encrypted_text_is_empty_string(self):
        encrypted_text, n = "", 0
        actual = encrypt(encrypted_text, n)
        self.assertEqual(actual, "")

    def test_should_return_empty_string_when_n_is_0_and_encrypted_text_is_none(self):
        encrypted_text, n = None, 0
        actual = encrypt(encrypted_text, n)
        self.assertEqual(actual, None)

    def test_encrypt_one_times(self):
        encrypted_text, n = "This is a test!", 1
        actual = encrypt(encrypted_text, n)
        self.assertEqual(actual, "hsi  etTi sats!")

    def test_encrypt_two_times(self):
        encrypted_text, n = "This is a test!", 2
        actual = encrypt(encrypted_text, n)
        self.assertEqual(actual, "s eT ashi tist!")

    def test_should_return_empty_string_when_n_is_0_and_text_is_empty_string(self):
        text, n = "", 0
        actual = decrypt(text, n)
        self.assertEqual(actual, "")

    def test_should_return_none_when_n_is_0_and_text_is_none(self):
        text, n = None, 0
        actual = decrypt(text, n)
        self.assertEqual(actual, None)

    def test_decrypt_should_return_origin_text_when_n_is_0(self):
        text, n = "This is a test!", 0
        actual = decrypt(text, n)
        self.assertEqual(actual, "This is a test!")

    def test_decrypt_should_return_origin_text_when_n_is_1(self):
        text, n = "hsi  etTi sats!", 1
        actual = decrypt(text, n)
        self.assertEqual(actual, "This is a test!")

    def test_decrypt_should_return_origin_text_when_n_is_2(self):
        text, n = "s eT ashi tist!", 2
        actual = decrypt(text, n)
        self.assertEqual(actual, "This is a test!")
