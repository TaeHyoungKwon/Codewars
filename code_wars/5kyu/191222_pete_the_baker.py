# https://www.codewars.com/kata/pete-the-baker/train/python
import math
import unittest


def cakes(recipe, available):
    set_recipe = set(recipe)
    set_available = set(available)
    return (0 if set_recipe.difference(set_available)
            else min(available[ele] // recipe[ele] for ele in set_recipe & set_available))


class TestCakes(unittest.TestCase):
    def test_should_return_0_when_recipe_is_not_belong_to_available(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        result = cakes(recipe, available)
        self.assertEqual(result, 0)

    def test_should_return_min_value_is_2_of_dividing_each_element_when_recipe_is_belong_to_available_and_dividing_each_element(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        result = cakes(recipe, available)
        self.assertEqual(result, 2)
