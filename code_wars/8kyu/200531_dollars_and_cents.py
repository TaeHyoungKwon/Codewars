import unittest


def format_money(amount):
    return f'${amount:.2f}'
    
    
class TestFormatMoney(unittest.TestCase):
    def test_format_money_when_amount_is_int(self):
        self.assertEqual(format_money(3), '$3.00')

    def test_format_money_when_amount_with_decimal_point(self):
        self.assertEqual(format_money(3.1), '$3.10')
