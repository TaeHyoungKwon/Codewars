import unittest


def sort_ranks(ranks):
    for ele in ranks:
        if ele 
    return sorted(ranks)
    
    
class TestSortRanks(unittest.TestCase):
    def test_sort_ranks(self):
        ranks = ['1.1', '1', '1.1.1.1', '1.1.1']
        actual = sort_ranks(ranks)
        self.assertEqual(actual, ['1', '1.1', '1.1.1', '1.1.1.1'])
