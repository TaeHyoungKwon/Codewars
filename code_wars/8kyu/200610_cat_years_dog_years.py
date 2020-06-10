import unittest


def _calc_years(year, is_cat):
    if year == 1:
        return 15
    elif year == 2:
        return 24
    else:
        return (year - 2) * (4 if is_cat else 5) + 24


def get_cat_years(year):
    return _calc_years(year, is_cat=True)


def get_dog_years(year):
    return _calc_years(year, is_cat=False)


def human_years_cat_years_dog_years(human_years):
    return [human_years, get_cat_years(human_years), get_dog_years(human_years)]


class TestHumanYearsCatYearsDogYears(unittest.TestCase):
    def test_get_cat_years_on_1_years(self):
        self.assertEqual(get_cat_years(1), 15)

    def test_get_cat_years_on_2_years(self):
        self.assertEqual(get_cat_years(2), 24)

    def test_get_cat_years_on_10_years(self):
        self.assertEqual(get_cat_years(10), 56)

    def test_get_dog_years_on_1_years(self):
        self.assertEqual(get_dog_years(1), 15)

    def test_get_dog_years_on_2_years(self):
        self.assertEqual(get_dog_years(2), 24)

    def test_get_dog_years_on_10_years(self):
        self.assertEqual(get_dog_years(10), 64)

    def test_human_years_cat_years_dog_years_on_10_years(self):
        self.assertEqual(human_years_cat_years_dog_years(10), [10,56,64])
