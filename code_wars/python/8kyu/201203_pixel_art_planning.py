import unittest


def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


class TestIsDivisible(unittest.TestCase):
    def test_is_divisible(self):
        self.assertTrue(is_divisible(wall_length=4050, pixel_size=27))
