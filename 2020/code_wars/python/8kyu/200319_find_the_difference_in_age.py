import unittest


def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))
    
    
class TestDifferenceInAges(unittest.TestCase):
    def test_difference_in_ages(self):
        # Given: Set ages -> array
        ages = [1, 2, 3, 4, 5]
        # When: Call difference_in_ages
        actual = difference_in_ages(ages)
        # Then: should return [youngest, oldest, difference between the youngest and oldest age]
        self.assertEqual(actual, (1, 5, 4))
