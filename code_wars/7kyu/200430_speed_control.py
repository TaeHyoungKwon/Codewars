import unittest

ONE_HOUR_TO_SECONDS = 3600


def gps(s, x):
    if not x:
        return 0
    delta_distance = [second - first for first, second in zip(x, x[1:])]
    return max(ONE_HOUR_TO_SECONDS * distance // s for distance in delta_distance)
    
    
class TestGps(unittest.TestCase):
    def test_gps(self):
        s, x = 15, [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
        actual = gps(s, x)
        self.assertEqual(actual, 74)

    def test_gps_shoud_return_0_when_given_x_is_empty(self):
        s, x = 15, []
        actual = gps(s, x)
        self.assertEqual(actual, 0)
