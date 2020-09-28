import unittest


def say_hello(name):
    return 'Hello, {}'.format(name)
    
    
class TestSayHello(unittest.TestCase):
    def test_say_hello(self):
        name = 'Mr. Spock'
        actual = say_hello(name)
        self.assertEqual(actual, 'Hello, Mr. Spock')
