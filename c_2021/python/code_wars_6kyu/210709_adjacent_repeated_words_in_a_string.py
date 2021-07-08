import unittest
from itertools import groupby


def count_adjacent_pairs(st):
    st = st.split()
    return sum(list(group).count(key) > 1 for key, group in groupby(map(str.lower, st)))


class TestCountAdjacentPairs(unittest.TestCase):
    def test_count_adjacent_pairs(self):
        self.assertEqual(count_adjacent_pairs(st="orange Orange kiwi pineapple apple"), 1)

    def test_count_adjacent_pairs_with_edge(self):
        self.assertEqual(
            count_adjacent_pairs(
                st="HAsatTR HaSAtTr hasaTTR INPut InpUT inPuT rEPR rEPR REPr rEpr AScII aSciI aSCii InPuT INpuT iNpuT inpUt"
            ),
            5,
        )
