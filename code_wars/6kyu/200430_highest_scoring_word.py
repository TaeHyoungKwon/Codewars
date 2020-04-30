import string
import unittest


def high(x):
    alphabet_int_mapping_dict = {ele: idx + 1
                                 for idx, ele in enumerate(string.ascii_lowercase)}

    result = []
    for idx, word in enumerate(x.split()):
        temp = []
        for alphabet in word:
            temp.append(alphabet_int_mapping_dict[alphabet])
        result.append((sum(temp), word, idx))
    return sorted(result, reverse=True, key=lambda x: (x[0], x[2]))[0][1]
    
    
class TestHigh(unittest.TestCase):
    def test_high_high_score_result_is_only_one(self):
        x = 'man i need a taxi up to ubud'
        actual = high(x)
        self.assertEqual(actual, 'taxi')
