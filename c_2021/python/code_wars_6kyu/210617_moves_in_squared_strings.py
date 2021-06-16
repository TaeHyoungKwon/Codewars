import unittest
from typing import Callable, Generator


def rot(strng: str) -> str:
    return "\n".join(ele[::-1] for ele in strng.split("\n")[::-1])


def selfie_and_rot(strng: str) -> str:
    def generate_selfie_and_rot() -> Generator:
        for ele in strng.split("\n"):
            dot = "." * len(ele)
            yield f"{ele}{dot}"

        for ele in rot(strng).split("\n"):
            dot = "." * len(ele)
            yield f"{dot}{ele}"
    return "\n".join(list(generate_selfie_and_rot()))


def oper(fct: Callable, s: str) -> str:
    return fct(s)


class TestRot(unittest.TestCase):
    def test_rot(self):
        self.assertEqual(
            oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"),
            "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif",
        )


class TestSelfieAndRot(unittest.TestCase):
    def test_selfie_and_rot(self):
        self.assertEqual(
            oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP"),
            "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx",
        )


"""
문제
* 각각 함수를 작성하고 리턴 값을 확인
해결
* 각 함수를 조건에 맞게 풀이한다
조건
rot
    input -> strng: str/ output -> str
selfie_and_rot
    input -> strng: str/ output -> str
oper
    input -> fct: Callable, s: str/ output -> str
절차
1. rot
    1. \n을 기준으로 split 한다
    2. 다시 \n 기준으로 join 할 때, 각 element는 뒤집는다
    3. 출력
2. selfie_and_rot
    1. \n을 기준으로 split 한다
    2. 다시 \n 기준으로 join 할 때, .... 을 붙이고 append 한다
    3. rot(strng) 결과를 가져와서 \n 기준으로 split 한다
    4. 다시 \n 기준으로 join 할 때, ....를 앞에 붙이고 append 한다
    5. append 된 temp를 \n 기준으로 join 한다

3. oper
테스트
1. rot
    * \n을 기준으로 각 element들이 뒤집힌 형태로 출력
2. selfie_and_rot
    * origin element + .... or .... + rot element
3. oper
    * 1번과, 2번을 fct로 받아서, 주어진 s를 인자로 받아서 처리

"""