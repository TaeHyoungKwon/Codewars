import unittest


def decipher_this(string):
    result = []
    for word in string.split():
        if int(word[0]) != 1:
            word = _int_to_alphabet(word, 2)
        else:
            word = _int_to_alphabet(word, 3)

        if len(word) >= 3:
            result.append(_align_word_order(word))
        else:
            result.append(word)
    return " ".join(result)


def _int_to_alphabet(word, size):
    return chr(int(word[:size])) + word[size:]


def _align_word_order(word):
    return word[0] + word[-1] + word[2:-1] + word[1]


class TestDecipherThis(unittest.TestCase):
    def test_decipher_this(self):
        self.assertEqual(
            decipher_this(string="65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak"
        )
