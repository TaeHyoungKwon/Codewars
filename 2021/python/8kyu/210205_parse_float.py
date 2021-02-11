import unittest


def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None


class TestParseFloat(unittest.TestCase):
    def test_parse_float(self):
        self.assertEqual(parse_float(string="1.0"), 1.0)

    def test_parse_float_with_string_is_list(self):
        self.assertIsNone(parse_float(string=["a", "b", "1"]))

    def test_parse_float_with_none(self):
        self.assertIsNone(parse_float(string="a"), None)
