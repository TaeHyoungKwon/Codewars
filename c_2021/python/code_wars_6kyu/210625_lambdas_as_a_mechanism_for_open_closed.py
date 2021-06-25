import unittest


spoken = lambda greeting: f"{greeting}."
shouted = lambda greeting: f"{greeting.upper()}!"
whispered = lambda greeting: f"{greeting.lower()}."

greet = lambda style, msg: style(msg)


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(spoken, "Hello"), "Hello.")
        self.assertEqual(greet(shouted, "Hello"), "HELLO!")
        self.assertEqual(greet(whispered, "Hello"), "hello.")
