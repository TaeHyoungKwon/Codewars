import unittest


def vampire_test(x, y):
    return sorted(str(x * y)) == sorted(''.join([str(x), str(y)]))


class TestVampireTest(unittest.TestCase):
    def test_vampire_test_should_return_true(self):
        x, y = 21, 6
        actual = vampire_test(x, y)
        self.assertEqual(actual, True)

    def test_vampire_test_should_return_false(self):
        x, y = -246, -510
        actual = vampire_test(x, y)
        self.assertEqual(actual, False)
