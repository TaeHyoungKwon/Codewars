import unittest


def greek_comparator(lhs, rhs):
    if lhs > rhs:
        return 1
    elif lhs < rhs:
        return -1
    else:
        return 0
    
    
class TestGreekComparator(unittest.TestCase):

    def test_should_return_0_when_given_lhs_and_rhs_is_same(self):
        lhs, rhs = 'psi', 'psi'
        actual = greek_comparator(lhs, rhs)
        self.assertEqual(actual, 0)

    def test_should_return_1_when_given_lhs_is_less_than_rhs(self):
        lhs, rhs = 'upsilon', 'rho'
        actual = greek_comparator(lhs, rhs)
        self.assertEqual(actual, 1)

    def test_should_return_negative_1_when_given_rhs_is_less_than_lhs(self):
        lhs, rhs = 'alpha', 'beta'
        actual = greek_comparator(lhs, rhs)
        self.assertEqual(actual, -1)
