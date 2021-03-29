import unittest


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m
    
    
class TestPaperWork(unittest.TestCase):
    def test_should_return_25_when_given_n_m_is_5(self):
        actual = paperwork(5, 5)
        self.assertEqual(actual, 25)

    def test_should_return_0_when_given_n_or_m_is_negative(self):
        actual = paperwork(25, -25)
        self.assertEqual(actual, 0)
