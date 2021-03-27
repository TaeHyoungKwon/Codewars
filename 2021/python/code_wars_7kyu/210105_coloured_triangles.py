import unittest

COLOR = {'R', 'G', 'B'}


def triangle(row):
    if len(row) == 1:
        return row

    while True:
        temp = []
        for c1, c2 in zip(row, row[1:]):
            if c1 != c2:
                temp.append((COLOR - {c1, c2}).pop())
            else:
                temp.append(c1)
            row = temp
        if len(temp) == 1:
            return temp[0]


class TestTriangle(unittest.TestCase):
    def test_triangle_row_length_is_one(self):
        self.assertEqual(triangle('B'), 'B')

    def test_triangle_row_length_is_two_with_different_color(self):
        self.assertEqual(triangle('GB'), 'R')

    def test_triangle_row_length_is_two_with_same_color(self):
        self.assertEqual(triangle('RR'), 'R')

    def test_triangle_row_length_is_three_with_same_color(self):
        self.assertEqual(triangle('RRR'), 'R')

    def test_triangle_row_length_is_four_with_same_color(self):
        self.assertEqual(triangle('RGBG'), 'B')
