import unittest
from itertools import count


class Harshad:
    @staticmethod
    def is_valid(number):
        return number % sum(int(ele) for ele in str(number)) == 0 if number else False

    @staticmethod
    def get_next(number):
        return next(ele for ele in count(number + 1) if Harshad.is_valid(ele))

    @staticmethod
    def get_series(count, start=0):
        def generate(count, start):
            while count > 0:
                if Harshad.is_valid(number=start + 1):
                    yield start + 1
                    count -= 1
                start += 1
        return list(generate(count, start))


class TestHarshad(unittest.TestCase):
    def test_harshad_is_valid_on_true(self):
        self.assertTrue(Harshad.is_valid(number=1))

    def test_harshad_is_valid_on_false(self):
        self.assertFalse(Harshad.is_valid(number=19))

    def test_harshad_get_next(self):
        self.assertEqual(Harshad.get_next(number=17), 18)

    def test_harshad_is_valid_on_getting_series(self):
        self.assertEqual(
            Harshad.get_series(count=20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42]
        )
