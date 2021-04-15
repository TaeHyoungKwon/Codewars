import unittest


def mineLocation(field):
    return next([i, j] for i, row in enumerate(field) for j, column in enumerate(row) if column)


class TestMineLocation(unittest.TestCase):
    def test_minelocation(self):
        self.assertEqual(mineLocation([[1, 0], [0, 0]]), [0, 0])
