import unittest


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= fuel_left * mpg


class TestZeroFuel(unittest.TestCase):
    def test_possible_to_get_to_the_pump(self):
        actual = zero_fuel(distance_to_pump=50, mpg=25, fuel_left=2)
        self.assertEqual(actual, True)

    def test_not_possible_to_get_to_the_pump(self):
        actual = zero_fuel(distance_to_pump=100, mpg=50, fuel_left=1)
        self.assertEqual(actual, False)
