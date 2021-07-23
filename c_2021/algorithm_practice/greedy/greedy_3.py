# 1이 될 때까지 p.92
import unittest


def to_be_number_one(n, k):
    count = 0
    for _ in range(n):
        if n == 1:
            break
        q, r = divmod(n, k)
        if r == 0:
            n //= k
        else:
            n -= 1
        count += 1
    return count


class TestTobeNumberOne(unittest.TestCase):
    def test_to_be_number_one(self):
        self.assertEqual(to_be_number_one(n=25, k=5), 2)
        self.assertEqual(to_be_number_one(n=25, k=3), 6)
        self.assertEqual(to_be_number_one(n=17, k=4), 3)
