import unittest


def build_string(*args):
    built_string = ", ".join(args)
    return f"I like {built_string}!"


class TestBuildString(unittest.TestCase):
    def test_build_string(self):
        words = ("Cheese", "Milk", "Chocolate")
        actual = build_string(*words)
        self.assertEqual(actual, "I like Cheese, Milk, Chocolate!")
