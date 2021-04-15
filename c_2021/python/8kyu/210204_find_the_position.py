import unittest


def position(alphabet):
    position_of_alphabet = ord(alphabet) - 96
    return f"Position of alphabet: {position_of_alphabet}"
    
    
class TestPosition(unittest.TestCase):
    def test_position(self):
        self.assertEqual(position(alphabet='a'), "Position of alphabet: 1")
