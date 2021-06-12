import unittest


DARKER_CELL = {"1", "3", "5", "7", "A", "C", "E", "G"}


def chess_board_cell_color(cell1: str, cell2: str) -> bool:

    def check_member_in_darker_cell(x, y):
        return (x in DARKER_CELL) and (y in DARKER_CELL) or (x not in DARKER_CELL) and (y not in DARKER_CELL)

    x1, y1 = cell1
    x2, y2 = cell2
    return check_member_in_darker_cell(x1, y1) == check_member_in_darker_cell(x2, y2)


class TestChessBoardCellColor(unittest.TestCase):
    def test_chess_board_cell_color(self):
        self.assertTrue(chess_board_cell_color("A8", "A2"))

    def test_chess_board_cell_color_should_be_false(self):
        self.assertFalse(chess_board_cell_color("A1", "H3"))

    def test_chess_board_cell_color_with_edge(self):
        self.assertFalse(chess_board_cell_color("F2", "D7"))


"""
문제
- cell1, cell2가 주어 질 때, 이게 같은 색깔인지를 판단해라
해결
- cell1, cell2의 각각 값을 쪼개서 비교를 해서, 홀수 / 짝수, 홀수번째 / 짝수번째 로 나누어서 판단한다
조건
- input -> cell1: str, cell2: str / output -> bool
절차
1. 같은지 않은지 판단하기 위해서, LIGHT_CELL set을 미리 만들어둔다.
2. cell1, cell2 모두 길이가 2 인데, cell1부터 각각 한개씩 LIGHT_CELL set에 속하는지 검사해서 결과값을 AND로 내놓고,
cell2 를 같은 방식으로 조사했을 때, 값이 같은지 확인해서 같으면 True, 틀리면 False를 리턴한다
테스트
1. 같은 경우
2. 다른 경우
"""
