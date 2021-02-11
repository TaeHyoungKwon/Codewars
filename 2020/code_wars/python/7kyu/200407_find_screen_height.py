import unittest


def find_screen_height(width, ratio):
    ratio_width, ratio_height = ratio.split(':')
    result = (width * int(ratio_height)) // int(ratio_width)
    return str(width) + 'x' + str(result)
    
    
class TestFindScreenSize(unittest.TestCase):
    def test_find_screen_height(self):
        width = 1024
        actual = find_screen_height(width, '4:3')
        self.assertEqual(actual, '1024x768')
