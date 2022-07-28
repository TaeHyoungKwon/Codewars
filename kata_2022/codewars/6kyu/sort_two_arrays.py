from typing import List, Union


def sort_two_arrays(arr1: List[int], arr2: List[int]) -> List[List[int]]:

    def _sorted(_arr: List[int]) -> List[List[int]]:
        return sorted([[ele, index] for index, ele in enumerate(_arr)])

    def _rearrange(_arr, _sorted_list: List[List[int]]) -> list[int]:
        return [_arr[ele[1]] for ele in _sorted_list]

    return [_rearrange(arr1, _sorted(arr2)), _rearrange(arr2, _sorted(arr1))]


class TestSortTwoArrays:
    def test_sort_two_arrays(self):
        assert sort_two_arrays([5, 4, 3, 2, 1], [6, 5, 7, 8, 9]) == [[4, 5, 3, 2, 1], [9, 8, 7, 5, 6]]