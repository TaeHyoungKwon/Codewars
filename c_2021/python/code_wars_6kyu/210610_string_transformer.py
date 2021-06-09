import unittest


def string_transformer(s):
    return " ".join(char for char in s.swapcase().split(" ")[::-1])

    
    
class TestStringTransformer(unittest.TestCase):
    def test_string_transformer(self):
        self.assertEqual(string_transformer(s="Example string"), "STRING eXAMPLE")

    def test_string_transformer_with_edge_case(self):
        self.assertEqual(string_transformer(s=" A b C d E f G "), " g F e D c B a ")


"""
문제
- input s를 받았을 때, 아래 조건의 형태로 변경해서 리턴하여라
해결
- 
조건
1. 각 case의 모든 case를 바꾼다
2. 단어를 반대로 뒤집는다
- s는 오직 alphabet이거나, 공백이다
절차
1. s.swapcase()로 case를 변경한다
2. 변경된 s를 split(" ")해서 띄어쓰기 단위로 나눈뒤,(공백포함)
3. 역순으로 출력되도록 리스트 컴프리헨션을 만들고,
4. 조인한다
테스트
* alphabet과 숫자로만 이루어져 있어서, 케이스는 성공 케이스 1개만 해도 될것 같다
"""