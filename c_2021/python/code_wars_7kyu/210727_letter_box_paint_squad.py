import unittest


def paint_letterboxes(start, finish):
    all_letters = "".join(str(ele) for ele in range(start, finish + 1))
    return [all_letters.count(str(i)) for i in range(10)]


class TestPaintLetterboxes(unittest.TestCase):
    def test_paint_letterboxes(self):
        self.assertEqual(paint_letterboxes(start=125, finish=132), [1, 9, 6, 3, 0, 1, 1, 1, 1, 1])
