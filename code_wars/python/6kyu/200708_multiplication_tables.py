import unittest


def multiplication_table(row, col):
    result = []
    for i in range(1, row + 1):
        temp = []
        for j in range(1, col + 1):
            temp.append(i * j)
        result.append(temp)
    return result
    
    
class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table(self):
        row, col = 3, 3
        actual = multiplication_table(row, col)
        self.assertEqual(actual, [[1,2,3],[2,4,6],[3,6,9]])
