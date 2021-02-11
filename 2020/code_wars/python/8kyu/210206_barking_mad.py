import unittest


class Dog(object):
    def __init__(self, breed):
        self.breed = breed

    @staticmethod
    def bark():
        return "Woof"


class TestDog(unittest.TestCase):
    def test_dog_with_snoopy(self):
        snoopy = Dog("Beagle")
        self.assertEqual(snoopy.bark(), "Woof")

    def test_dog_with_scoobydoo(self):
        scoobydoo = Dog("Great Dane")
        self.assertEqual(scoobydoo.bark(), "Woof")
