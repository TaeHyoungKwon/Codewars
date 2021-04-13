import unittest


def to_nato(words):
    return ' '.join(MAPPING[char.lower()] if char.isalpha() else char for char in words if char != " ")


class TestToNato(unittest.TestCase):
    def test_to_nato(self):
        self.assertEqual(
            to_nato(words="If you can read"),
            "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta",
        )


MAPPING = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu",
}
