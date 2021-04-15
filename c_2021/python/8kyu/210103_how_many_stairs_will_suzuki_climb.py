import unittest

TWENTY_YEARS = 20


def stairs_in_20(stairs):
    return sum(sum(day) for day in stairs) * TWENTY_YEARS


class TestStairsIn20(unittest.TestCase):
    def test_stairs_in_20(self):
        stairs = [[1], [2], [3], [4], [5], [6], [7]]
        self.assertEqual(stairs_in_20(stairs), 28 * TWENTY_YEARS)
