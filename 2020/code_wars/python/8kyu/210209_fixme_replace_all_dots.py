import re
import unittest


# def replace_dots(str_):
#     return str_.replace(".", "-")


def replace_dots(str_):
    return re.sub(r"\.", "-", str_)

    
class TestReplaceDots(unittest.TestCase):
    def test_replace_dots_with_empty_string(self):
        self.assertEqual(replace_dots(str_=""), "")

    def test_replace_dots_with_dot(self):
        self.assertEqual(replace_dots(str_="one.two.three"), "one-two-three")
