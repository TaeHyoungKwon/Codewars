import unittest


def lovefunc(flower1, flower2):
    equal = flower1 == flower2
    even_or_odd = (flower1 % 2 == 0 and flower2 % 2 == 1) or (flower1 % 2 == 1 and flower2 % 2 == 0)

    return False if equal else even_or_odd


class TestLoveFunc(unittest.TestCase):
    def test_should_return_false_when_flower1_and_flower2_are_same(self):
        flower1, flower2 = 0, 0
        actual = lovefunc(flower1, flower2)
        self.assertEqual(actual, False)

    def test_should_return_true_when_flower1_is_odd_and_flower2_is_even(self):
        flower1, flower2 = 1, 4
        actual = lovefunc(flower1, flower2)
        self.assertEqual(actual, True)

    def test_should_return_false_when_flower1_is_even_and_flower2_is_odd(self):
        flower1, flower2 = 2, 5
        actual = lovefunc(flower1, flower2)
        self.assertEqual(actual, True)
