import unittest


def is_valid_coordinates(coordinates):
    try:
        lat, lng = map(float, coordinates.split(","))
    except ValueError:
        return False
    return -90 <= lat <= 90 and -180 <= lng <= 180 and coordinates.isdigit()


class TestCoordinates(unittest.TestCase):
    def test_coordinates(self):
        self.assertTrue(is_valid_coordinates("43.91343345, 143"))
