from typing import Dict
import unittest


def split_the_bill(x: Dict[str, int]) -> Dict[str, int]:
    standard_value = sum(x.values()) / len(x)
    new = {}
    for index, (key, value) in enumerate(x.items()):
        new[key] = round(value - standard_value, 2)
    return new


class TestSplitTheBill(unittest.TestCase):
    def test_split_the_bill(self):
        self.assertEqual(
            split_the_bill(x={"A": 40, "B": 25, "C": 10, "D": 153, "E": 58}),
            {"A": -17.2, "B": -32.2, "C": -47.2, "D": 95.8, "E": 0.8},
        )
