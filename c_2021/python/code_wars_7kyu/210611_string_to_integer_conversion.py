import unittest
from typing import Union


def my_parse_int(string: str) -> Union[str, int]:
    try:
        return int(string)
    except ValueError:
        return "NaN"
    
    
class TestMyParseInt(unittest.TestCase):
    def test_my_parse_int_on_only_having_int_value(self):
        self.assertEqual(my_parse_int(string="1"), 1)

    def test_my_parse_int_on_having_int_value_with_space(self):
        self.assertEqual(my_parse_int(string="  1  "), 1)

    def test_my_parse_int_on_having_int_value_with_padding_zero(self):
        self.assertEqual(my_parse_int(string="001  "), 1)

    def test_my_parse_int_on_having_int_with_string(self):
        self.assertEqual(my_parse_int(string="001  string"), "NaN")

    def test_my_parse_int_on_having_float_type(self):
        self.assertEqual(my_parse_int(string="17.5"), "NaN")
        