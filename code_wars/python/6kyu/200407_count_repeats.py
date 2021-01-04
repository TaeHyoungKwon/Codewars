import unittest


def count_repeats(txt):
    cnt = 0
    for i, char in enumerate(txt):
        if i == len(txt) - 1:
            break
        if char == txt[i + 1]:
            cnt += 1
    return cnt
    
    
class TestCountRepeats(unittest.TestCase):
    def test_should_return_1_when_given_txt_is_abbc(self):
        txt = 'abbc'
        actual = count_repeats(txt)
        self.assertEqual(actual, 1)

    def test_should_return_2_when_given_txt_is_abbcca(self):
        txt = 'abbcca'
        actual = count_repeats(txt)
        self.assertEqual(actual, 2)

    def test_count_repeats_with_space(self):
        txt = 'ab cca'
        actual = count_repeats(txt)
        self.assertEqual(actual, 1)

