import unittest


def mix(s1, s2):
    common_alphabet_set = get_common_alphabet(s1, s2)
    result = []
    for char in common_alphabet_set:
        if s1.count(char) > s2.count(char):
            result.append((char, s1.count(char), 1))
        elif s2.count(char) > s1.count(char):
            result.append((char, s2.count(char), 2))
        else:
            result.append((char, s1.count(char), 3))

    s1_or_s2 = [ele for ele in result if ele[1] != 1]
    sorted_s1_or_s2 = sorted(s1_or_s2, key=lambda x: (-x[1], x[2], x[0]))
    return "/".join(
        str(ele[2]) + ":" + ele[0] * ele[1]
        if ele[2] != 3
        else '=' + ":" + ele[0] * ele[1] for ele in sorted_s1_or_s2
    )


def _filter_lower_alphabet(str_):
    return [char for char in str_ if char.isalpha() and char.islower()]


def get_common_alphabet(s1, s2):
    filtered_s1 = _filter_lower_alphabet(s1)
    filtered_s2 = _filter_lower_alphabet(s2)
    return set(filtered_s1) | set(filtered_s2)


class TestMix(unittest.TestCase):
    def test_mix(self):
        s1, s2 = "Are they here", "yes, they are here"
        actual = mix(s1, s2)
        self.assertEqual(actual, "2:eeeee/2:yy/=:hh/=:rr")

    def test_mix_2(self):
        s1, s2 = "looping is fun but dangerous", "less dangerous than coding"
        actual = mix(s1, s2)
        self.assertEqual(actual, "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")

    def test_mix_3(self):
        s1, s2 = " In many languages", " there's a pair of functions"
        actual = mix(s1, s2)
        self.assertEqual(actual, "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
