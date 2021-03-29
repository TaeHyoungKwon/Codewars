import unittest

MAPPING = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer":  "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}


def get_drink_by_profession(param):
    return MAPPING.get(param.lower(), 'Beer')
    
    
class TestGetDrink(unittest.TestCase):
    def test_get_drink_by_profession(self):
        self.assertEqual(get_drink_by_profession('jabrOni'), "Patron Tequila")

    def test_get_drink_by_profession_with_not_case_sensitive(self):
        self.assertEqual(get_drink_by_profession('JABRONI'), "Patron Tequila")

    def test_get_drink_by_profession_with_not_existing(self):
        self.assertEqual(get_drink_by_profession('KWON'), "Beer")
