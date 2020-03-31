import unittest


def last(x):
    return sorted([ele for ele in x.split()], key=lambda char: char[-1])
    
    
class TestSortByLastChar(unittest.TestCase):
    def test_sort_by_last_char(self):
        x = "man i need a taxi up to ubud"
        actual = last(x)
        self.assertEqual(actual, ["a", "need", "ubud", "i", "taxi", "man", "to", "up"])
