import unittest


def manhattan_distance(point_a, point_b):
    a_x, a_y = point_a
    b_x, b_y = point_b
    return abs(b_x - a_x) + abs(b_y - a_y)


class TestManhattaDistance(unittest.TestCase):
    def test_manhattan_distance(self):
        self.assertEqual(manhattan_distance([5, 4], [3, 2]), 4)
