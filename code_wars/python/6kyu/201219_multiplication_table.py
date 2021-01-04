import unittest


def multiplication_table(size):
    size = range(1, size + 1)
    return [[i * j for j in size] for i in size]


class TestMultiplicationTable(unittest.TestCase):
    def test_should_fail(self):
        self.assertEqual(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
