import unittest

BUMPS_OVER_15_MSG = "Car Dead"
BUMPS_UNDER_15_MSG = "Woohoo!"


def bumps(road):
    return BUMPS_UNDER_15_MSG if road.count("n") <= 15 else BUMPS_OVER_15_MSG


class TestBumps(unittest.TestCase):
    def test_bumps_with_bumps_is_equal_lower_than_15(self):
        self.assertEqual(bumps(road="n"), BUMPS_UNDER_15_MSG)

    def test_bumps_with_bumps_is_over_15(self):
        self.assertEqual(bumps(road="_nnnnnnn_n__n______nn__nn_nnn"), BUMPS_OVER_15_MSG)
