import unittest


def expression_matter(a, b, c):
    c1 = lambda x, y, z: x * (y + z)
    c2 = lambda x, y, z: x * y * z
    c3 = lambda x, y, z: x + y * z
    c4 = lambda x, y, z: (x + y) * z
    c5 = lambda x, y, z: x + y + z
    return max(c1(a, b, c), c2(a, b, c), c3(a, b, c), c4(a, b, c), c5(a, b, c))


class TestExpressionmatter(unittest.TestCase):
    def test_should_return_8_when_given_a_b_c_is_2(self):
        a, b, c = 2, 2, 2
        actual = expression_matter(a, b, c)
        self.assertEqual(actual, 8)
