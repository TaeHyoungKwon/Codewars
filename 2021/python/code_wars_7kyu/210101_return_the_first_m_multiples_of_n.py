import unittest


def multiples(m, n):
    return [n * index for index in range(1, m + 1)]


class TestMultiples(unittest.TestCase):
    def test_multiples_with_m_is_3_n_is_5(self):
        self.assertEqual(multiples(m=3, n=5), [5, 10, 15])

    def test_multiples_with_m_is_2_n_is_4(self):
        self.assertEqual(multiples(m=2, n=4), [4, 8])
