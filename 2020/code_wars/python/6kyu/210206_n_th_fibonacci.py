import unittest


def nth_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return nth_fib(n - 1) + nth_fib(n - 2)
    
    
class TestNthFib(unittest.TestCase):
    def test_nth_fib_with_n_is_1(self):
        self.assertEqual(nth_fib(n=1), 0)

    def test_nth_fib_with_n_is_2(self):
        self.assertEqual(nth_fib(n=2), 1)

    def test_nth_fib_with_n_is_3(self):
        self.assertEqual(nth_fib(n=3), 1)

    def test_nth_fib_with_n_is_4(self):
        self.assertEqual(nth_fib(n=4), 2)

    def test_nth_fib_with_n_is_5(self):
        self.assertEqual(nth_fib(n=5), 3)

    def test_nth_fib_with_n_is_6(self):
        self.assertEqual(nth_fib(n=6), 5)
