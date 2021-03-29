import math
import unittest

TWO_DECIMAL_PLACES = 2

def furthestDistance(arr):
    # 테스트는 통과하는데, 답 제출이 안됨..
    max_by_first_element, min_by_first_element = max(arr, key=lambda x: x[0]), min(arr, key=lambda x: x[0])
    max_by_second_element, min_by_second_element = max(arr, key=lambda x: x[1]), min(arr, key=lambda x: x[1])
    print(max_by_first_element, min_by_first_element)
    print(max_by_second_element, min_by_second_element)
    return max(
        round(math.sqrt(
            abs((max_by_first_element[0] - min_by_first_element[0]) ** 2 +
                (max_by_first_element[1] - min_by_first_element[1]) ** 2)), TWO_DECIMAL_PLACES),
        round(math.sqrt(
            abs((max_by_second_element[0] - min_by_second_element[0]) ** 2 +
                (max_by_second_element[1] - min_by_second_element[1]) ** 2)), TWO_DECIMAL_PLACES)
    )
    
    
class TestFurthestDistance(unittest.TestCase):
    def test_furthest_distance(self):
        arr = [[3, 8], [10, 4]]
        actual = furthestDistance(arr)
        self.assertEqual(actual, 8.06)

    def test_furthest_distance_arr_count_more_than_three(self):
        arr = [[1, 2], [3, 8], [4, 3]]
        actual = furthestDistance(arr)
        self.assertEqual(actual, 6.32)

    def test_furthest_distance_arr_edge_case(self):
        arr = [[8, 10], [2, 4], [8, 15], [6, 3], [7, 0], [12, 3], [0, 1], [1, 14]]
        actual = furthestDistance(arr)
        self.assertEqual(actual, 15.03)


