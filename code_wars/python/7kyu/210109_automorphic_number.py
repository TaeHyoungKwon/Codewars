import unittest


def automorphic(n):
    str_n = str(n)
    return "Automorphic" if str_n == str(n ** 2)[-len(str_n):] else "Not!!"


class TestAutomorphic(unittest.TestCase):
    def test_automorphic(self):
        self.assertEqual(automorphic(1), "Automorphic")
        self.assertEqual(automorphic(3), "Not!!")
        self.assertEqual(automorphic(25), "Automorphic")
        self.assertEqual(automorphic(6), "Automorphic")
        self.assertEqual(automorphic(625), "Automorphic")

