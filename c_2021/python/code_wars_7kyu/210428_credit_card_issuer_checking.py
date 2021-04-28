import re
import unittest

VISA_PATTERN = re.compile(r"^4([\d]{12}|[\d]{15})$")
AMEX_PATTERN = re.compile(r"^(34|37)[\d]{13}$")
DISCOVER_PATTERN = re.compile(r"^6011[\d]{12}$")
MASTER_PATTERN = re.compile(r"^(51|52|53|54|55)[\d]{14}$")


def get_issuer(number: int) -> str:
    if re.match(VISA_PATTERN, str(number)):
        return "VISA"
    elif re.match(AMEX_PATTERN, str(number)):
        return "AMEX"
    elif re.match(DISCOVER_PATTERN, str(number)):
        return "Discover"
    elif re.match(MASTER_PATTERN, str(number)):
        return "Mastercard"
    else:
        return "Unknown"


class TestGetIssuer(unittest.TestCase):
    def test_get_issuer_with_visa(self):
        self.assertEqual(get_issuer(number=4111111111111111), "VISA")

    def test_get_issuer_with_amex(self):
        self.assertEqual(get_issuer(number=378282246310005), "AMEX")

    def test_get_issuer_with_discover(self):
        self.assertEqual(get_issuer(number=6011111111111117), "Discover")

    def test_get_issuer_with_mastercard(self):
        self.assertEqual(get_issuer(number=5105105105105100), "Mastercard")

    def test_get_issuer_with_unknown(self):
        self.assertEqual(get_issuer(number=1234566), "Unknown")

    def test_get_issuer_with_edge_case(self):
        self.assertEqual(get_issuer(number=41111111111111), "Unknown")
