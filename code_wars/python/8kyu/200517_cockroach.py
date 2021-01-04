import unittest


def cockroach_speed(s):
    return s * 100000 // 3600
    
    
class TestCockroach(unittest.TestCase):
    def test_should_return_0_when_given_s_is_0(self):
        s = 0
        actual = cockroach_speed(s)
        self.assertEqual(actual, 0)

    def test_cockroach_speed(self):
        s = 1.08
        actual = cockroach_speed(s)
        self.assertEqual(actual, 30)

    def test_cockroach_speed_second_case(self):
        s = 1.09
        actual = cockroach_speed(s)
        self.assertEqual(actual, 30)
