import unittest


def increment_(n):
    return n + 1


def get_double(n):
    return n * 2


def get_triple(n):
    return n * 3


def create_iterator(func, iterator_count):
    def inner(x):
        for i in range(iterator_count):
            x = func(x)
        return x

    return inner


class TestCreateIterator(unittest.TestCase):
    def test_create_iterator_with_get_double(self):
        get_double_twice = create_iterator(get_double, 2)
        self.assertEqual(get_double_twice(2), 8)

    def test_create_iterator_with_get_triple(self):
        get_triple_three_times = create_iterator(get_triple, 3)
        self.assertEqual(get_triple_three_times(2), 54)

    def test_create_iterator_with_increment(self):
        new_increment = create_iterator(increment_, 3)
        self.assertEqual(new_increment(2), 5)
