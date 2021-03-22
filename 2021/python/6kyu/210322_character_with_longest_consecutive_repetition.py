import unittest


# def longest_repetition(chars):
#     ## 못품
#     if not chars:
#         return ('', 0)
#     temp = {}
#     for first, second in list(zip(chars, chars[1:])):
#         if first.isdigit() or second.isdigit():
#             continue
#
#         if first == second:
#             if first not in temp:
#                 cnt = 0
#                 temp[first] = cnt + 1
#             else:
#                 temp[first] += 1
#         else:
#             if first not in temp:
#                 cnt = 0
#                 temp[first] = cnt + 1
#                 temp[second] = cnt + 1
#             else:
#                 temp[first] += 1
#                 cnt = 0
#                 temp[second] = cnt + 1
#     result = sorted(temp, key=temp.get, reverse=True)[0]
#     return (result, temp[result])


def longest_repetition(chars):
    max_char, max_count = '', 0
    char, count = '', 0
    for c in chars:
        if c != char:
            count, char = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count


class TestLongestRepetition(unittest.TestCase):
    def test_longest_repetition_with_empty_chars(self):
        self.assertEqual(longest_repetition(chars=''), ('', 0))

    def test_longest_repetition_with_common_case(self):
        self.assertEqual(longest_repetition(chars='aaaabb'), ('a', 4))

    def test_longest_repetition_with_common_case_2(self):
        self.assertEqual(longest_repetition(chars='bbbaaabaaaa'), ('a', 4))

    def test_longest_repetition_with_common_case_3(self):
        self.assertEqual(longest_repetition(chars='cbdeuuu900'), ('u', 3))

    def test_longest_repetition_with_common_case_4(self):
        self.assertEqual(longest_repetition(chars='abbbbb'), ('b', 5))

    def test_longest_repetition_with_common_case_5(self):
        self.assertEqual(longest_repetition(chars='aabb'), ('a', 2))

    def test_longest_repetition_with_common_case_6(self):
        self.assertEqual(longest_repetition(chars='ba'), ('b', 1))


