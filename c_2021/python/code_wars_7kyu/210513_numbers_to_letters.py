import unittest
import string

REVERSED_ALPHABET_INDEX_MAP = {
    f"{27 - index}": alphabet
    for index, alphabet in enumerate(string.ascii_lowercase, start=1)
}
ADDITIONAL = {
    "27": "!",
    "28": "?",
    "29": " ",
}
REVERSED_ALPHABET_INDEX_MAP.update(ADDITIONAL)


def switcher(arr):
    return ''.join(REVERSED_ALPHABET_INDEX_MAP[ele] for ele in arr)
    
    
class TestSwitcher(unittest.TestCase):
    def test_switcher(self):
        self.assertEqual(switcher(arr=['24', '12', '23', '22', '4', '26', '9', '8']), 'codewars')


"""
문제
- 주어진 arr에 매핑되는 문자를 합쳐서 문자열로 리턴한다
해결
- 새롭게 매핑된 dict를 만든 후에, 루프를 도면서 문자열을 만든다
조건
- 알파벳 index가 역으로 매핑된 상태(a-26, z-1)
- !, ?, " " 는 27, 28, 29 로 각각 추가 매핑 해준다.
- input: List[int] output: str
절차
1. 알파벳 역순 dict를 정의한다.
2. arr 루프를 돌면서, 매핑되는 알파벳을 list에 더한다
3. list를 join으로 문자열을 만들어서 리턴한다
"""