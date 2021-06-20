import unittest


def make_sentences(parts):
    return f"{' '.join(word for word in parts if word != '.')}.".replace(" ,", ",")
    
    
class TestMakeSentences(unittest.TestCase):
    def test_make_sentences_with_only_word(self):
        self.assertEqual(make_sentences(parts=['hello', 'world']), "hello world.")

    def test_make_sentences_with_comma(self):
        self.assertEqual(make_sentences(parts=['hello', ',', 'my', 'dear']), 'hello, my dear.')

    def test_make_sentences_with_multiple_period(self):
        self.assertEqual(make_sentences(parts=['hello', 'world', '.', '.', '.']), 'hello world.')
