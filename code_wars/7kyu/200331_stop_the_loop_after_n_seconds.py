import unittest


def increment_loop(n):
    # 못품..
    i = 0
    while i < n:
        i += 1
    return i
    
    
class TestIncrementLoop(unittest.TestCase):
    def test_should_return_3_when_given_n_is_3(self):
        n = 3
        actual = increment_loop(n)
        self.assertEqual(actual, 3)

    def test_should_return_1_when_given_n_is_less_than_1(self):
        n = 0.45
        actual = increment_loop(n)
        self.assertEqual(actual, 1)
