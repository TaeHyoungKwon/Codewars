import unittest


def derive(coefficient, exponent):
    return f"{str(coefficient * exponent)}x^{str(exponent - 1)}"


class TestDerive(unittest.TestCase):
    def test_derive_case_1(self):
        self.assertEqual(derive(coefficient=1, exponent=2), "2x^1")

    def test_derive_case_2(self):
        self.assertEqual(derive(coefficient=2, exponent=3), "6x^2")
