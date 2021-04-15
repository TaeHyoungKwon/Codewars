import unittest
from typing import Optional


def greet(name: Optional[str]) -> Optional[str]:
    return f"hello {name}!" if name else None


class TestGreet(unittest.TestCase):
    def test_greet_should_return_none_on_name_is_empty_string(self):
        self.assertEqual(greet(name=""), None)

    def test_greet_should_return_none_on_name_is_none(self):
        self.assertEqual(greet(name=None), None)

    def test_greet(self):
        self.assertEqual(greet(name="Niks"), "hello Niks!")
