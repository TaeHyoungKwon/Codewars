import unittest


def pairs(ar):
    number_pairs = list(zip(ar, ar[1:]))[::2]
    print(number_pairs)
    return sum(abs(first - last) == 1 for first, last in number_pairs)


class TestPairs(unittest.TestCase):
    def test_pairs_common_case_1(self):
        self.assertEqual(pairs(ar=[1, 2, 5, 8, -4, -3, 7, 6, 5]), 3)

    def test_pairs_common_case_2(self):
        self.assertEqual(pairs(ar=[21, 20, 22, 40, 39, -56, 30, -55, 95, 94]), 2)
