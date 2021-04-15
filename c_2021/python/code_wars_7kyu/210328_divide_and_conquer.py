from typing import List, Union
import unittest


def div_con(x: List[Union[str, int]]) -> int:
    return sum(ele if isinstance(ele, int) else -int(ele) for ele in x)


class TestDivCon(unittest.TestCase):
    def test_div_con(self):
        self.assertEqual(div_con(x=[9, 3, "7", "3"]), 2)
