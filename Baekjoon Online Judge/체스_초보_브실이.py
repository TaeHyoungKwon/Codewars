from dataclasses import dataclass
from enum import IntEnum


rows = 8

chess_board = []

for _ in range(rows):
    cols = input()
    chess_board.append(cols)

black_score = 0
white_score = 0


class Score(IntEnum):
    K = 0
    P = 1
    N = 3
    B = 3
    R = 5
    Q = 9

    @classmethod
    def get_score(cls, col):
        col = col.upper()

        if col == "K":
            return cls.K
        elif col == "P":
            return cls.P
        elif col == "N":
            return cls.N
        elif col == "B":
            return cls.B
        elif col == "R":
            return cls.R
        else:
            return cls.Q


for cols in chess_board:
    for col in cols:
        if col == ".":
            continue

        is_black = col.islower()

        if is_black:
            black_score += Score.get_score(col)
        else:
            white_score += Score.get_score(col)

print(white_score - black_score)
