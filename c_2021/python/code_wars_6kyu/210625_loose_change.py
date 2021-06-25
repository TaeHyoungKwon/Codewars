import unittest

CURRENCY_MAP = {"Quarters": 25, "Dimes": 10, "Nickels": 5, "Pennies": 1}


def loose_change(cents):
    result = dict.fromkeys(CURRENCY_MAP.keys(), 0)
    if cents <= 0:
        return result
    if isinstance(cents, float):
        cents = int(cents)
    for k, v in CURRENCY_MAP.items():
        if cents < v:
            continue
        result[k], cents = divmod(cents, v)
    return result


class TestLooseChange(unittest.TestCase):
    def test_loose_change_on_cents_is_0(self):
        self.assertEqual(loose_change(cents=0), {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0})

    def test_loose_change_on_cents_is_negative(self):
        self.assertEqual(loose_change(cents=-2), {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0})

    def test_loose_change_on_cents_is_float(self):
        self.assertEqual(loose_change(cents=3.9), {"Nickels": 0, "Pennies": 3, "Dimes": 0, "Quarters": 0})

    def test_loose_change_on_cents(self):
        self.assertEqual(loose_change(cents=91), {"Nickels": 1, "Pennies": 1, "Dimes": 1, "Quarters": 3})
