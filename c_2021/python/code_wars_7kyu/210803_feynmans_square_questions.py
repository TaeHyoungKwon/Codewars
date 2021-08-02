import unittest


def count_square(n):
    return sum(i * i for i in range(1, n + 1))


class TestCountSquare(unittest.TestCase):
    def test_count_square_when_n_is_1(self):
        self.assertEqual(count_square(n=1), 1)

    def test_count_square_when_n_is_2(self):
        self.assertEqual(count_square(n=2), 5)

    def test_count_square_when_n_is_3(self):
        self.assertEqual(count_square(n=3), 14)
