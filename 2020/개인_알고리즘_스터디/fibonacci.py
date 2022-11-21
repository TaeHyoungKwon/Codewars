import unittest

MEMOIZATION = [0] * 100


def fibonacci(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    if MEMOIZATION[num] != 0:
        return MEMOIZATION[num]
    MEMOIZATION[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return MEMOIZATION[num]


def fibonacci(num):
    a, b = 0, 1
    for i in range(0, num):
        a, b = b, a + b
        if b > num:
            b = sum(map(int, str(b)))
    return a



num = int(input())
print(fibonacci(num))


class TestFibonacci(unittest.TestCase):
    def test_should_return_1_when_given_n_is_1(self):
        n = 1
        actual = fibonacci(n)
        self.assertEqual(actual, 1)

    def test_should_return_1_when_given_n_is_2(self):
        n = 2
        actual = fibonacci(n)
        self.assertEqual(actual, 1)

    def test_should_return_2_when_given_n_is_3(self):
        n = 3
        actual = fibonacci(n)
        self.assertEqual(actual, 2)

    def test_should_return_3_when_given_n_is_4(self):
        n = 4
        actual = fibonacci(n)
        self.assertEqual(actual, 3)

    def test_should_return_55_when_given_n_is_10(self):
        n = 10
        actual = fibonacci(n)
        self.assertEqual(actual, 55)

