import unittest
from typing import Dict, List, Tuple


def sort_dict(d: Dict[int, int]) -> List[Tuple[int, int]]:
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


class TestSortDict(unittest.TestCase):
    def test_sort_dict(self):
        self.assertEqual(sort_dict(d={3: 1, 2: 2, 1: 3}), [(1, 3), (2, 2), (3, 1)])
