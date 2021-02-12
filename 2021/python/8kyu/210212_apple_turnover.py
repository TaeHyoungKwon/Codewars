import unittest

HELP_YOURSELF_MSG = "Help yourself to a honeycomb Yorkie for the glovebox."
HOTTER_MSG = "It's hotter than the sun!!"


def apple(x):
    return HOTTER_MSG if int(x) ** 2 > 1000 else HELP_YOURSELF_MSG
    
    
class TestApple(unittest.TestCase):
    def test_apple_x_type_is_string_and_squared_is_more_than_1000(self):
        self.assertEqual(apple(x='50'), HOTTER_MSG)

    def test_apple_x_type_is_string_and_squared_is_not_more_than_1000(self):
        self.assertEqual(apple(x='2'), HELP_YOURSELF_MSG)

    def test_apple_x_type_is_int_and_squared_is_not_more_than_1000(self):
        self.assertEqual(apple(x=2), HELP_YOURSELF_MSG)

    def test_apple_x_type_is_int_and_squared_is_more_than_1000(self):
        self.assertEqual(apple(x=50), HOTTER_MSG)
