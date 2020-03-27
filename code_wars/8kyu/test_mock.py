from unittest import TestCase
import inspect


def hello():

    a = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    return 'Hello!'


class TestMe(TestCase):
    def test_hello(self):
        print(inspect.getmodule(hello).__file__)
        self.assertEqual(hello(), "Mock!")