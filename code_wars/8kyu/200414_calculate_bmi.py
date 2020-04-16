import unittest

UNDER_WEIGHT = 'Underweight'
NORMAL = 'Normal'
OVERWEIGHT = 'Overweight'
OBESE = 'Obese'


def bmi(weight, height):
    bmi_rate = weight / (height ** 2)

    if bmi_rate <= 18.5:
        return UNDER_WEIGHT
    elif bmi_rate <= 25.0:
        return NORMAL
    elif bmi_rate <= 30.0:
        return OVERWEIGHT
    else:
        return OBESE


class TestCalculateBMI(unittest.TestCase):
    def test_bmi_under_weight(self):
        self.assertEqual(bmi(weight=50, height=1.80), UNDER_WEIGHT)

    def test_bmi_normal(self):
        self.assertEqual(bmi(weight=80, height=1.80), NORMAL)

    def test_bmi_over_weight(self):
        self.assertEqual(bmi(weight=90, height=1.80), OVERWEIGHT)

    def test_bmi_over_obese(self):
        self.assertEqual(bmi(weight=110, height=1.80), OBESE)
