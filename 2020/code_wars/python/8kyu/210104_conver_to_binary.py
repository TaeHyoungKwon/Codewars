import unittest


def to_binary(n: int) -> int:
    return int(f"{n:b}")
    
    
class TestConvertToBinary(unittest.TestCase):
    def test_convert_to_binary(self):
        self.assertEqual(to_binary(1), 1)
        self.assertEqual(to_binary(2), 10)
        self.assertEqual(to_binary(3), 11)
        self.assertEqual(to_binary(5), 101)
