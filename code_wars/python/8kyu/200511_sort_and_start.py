import unittest


def two_sort(array):
    return '***'.join(list(sorted(array)[0]))
    
    
class TestTwoSort(unittest.TestCase):
    def test_should_fail(self):
        array = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
        actual = two_sort(array)
        self.assertEqual(actual, 'b***i***t***c***o***i***n')
