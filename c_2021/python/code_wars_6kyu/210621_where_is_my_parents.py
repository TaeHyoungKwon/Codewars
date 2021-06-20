import unittest
from itertools import groupby


def find_children(dancing_brigade: str) -> str:
    return "".join("".join(group).capitalize() for _, group in groupby(sorted(dancing_brigade.lower())))
    
    
class TestFindChildren(unittest.TestCase):
    def test_find_children(self):
        self.assertEqual(find_children(dancing_brigade="CbcBcbaA"), "AaBbbCcc")
        