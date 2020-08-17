# LV3. 등굣
import pytest

CONDITION_CONSTANT = 1000000007


def get_board_with_puddles(m, n):
    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1
    return board


def calc_shortest_path(m, n, puddles, board):
    def set_board_value():
        if [j, i] in puddles:
            board[i][j] = 0
        else:
            board[i][j] = board[i - 1][j] + board[i][j - 1]

    for i in range(1, n+1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            set_board_value()

    return board


def solution(m, n, puddles):
    board = get_board_with_puddles(m, n)
    return calc_shortest_path(m, n, puddles, board)[n][m] % CONDITION_CONSTANT


@pytest.mark.parametrize("m, n, puddles, expected", [(4, 3, [[2, 2]], 4),])
def test_shortest_path_with_puddles(m, n, puddles, expected):
    solution(m, n, puddles) == expected


def solution(m, n, puddles):
    arr = [[0]*(m+1) for i in range(n+1)]
    arr[1][1] = 1
    for puddle in puddles:
        arr[puddle[1]][puddle[0]] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif arr[i][j] == -1:
                arr[i][j] = 0
            else:
                arr[i][j] += (arr[i-1][j] + arr[i][j-1]) % 1000000007
    return arr[n][m]
