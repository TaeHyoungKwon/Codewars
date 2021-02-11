import unittest

NOT_A_STRING = "Not a string"


def repeat_it(string, n):
    return string * n if isinstance(string, str) else NOT_A_STRING


class TestRepeatIt(unittest.TestCase):
    def test_repeat_it(self):
        self.assertEqual(repeat_it(string="Hello", n=5), "HelloHelloHelloHelloHello")

    def test_repeat_it_with_string_param_type_is_not_string(self):
        self.assertEqual(repeat_it(string=12345, n=5), "Not a string")
