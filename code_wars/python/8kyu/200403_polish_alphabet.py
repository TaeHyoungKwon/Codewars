import unittest


def correct_polish_letters(st):
    mapping = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z',
    }
    return ''.join(mapping[ele] if ele in mapping.keys() else ele for ele in st)
    
    
class TestCorrectPolishLetters(unittest.TestCase):
    def test_correct_polish_letters(self):
        st = "Jędrzej Błądziński"
        actual = correct_polish_letters(st)
        self.assertEqual(actual, "Jedrzej Bladzinski")
