import unittest

VOWEL_NUM = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5',
}

NUM_TO_VOWEL = {
    '1': 'a',
    '2': 'e',
    '3': 'i',
    '4': 'o',
    '5': 'u',
}


def encode(st):
    return ''.join(VOWEL_NUM[char] if char in VOWEL_NUM else char for char in st)


def decode(st):
    return ''.join(NUM_TO_VOWEL[char] if char in NUM_TO_VOWEL else char for char in st)
    
    
class TestEncodeDecode(unittest.TestCase):
    def test_encode(self):
        st = 'hello'
        actual = encode(st)
        self.assertEqual(actual, 'h2ll4')

    def test_decode(self):
        st = 'How are you today?'
        actual = encode(st)
        self.assertEqual(actual, 'H4w 1r2 y45 t4d1y?')
