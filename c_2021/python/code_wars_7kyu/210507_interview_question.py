import unittest
from collections import Counter


def get_strings(city):
    return ",".join(f"{letter}:{count_ * '*'}" for letter, count_ in Counter(city.replace(" ", "").lower()).items())


class TestGetStrings(unittest.TestCase):
    def test_get_strings(self):
        self.assertEqual(get_strings(city="Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*")

    def test_get_strings_with_edge_case(self):
        self.assertEqual(get_strings(city="Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*")


"""
문제
- city 문자열을 받아서, 해당하는 문자가 몇번나오는지 *로 표현하도록 해야한다
- input -> city:str, output -> str
해결
- 각 알파벳이 몇번 나오는지(case insensitive) 세어서, c:** 형태를 만든다음 이를 리스트에 모두 추가한다
- 리스트에 추가된 element를 ','.join() 으로 이어준다
조건
- 오직 알파벳만 가능
- output에는 space가 없다 
- , 로 나뉘어져 있다
- 순서를 지켜야한다
절차
1. 문자열을 for loop를 돌린다
2. 리스트에 해당 문자열이 포함되어있는지 확인한다
3. 있으면 continue
4. 없으면, 각 element를 lowercase 기준으로, element 개수가 몇개인지 확인 후, dict 형태로 저장 - ex) {c:2}
5. 루프가 끝났을 때, dict 형태로 저장된 각 element들을 output에 맞게 변경하여서 join을 이용해서 리턴할 수 있도록 한다
"""
