import unittest


def even_chars(st):
    if not (2 <= len(st) <= 100):
        return "invalid string"
    return list(st)[1::2]
    
    
class TestEvenChars(unittest.TestCase):
    def test_even_chars_should_return_invalid_string_on_length_of_st_less_than_2(self):
        self.assertEqual(even_chars(st="a"), "invalid string")

    def test_even_chars_should_return_invalid_string_on_length_of_st_greater_than_100(self):
        st = "a" * 101
        self.assertEqual(even_chars(st=st), "invalid string")

    def test_even_chars_with_happy_path(self):
        self.assertEqual(even_chars(st="abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])


"""
문제
* 주어진 리스트에서, 짝수번째 알파벳을 리턴하는 sequence를 만들어라
해결
* 아래 조건에 맞게 개발한다
조건
* invalid string을 리턴
    * st의 길이가 2보다 작거나
    * 100보다 더 길면
절차
1. st의 valid 체크를한다 ( 2 <= st <= 100)
    * 유효하다면,
        다음 스텝으로 넘어간다
    * 유효하지 않다면,
        invalid string을 리턴한다

2. 짝수번째 char를 뽑아내서, 리스트로 만들고 리턴한다

테스트
happy path
* st가 2보다 크고, 100보다 같거나 작은 상태에서 짝수번째 char들을 sequence 형태로 리턴해야한다

unhappy path
* invalid string
    1. st가 2 보다 작을 때
    2. st가 100보다 클 때,
"""