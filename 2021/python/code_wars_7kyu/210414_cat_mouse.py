import unittest

ESCAPED = "Escaped!"
CAUGHT = "Caught!"


def cat_mouse(x: str) -> str:
    return CAUGHT if x.count(".") <= 3 else ESCAPED


class TestCatMouse(unittest.TestCase):
    def test_cat_mouse_with_return_escaped_string(self):
        self.assertEqual(cat_mouse(x="C....m"), "Escaped!")

    def test_cat_mouse_with_return_caught_string(self):
        self.assertEqual(cat_mouse(x="C.m"), "Caught!")
