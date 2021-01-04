import unittest


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    rest_of_blue = (blue_start - blue_pulled)
    rest_of_red = (red_start - red_pulled)
    return rest_of_blue / (rest_of_blue + rest_of_red)
    
    
class TestGuessBlue(unittest.TestCase):
    def test_guess_blue(self):
        blue_start, red_start, blue_pulled, red_pulled = 5, 7, 4, 3
        actual = guess_blue(blue_start, red_start, blue_pulled, red_pulled)
        self.assertEqual(actual, 0.2)
