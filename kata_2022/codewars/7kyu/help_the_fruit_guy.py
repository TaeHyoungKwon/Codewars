from typing import List, Optional


# My solution
# def remove_rotten(bag_of_fruits: Optional[List[str]]) -> List[str]:
#     if bag_of_fruits is None:
#         return []
#
#     return [
#         fruit_name.lstrip("rotten").lower() if fruit_name.startswith("rotten") else fruit_name
#         for fruit_name in bag_of_fruits
#     ]

def remove_rotten(bag_of_fruits: Optional[List[str]]) -> List[str]:
    return [f.replace('rotten', '').lower() for f in bag_of_fruits or []]


class TestRemoveRotten:
    def test_remove_rotten_edge_case(self):
        assert remove_rotten(bag_of_fruits=[]) == []
        assert remove_rotten(bag_of_fruits=None) == []

    def test_remove_rotten_common_case(self):
        assert remove_rotten(
            bag_of_fruits=["rottenApple", "rottenBanana", "rottenApple", "rottenPineapple", "rottenKiwi"]
        ) == ["apple", "banana", "apple", "pineapple", "kiwi"]


"""
Problem
    * Replace all the rotten pieces of fruit from list
Solution
    * Check that each fruit name starts with "rotten" or not all fruit in array
    * If it starts with "rotten", Delete rotten and return lowercase fruit name
Conditions
    * if the array is None, should return []
    * rotten fruit name will be calmelcase -> rottenBanana
    * The returned array should be lowercase
Steps
    1. Start loop all elements - bag_of_fruits: list[str]
    2. Check that each fruit name starts with "rotten" or not
    3. If True, Delete rotten part and make word lowercase
    4. If False, just pass
Tests
    Cases:
        1. common case
        2. edge case
            * bag_of_fruits is empty
            * bag_of_fruits is None
"""