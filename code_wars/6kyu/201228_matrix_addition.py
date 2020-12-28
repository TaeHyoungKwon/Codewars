import unittest


def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


class TestMatrixAddition(unittest.TestCase):
    def test_matrix_addition_with_one_element(self):
        self.assertEqual(matrix_addition([[1]], [[2]]), [[3]])

    def test_matrix_addition_with_two_element(self):
        self.assertEqual(matrix_addition([[1, 2], [2, 3]], [[1, 2], [2, 3]]), [[2, 4], [4, 6]])

    def test_matrix_addition_with_three_element(self):
        self.assertEqual(
            matrix_addition([[1, 2, 3], [3, 2, 1], [1, 1, 1]], [[2, 2, 1], [3, 2, 3], [1, 1, 3]]),
            [[3, 4, 4], [6, 4, 4], [2, 2, 4]],
        )
