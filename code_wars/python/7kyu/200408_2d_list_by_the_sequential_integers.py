import unittest


def make_2d_list(head, row, col):
    result = []
    temp = []
    multiply_of_row_and_col = row * col

    if head == 0 and (row == 0 or col == 0):
        return [[]]

    for idx, num in enumerate(range(head, multiply_of_row_and_col + head), 1):
        temp.append(num)
        if idx % col == 0:
            result.append(temp)
            temp = []

    return result
    
    
class TestMake2DList(unittest.TestCase):
    def test_make_2d_list(self):
        head, row, col = 1, 2, 3
        actual = make_2d_list(head, row, col)
        self.assertEqual(actual, [[1, 2, 3], [4, 5, 6]])

    def test_make_2d_list_with_big_num(self):
        head, row, col = 10**10, 2, 2
        actual = make_2d_list(head, row, col)
        self.assertEqual(actual, [[10000000000, 10000000001], [10000000002, 10000000003]])

    def test_make_2d_list_with_small_col_num(self):
        head, row, col = 5, 6, 1
        actual = make_2d_list(head, row, col)
        self.assertEqual(actual, [[5], [6], [7], [8], [9], [10]])

    def test_make_2d_list_with_head_and_col_is_zero(self):
        head, row, col = 0, 1, 0
        actual = make_2d_list(head, row, col)
        self.assertEqual(actual, [[]])
