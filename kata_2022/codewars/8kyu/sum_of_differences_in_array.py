from itertools import zip_longest

import pytest


def sum_of_differences(arr: list[int]) -> int:
    if not arr or len(arr) == 1:
        return 0
    descending_arr = sorted(arr, reverse=True)
    return sum(first - second for first, second in zip(descending_arr, descending_arr[1:]))


class TestSumOfDifferences:
    def test_sum_of_differences_on_exception(self):
        assert sum_of_differences(arr=[]) == 0
        assert sum_of_differences(arr=[0]) == 0

    def test_sum_of_differences_on_common_case(self):
        assert sum_of_differences(arr=[1, 2, 10]) == 9
        assert sum_of_differences([-3, -2, -1]) == 2
