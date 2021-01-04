import unittest


def encrypt_this(text):
    result = []
    for word in text.split():
        temp = []
        for index, alphabet in enumerate(word):
            if index == 0:
                temp.append(str(ord(alphabet)))
            elif index == 1:
                temp.append(word[-1])
            elif index + 1 == len(word):
                temp.append(word[1])
            else:
                temp.append(alphabet)
        result.append(''.join(temp))
    return ' '.join(result)

    
class TestEncryptThis(unittest.TestCase):
    def test_encrypt_this_with_empty_string(self):
        self.assertEqual(encrypt_this(text=''), '')

    def test_encrypt_this_with_hello(self):
        self.assertEqual(encrypt_this(text='Hello'), '72olle')

    def test_encrypt_this_with_hello(self):
        self.assertEqual(encrypt_this(text='The more he saw the less he spoke'), '84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp')
