import unittest


def how_many_light_sabers_do_you_own(name=None):
    return 0 if not (name and name == 'Zach') else 18


class TestHowManyLightSabersDoYouOwn(unittest.TestCase):
    def test_should_return_0_when_name_is_none(self):
        actual = how_many_light_sabers_do_you_own()
        self.assertEqual(actual, 0)

    def test_should_return_0_when_name_is_not_zach(self):
        name = 'zach'
        actual = how_many_light_sabers_do_you_own(name)
        self.assertEqual(actual, 0)

    def test_should_return_18_when_name_is_Zach(self):
        name = 'Zach'
        actual = how_many_light_sabers_do_you_own(name)
        self.assertEqual(actual, 18)
