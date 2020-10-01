import unittest

ALPHABET_LIST = [
    ['1'],
    ['A', 'B', 'C', '2'],
    ['D', 'E', 'F', '3'],
    ['G', 'H', 'I', '4'],
    ['J', 'K', 'L', '5'],
    ['M', 'N', 'O', '6'],
    ['P', 'Q', 'R', 'S', '7'],
    ['T', 'U', 'V', '8'],
    ['W', 'X', 'Y', 'Z', '9'],
    ['*'],
    [' ', '0'],
    ['#'],
]


def presses(phrease):
    press_count = 0
    for char in phrease:

        if char.isalpha():
            char = char.upper()

        for index_, alphabet_group in enumerate(ALPHABET_LIST):
            if char in alphabet_group:
                press_count += ALPHABET_LIST[index_].index(char) + 1
                break
            elif char == ' ':
                press_count += 1
                break
    return press_count


class TestPresses(unittest.TestCase):
    def test_presses_common_case_one(self):
        phrease = 'LOL'
        actual = presses(phrease)
        self.assertEqual(actual, 9)

    def test_presses_common_case_two(self):
        phrease = 'HOW R U'
        actual = presses(phrease)
        self.assertEqual(actual, 13)

    def test_presses_with_lower_case(self):
        phrease = 'lol'
        actual = presses(phrease)
        self.assertEqual(actual, 9)

    def test_presses_with_numbers(self):
        phrease = 'WHERE DO U WANT 2 MEET L8R'
        actual = presses(phrease)
        self.assertEqual(actual, 47)
