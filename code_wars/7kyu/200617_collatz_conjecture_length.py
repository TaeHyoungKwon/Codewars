import unittest


def collatz(n):
    print(n)
    cnt = 0
    result = []
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        result.append(n)
        cnt += 1
    print(result)
    return cnt + 1


class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        n = 73567465519280238573
        actual = collatz(n)
        self.assertEqual(actual, 362)
