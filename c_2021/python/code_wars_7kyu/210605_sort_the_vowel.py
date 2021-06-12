import unittest

VOWEL = "aeiouAEIOU"


def sort_vowels(s: str) -> str:
    if not isinstance(s, str):
        return ""
    return "\n".join("|" + char if char in VOWEL else char + "|" for char in s)
    
    
class TestSortTheVowels(unittest.TestCase):
    def test_sort_vowels_with_invalid_s(self):
        self.assertEqual(sort_vowels(s=None), '')

    def test_sort_vowels_with_success(self):
        self.assertEqual(sort_vowels(s="Codewars"), 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|')


"""
문제
- 주어진 s를 대문자로 바꾼 후, 예시의 답 처럼 나오도록 출력한다
해결
- 
조건
- 모든 모음은 |의 오른쪽에
- 모음외 나머지는 |의 왼쪽에
- Case insensitive
- invalid input은 empty string을 리턴한다
절차

테스트
1. invalid input은 empty string을 리턴
2. Success Case
"""