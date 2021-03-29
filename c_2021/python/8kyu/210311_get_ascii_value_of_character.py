import unittest


def get_ascii(c):
    return ord(c)
    
    
class TestGetAscii(unittest.TestCase):
    def test_get_ascii(self):
        self.assertEqual(get_ascii(c="A"), 65)
