import unittest

FRONT = "010"
REPEATED_PIANO_KEY = "010100101010"
BACK = "0"

PIANO_KEY = f"{FRONT}{REPEATED_PIANO_KEY * 7}{BACK}"


def black_or_white_key(key_press_count):
    return "black" if PIANO_KEY[key_press_count % len(PIANO_KEY) - 1] == "1" else "white"


class TestBlackOrWhiteKey(unittest.TestCase):
    def test_black_or_white_key(self):
        self.assertEqual(black_or_white_key(key_press_count=1), "white")
