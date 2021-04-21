import unittest
from typing import Dict, List, Optional


def pluck(objs: List[Dict[str, int]], name: str) -> List[Optional[int]]:
    return [obj.get(name) for obj in objs]


class TestPluck(unittest.TestCase):
    def test_pluck(self):
        self.assertEqual(
            pluck(
                [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}, {"a": 7, "b": 8, "c": 9}, {"a": 10, "b": 11}], "a"
            ),
            [1, 4, 7, 10],
        )
