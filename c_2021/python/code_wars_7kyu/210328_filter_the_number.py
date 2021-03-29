import unittest


def filter_string(string: str) -> int:
    return int("".join(c for c in string if c.isdigit()))


class TestFilterString(unittest.TestCase):
    def test_filter_string(self):
        self.assertEqual(filter_string(string="a1b2c3"), 123)
