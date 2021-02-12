import unittest


def divisible_by_three(st):
    while len(st) != 1:
        st = str(sum(int(ele) for ele in st))
    return int(st) in {0, 3, 6, 9}


class TestDivisibleByThree(unittest.TestCase):
    def test_divisible_by_three_should_return_true_when_st_is_divisible_by_three(self):
        self.assertTrue(divisible_by_three(st='123'))

    def test_divisible_by_three_should_return_false_when_st_is_not_divisible_by_three(self):
        self.assertFalse(divisible_by_three(st='124'))

    def test_divisible_by_three(self):
        self.assertTrue(divisible_by_three(st='333333333'))
