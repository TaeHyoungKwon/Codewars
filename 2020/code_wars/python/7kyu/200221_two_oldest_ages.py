import unittest


def two_oldest_ages(ages):
    return sorted(ages)[len(ages) - 2:]
    
    
class TestTwoOldestAges(unittest.TestCase):
    def test_should_return_1_and_10_when_given_ages_is_10_and_1(self):
        ages = [10, 1]
        actual = two_oldest_ages(ages)
        self.assertEqual(actual, [1, 10])

    def test_two_oldest_ages(self):
        ages = [6, 5, 83, 5, 3, 18]
        actual = two_oldest_ages(ages)
        self.assertEqual(actual, [18, 83])
