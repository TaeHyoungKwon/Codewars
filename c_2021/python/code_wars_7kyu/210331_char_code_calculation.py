import unittest


def calc(x: str) -> int:
    total_1 = "".join(str(ord(ele)) for ele in x)
    total_2 = (1 if ele == "7" else int(ele) for ele in total_1)
    return sum(map(int, total_1)) - sum(total_2)


class TestCalc(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calc(x="abcdef"), 6)
