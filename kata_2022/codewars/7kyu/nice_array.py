from typing import List


def is_nice(arr: List[int]) -> bool:
    s = set(arr)
    return bool(arr and all(x - 1 in s or x + 1 in s for x in arr))


# def is_nice(arr: List[int]) -> bool:
#     if not arr:
#         return False
#     for ele in arr:
#         prev_num = ele - 1
#         next_num = ele + 1
#         if not (prev_num in arr or next_num in arr):
#             return False
#     return True


class TestIsNice:
    def test_is_nice_with_edge(self):
        assert is_nice(arr=[]) is False

    def test_is_nice_with_common(self):
        assert is_nice(arr=[2, 10, 9, 3]) is True
        assert is_nice(arr=[4, 2, 1]) is False


"""
Problem
    * Write a function that returns true if arr argument is a nice array, else false
Solution
    * Just do steps below
Conditions
    * input / output
        * input: arr: List[int] / output -> bool
    * edge cases
        1. If arr is empty, arr is not Nice Array
Steps
    1. Take arr array
    2. Iterate for loop
        1. Check existing element that equal to value - 1 or value + 1
            * if exists -> pass
            * else -> return False
    3. After, all elements Checked from loop, function should return True
Tests
    * common cases
        1. Array is Nice Array
        2. Array is not Nice Array
    * edge cases
        1. If arr is empty, arr is not Nice Array
        
"""
