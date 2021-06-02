import unittest

dictionary = {
    "A": "awesome",
    "B": "beautiful",
    "C": "confident",
    "D": "disturbing",
    "E": "eager",
    "F": "fantastic",
    "G": "gregarious",
    "H": "hippy",
    "I": "ingestable",
    "J": "joke",
    "K": "klingon",
    "L": "literal",
    "M": "mustache",
    "N": "newtonian",
    "O": "oscillating",
    "P": "perfect",
    "Q": "queen",
    "R": "rant",
    "S": "stylish",
    "T": "turn",
    "U": "underlying",
    "V": "volcano",
    "W": "weird",
    "X": "xylophone",
    "Y": "yogic",
    "Z": "zero",
}


def make_backronym(acronym):
    return " ".join(dictionary[letter.upper()] for letter in acronym)


class TestMakeBackRonym(unittest.TestCase):
    def test_make_backronym(self):
        self.assertEqual(make_backronym(acronym="dgm"), "disturbing gregarious mustache")


"""
문제
- acronym을 받았을 때, dictionary를 참고해서 적절한 단어 모음 형태로 리턴해라

해결
- 주어진 사전 데이터를 활용 하여서, acronym 각 element에 해당하는 단어를 띄어쓰기로 붙여서 출력 한다

조건
input -> acronym: str, output -> str
1. 사전의 key 알파벳이 대문자 이다

절차
1. acronym을 루프를 돈다
2. 각 letter에 해당하는 문자열을 temp 리스트에 넣는다
3. " ".join(temp)로 리턴한다

테스트
- 정상케이스만 확인 해도 됨
"""