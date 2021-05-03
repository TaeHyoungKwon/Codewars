import unittest
from typing import Union


def discover_original_price(
    discounted_price: Union[int, float], sale_percentage: Union[int, float]
) -> Union[int, float]:
    return round(discounted_price / (1 - sale_percentage * 0.01), 2)


class TestDisCoverOriginalPrice(unittest.TestCase):
    def test_discover_original_price(self):
        self.assertEqual(discover_original_price(75, 25), 100)

    def test_discover_original_price_with_edge_case(self):
        self.assertEqual(discover_original_price(458.2,17.13), 552.91)
