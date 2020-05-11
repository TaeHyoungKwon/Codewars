import unittest


def get_size(w, h, d):
    return [2 * ((w * h) + (w * d) + (h * d)), w * h * d]
    
    
class TestGetSize(unittest.TestCase):
    def test_get_size(self):
        w, h, d = 1, 1, 1
        actual = get_size(w, h, d)
        self.assertEqual(actual, [6, 1])
