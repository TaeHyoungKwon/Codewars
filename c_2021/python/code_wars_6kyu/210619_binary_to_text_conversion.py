import unittest


def _chunks(input_, length):
    # https://stackoverflow.com/a/312464
    for i in range(0, len(input_), length):
        yield input_[i : i + length]


def binary_to_string(binary):
    return "".join(chr(int(binary_chunk, 2)) for binary_chunk in _chunks(binary, 8))


class TestBinaryToString(unittest.TestCase):
    def test_binary_to_string(self):
        self.assertEqual(binary_to_string(binary="0100100001100101011011000110110001101111"), "Hello")

    def test_binary_to_string_with_empty_input(self):
        self.assertEqual(binary_to_string(binary=""), "")


"""
문제
* 주어진 binary를 ascii table에 매칭하는 문자열로 리턴해라
해결
* 8개씩 binary를 짤라서, 각각을 int로 변경한 후, ascii table에 매핑되는 문자열로 만든다
조건
input -> binary: str, output -> str
binary string이 empty 하면, empty를 리턴해야한다
절차
1. 주어진 binary를 8개씩 짜른다
2. 각각 짤라진 binary를 루프를 돌면서, int로 변경 후, 알맞은 ascii 값을 리턴한다
3. 리턴된 char 값을 묶어서 리턴한다
테스트
1. binary가 empty 인 경우
2. binary가 정상적ㅇ로 주어졌을 경우,
"""
