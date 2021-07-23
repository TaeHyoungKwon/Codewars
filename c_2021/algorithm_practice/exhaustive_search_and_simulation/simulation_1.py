import unittest
from typing import List, Tuple

MOVE_MAP_X = [-1, 1, 0, 0]
MOVE_MAP_Y = [0, 0, -1, 1]
MOVE_TYPES = ("L", "R", "U", "D")


def _is_valid_position(next_x, next_y, max_size):
    return (1 <= next_x <= max_size) and (1 <= next_y <= max_size)


def _move(plan, x, y) -> Tuple[int, int]:
    index = MOVE_TYPES.index(plan)
    return x + MOVE_MAP_X[index], y + MOVE_MAP_Y[index]


def find_path(plans: List[str]) -> Tuple[int, int]:
    x, y = 1, 1
    max_size = len(plans)
    for plan in plans:
        next_x, next_y = _move(plan, x, y)
        if not _is_valid_position(next_x, next_y, max_size):
            continue
        x, y = next_x, next_y
    return y, x


class TestFindPath(unittest.TestCase):
    def test_find_path(self):
        self.assertEqual(find_path(plans=["R", "R", "R", "U", "D", "D"]), (3, 4))
