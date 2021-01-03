import unittest


def _inner_get_triangle_type(a, b, c):
    add_square_shortest_two_sides = a ** 2 + b ** 2
    square_longest_side = c ** 2

    if add_square_shortest_two_sides - square_longest_side > 0:
        return 1

    elif add_square_shortest_two_sides - square_longest_side == 0:
        return 2

    elif add_square_shortest_two_sides - square_longest_side < 0:
        return 3


def triangle_type(a, b, c):
    c, a, b = sorted([a, b, c], reverse=True)
    if a + b <= c:
        return 0
    return _inner_get_triangle_type(a, b, c)


class TestTriangleType(unittest.TestCase):
    def test_triangle_type_with_none(self):
        self.assertEqual(triangle_type(7, 3, 2), 0)

    def test_triangle_type_with_right(self):
        self.assertEqual(triangle_type(8, 7, 5), 1)

    def test_triangle_type_with_acute(self):
        self.assertEqual(triangle_type(3, 4, 5), 2)

    def test_triangle_type_with_obtuse(self):
        self.assertEqual(triangle_type(7, 12, 8), 3)


"""
* 조건
None
  1. None, 3개의 면 삼각형을 이룰 수 없을 때, --> 완료
  2. None, 한개의 각도 180도 일 떄,

acute - 모든 각이 90도 이
* 1
right - 1개의 각이 무조건 90도
* 2
obtuse - 1개 이상이 90도
* 3
"""