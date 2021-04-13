import unittest

DRINK_TODDY = 'drink toddy'
DRINK_COKE = 'drink coke'
DRINK_BEER = 'drink beer'
DRINK_WHISKY = 'drink whisky'


def people_with_age_drink(age):
    if age < 14:
        return DRINK_TODDY
    elif age < 18:
        return DRINK_COKE
    elif age < 21:
        return DRINK_BEER
    else:
        return DRINK_WHISKY


class TestPeopleWithAgeDrink(unittest.TestCase):
    def test_should_return_drink_toddy_when_age_is_less_than_14(self):
        age = 13
        actual = people_with_age_drink(age)
        self.assertEqual(actual, 'drink toddy')

    def test_should_return_drink_coke_when_age_is_equal_more_than_14_and_less_than_18(self):
        age = 15
        actual = people_with_age_drink(age)
        self.assertEqual(actual, 'drink coke')

    def test_should_return_drink_coke_when_age_is_equal_more_than_18_and_less_than_21(self):
        age = 20
        actual = people_with_age_drink(age)
        self.assertEqual(actual, 'drink beer')

    def test_should_return_drink_coke_when_age_is_eqaul_greater_than_21(self):
        age = 21
        actual = people_with_age_drink(age)
        self.assertEqual(actual, 'drink whisky')
