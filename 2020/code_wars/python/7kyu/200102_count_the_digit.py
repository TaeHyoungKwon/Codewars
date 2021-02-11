import unittest


def nb_dig(n, d):

    return sum(str(ele ** 2).count(str(d)) for ele in range(n + 1))

    
class TestNbDig(unittest.TestCase):
    def test_should_return_1_when_given_n_is_4_and_d_is_0(self):
        # Given: Set n, d
        n, d = 4, 1
        # When: Call nb_dig
        actual = nb_dig(n, d)
        # Then: should return 1
        self.assertEqual(actual, 2)

    def test_should_return_2_when_given_n_is_6_and_d_is_1(self):
        # Given: Set n, d
        n, d = 6, 1
        # When: Call nb_dig
        actual = nb_dig(n, d)
        # Then: should return 1
        self.assertEqual(actual, 2)

    def test_should_return_4_when_given_n_is_10_and_d_is_1(self):
        # Given: Set n, d
        n, d = 10, 1
        # When: Call nb_dig
        actual = nb_dig(n, d)`
        # Then: should return 4
        self.assertEqual(actual, 4)

    def test_should_return_11905_when_given_n_is_11549_and_d_is_1(self):
        # Given: Set n, d
        n, d = 11549, 1
        # When: Call nb_dig
        actual = nb_dig(n, d)
        # Then: should return 7733
        self.assertEqual(actual, 11905)


