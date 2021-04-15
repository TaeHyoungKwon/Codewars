import unittest


def pyramid(n):
    return [[1] * index for index in range(1, n + 1)]


class TestPyramid(unittest.TestCase):
    def test_pyramid_n_is_0(self):
        self.assertEqual(pyramid(n=0), [])

    def test_pyramid_n_is_1(self):
        self.assertEqual(pyramid(n=1), [[1]])

    def test_pyramid_n_is_2(self):
        self.assertEqual(pyramid(n=2), [[1], [1, 1]])

    def test_pyramid_n_is_3(self):
        self.assertEqual(pyramid(n=3), [[1], [1, 1], [1, 1, 1]])
