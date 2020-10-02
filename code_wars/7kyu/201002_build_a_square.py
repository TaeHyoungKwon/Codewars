import unittest


def generate_shape(integer):
    return '\n'.join('+' * integer for _ in range(integer))
    
    
class TestGenerateShape(unittest.TestCase):
    def test_generate_shape(self):
        self.assertEqual(generate_shape(integer=3), '+++\n+++\n+++')
