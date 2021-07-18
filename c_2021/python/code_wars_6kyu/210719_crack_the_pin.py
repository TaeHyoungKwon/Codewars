import hashlib
import unittest
from itertools import count


def crack(hash):
    return next(str(i).zfill(5) for i in count(0) if hashlib.md5(str(i).zfill(5).encode()).hexdigest() == hash)


class TestCrack(unittest.TestCase):
    def test_crack(self):
        self.assertEqual(crack(hash="827ccb0eea8a706c4c34a16891f84e7b"), "12345")
