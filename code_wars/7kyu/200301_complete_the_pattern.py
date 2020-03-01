import unittest


def pattern(n):
    return "\n".join("".join(str(ele) for ele in range(n, idx, -1)) for idx in range(n))


class TestPattern(unittest.TestCase):
    def test_should_reutnr_1_when_n_is_1(self):
        n = 1
        actual = pattern(n)
        self.assertEqual(actual, "1")

    def test_n_is_more_than_2(self):
        # Given: Set n
        n = 2
        # When: Call pateern(n)
        actual = pattern(n)
        # Then: Should return '21\n2'
        self.assertEqual(actual, "21\n2")

    def test_n_is_more_than_5(self):
        # Given: Set n
        n = 5
        # When: Call pateern(n)
        actual = pattern(n)
        # Then: Should return '21\n2'
        self.assertEqual(actual, "54321\n5432\n543\n54\n5")
