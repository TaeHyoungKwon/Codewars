import unittest

ALPHABET_TO_MORSE_CODE = {
    ".-": "A",
    "-.": "N",
    "-...": "B",
    "---": "O",
    "-.-.": "C",
    ".--.": "P",
    "-..": "D",
    "--.-": "Q",
    ".": "E",
    ".-.": "R",
    "..-.": "F",
    "...": "S",
    "--.": "G",
    "-": "T",
    "....": "H",
    "..-": "U",
    "..": "I",
    "...-": "V",
    "-.-": "K",
    "-..-": "X",
    ".---": "J",
    ".--": "W",
    ".-..": "L",
    "-.--": "Y",
    "--": "M",
    "--..": "Z",
}


def decodeMorse(morse_code):
    return ' '.join(''.join(ALPHABET_TO_MORSE_CODE[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))


class TestDecodeMorse(unittest.TestCase):
    def test_decode_morese(self):
        morse_code = ".... . -.--   .--- ..- -.. ."
        actual = decodeMorse(morse_code)
        self.assertEqual(actual, "HEY JUDE")
