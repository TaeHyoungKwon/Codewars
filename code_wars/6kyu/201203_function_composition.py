import unittest


def compose(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))
    
    
class TestCompose(unittest.TestCase):
    def test_compose(self):
        add1 = lambda a: a + 1
        this = lambda a: a
        actual = compose(add1, this)(0)
        self.assertEqual(actual, 1)
