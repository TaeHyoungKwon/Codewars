import unittest


EMPTY_STRING = ""
STEP = 2


def convert(number):
    return EMPTY_STRING.join(chr(int(number[idx : idx + STEP])) for idx in range(0, len(number), STEP))


class TestConvert(unittest.TestCase):
    def test_convert(self):
        number = "656667"
        actual = convert(number)
        self.assertEqual(actual, "ABC")

    def test_convert_long_number(self):
        number = "73327673756932858080698267658369"
        actual = convert(number)
        self.assertEqual(actual, "I LIKE UPPERCASE")
