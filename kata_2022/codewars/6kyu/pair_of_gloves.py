from itertools import groupby
from collections import Counter

# def number_of_pairs(gloves):
#     def calculate():
#         for _, group in groupby(sorted(gloves)):
#             yield len(list(group)) // 2
#     return sum(calculate())

def number_of_pairs(gloves):

    return sum(c // 2 for c in Counter(gloves).values())

    
class TestNumberOfPairs:
    def test_number_of_pairs(self):
        # assert number_of_pairs(["red","red"]) == 1
        assert number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]) == 4
