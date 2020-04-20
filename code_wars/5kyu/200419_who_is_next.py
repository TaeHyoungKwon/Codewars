import unittest


def who_is_next(names, r):
    while r > len(names):
        r = (r - (len(names) - 1)) // 2
    return names[r - 1]
    
    
class TestWhoIsNext(unittest.TestCase):
    def test_should_return_Sheldon_when_given_r_is_1(self):
        names, r = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1
        actual = who_is_next(names, r)
        self.assertEqual(actual, "Sheldon")

    def test_should_return_Penny_when_given_r_is_52(self):
        names, r = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52
        actual = who_is_next(names, r)
        self.assertEqual(actual, "Penny")

    def test_should_return_Penny_when_given_r_is_7230702951(self):
        names, r = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951
        actual = who_is_next(names, r)
        self.assertEqual(actual, "Leonard")
