import unittest


def greet(me):
    return f'Hello {me.capitalize()}!'
    
    
class TestGreet(unittest.TestCase):
    def test_greet(self):
        me = 'riley'
        actual = greet(me)
        self.assertEqual(actual, 'Hello Riley!')
