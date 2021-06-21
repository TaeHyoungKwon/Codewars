import unittest

edge_ordinal = {11, 12, 13}

ordinal_map = {
    1: "st",
    2: "nd",
    3: "rd",
}


def number_to_ordinal(n):
    if n == 0:
        return '0'
    n = str(n)
    if int(n[len(n) - 2:]) in edge_ordinal:
        return f"{n}th"

    ordinal = ordinal_map.get(int(n[-1]))
    if ordinal:
        return f"{n}{ordinal}"

    return f"{n}th"
    
    
class TestNumberToOrdinal(unittest.TestCase):
    def test_number_to_ordinal_on_default_edge(self):
        self.assertEqual(number_to_ordinal(n=1), '1st')
        self.assertEqual(number_to_ordinal(n=2), '2nd')
        self.assertEqual(number_to_ordinal(n=3), '3rd')

    def test_number_to_ordinal_on_edge(self):
        self.assertEqual(number_to_ordinal(n=11), '11th')
        self.assertEqual(number_to_ordinal(n=12), '12th')
        self.assertEqual(number_to_ordinal(n=112), '112th')

    def test_number_to_ordinal(self):
        self.assertEqual(number_to_ordinal(n=9), '9th')
        self.assertEqual(number_to_ordinal(n=10), '10th')
        self.assertEqual(number_to_ordinal(n=33), '33rd')

    def test_number_to_ordinal_on_n_is_0(self):
        self.assertEqual(number_to_ordinal(n=0), '0')
        