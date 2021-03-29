import unittest


def plural(n):
    return n != 1
    
    
class TestPlural(unittest.TestCase):
    def test_should_return_false_when_given_n_is_1(self):
        self.assertFalse(plural(1))

    def test_should_return_true_when_given_n_is_not_1(self):
        self.assertTrue(plural(100))
