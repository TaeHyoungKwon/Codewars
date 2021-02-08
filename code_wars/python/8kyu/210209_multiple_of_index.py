import unittest


def multiple_of_index(ar):
    return [element for index, element in enumerate(ar) if index != 0 if element % index == 0]
    
    
class TestMultipleOfIndex(unittest.TestCase):
    def test_multiple_of_index(self):
        self.assertEqual(multiple_of_index(ar=[22, -6, 32, 82, 9, 25]), [-6, 32, 25])
