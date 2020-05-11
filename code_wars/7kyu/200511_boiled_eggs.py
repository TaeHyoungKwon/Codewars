import unittest
import math


def cooking_time(eggs):
    return math.ceil(eggs / 8) * 5
    
    
class TestCookingTime(unittest.TestCase):
    def test_should_return_0_when__given_eggs_is_0(self):
        eggs = 0
        actual = cooking_time(eggs)
        self.assertEqual(actual, 0)

    def test_should_return_5_when__given_eggs_is_5(self):
        eggs = 5
        actual = cooking_time(eggs)
        self.assertEqual(actual, 5)
