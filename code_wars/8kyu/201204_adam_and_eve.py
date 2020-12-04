import unittest


def God():
    man = Man()
    woman = Woman()
    return [man, woman]


class Human(object):
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


class TestGod(unittest.TestCase):
    def test_god(self):
        paradise = God()
        self.assertTrue(isinstance(paradise[0], Man))
