import unittest


def chunks(string: str):
    """https://stackoverflow.com/a/312464"""
    for i in range(0, len(string), 2):
        yield string[i : i + 2]


def count_deaf_rats(town: str) -> int:
    left_part, right_part = town.split("P")
    left_part = "".join(left_part.split())
    right_part = "".join(right_part.split())
    return list(chunks(left_part)).count("O~") + list(chunks(right_part)).count("~O")


class TestCountDeafRats(unittest.TestCase):
    def test_count_deaf_rats_on_existing_only_right(self):
        self.assertEqual(count_deaf_rats(town="P O~ O~ ~O O~"), 1)

    def test_count_deaf_rats_on_existing_only_left(self):
        self.assertEqual(count_deaf_rats(town="O~ O~ ~O O~P"), 3)

    def test_count_deaf_rats_on_existing_both_left_and_right_parts(self):
        self.assertEqual(count_deaf_rats(town="O~~OO~~OO~~OO~P~OO~~OO~~OO~~O"), 8)

    def test_count_deaf_rats_on_edge_case_1(self):
        self.assertEqual(count_deaf_rats(town="~O~O~O~O P"), 0)

    def test_count_deaf_rats_on_edge_case_2(self):
        self.assertEqual(count_deaf_rats(town="~O~O~O~OP~O~OO~"), 2)


"""
문제
 - town 값이 주어질 때, P를 기준으로 ~0 의 개수를 구해라
해결
 - P를 기준으로 왼쪽 오른쪽으로 나누고, 오른쪽에서 ~0의 개수를 리턴한다
조건
input -> town: str, output -> int
절차
1. P를 기준으로 split 한다
2. 1번 index의 문자열을 기준으로 볼 때, ~0 의 개수를 리턴한다
3. 0번 index의 문자열을 기준으로 볼 때, 0~의 개수를 리턴해야한

--> 라고 생각했지만, ~O~O~O~O 혹은 O~O~O~ 의 경우는 고려하지 못함 -> 그래서 순서대로 청크 해줘야한다는 것을 나중에 깨닫고 적용 
테스트
1. only left
2. only right
3. left + right
"""
