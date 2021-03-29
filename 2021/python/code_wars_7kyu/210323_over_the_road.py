import unittest


def over_the_road(address, n):
    odd_map = {}
    even_map = {}
    max_even = 2 * n
    for i in range(1, n + 1):
        odd_map[2 * i - 1] = -2 * i + (max_even + 2)
        # even_map[-2 * i + (max_even + 2)] = 2 * i - 1

    if address % 2:
        return odd_map[address]
    else:
        return even_map[address]


class TestOverTheRoad(unittest.TestCase):
    def test_over_the_road_with_address_odd(self):
        self.assertEqual(over_the_road(1, 3), 6)

    def test_over_the_road_with_address_even(self):
        self.assertEqual(over_the_road(2, 3), 5)

    def test_over_the_road_with_address_edge(self):
        self.assertEqual(over_the_road(23633656673, 310027696726), 596421736780)
