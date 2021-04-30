import unittest
from itertools import zip_longest
from typing import Generator


def insert_dash(num: int) -> str:
    def generate_insert_dash(num: str) -> Generator:
        for front, back in zip_longest(num, num[1:]):
            if back is None:
                yield front
                continue

            if int(front) % 2 and int(back) % 2:
                yield f"{front}-"
            else:
                yield front

    num: str = str(num)
    return "".join(generate_insert_dash(num))


class TestInsertDash(unittest.TestCase):
    def test_insert_dash(self):
        self.assertEqual(insert_dash(num=454793), "4547-9-3")


"""
문제
- insert_dash 함수를 작성해라
해결
- zip_longest를 활용 2개씩 나눠서, 각각 홀수인지 체크한후, temp에 dash가 추가된 형태로 append 한다
- 이후 ''.join 한다
조건
1. 2개의 홀수 사이에 있어야 함
2. 0은 홀수로 치지 않는다
절차
1. zip_longest(s, s[1:]) 2개씩 나눈다.
2. 앞뒤를 검사해서, 둘다 홀수가 아니면 앞의 것을 리스트에 append 한다
3. 둘다 홀수 이면, 앞의 것을 - 를 포함시켜서 append 한다
4. 뒤의 것이 None이면 그냥 append 시킨다
"""
