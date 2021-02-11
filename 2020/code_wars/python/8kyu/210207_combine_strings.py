import unittest


def combine_names(name1, name2):
    return f"{name1} {name2}"
    
    
class TestCombineName(unittest.TestCase):
    def test_combine_names(self):
        self.assertEqual(combine_names(name1="James", name2="Stevens"), "James Stevens")
