import unittest


class Person:
    def __init__(self, my_name):
        self.my_name = my_name

    def greet(self, name):
        return f"Hello {name}, my name is {self.my_name}"

    @property
    def name(self):
        return self.my_name
    
    
class TestPerson(unittest.TestCase):
    def test_greet_when_name_is_jack(self):
        jack = Person('Jack')
        actual = jack.greet('Jill')
        self.assertEqual(actual, "Hello Jill, my name is Jack")

    def test_name_property_should_return_my_name(self):
        jill = Person('Jill')
        actual = jill.name
        self.assertEqual(actual, 'Jill')