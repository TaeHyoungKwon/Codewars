import unittest

ASCII_MAX_RANGE = 256


def encrypt(text: str, rule: int) -> str:
    return "".join(
        map(
            chr,
            [
                ele - ASCII_MAX_RANGE if ele >= ASCII_MAX_RANGE else ele
                for ele in map(lambda x: x + (rule % ASCII_MAX_RANGE), map(ord, text))
            ],
        )
    )


class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt(text="please encrypt me", rule=2), 'rngcug"gpet{rv"og')
