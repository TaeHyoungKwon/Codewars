import string
import unittest
from itertools import cycle

ALPHABET_INDEX_MAPPING = {letter: index for index, letter in enumerate(string.ascii_lowercase, 1)}


def encode(message, key):
    def generate_encoded():
        key_cycle = cycle(str(key))
        for letter in message:
            yield ALPHABET_INDEX_MAPPING[letter] + int(next(key_cycle))

    return list(generate_encoded())


class TestEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode(message="scout", key=1939), [20, 12, 18, 30, 21])


"""
문제
- message와 key가 주어질 때, encoding된 리스트를 출력 해라
해결
- 알파벳 인덱스와 매핑되어있는 message와, cycle 하는 특징이 있는 key 값들의 숫자 합을 구해서 리스트에 추가한다
조건
- input -> message: str, key: int, output -> List[int]
절차
1. 알파벳, 숫자 매핑 테이블을 만든다
2. message를 루프를 돌면서, 매핑테이블의 index와 key의 순환하는 각 digit 값을 더해서 리스트에 넣는다
3. 출력 한다
테스트
1. 다른 조건들이 적혀 있진 않아서, 성공케이스만 보면 될 것 같음
"""
