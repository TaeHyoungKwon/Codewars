import unittest


def mygcd(x, y):
    while y:
        x, y = y, x % y
    return x
    
    
class TestMygCd(unittest.TestCase):
    def test_should_return_1_when_given_x_and_y_is_1(self):
        x, y = 1, 1
        actual = mygcd(x, y)
        self.assertEqual(actual, 1)

    def test_mygcd(self):
        x, y = 30, 12
        actual = mygcd(x, y)
        self.assertEqual(actual, 6)
