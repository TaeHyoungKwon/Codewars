import unittest


def power_of_two(x):
    if x == 0:
        return False
    while x > 1:
        if x % 2 == 1:
            return False
        x = x // 2
    return True
    
    
class TestPowerOfTwo(unittest.TestCase):
    def test_should_return_false_when_given_x_is_0(self):
        x = 0
        actual = power_of_two(x)
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_x_is_4096(self):
        x = 4096
        actual = power_of_two(x)
        self.assertEqual(actual, True)
