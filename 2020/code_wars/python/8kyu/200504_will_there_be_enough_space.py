import unittest


def enough(cap, on, wait):
    print(cap, on, wait)
    return 0 if cap - on >= wait else wait - (cap - on)


class TestEnough(unittest.TestCase):
    def test_should_return_0_on_enough_space(self):
        cap, on, wait = 10, 5, 5
        actual = enough(cap, on, wait)
        self.assertEqual(actual, 0)

    def test_should_return_10_on_not_enough_space(self):
        cap, on, wait = 100, 60, 50
        actual = enough(cap, on, wait)
        self.assertEqual(actual, 10)
