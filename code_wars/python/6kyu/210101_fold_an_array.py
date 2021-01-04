import unittest


def fold_array(array, runs):
    for i in range(runs):
        temp = []
        mid_index = len(array) // 2
        if len(array) % 2:
            temp.append(array[mid_index])
            for j in range(1, mid_index + 1):
                temp.append(array[mid_index - j] + array[mid_index + j])
        else:
            temp = [i + j for i, j in zip(array[:mid_index], array[::-1][:mid_index])][::-1]
        array = temp
    return temp[::-1]


class TestFoldArray(unittest.TestCase):
    def test_fold_array_with_odd_count_case_1(self):
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 1), [6, 6, 3])

    def test_fold_array_with_odd_count_case_2(self):
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 2), [9, 6])

    def test_fold_array_with_odd_count_case_3(self):
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 3), [15])

    def test_fold_array_with_edge_case(self):
        self.assertEqual(
            fold_array(
                [
                    -164,
                    -124,
                    200,
                    69,
                    7,
                    143,
                    54,
                    -159,
                    -189,
                    -43,
                    65,
                    -7,
                    195,
                    -19,
                    -46,
                    -24,
                    177,
                    -32,
                    -123,
                    182,
                    -77,
                    66,
                    33,
                    188,
                    -11,
                    80,
                ],
                15,
            ),
            [441],
        )
