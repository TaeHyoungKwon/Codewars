import unittest


def fortune(f0, p, c0, n, i) -> bool:
    f = f0
    c = c0
    for count in range(1, n):
        f = int(f + (f * p * 0.01))
        if count > 1:
            c = int(c + (c * i * 0.01))
        f -= int(c)
    return f >= 0


class TestFortune(unittest.TestCase):
    def test_fortune(self):
        self.assertTrue(fortune(f0=100000, p=1, c0=2000, n=15, i=1))

    def test_fortune_with_big_f0(self):
        self.assertTrue(fortune(f0=100000000, p=1, c0=100000, n=50, i=1))

    def test_fortune_with_big_f0_case_2(self):
        self.assertFalse(fortune(f0=100000000, p=1.5, c0=10000000, n=50, i=1))

    def test_fortune_with_edge_case(self):
        self.assertFalse(fortune(f0=9999, p=61.8161, c0=10000.0, n=3, i=0))

    def test_fortune_with_edge_case_2(self):
        self.assertTrue(fortune(f0=10000.0, p=0, c0=10000.0, n=2, i=0))