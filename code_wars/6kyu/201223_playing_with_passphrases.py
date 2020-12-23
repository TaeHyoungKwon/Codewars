import unittest


def play_pass(s, n):
    first_to_third_step_result = _get_first_to_third_step(s, n)
    result = _get_fourth_to_fifth_step(first_to_third_step_result)
    return ''.join(result[::-1])


def _complement_by_9(number):
    for i in range(0, len(number)):
        a = 9 - int(number[i])
        number = (number[:i] + str(a) + number[i + 1:])
    return number


def _shift_alphabet(alphabet, n):
    shifted_alphabet_ascii = ord(alphabet) + n
    if shifted_alphabet_ascii > ord('Z'):
        return chr(ord('A') + (shifted_alphabet_ascii - ord('Z')) - 1)
    else:
        return chr(shifted_alphabet_ascii)


def _get_first_to_third_step(s, n):
    result = []
    for ele in s:
        if ele.isalpha():
            result.append(_shift_alphabet(ele, n))
        elif ele.isdigit():
            result.append(_complement_by_9(ele))
        else:
            result.append(ele)
    return result


def _get_fourth_to_fifth_step(first_to_third_step_result):
    result = []
    for index, ele in enumerate(first_to_third_step_result):
        if ele.isalpha():
            if index % 2 == 0:
                result.append(ele.upper())
            else:
                result.append(ele.lower())
        else:
            result.append(ele)
    return result


class TestPlayPass(unittest.TestCase):
    def test_paly_pass(self):
        self.assertEqual(play_pass("BORN IN 2015!", 1), "!4897 Oj oSpC")
