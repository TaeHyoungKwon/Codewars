import unittest


# def split_in_parts(s: str, part_length: int) -> str:
#
#     def generate_split_in_parts():
#         for index, ele in enumerate(s, start=1):
#             if index % part_length == 0:
#                 yield ele
#                 yield " "
#             else:
#                 yield ele
#
#     return "".join(generate_split_in_parts()).strip()

from textwrap import wrap


def split_in_parts(s, part_length):
    return " ".join(wrap(s,part_length))

"""
In [15]: from textwrap import wrap                                                                                                                                                                                                

In [16]: wrap("HelloKwon", 2)                                                                                                                                                                                                     
Out[16]: ['He', 'll', 'oK', 'wo', 'n']

"""
    
    
class TestSplitInparts(unittest.TestCase):
    def test_split_in_parts_with_part_length_is_less_equal_than_given_s_length(self):
        self.assertEqual(split_in_parts(s="HelloKata", part_length=1), "H e l l o K a t a")

    def test_split_in_parts_with_part_length_is_greater_than_given_s_length(self):
        self.assertEqual(split_in_parts(s="HelloKata", part_length=9), "HelloKata")



"""
문제
- 문자열과 나눠야 하는 길이가 주어졌을 때, 길이 만큼 문자열을 공백으로 나눠서 리턴해야한다
해결
- s를 루프를 돌면서, index가 part_length로 나누어 떨어질 때 마다, 공백을 추가해주는 식으로 문자열을 재생성
조건
1. s의 길이는 0보다 크다
2. string에 띄어쓰기는 없음
3. size는 항상 positive
input: s -> str, part_length -> int, output -> str
절차
1. s를 루프를 돌린다
2. 각 char의 index가 part_length로 나누어 떨어질 때마다, char + temp list에 공백을 추가해준다, 나누어떨어지지 않으면 temp_list에 char를 그대로 추가한다
3. join해서 리턴한다 
테스트
1. 문자열 길이보다 작을 때,
2. 문자열 길이 보다 클 때,
"""