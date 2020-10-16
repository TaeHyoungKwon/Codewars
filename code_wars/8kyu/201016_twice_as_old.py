import unittest


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)
    
    
class TestTwiceAsOld(unittest.TestCase):
    def test_twice_as_old_case_one(self):
        dad_years_old, son_years_old = 36, 7
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 22)

    def test_twice_as_old_case_two(self):
        dad_years_old, son_years_old = 55, 30
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 5)

    def test_twice_as_old_case_three(self):
        dad_years_old, son_years_old = 29, 0
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 29)
