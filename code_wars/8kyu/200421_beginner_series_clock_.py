import unittest


def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000
    
    
class TestPast(unittest.TestCase):
    def test_should_return_0_when_all_of_argument_values_is_0(self):
        h, m, s = 0, 0, 0
        actual = past(h, m, s)
        self.assertEqual(actual, 0)

    def test_should_return_61000_when_m_is_1_and_s_is_1(self):
        h, m, s = 0, 1, 1
        actual = past(h, m, s)
        self.assertEqual(actual, 61000)
