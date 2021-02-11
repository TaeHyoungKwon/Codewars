import unittest


def predict_age(*age_list):
    multiply_each_number = [age ** 2 for age in age_list]
    return (sum(multiply_each_number) ** 0.5) // 2


class TestPredictAge(unittest.TestCase):
    def test_predict_age(self):
        ages = [65, 60, 75, 55, 60, 63, 64, 45]
        actual = predict_age(*ages)
        self.assertEqual(actual, 86)
