import unittest


def reverse_alternate(string: str) -> str:
    return " ".join(ele if index % 2 else ele[::-1] for index, ele in enumerate(string.split(), 1))


class TestReverseAlternate(unittest.TestCase):
    def test_reverse_alternate_should_return_empty_string_on_given_string_is_empty_string(self):
        self.assertEqual(reverse_alternate(string=""), "")

    def test_reverse_alternate(self):
        self.assertEqual(reverse_alternate(string="Did it work?"), "Did ti work?")


"""
문제
 - string을 받아서, 띄어쓰기 기반으로 나눴을 때, 짝수번째 element를 reversing 해서 리턴한다
해결
 - split을 해서, list를 만들고 짝수번째 element를 reversing 해서 리턴한다
조건
 - input -> string: str, output -> str
절차
1. string을 split() 하여 리스트를 만든다
2. 루프를 돌면서, 짝수번째 이면, ele[::-1]로 새로운 리스트에 추가하고, 홀수번째 이면, 그대로 추가한다.
3. 새로운 리스트에 join으로 리턴한다
테스트
엣지
1. 빈값은 빈값을 리턴해야 한다
성공
1. 보통  케이스로 커버 가능
"""