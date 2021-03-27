from typing import List, Dict
import unittest


def count(array: List[str]) -> Dict[str, int]:
    return {ele: array.count(ele) for ele in array}


class TestCount(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count(array=["a", "a", "b", "b", "b"]), {"a": 2, "b": 3})
